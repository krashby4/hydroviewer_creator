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

africa_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-121bbce392a841178476001843e7510b:africa-geoglows-catchment africa-geoglows-catchment,HS-121bbce392a841178476001843e7510b:africa-geoglows-drainageline africa-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Africa',
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

centralamerica_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-36fae4f0e04d40ccb08a8dd1df88365e:central_america-geoglows-catchment central_america-geoglows-catchment,HS-36fae4f0e04d40ccb08a8dd1df88365e:central_america-geoglows-drainageline central_america-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Central America',
    show=False
)

centralasia_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-383bc50a88ae4711a8d834a322ced2d5:central_asia-geoglows-catchment central_asia-geoglows-catchment,HS-383bc50a88ae4711a8d834a322ced2d5:central_asia-geoglows-drainageline central_asia-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Central Asia',
    show=False
)

eastasia_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-85ac5bf29cff4aa48a08b8aaeb8e3023:east_asia-geoglows-catchment east_asia-geoglows-catchment,HS-85ac5bf29cff4aa48a08b8aaeb8e3023:east_asia-geoglows-drainageline east_asia-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='East Asia',
    show=False
)

europe_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-c14e1644a94744d8b3204a5be91acaed:europe-geoglows-catchment europe-geoglows-catchment,HS-c14e1644a94744d8b3204a5be91acaed:europe-geoglows-drainageline europe-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Europe',
    show=False
)

islands_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-e3910292be5e4fd79597c6c91cb084cf:islands-geoglows-catchment islands-geoglows-catchment,HS-e3910292be5e4fd79597c6c91cb084cf:islands-geoglows-drainageline islands-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Islands',
    show=False
)

japan_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-df5f3e52c51b419d8ee143b919a449b3:japan-geoglows-catchment japan-geoglows-catchment,HS-df5f3e52c51b419d8ee143b919a449b3:japan-geoglows-drainageline japan-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Japan',
    show=False
)

japan_shapefiles.add_to(m)

shapefile_control = folium.LayerControl()

shapefile_control.add_to(m)

m

# %%

# The code here reads the exported GeoJSON file drawn on the map, changes the projection, exports the GeoJSON to a shapefile, then reads the shapefile into a GeoDataFrame
# The code also reads the necessary shapefiles into GeoDataFrames.
gjson_file = geopandas.read_file("/home/kyler/Documents/gjson_files/data.geojson")
gjson_file = gjson_file.to_crs("EPSG:3857")

gjson_file = gjson_file.to_file("/home/kyler/Documents/shapefiles/gjson/gshape.shp")

gjson_shp = geopandas.read_file("/home/kyler/Documents/shapefiles/gjson/gshape.shp")

dl_shp = geopandas.read_file("zip:///home/kyler/Documents/drainagelines/japan-geoglows-drainageline.zip/japan-geoglows-drainageline/japan-geoglows-drainageline.shp")

ctch_shp = geopandas.read_file("zip:///home/kyler/Documents/catchments/japan-geoglows-catchment.zip/japan-geoglows-catchment/japan-geoglows-catchment.shp")


# Here the code generates representative points for each polygon in the catchment shapefile/GeoDataFrame
ctch_point = ctch_shp.representative_point()

# Here the points are exported to a shapefile, if one wishes to view these points in a GIS application. This line is unnecessary in the selection process.
ctch_point.to_file("/home/kyler/Documents/shapefiles/reppoint_shape/ctch/ctch_point.shp")

# The representative points are clipped to the GeoJSON shapefile
ctch_point_clip = geopandas.clip(ctch_point, gjson_shp)

# Using the clipped point GeoDataFrame, a boolean list is created. Polygons from the catchment shapefile that have the clipped points within their boundaries are marked as true.
# The polygons that do not have points within their boundaries are marked as false.
ctch_boo_list = ctch_point_clip.within(ctch_shp)

# The boolean list is then used to select certain polygons from the catchment GeoDataFrame. A new GeoDataFrame is created from this selection.
ctch_select = ctch_shp[ctch_boo_list]

# The created GeoDataFrame is then exported into a shapefile
ctch_select.to_file("/home/kyler/Documents/shapefiles/clip/ctch/ctch_select.shp")

# Here the selected catchment shapefile is read into its own GeoDataFrame.
ctch_select_shp = geopandas.read_file("/home/kyler/Documents/shapefiles/clip/ctch/ctch_select.shp")


# The process to select the corresponding drainagelines is very similar to the process used to select the correct catchments.

# Here, representative points for the drainagelines are created.
dl_point = dl_shp.representative_point()

# The points are exported to a shapefile. As before, this line of code serves no real purpose beyond being able to see the points in a GIS application
dl_point.to_file("/home/kyler/Documents/shapefiles/reppoint_shape/drain/dl_point.shp")

# The representative points are clipped to the selected catchments shapefile
dl_point_clip = geopandas.clip(dl_point, ctch_select_shp)

# Another boolean list is created. This time, any drainageline that intersects a clipped point is marked as true. Otherwise, it's marked as false.
dl_boo_list = dl_point_clip.intersects(dl_shp)

# Using the new boolean list, the appropriate drainagelines are selected and added to a new GeoDataFrame
dl_select = dl_shp[dl_boo_list]

# The GeoDataFrame is then exported into a shapefile.
dl_select.to_file("/home/kyler/Documents/shapefiles/clip/drain/dl_select.shp")


# %%
