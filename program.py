import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# 1. Cargar el archivo GeoJSON que acabas de generar
ruta_archivo = "manzanas_castilla.geojson"
gdf = gpd.read_file(ruta_archivo)

# 2. Calcular el área real de cada polígono en metros cuadrados
# (Como el GeoJSON está en EPSG:3116, .geometry.area calcula directamente en m²)
gdf["area"] = gdf.geometry.area

# Filtrar geometrías vacías o inválidas por seguridad
gdf = gdf[gdf.geometry.notnull() & (gdf["area"] > 0)]

# 3. Clasificar los polígonos por grupos de área usando cuantiles (3 categorías: Pequeño, Mediano, Grande)
gdf["grupo_area"] = pd.qcut(
    gdf["area"], q=3, labels=["Pequeño", "Mediano", "Grande"]
)

# 4. Crear la gráfica y visualizar los polígonos coloreados por grupo
fig, ax = plt.subplots(figsize=(12, 12))
gdf.plot(
    column="grupo_area",
    cmap="Set2",  # Paleta de colores diferenciados
    legend=True,
    edgecolor="black",
    linewidth=0.3,
    ax=ax,
    legend_kwds={
        "title": "Grupos de Área",
        "loc": "upper left",
        "bbox_to_anchor": (1, 1),
    },
)

plt.title(
    "Clasificación de Polígonos en Castilla por Grupos de Área",
    fontsize=14,
    pad=15,
)
plt.xlabel("Coordenada Este (X) - Metros", fontsize=10)
plt.ylabel("Coordenada Norte (Y) - Metros", fontsize=10)
plt.tight_layout()
plt.show()