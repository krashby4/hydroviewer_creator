#%%
import geopandas
import folium
import folium.plugins

m = folium.Map(
    location=[37.105491, 139.835068],
    tiles='',
    zoom_start=5
)

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

draw_control = folium.plugins.Draw(
    draw_options={
        'polyline':False,
        'marker':False,
        'circlemarker':False,
        'polygon':{
            'shapeOptions':{
                'color':'#9933ff',
                'weight':'1'
            }
        }
        },
    export=True,
)

draw_control.add_to(m)

m

# %%
gjson_file = geopandas.read_file("/home/kyler/hydroviewer_creator/gjson_files/data.geojson")
gjson_file = gjson_file.to_crs("EPSG:3857")
gjson_shp = gjson_file.to_file("/home/kyler/hydroviewer_creator/shapefiles/gjson/gshape.shp")
gjson_shp_read = geopandas.read_file("/home/kyler/hydroviewer_creator/shapefiles/gjson/gshape.shp")

zipfile_dl = "zip:///home/kyler/hydroviewer_creator/drainagelines/japan-geoglows-drainageline.zip/japan-geoglows-drainageline/japan-geoglows-drainageline.shp"
gdf_zip_dl = geopandas.read_file(zipfile_dl)

zipfile_ctch = "zip:///home/kyler/hydroviewer_creator/catchments/japan-geoglows-catchment.zip/japan-geoglows-catchment/japan-geoglows-catchment.shp"
gdf_zip_ctch = geopandas.read_file(zipfile_ctch)

# %%
gjson_poly = gjson_file.geometry

gjson_poly.head()

# %%
gdf_ctch_geo = gdf_zip_ctch.geometry

gdf_ctch_geo.head()
# %%
within = gjson_poly.within(gdf_ctch_geo)

within.head()

# %%
subset = gdf_zip_ctch[within]

subset.head()

# %%
subset.plot()

# %%
