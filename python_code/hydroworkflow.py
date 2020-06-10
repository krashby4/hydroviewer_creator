#%%
import geopandas
import folium
import folium.plugins
import os

# %%
home_dir = os.path.expanduser("~")

if os.path.isdir(os.path.join(home_dir,'hydroviewer_creator')) == False:
    os.mkdir(os.path.join(home_dir,'hydroviewer_creator'))

if os.path.isdir(os.path.join(home_dir,'hydroviewer_creator', 'shapefiles')) == False:
    os.mkdir(os.path.join(home_dir,'hydroviewer_creator', 'shapefiles'))

if os.path.isdir(os.path.join(home_dir,'hydroviewer_creator','shapefiles','downloaded_shapefiles')) == False:
    os.mkdir(os.path.join(home_dir,'hydroviewer_creator','shapefiles','downloaded_shapefiles'))

if os.path.isdir(os.path.join(home_dir,'hydroviewer_creator','shapefiles','downloaded_shapefiles','catchment')) == False:
    os.mkdir(os.path.join(home_dir,'hydroviewer_creator','shapefiles','downloaded_shapefiles','catchment'))

if os.path.isdir(os.path.join(home_dir,'hydroviewer_creator','shapefiles','downloaded_shapefiles','drainageline')) == False:
    os.mkdir(os.path.join(home_dir,'hydroviewer_creator','shapefiles','downloaded_shapefiles','drainageline'))

if os.path.isdir(os.path.join(home_dir,'hydroviewer_creator','shapefiles','selected_shapefiles')) == False:
    os.mkdir(os.path.join(home_dir,'hydroviewer_creator','shapefiles','selected_shapefiles'))

if os.path.isdir(os.path.join(home_dir,'hydroviewer_creator','shapefiles','selected_shapefiles','catchment_select')) == False:
    os.mkdir(os.path.join(home_dir,'hydroviewer_creator','shapefiles','selected_shapefiles','catchment_select'))

if os.path.isdir(os.path.join(home_dir,'hydroviewer_creator','shapefiles','selected_shapefiles','drainageline_select')) == False:
    os.mkdir(os.path.join(home_dir,'hydroviewer_creator','shapefiles','selected_shapefiles','drainageline_select'))

if os.path.isdir(os.path.join(home_dir,'hydroviewer_creator','gjson_files')) == False:
    os.mkdir(os.path.join(home_dir,'hydroviewer_creator','gjson_files'))
# %%
# Creates the map
m = folium.Map(
    location=[40.76524, 140.399], #This coordinate shows example issue with catchments
    tiles='',
    zoom_start=3
)

# Define draw control options
draw_control = folium.plugins.Draw(
    export=True
).add_to(m)

# Defines url to HydroShare Geoserver
geoserver_url = "https://geoserver.hydroshare.org/geoserver/wms"

# Defines basemaps
stamen_layer = folium.TileLayer(
    tiles='Stamen Terrain',
    name='Stamen Terrain'
).add_to(m)

stamen_layerwc = folium.TileLayer(
    tiles='Stamen Watercolor',
    name='Stamen Watercolor'
).add_to(m)

# WMS Layers for all the shapefiles. Adds both draingeline and catchments simultaneously.
africa_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-121bbce392a841178476001843e7510b:africa-geoglows-catchment africa-geoglows-catchment,HS-121bbce392a841178476001843e7510b:africa-geoglows-drainageline africa-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Africa',
    show=False
).add_to(m)

australia_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-9572eb7fa8744807962b9268593bd4ad:australia-geoglows-catchment australia-geoglows-catchment,HS-9572eb7fa8744807962b9268593bd4ad:australia-geoglows-drainageline australia-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Australia',
    show=False
).add_to(m)

centralamerica_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-36fae4f0e04d40ccb08a8dd1df88365e:central_america-geoglows-catchment central_america-geoglows-catchment,HS-36fae4f0e04d40ccb08a8dd1df88365e:central_america-geoglows-drainageline central_america-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Central America',
    show=False
).add_to(m)

centralasia_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-383bc50a88ae4711a8d834a322ced2d5:central_asia-geoglows-catchment central_asia-geoglows-catchment,HS-383bc50a88ae4711a8d834a322ced2d5:central_asia-geoglows-drainageline central_asia-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Central Asia',
    show=False
).add_to(m)

eastasia_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-85ac5bf29cff4aa48a08b8aaeb8e3023:east_asia-geoglows-catchment east_asia-geoglows-catchment,HS-85ac5bf29cff4aa48a08b8aaeb8e3023:east_asia-geoglows-drainageline east_asia-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='East Asia',
    show=False
).add_to(m)

europe_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-c14e1644a94744d8b3204a5be91acaed:europe-geoglows-catchment europe-geoglows-catchment,HS-c14e1644a94744d8b3204a5be91acaed:europe-geoglows-drainageline europe-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Europe',
    show=False
).add_to(m)

islands_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-e3910292be5e4fd79597c6c91cb084cf:islands-geoglows-catchment islands-geoglows-catchment,HS-e3910292be5e4fd79597c6c91cb084cf:islands-geoglows-drainageline islands-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Islands',
    show=False
).add_to(m)

japan_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-df5f3e52c51b419d8ee143b919a449b3:japan-geoglows-catchment japan-geoglows-catchment,HS-df5f3e52c51b419d8ee143b919a449b3:japan-geoglows-drainageline japan-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Japan',
    show=False
).add_to(m)

middleeast_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-6de72e805b34488ab1742dae64202a29:middle_east-geoglows-catchment middle_east-geoglows-catchment,HS-6de72e805b34488ab1742dae64202a29:middle_east-geoglows-drainageline middle_east-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Middle East',
    show=False
).add_to(m)

northamerica_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-43ae93136e10439fbf2530e02156caf0:north_america-geoglows-catchment north_america-geoglows-catchment,HS-43ae93136e10439fbf2530e02156caf0:north_america-geoglows-drainageline north_america-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='North America',
    show=False
).add_to(m)

southamerica_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-94f7e730ea034706ae3497a75c764239:south_america-geoglows-catchment south_america-geoglows-catchment,HS-94f7e730ea034706ae3497a75c764239:south_america-geoglows-drainageline south_america-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='South America',
    show=False
).add_to(m)

southasia_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-e8f2896be57643eb91220351b961b494:south_asia-geoglows-catchment south_asia-geoglows-catchment,HS-e8f2896be57643eb91220351b961b494:south_asia-geoglows-drainageline south_asia-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='South Asia',
    show=False
).add_to(m)

westasia_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-b62087b814804242a1005368d0ba1b82:west_asia-geoglows-catchment west_asia-geoglows-catchment,HS-b62087b814804242a1005368d0ba1b82:west_asia-geoglows-drainageline west_asia-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='West Asia',
    show=False
).add_to(m)

layercontroller = folium.LayerControl().add_to(m)

# Call and display map
m

# %%

# The code here reads the exported GeoJSON file drawn on the map
gjson_file = geopandas.read_file("/home/kyler/Documents/gjson_files/data.geojson")

# This changes the projection of the GeoJSON to match the shapefiles
gjson_file = gjson_file.to_crs("EPSG:3857")

# Exports the GeoJSON to a shapefile
gjson_file = gjson_file.to_file("/home/kyler/Documents/shapefiles/gjson/gshape.shp")

# Reads the GeoJSON shapefile into a GeoDataFrame
gjson_shp = geopandas.read_file("/home/kyler/Documents/shapefiles/gjson/gshape.shp")

africa_bndry_shp = geopandas.read_file("zip:///home/kyler/Documents/boundaries/africa-geoglows-boundary.shp.zip/africa-geoglows-boundary.shp/africa-geoglows-boundary.shp")
australia_bndry_shp = geopandas.read_file("zip:///home/kyler/Documents/boundaries/australia-geoglows-boundary.shp.zip/australia-geoglows-boundary.shp/australia-geoglows-boundary.shp")
centralam_bndry_shp = geopandas.read_file("zip:///home/kyler/Documents/boundaries/central_america-geoglows-boundary.shp.zip/central_america-geoglows-boundary.shp/central_america-geoglows-boundary.shp")
centralas_bndry_shp = geopandas.read_file("zip:///home/kyler/Documents/boundaries/central_asia-geoglows-boundary.shp.zip/central_asia-geoglows-boundary.shp/central_asia-geoglows-boundary.shp")
eastas_bndry_shp = geopandas.read_file("zip:///home/kyler/Documents/boundaries/east_asia-geoglows-boundary.shp.zip/east_asia-geoglows-boundary.shp/east_asia-geoglows-boundary.shp")
europe_bndry_shp = geopandas.read_file("zip:///home/kyler/Documents/boundaries/europe-geoglows-boundary.shp.zip/europe-geoglows-boundary.shp/europe-geoglows-boundary.shp")
islands_bndry_shp = geopandas.read_file("zip:///home/kyler/Documents/boundaries/islands-geoglows-boundary.shp.zip/islands-geoglows-boundary.shp/islands-geoglows-boundary.shp")
japan_bndry_shp = geopandas.read_file("zip:///home/kyler/Documents/boundaries/japan-geoglows-boundary.shp.zip/japan-geoglows-boundary.shp/japan-geoglows-boundary.shp")
mideast_bndry_shp = geopandas.read_file("zip:///home/kyler/Documents/boundaries/middle_east-geoglows-boundary.shp.zip/middle_east-geoglows-boundary.shp/middle_east-geoglows-boundary.shp")
namerica_bndry_shp = geopandas.read_file("zip:///home/kyler/Documents/boundaries/north_america-geoglows-boundary.shp.zip/north_america-geoglows-boundary.shp/north_america-geoglows-boundary.shp")
samerica_bndry_shp = geopandas.read_file("zip:///home/kyler/Documents/boundaries/south_america-geoglows-boundary.shp.zip/south_america-geoglows-boundary.shp/south_america-geoglows-boundary.shp")
sasia_bndry_shp = geopandas.read_file("zip:///home/kyler/Documents/boundaries/south_asia-geoglows-boundary.shp.zip/south_asia-geoglows-boundary.shp/south_asia-geoglows-boundary.shp")
wasia_bndry_shp = geopandas.read_file("zip:///home/kyler/Documents/boundaries/west_asia-geoglows-boundary.shp.zip/west_asia-geoglows-boundary.shp/west_asia-geoglows-boundary.shp")


# %%
if gjson_shp.intersects(africa_bndry_shp)[0]==True:
    dl_url = "zip:///home/kyler/Documents/drainagelines/africa_drainageline.zip/africa_drainageline.shp"
    ctch_url = "zip:///home/kyler/Documents/catchments/africa_catchment.zip/africa_catchment.shp"

elif gjson_shp.intersects(australia_bndry_shp)[0]==True:
    dl_url = "zip:///home/kyler/Documents/drainagelines/australia_drainageline.zip/australia_drainageline.shp"
    ctch_url = "zip:///home/kyler/Documents/catchments/australia_catchment.zip/australia_catchment.shp"

elif gjson_shp.intersects(centralam_bndry_shp)[0]==True:
    dl_url = "zip:///home/kyler/Documents/drainagelines/centralam_drainageline.zip/centralam_drainageline.shp"
    ctch_url = "zip:///home/kyler/Documents/catchments/centralam_catchment.zip/centralam_catchment.shp"

elif gjson_shp.intersects(centralas_bndry_shp)[0]==True:
    dl_url = "zip:///home/kyler/Documents/drainagelines/centralasia_drainageline.zip/centralasia_drainageline.shp"
    ctch_url = "zip:///home/kyler/Documents/catchments/centralasia_catchment.zip/centralasia_catchment.shp"

elif gjson_shp.intersects(eastas_bndry_shp)[0]==True:
    dl_url = "zip:///home/kyler/Documents/drainagelines/eastasia_drainageline.zip/eastasia_drainageline.shp"
    ctch_url = "zip:///home/kyler/Documents/catchments/eastasia_catchment.zip/eastasia_catchment.shp"

elif gjson_shp.intersects(europe_bndry_shp)[0]==True:
    dl_url = "zip:///home/kyler/Documents/drainagelines/europe_drainageline.zip/europe_drainageline.shp"
    ctch_url = "zip:///home/kyler/Documents/catchments/europe_catchment.zip/europe_catchment.shp"

elif gjson_shp.intersects(islands_bndry_shp)[0]==True:
    dl_url = "zip:///home/kyler/Documents/drainagelines/islands_drainageline.zip/islands_drainageline.shp"
    ctch_url = "zip:///home/kyler/Documents/catchmentsislands_catchment.zip/islands_catchment.shp"

elif gjson_shp.intersects(japan_bndry_shp)[0]==True:
    dl_url = "zip:///home/kyler/Documents/drainagelines/japan_drainageline.zip/japan_drainageline.shp"
    ctch_url = "zip:///home/kyler/Documents/catchments/japan_catchment.zip/japan_catchment.shp"

elif gjson_shp.intersects(mideast_bndry_shp)[0]==True:
    dl_url = "zip:///home/kyler/Documents/drainagelines/middleeast_drainageline.zip/middleeast_drainageline.shp"
    ctch_url = "zip:///home/kyler/Documents/catchments/middleeast_catchment.zip/middleeast_catchment.shp"

elif gjson_shp.intersects(namerica_bndry_shp)[0]==True:
    dl_url = "zip:///home/kyler/Documents/drainagelines/northamerica_drainageline.zip/northamerica_drainageline.shp"
    ctch_url = "zip:///home/kyler/Documents/catchments/northamerica_catchment.zip/northamerica_catchment.shp"

elif gjson_shp.intersects(samerica_bndry_shp)[0]==True:
    dl_url = "zip:///home/kyler/Documents/drainagelines/samerica_drainageline.zip/samerica_drainageline.shp"
    ctch_url = "zip:///home/kyler/Documents/catchments/samerica_catchment.zip/samerica_catchment.shp"

elif gjson_shp.intersects(sasia_bndry_shp)[0]==True:
    dl_url = "zip:///home/kyler/Documents/drainagelines/southasia_drainageline.zip/southasia_drainageline.shp"
    ctch_url = "zip:///home/kyler/Documents/catchments/southasia_catchment.zip/southasia_catchment.shp"

elif gjson_shp.intersects(wasia_bndry_shp)[0]==True:
    dl_url = "zip:///home/kyler/Documents/drainagelines/wasia_drainageline.zip/wasia_drainageline.shp"
    ctch_url = "zip:///home/kyler/Documents/catchments/wasia_catchment.zip/wasia_catchment.shp"


# %%

# The two lines below read the downloaded files for the catchment and drainageline shapefiles into GeoDataFrames
dl_shp = geopandas.read_file(dl_url)

ctch_shp = geopandas.read_file(ctch_url)

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

dl_select_shp = geopandas.read_file("/home/kyler/Documents/shapefiles/clip/drain/dl_select.shp")

# %%
nm = folium.Map(
    location=[40.76524, 140.399],
    tiles='',
    zoom_start=3
)

# Adds basemaps to map
stamen_layer.add_to(nm)

ctch_select_shp.to_file("/home/kyler/Documents/gjson_files/ctch.geojson", driver='GeoJSON')

dl_select_shp.to_file("/home/kyler/Documents/gjson_files/dl.geojson", driver='GeoJSON')

ctch_select_gjson = geopandas.read_file("/home/kyler/Documents/gjson_files/ctch.geojson")

dl_select_gjson = geopandas.read_file("/home/kyler/Documents/gjson_files/dl.geojson")

folium.Choropleth(
    geo_data=ctch_select_gjson,
    fill_color='#EB9D00',
    highlight=True,
    name='Selected catchments'
).add_to(nm)

newshapefile_control = folium.LayerControl()

newshapefile_control.add_to(nm)
 
nm
# %%
nm.save('/home/kyler/hydroviewer_creator/app_code/hv_selector.html')

# %%