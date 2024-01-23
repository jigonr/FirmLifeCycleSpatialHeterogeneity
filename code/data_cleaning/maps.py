
import geopandas as gpd

# read in the shapefile
gdf = gpd.read_file("data/0-raw_data/mx_municipalities_maps.geojson")

# plot the shapefile
gdf.plot()
