import json
import re
from io import BytesIO
from PIL import Image
import urllib
import os
import argparse
import sys

def Pulling_satellite_Images(Cluster_Json_file,page_no,Image_save_path):
    clusters=json.load(open(Cluster_Json_file,"r"))
    final_coords={}
    for k,v in clusters[page_no].iteritems():
            final_coords[k]=[(re.sub(r'[\(\']',"",str(clust)).split(",")) for clust in clusters[page_no][k]]
    cluster_coords1={}
    for k2,v2 in final_coords.iteritems():
        cluster_coords1[k2]=[[x for x in i if x != ''] for i in final_coords[k2]]
    cluster_coords={}
    for k4 in cluster_coords1.iterkeys():
        cluster_coords[k4]=[x for x in cluster_coords1[k4] if x != []]
    for k5 in cluster_coords.iterkeys():
        if not os.path.exists(Image_save_path):
            os.mkdir(Image_save_path)
        if not os.path.exists(Image_save_path+k5):
            os.mkdir(Image_save_path+k5)
        for c in cluster_coords[k5]:
            coords_path=Image_save_path+k5+"/"+c[0].split(" ")[2]+"_"+c[0].split(" ")[1]
            if not os.path.exists(coords_path):
                os.mkdir(coords_path)
            try:
                for lalo in c:
                    path=Image_save_path+k5+"/"+c[0].split(" ")[2]+"_"+c[0].split(" ")[1]+\
                    "/"+lalo.split(" ")[2]+"_"+lalo.split(" ")[1]+".png"
                    print path
                    if not os.path.exists(path):
                        url = "https://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center=" \
                        +lalo.split(" ")[2]+","+lalo.split(" ")[1]+"&zoom=15&size=512x512&key=AIzaSyCHkljUBCpcH3hokJnIV0rRwrcJ2M0_92M"
                        buff = BytesIO(urllib.urlopen(url).read())
                        image = Image.open(buff)
                        image.save(path)
            except:
                continue
if __name__=="__main__":
    a=argparse.ArgumentParser()
    a.add_argument("--Cluster_json_file",help="path to cluster json file")
    a.add_argument("--page_no",help="specify page no for api(0 to 3)")
    a.add_argument("--output_dir",help="output directory to save all Images")
    args=a.parse_args()
    
    if args.output_dir is None:
        a.print_help()
        sys.exit(1)
    Pulling_satellite_Images(args.Cluster_json_file,args.page_no,args.output_dir)