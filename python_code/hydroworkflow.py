#%%
import geopandas
import pandas
import folium
import folium.plugins
import os
import numpy
from timeit import default_timer as timer
# %%
from hs_restclient import HydroShare, HydroShareAuthBasic
auth = HydroShareAuthBasic(username='', password='*')
hs = HydroShare(auth=auth)

home_dir = os.path.expanduser("~")

if os.path.isdir(os.path.join(home_dir,'hydroviewer_creator')) == False:
    os.mkdir(os.path.join(home_dir,'hydroviewer_creator'))

proj_dir = os.path.join(home_dir,'hydroviewer_creator')
# %%
if os.path.isdir(os.path.join(proj_dir,'shapefiles')) == False:
    os.mkdir(os.path.join(proj_dir,'shapefiles'))

if os.path.isdir(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles')) == False:
    os.mkdir(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles'))

if os.path.isdir(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment')) == False:
    os.mkdir(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))

if os.path.isdir(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline')) == False:
    os.mkdir(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))

if os.path.isdir(os.path.join(proj_dir,'shapefiles','selected_shapefiles')) == False:
    os.mkdir(os.path.join(proj_dir,'shapefiles','selected_shapefiles'))

if os.path.isdir(os.path.join(proj_dir,'shapefiles','selected_shapefiles','catchment_select')) == False:
    os.mkdir(os.path.join(proj_dir,'shapefiles','selected_shapefiles','catchment_select'))

if os.path.isdir(os.path.join(proj_dir,'shapefiles','selected_shapefiles','drainageline_select')) == False:
    os.mkdir(os.path.join(proj_dir,'shapefiles','selected_shapefiles','drainageline_select'))

if os.path.isdir(os.path.join(proj_dir,'gjson_files')) == False:
    os.mkdir(os.path.join(proj_dir,'gjson_files'))

if os.path.isdir(os.path.join(proj_dir,'shapefiles','gjson_shapefiles')) == False:
    os.mkdir(os.path.join(proj_dir,'shapefiles','gjson_shapefiles'))

if os.path.isdir(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries')) == False:
    os.mkdir(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

if os.path.isdir(os.path.join(proj_dir,'shapefiles','reppoint_shapefile')) == False:
    os.mkdir(os.path.join(proj_dir,'shapefiles','reppoint_shapefile'))

if os.path.isdir(os.path.join(proj_dir,'shapefiles','reppoint_shapefile','ctch_point')) == False:
    os.mkdir(os.path.join(proj_dir,'shapefiles','reppoint_shapefile','ctch_point'))

if os.path.isdir(os.path.join(proj_dir,'shapefiles','reppoint_shapefile','dl_point')) == False:
    os.mkdir(os.path.join(proj_dir,'shapefiles','reppoint_shapefile','dl_point'))

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

central_america_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-36fae4f0e04d40ccb08a8dd1df88365e:central_america-geoglows-catchment central_america-geoglows-catchment,HS-36fae4f0e04d40ccb08a8dd1df88365e:central_america-geoglows-drainageline central_america-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Central America',
    show=False
).add_to(m)

central_asia_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-383bc50a88ae4711a8d834a322ced2d5:central_asia-geoglows-catchment central_asia-geoglows-catchment,HS-383bc50a88ae4711a8d834a322ced2d5:central_asia-geoglows-drainageline central_asia-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Central Asia',
    show=False
).add_to(m)

east_asia_shapefiles = folium.WmsTileLayer(
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

middle_east_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-6de72e805b34488ab1742dae64202a29:middle_east-geoglows-catchment middle_east-geoglows-catchment,HS-6de72e805b34488ab1742dae64202a29:middle_east-geoglows-drainageline middle_east-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='Middle East',
    show=False
).add_to(m)

north_america_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-43ae93136e10439fbf2530e02156caf0:north_america-geoglows-catchment north_america-geoglows-catchment,HS-43ae93136e10439fbf2530e02156caf0:north_america-geoglows-drainageline north_america-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='North America',
    show=False
).add_to(m)

south_america_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-94f7e730ea034706ae3497a75c764239:south_america-geoglows-catchment south_america-geoglows-catchment,HS-94f7e730ea034706ae3497a75c764239:south_america-geoglows-drainageline south_america-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='South America',
    show=False
).add_to(m)

south_asia_shapefiles = folium.WmsTileLayer(
    url=geoserver_url,
    layers='HS-e8f2896be57643eb91220351b961b494:south_asia-geoglows-catchment south_asia-geoglows-catchment,HS-e8f2896be57643eb91220351b961b494:south_asia-geoglows-drainageline south_asia-geoglows-drainageline',
    fmt='image/png',
    transparent=True,
    name='South Asia',
    show=False
).add_to(m)

west_asia_shapefiles = folium.WmsTileLayer(
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
gjson_file = geopandas.read_file(os.path.join(proj_dir,'gjson_files','saudi_arabia.json'))

# This changes the projection of the GeoJSON to match the shapefiles
gjson_file = gjson_file.to_crs("EPSG:3857")

# Exports the GeoJSON to a shapefile
gjson_file = gjson_file.to_file(os.path.join(proj_dir,'shapefiles','gjson_shapefiles','gshape.shp'))

# Reads the GeoJSON shapefile into a GeoDataFrame
gjson_shp = geopandas.read_file(os.path.join(proj_dir,'shapefiles','gjson_shapefiles','gshape.shp'))

print("Exported gjson shapefile")

# HydorShare Resource IDs
africa_id = '121bbce392a841178476001843e7510b'
australia_id = '9572eb7fa8744807962b9268593bd4ad'
central_america_id = '36fae4f0e04d40ccb08a8dd1df88365e'
central_asia_id = '383bc50a88ae4711a8d834a322ced2d5'
east_asia_id = '85ac5bf29cff4aa48a08b8aaeb8e3023'
europe_id = 'c14e1644a94744d8b3204a5be91acaed'
islands_id = 'e3910292be5e4fd79597c6c91cb084cf'
japan_id = 'df5f3e52c51b419d8ee143b919a449b3'
middle_east_id = '6de72e805b34488ab1742dae64202a29'
north_america_id = '43ae93136e10439fbf2530e02156caf0'
south_america_id = '94f7e730ea034706ae3497a75c764239'
south_asia_id = 'e8f2896be57643eb91220351b961b494'
west_asia_id = 'b62087b814804242a1005368d0ba1b82'

if os.path.isfile(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','africa-geoglows-boundary.zip')) == False:
    fname = 'africa-geoglows-boundary.zip'
    fpath = hs.getResourceFile(africa_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

if os.path.isfile(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','australia-geoglows-boundary.zip')) == False:
    fname = 'australia-geoglows-boundary.zip'
    fpath = hs.getResourceFile(australia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

if os.path.isfile(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','central_america-geoglows-boundary.zip')) == False:
    fname = 'central_america-geoglows-boundary.zip'
    fpath = hs.getResourceFile(central_america_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

if os.path.isfile(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','central_asia-geoglows-boundary.zip')) == False:
    fname = 'central_asia-geoglows-boundary.zip'
    fpath = hs.getResourceFile(central_asia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

if os.path.isfile(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','east_asia-geoglows-boundary.zip')) == False:
    fname = 'east_asia-geoglows-boundary.zip'
    fpath = hs.getResourceFile(east_asia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

if os.path.isfile(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','europe-geoglows-boundary.zip')) == False:
    fname = 'europe-geoglows-boundary.zip'
    fpath = hs.getResourceFile(europe_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

if os.path.isfile(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','islands-geoglows-boundary.zip')) == False:
    fname = 'islands-geoglows-boundary.zip'
    fpath = hs.getResourceFile(islands_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

if os.path.isfile(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','japan-geoglows-boundary.zip')) == False:
    fname = 'japan-geoglows-boundary.zip'
    fpath = hs.getResourceFile(japan_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

if os.path.isfile(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','middle_east-geoglows-boundary.zip')) == False:
    fname = 'middle_east-geoglows-boundary.zip'
    fpath = hs.getResourceFile(middle_east_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

if os.path.isfile(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','north_america-geoglows-boundary.zip')) == False:
    fname = 'north_america-geoglows-boundary.zip'
    fpath = hs.getResourceFile(north_america_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

if os.path.isfile(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','south_america-geoglows-boundary.zip')) == False:
    fname = 'south_america-geoglows-boundary.zip'
    fpath = hs.getResourceFile(south_america_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

if os.path.isfile(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','south_asia-geoglows-boundary.zip')) == False:
    fname = 'south_asia-geoglows-boundary.zip'
    fpath = hs.getResourceFile(south_asia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

if os.path.isfile(os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','west_asia-geoglows-boundary.zip')) == False:
    fname = 'west_asia-geoglows-boundary.zip'
    fpath = hs.getResourceFile(west_asia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries'))

print("All boundaries downloaded")

africa_bndry_gdf = geopandas.read_file("zip:///"+os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','africa-geoglows-boundary.zip','africa-geoglows-boundary.shp'))
australia_bndry_gdf = geopandas.read_file("zip:///"+os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','australia-geoglows-boundary.zip','australia-geoglows-boundary.shp'))
central_america_bndry_gdf = geopandas.read_file("zip:///"+os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','central_america-geoglows-boundary.zip','central_america-geoglows-boundary.shp'))
central_asia_bndry_gdf = geopandas.read_file("zip:///"+os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','central_asia-geoglows-boundary.zip','central_asia-geoglows-boundary.shp'))
east_asia_bndry_gdf = geopandas.read_file("zip:///"+os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','east_asia-geoglows-boundary.zip','east_asia-geoglows-boundary.shp'))
europe_bndry_gdf = geopandas.read_file("zip:///"+os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','europe-geoglows-boundary.zip','europe-geoglows-boundary.shp'))
islands_bndry_gdf = geopandas.read_file("zip:///"+os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','islands-geoglows-boundary.zip','islands-geoglows-boundary.shp'))
japan_bndry_gdf = geopandas.read_file("zip:///"+os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','japan-geoglows-boundary.zip','japan-geoglows-boundary.shp'))
middle_east_bndry_gdf = geopandas.read_file("zip:///"+os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','middle_east-geoglows-boundary.zip','middle_east-geoglows-boundary.shp'))
north_america_bndry_gdf = geopandas.read_file("zip:///"+os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','north_america-geoglows-boundary.zip','north_america-geoglows-boundary.shp'))
south_america_bndry_gdf = geopandas.read_file("zip:///"+os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','south_america-geoglows-boundary.zip','south_america-geoglows-boundary.shp'))
south_asia_bndry_gdf = geopandas.read_file("zip:///"+os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','south_asia-geoglows-boundary.zip','south_asia-geoglows-boundary.shp'))
west_asia_bndry_gdf = geopandas.read_file("zip:///"+os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','boundaries','west_asia-geoglows-boundary.zip','west_asia-geoglows-boundary.shp'))

if gjson_shp.intersects(africa_bndry_gdf)[0]:
    fname = 'africa-geoglows-catchment.zip'
    fpath = hs.getResourceFile(africa_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))
    ctch_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment','africa-geoglows-catchment.zip','africa-geoglows-catchment.shp')
    fname = 'africa-geoglows-drainageline.zip'
    fpath = hs.getResourceFile(africa_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))
    dl_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline','africa-geoglows-drainageline.zip','africa-geoglows-drainageline.shp')

elif gjson_shp.intersects(australia_bndry_gdf)[0]:
    fname = 'australia-geoglows-catchment.zip'
    fpath = hs.getResourceFile(australia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))
    ctch_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment','australia-geoglows-catchment.zip','australia-geoglows-catchment.shp')
    fname = 'australia-geoglows-drainageline.zip'
    fpath = hs.getResourceFile(australia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))
    dl_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline','australia-geoglows-drainageline.zip','australia-geoglows-drainageline.shp')

elif gjson_shp.intersects(central_america_bndry_gdf)[0]:
    fname = 'central_america-geoglows-catchment.zip'
    fpath = hs.getResourceFile(central_america_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))
    ctch_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment','central_america-geoglows-catchment.zip','central_america-geoglows-catchment.shp')
    fname = 'central_america-geoglows-drainageline.zip'
    fpath = hs.getResourceFile(central_america_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))
    dl_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline','central_america-geoglows-drainageline.zip','central_america-geoglows-drainageline.shp')

elif gjson_shp.intersects(central_asia_bndry_gdf)[0]:
    fname = 'central_asia-geoglows-catchment.zip'
    fpath = hs.getResourceFile(central_asia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))
    ctch_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment','central_asia-geoglows-catchment.zip','central_asia-geoglows-catchment.shp')
    fname = 'central_asia-geoglows-drainageline.zip'
    fpath = hs.getResourceFile(central_asia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))
    dl_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline','central_asia-geoglows-drainageline.zip','central_asia-geoglows-drainageline.shp')

elif gjson_shp.intersects(east_asia_bndry_gdf)[0]:
    fname = 'east_asia-geoglows-catchment.zip'
    fpath = hs.getResourceFile(east_asia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))
    ctch_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment','east_asia-geoglows-catchment.zip','east_asia-geoglows-catchment.shp')
    fname = 'east_asia-geoglows-drainageline.zip'
    fpath = hs.getResourceFile(east_asia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))
    dl_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline','east_asia-geoglows-drainageline.zip','east_asia-geoglows-drainageline.shp')

elif gjson_shp.intersects(europe_bndry_gdf)[0]:
    fname = 'europe-geoglows-catchment.zip'
    fpath = hs.getResourceFile(europe_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))
    ctch_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment','europe-geoglows-catchment.zip','europe-geoglows-catchment.shp')
    fname = 'europe-geoglows-drainageline.zip'
    fpath = hs.getResourceFile(europe_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))
    dl_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline','europe-geoglows-drainageline.zip','europe-geoglows-drainageline.shp')

elif gjson_shp.intersects(islands_bndry_gdf)[0]:
    fname = 'islands-geoglows-catchment.zip'
    fpath = hs.getResourceFile(islands_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))
    ctch_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment','islands-geoglows-catchment.zip','islands-geoglows-catchment.shp')
    fname = 'islands-geoglows-drainageline.zip'
    fpath = hs.getResourceFile(islands_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))
    dl_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline','islands-geoglows-drainageline.zip','islands-geoglows-drainageline.shp')

elif gjson_shp.intersects(japan_bndry_gdf)[0]:
    fname = 'japan-geoglows-catchment.zip'
    fpath = hs.getResourceFile(japan_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))
    ctch_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment','japan-geoglows-catchment.zip','japan-geoglows-catchment.shp')
    fname = 'japan-geoglows-drainageline.zip'
    fpath = hs.getResourceFile(japan_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))
    dl_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline','japan-geoglows-drainageline.zip','japan-geoglows-drainageline.shp')

elif gjson_shp.intersects(middle_east_bndry_gdf)[0]:
    fname = 'middle_east-geoglows-catchment.zip'
    fpath = hs.getResourceFile(middle_east_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))
    ctch_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment','middle_east-geoglows-catchment.zip','middle_east-geoglows-catchment.shp')
    fname = 'middle_east-geoglows-drainageline.zip'
    fpath = hs.getResourceFile(middle_east_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))
    dl_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline','middle_east-geoglows-drainageline.zip','middle_east-geoglows-drainageline.shp')

elif gjson_shp.intersects(north_america_bndry_gdf)[0]:
    fname = 'north_america-geoglows-catchment.zip'
    fpath = hs.getResourceFile(north_america_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))
    ctch_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment','north_america-geoglows-catchment.zip','north_america-geoglows-catchment.shp')
    fname = 'north_america-geoglows-drainageline.zip'
    fpath = hs.getResourceFile(north_america_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))
    dl_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline','north_america-geoglows-drainageline.zip','north_america-geoglows-drainageline.shp')

elif gjson_shp.intersects(south_america_bndry_gdf)[0]:
    fname = 'south_america-geoglows-catchment.zip'
    fpath = hs.getResourceFile(south_america_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))
    ctch_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment','south_america-geoglows-catchment.zip','south_america-geoglows-catchment.shp')
    fname = 'south_america-geoglows-drainageline.zip'
    fpath = hs.getResourceFile(south_america_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))
    dl_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline','south_america-geoglows-drainageline.zip','south_america-geoglows-drainageline.shp')

elif gjson_shp.intersects(south_asia_bndry_gdf)[0]:
    fname = 'south_asia-geoglows-catchment.zip'
    fpath = hs.getResourceFile(south_asia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))
    ctch_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment','south_asia-geoglows-catchment.zip','south_asia-geoglows-catchment.shp')
    fname = 'south_asia-geoglows-drainageline.zip'
    fpath = hs.getResourceFile(south_asia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))
    dl_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline','south_asia-geoglows-drainageline.zip','south_asia-geoglows-drainageline.shp')

elif gjson_shp.intersects(west_asia_bndry_gdf)[0]:
    fname = 'west_asia-geoglows-catchment.zip'
    fpath = hs.getResourceFile(west_asia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment'))
    ctch_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','catchment','west_asia-geoglows-catchment.zip','west_asia-geoglows-catchment.shp')
    fname = 'west_asia-geoglows-drainageline.zip'
    fpath = hs.getResourceFile(west_asia_id,fname,destination=os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline'))
    dl_path = os.path.join(proj_dir,'shapefiles','downloaded_shapefiles','drainageline','west_asia-geoglows-drainageline.zip','west_asia-geoglows-drainageline.shp')

print("Catchments and drainagelines downloaded")
# The two lines below read the downloaded files for the catchment and drainageline shapefiles into GeoDataFrames
dl_shp = geopandas.read_file("zip:///"+dl_path)

ctch_shp = geopandas.read_file("zip:///"+ctch_path)

print(ctch_path)
print(dl_path)

# %%

# Here the code generates representative points for each polygon in the catchment shapefile/GeoDataFrame
ctch_point = ctch_shp.representative_point()

# Here the points are exported to a shapefile, if one wishes to view these points in a GIS application. This line is unnecessary in the selection process.
ctch_point.to_file(os.path.join(proj_dir,'shapefiles','reppoint_shapefile','ctch_point','ctch_reppoint.shp'))

# The representative points are clipped to the GeoJSON shapefile
ctch_point_clip = geopandas.clip(ctch_point, gjson_shp)

# Using the clipped point GeoDataFrame, a boolean list is created. Polygons from the catchment shapefile that have the clipped points within their boundaries are marked as true.
# The polygons that do not have points within their boundaries are marked as false.
ctch_boo_list = ctch_point_clip.within(ctch_shp)

# The boolean list is then used to select certain polygons from the catchment GeoDataFrame. A new GeoDataFrame is created from this selection.
ctch_select = ctch_shp[ctch_boo_list]

# The created GeoDataFrame is then exported into a shapefile
ctch_select.to_file(os.path.join(proj_dir,'shapefiles','selected_shapefiles','catchment_select','ctch_select.shp'))

# Here the selected catchment shapefile is read into its own GeoDataFrame.
ctch_select_shp = geopandas.read_file(os.path.join(proj_dir,'shapefiles','selected_shapefiles','catchment_select','ctch_select.shp'))

print("Catchments exported")
# The process to select the corresponding drainagelines is very similar to the process used to select the correct catchments.

ctch_select_df = pandas.DataFrame(ctch_select_shp, columns=['COMID'])

dl_shp_df = pandas.DataFrame(dl_shp)

ctch_select_comid_list = ctch_select_df['COMID'].to_list()

dl_select_df = dl_shp_df.loc[dl_shp_df['COMID'].isin(ctch_select_comid_list)]

dl_select = geopandas.GeoDataFrame(dl_select_df)

dl_select.to_file(os.path.join(proj_dir,'shapefiles','selected_shapefiles','drainageline_select','dl_select.shp'))

# %%
# Zip file
from zipfile import ZipFile

ctch_zip = ZipFile(os.path.join(proj_dir,'shapefiles','selected_shapefiles','catchment_select','catchment_select.zip'),'w')

ctch_zip.write(os.path.join(proj_dir,'shapefiles','selected_shapefiles','catchment_select','ctch_select.cpg'),arcname='ctch_select.cpg')
ctch_zip.write(os.path.join(proj_dir,'shapefiles','selected_shapefiles','catchment_select','ctch_select.dbf'),arcname='ctch_select.dbf')
ctch_zip.write(os.path.join(proj_dir,'shapefiles','selected_shapefiles','catchment_select','ctch_select.prj'),arcname='ctch_select.prj')
ctch_zip.write(os.path.join(proj_dir,'shapefiles','selected_shapefiles','catchment_select','ctch_select.shp'),arcname='ctch_select.shp')
ctch_zip.write(os.path.join(proj_dir,'shapefiles','selected_shapefiles','catchment_select','ctch_select.shx'),arcname='ctch_select.shx')

ctch_zip.close()

dl_zip = ZipFile(os.path.join(proj_dir,'shapefiles','selected_shapefiles','drainageline_select','drainageline_select.zip'),'w')

dl_zip.write(os.path.join(proj_dir,'shapefiles','selected_shapefiles','drainageline_select','dl_select.cpg'),arcname='dl_select.cpg')
dl_zip.write(os.path.join(proj_dir,'shapefiles','selected_shapefiles','drainageline_select','dl_select.dbf'),arcname='dl_select.dbf')
dl_zip.write(os.path.join(proj_dir,'shapefiles','selected_shapefiles','drainageline_select','dl_select.prj'),arcname='dl_select.prj')
dl_zip.write(os.path.join(proj_dir,'shapefiles','selected_shapefiles','drainageline_select','dl_select.shp'),arcname='dl_select.shp')
dl_zip.write(os.path.join(proj_dir,'shapefiles','selected_shapefiles','drainageline_select','dl_select.shx'),arcname='dl_select.shx')

dl_zip.close()

print("All files zipped")
# %%
# Add file to HydroShare resource
custom_resource_id = '3f30f822c7594a6c9b8c3da73a14da6f'

fpath = os.path.join(proj_dir,'shapefiles','selected_shapefiles','catchment_select','catchment_select.zip')
hs.addResourceFile(custom_resource_id,fpath)

fpath = os.path.join(proj_dir,'shapefiles','selected_shapefiles','drainageline_select','drainageline_select.zip')
hs.addResourceFile(custom_resource_id,fpath)

# Make resource public
result = hs.setAccessRules(custom_resource_id,public=True)

# Unzip resource file
options = {
    "zip_with_rel_path": "drainageline_select.zip",
    "remove_original_zip": False,
    "overwrite": False
}

result = hs.resource('3f30f822c7594a6c9b8c3da73a14da6f').functions.unzip(options)

options = {
    "zip_with_rel_path": "catchment_select.zip",
    "remove_original_zip": False,
    "overwrite": False
}

result = hs.resource('3f30f822c7594a6c9b8c3da73a14da6f').functions.unzip(options)
# %%
# Add shapefiles to geoserver
from geoserver.catalog import Catalog
import geoserver.util

cat = Catalog("https://tethys-staging.byu.edu/geoserver/rest/")
new_workspace = cat.create_workspace("hydroviewertests","https://tethys-staging.byu.edu/geoserver/rest/")
# %%
workspace = cat.get_workspace("hydroviewertests")
shapefile_plus_sidecars = geoserver.util.shapefile_and_friends(os.path.join(proj_dir,'shapefiles','selected_shapefiles','drainageline_select','dl_select'))
cat.create_featurestore('dl_select', workspace=workspace, data=shapefile_plus_sidecars)
# %%
workspace = cat.get_workspace("hydroviewertests")
shapefile_plus_sidecars = geoserver.util.shapefile_and_friends(os.path.join(proj_dir,'shapefiles','selected_shapefiles','catchment_select','ctch_select'))
cat.create_featurestore('ctch_select', workspace=workspace, data=shapefile_plus_sidecars)

# %%

# This code block will delete the layers and stores on the GeoServer

# dl_store = cat.get_store(name="dl_select",workspace="hydroviewertests")
# cat.delete(dl_store, recurse=True)

# ctch_store = cat.get_store(name="ctch_select",workspace="hydroviewertests")
# cat.delete(ctch_store, recurse=True)

# %%
import folium
import folium.plugins

nm = folium.Map(
    location=[40.76524, 140.399],
    tiles='',
    zoom_start=3
)

# Adds basemaps to map
stamen_layer = folium.TileLayer(
    tiles='Stamen Terrain',
    name='Stamen Terrain'
).add_to(nm)

stamen_layerwc = folium.TileLayer(
    tiles='Stamen Watercolor',
    name='Stamen Watercolor'
).add_to(nm)

tethys_geoserver_url = "https://tethys-staging.byu.edu/geoserver/wms"

select_shapefiles = folium.WmsTileLayer(
    url=tethys_geoserver_url,
    layers='hydroviewertests:ctch_select,hydroviewertests:dl_select',
    fmt='image/png',
    transparent=True,
    name='Selected area',
    show=True
).add_to(nm)

layercontroller = folium.LayerControl().add_to(nm)

nm
# %%
nm.save(os.path.join(proj_dir,'app_code','hv_selector.html'))
# %%
