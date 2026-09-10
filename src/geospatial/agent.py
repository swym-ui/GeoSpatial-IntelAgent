import geopandas as gpd
import json
def run_geospatial_demo():
    # create a tiny GeoDataFrame demo
    gdf = gpd.GeoDataFrame({'id':[1],'geometry':[None]})
    return {'status':'demo','features':len(gdf)}
