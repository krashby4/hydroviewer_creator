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

#%%
gjson_file = geopandas.read_file("/home/kyler/hydroviewer_creator/gjson_files/data.geojson")
gjson_file = gjson_file.to_crs("EPSG:3857")

gjson_file = gjson_file.to_file("/home/kyler/hydroviewer_creator/shapefiles/gjson/gshape.shp")

gjson_shp = geopandas.read_file("/home/kyler/hydroviewer_creator/shapefiles/gjson/gshape.shp")

dl_shp = geopandas.read_file("zip:///home/kyler/hydroviewer_creator/drainagelines/japan-geoglows-drainageline.zip/japan-geoglows-drainageline/japan-geoglows-drainageline.shp")

ctch_shp = geopandas.read_file("zip:///home/kyler/hydroviewer_creator/catchments/japan-geoglows-catchment.zip/japan-geoglows-catchment/japan-geoglows-catchment.shp")

# %%
ctch_cent = ctch_shp.centroid

cent_clip = geopandas.clip(ctch_cent, gjson_shp)

cent_clip.plot()

boo_list = ctch_shp.contains(cent_clip)

geo_select = ctch_shp[boo_list]

geo_select.plot()

#%%
geo_select_shp = geo_select.to_file("/home/kyler/hydroviewer_creator/shapefiles/clip.shp")

# %%
