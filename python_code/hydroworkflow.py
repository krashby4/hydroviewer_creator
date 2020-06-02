#%%
import geopandas
import folium
import folium.plugins

m = folium.Map(
    location=[40.76524, 140.399], #This coordinate shows example issue with catchments
    tiles='',
    zoom_start=3
)

draw_control = folium.plugins.Draw(
    export=True
)

draw_control.add_to(m)

geoserver_url = "https://geoserver.hydroshare.org/geoserver/wms"

stamen_layer = folium.TileLayer(
    tiles='Stamen Terrain',
    name='Stamen Terrain'
)

stamen_layerwc = folium.TileLayer(
    tiles='Stamen Watercolor',
    name='Stamen Watercolor'
)

stamen_layer.add_to(m)
stamen_layerwc.add_to(m)

japan_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-df5f3e52c51b419d8ee143b919a449b3:japan-geoglows-catchment japan-geoglows-catchment,HS-df5f3e52c51b419d8ee143b919a449b3:japan-geoglows-drainageline japan-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Japan',
    show=False
)

australia_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-9572eb7fa8744807962b9268593bd4ad:australia-geoglows-catchment australia-geoglows-catchment,HS-9572eb7fa8744807962b9268593bd4ad:australia-geoglows-drainageline australia-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Australia',
    show=False
)

japan_shapefiles.add_to(m)
australia_shapefiles.add_to(m)

shapefile_control = folium.LayerControl()

shapefile_control.add_to(m)

m

# %%
gjson_file = geopandas.read_file("/home/kyler/Documents/gjson_files/data.geojson")
gjson_file = gjson_file.to_crs("EPSG:3857")

gjson_file = gjson_file.to_file("/home/kyler/Documents/shapefiles/gjson/gshape.shp")

gjson_shp = geopandas.read_file("/home/kyler/Documents/shapefiles/gjson/gshape.shp")

dl_shp = geopandas.read_file("zip:///home/kyler/Documents/drainagelines/japan-geoglows-drainageline.zip/japan-geoglows-drainageline/japan-geoglows-drainageline.shp")

ctch_shp = geopandas.read_file("zip:///home/kyler/Documents/catchments/japan-geoglows-catchment.zip/japan-geoglows-catchment/japan-geoglows-catchment.shp")

# %%
ctch_point = ctch_shp.representative_point()

ctch_point.to_file("/home/kyler/Documents/shapefiles/reppoint_shape/ctch/ctch_point.shp")

ctch_point_clip = geopandas.clip(ctch_point, gjson_shp)

ctch_boo_list = ctch_point_clip.within(ctch_shp)

ctch_select = ctch_shp[ctch_boo_list]

ctch_select.to_file("/home/kyler/Documents/shapefiles/clip/ctch/ctch_select.shp")

# %%
dl_point = dl_shp.representative_point()

dl_point.to_file("/home/kyler/Documents/shapefiles/reppoint_shape/drainline/reppoint_dl.shp")

# %%