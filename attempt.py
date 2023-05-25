import csv
with open("assets/Fussabdruck_konvertiert.csv") as csvdatei:
    csv_reader_object = csv.DictReader(csvdatei)
    file= open("programm.html","w")
    #Head und Sources
    file.write('<html>\n<head>\n<script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>'
    +'\n<script src="https://unpkg.com/aframe-globe-component/dist/aframe-globe-component.min.js"></script>'
    +'\n<script src="https://unpkg.com/aframe-geojson-component/dist/aframe-geojson-component.min.js"></script>'
    +'\n<script src="https://cdn.rawgit.com/tizzle/aframe-orbit-controls-component/v0.1.14/dist/aframe-orbit-controls-component.min.js"></script>'
    +'\n<script src="https://d3js.org/d3.v6.min.js"></script>'
    +'\n<script src="https://d3js.org/d3-dsv.v2.min.js"></script>'
    +'\n<script src="https://d3js.org/d3-fetch.v2.min.js"></script>' 
    +'\n<script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script>\n</head>'

    #Body
    +'\n<body>\n<a-scene>\n<a-assets>\n<a-assets-item id="geo-json" src="assets/world-50m.v1.json"></a-asset-item>'
    +'\n<img id="sky" src="assets/stars.jpg"/>\n<img id="worldmapfloor" src="assets/earthmap1.jpg"/>\n</a-assets>'
    +'\n<a-sky src="#sky"></a-sky>'
    +'\n<a-plane material="color:#FFFFFF; src: #worldmapfloor;" rotation="-90 0 0" scale="360 180 0" class="not-clickable"></a-plane>'
    +'\n<a-entity geometry="primitive: plane;" position="0 0.01 0" rotation="-90 0 0" scale="360 180 0" material="color: yellow; shader: flat" geojson="src: #geo-json; topologyObject: countries; projection: geoEquirectangular" class="not-clickable"></a-entity>'
    +'\n<a-entity position="0 4 5">\n<a-camera>\n<a-cursor id="cursor" color="#3B3B3B" raycaster="objects: .clickable">'
    +'\n<a-text position="0 0.2 0" width="1" color="white" align="center" id="texthud1" value="Land" visible="false">'
    +'\n<a-text position="0 -0.05 0" width="1" color="white" align="center" id="texthud2" value="Hoehe" visible="false"></a-text>'
    +'\n</a-text>\n</a-cursor>\n</a-camera>\n</a-entity>')

    
    for row in csv_reader_object:
        country= row["Land"]
        footprint=row["Oekologischer_Fussabdruck"]
        footprint=str(round(float(footprint),3))
        factor=1.5
        bar_height=str(float(footprint)*factor)
        latitude=row["Breitengrade"]
        longitude=row["Laengengrade"]
        height_position=float(bar_height)/2
        text_position=str(height_position*(-1)+0.01)
        
        str_height_position=str(height_position)
        if (latitude[0]=="-"):
            latitude=latitude[1:len(latitude)]
        else :
        	latitude= "-"+latitude

        if(float(footprint)<1.7):
            color="#bbb88f"
        elif ((float(footprint)>=1.7) & (float(footprint)<=3.4)):
            color="#ba9c55"
        elif ((float(footprint)>3.4) & (float(footprint)<=5.1)):
            color="#ba5828"
        elif((float(footprint)>5.1) & (float(footprint)<=6.7)):
            color="#b73c20"
        elif(float(footprint)>6.7):
            color="#5e001c"

            
        #print("hallo "+country+ " " + footprint+" " +latitude+ " " + longitude)
        #box-bars
        #string='<a-box color="red" depth="0.3" height='+footprint+' width="0.3" position="'+latitude+ ' '+str_height_position +' '+ longitude+'"'+'\n event-set__enter1="_event: mouseenter; _target: #texthud1; value:'+country+'; visible: true; "'+'\nevent-set__enter2= "_event: mouseenter; _target: #texthud2; value:'+footprint+'; visible: true;"'+'\nevent-set__leave1="_event: mouseleave; _target:#texthud1; visible:false;"'+'\nevent-set__leave2="_event: mouseleave; _target:#texthud2; visible:false;"'+'\nclass="clickable"></a-box>'
        #cylinder-bars
        string='<a-cylinder color="'+ color +'" height='+bar_height+' radius="0.25" position="'+longitude+ ' '+str_height_position +' '+ latitude+'"'+'\n event-set__enter1="_event: mouseenter; _target: #texthud1; value:'+country+'; visible: true; "'+'\nevent-set__enter2= "_event: mouseenter; _target: #texthud2; value:'+footprint + ' gha/person'+'; visible: true;"'+'\nevent-set__leave1="_event: mouseleave; _target:#texthud1; visible:false;"'+'\nevent-set__leave2="_event: mouseleave; _target:#texthud2; visible:false;"'+'\nclass="clickable">\n<a-text position="0 ' + text_position +' 0.35" color="black" width="3" align="center" rotation="-90 0 0" value="'+country+'" visible="true" baseline="top" wrap-count="12"> \n</a-cylinder>'
        file.write(string+'\n')
        print(row)
    
    file.write('</a-scene>\n</body>\n</html>')
    file.close()

