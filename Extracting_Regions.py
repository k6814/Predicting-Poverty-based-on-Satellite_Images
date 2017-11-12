import json
import os
import re
import urllib
import cPickle as pickle
def Pulling_regions(Cluster_Json_file,page_no):
    clusters=json.load(open(Cluster_Json_file,"r"))
    final_coords={}
    for k,v in clusters[page_no].iteritems():
            final_coords[k]=[(re.sub(r'[\(\']',"",str(clust)).split(",")) for clust in clusters[page_no][k]]
    cluster_coords1={}
    for k2,v2 in final_coords.iteritems():
        cluster_coords1[k2]=[[x for x in i if x != ''] for i in final_coords[k2]]
    cluster_coords={}
    for k4 in cluster_coords1.keys():
        cluster_coords[k4]=[x for x in cluster_coords1[k4] if x != []] 
    flat_lists={}
    for k7 in cluster_coords.iterkeys():
        flat_lists[k7]=[item for sublist in cluster_coords[k7] for item in sublist]
    
    #lats={k7:l.split(" ")[2] for k7 in flat_lists.iterkeys() for l in flat_lists[k7]}
    #except IndexError:
    #    lats=None
    #longi={k7:l.split(" ")[1] for k7 in flat_lists.iterkeys() for l in flat_lists[k7]}
    return flat_lists
flat_list=Pulling_regions("Cluster_with_Countries.json","1")
values=flat_list['INDIA']
if not os.path.exists("lat_lon"):
    os.mkdir("lat_lon")
# flat_list['INDIA']
# flat_list['INDIA']
# flat_list['INDIA']
def give_me_latitude_longitude(lat,lon):
    c=0
    hi_web = urllib.urlopen('https://maps.googleapis.com/maps/api/geocode/json?latlng='+str(lat)+','+str(lon)+'&key=AIzaSyA7BPRI9wTwQI2fqknYJP_RWmfzyPsfDJY');
    #print hi_web
    with open("lat_lon/"+str(lat)+"_"+str(lon)+".json","wv") as hi_file:
        hi_file.write(hi_web.read())
    sample=json.load(open("lat_lon/"+str(lat)+"_"+str(lon)+".json","r"))
    try:
        for i in sample["results"][1]['address_components']:
            if'administrative_area_level_1' in i["types"]:
                return(i["long_name"].encode('utf-8'))
        c=c+1
    except IndexError:
        None
        

values=flat_list['INDIA'][7902:]
regions={}
for v in values:
    print v
    try:
        regions[(v.split(" ")[2],v.split(" ")[1])]=give_me_latitude_longitude(v.split(" ")[2],v.split(" ")[1])
    except IndexError:
        None
with open("Regions_new/Regions_7902_.p","wb") as f:
    pickle.dump(regions,f)