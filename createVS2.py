import csv
with open("Fussabdruck.csv") as csvdatei:
    csv_reader_object = csv.DictReader(csvdatei)
    file= open("Visualisierung2.html","w")
    #Head und Sources
    file.write('<html>\n<head>\n<script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>'
    +'\n<script src="https://unpkg.com/aframe-geojson-component/dist/aframe-geojson-component.min.js"></script>' 
    +'\n<script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script>'
    +'\n<script src="https://cdn.jsdelivr.net/gh/c-frame/aframe-extras@7.0.0/dist/aframe-extras.min.js"></script>\n<head>'
    #Body
    +'\n<body>\n<a-scene vr-mode-ui="cardboardModeEnabled:true"><!--renderer="antialias:true"-->\n<a-assets>\n<a-assets-item id="geo-json" src="assets/world-50m.v1.json"></a-asset-item>'
    +'\n<img id="sky" src="assets/sky.jpg"/>\n<img id="worldmapfloor" src="assets/earthmap1.jpg"/>\n</a-assets>'
    +'\n<a-sky src="#sky"></a-sky>'
    +'\n<a-plane material="color:#FFFFFF; src: #worldmapfloor;" rotation="-90 0 0" scale="360 180 0" class="not-clickable"></a-plane>'
    +'\n<a-entity geometry="primitive: plane;" class="not-clickable" position="0 0.01 0" rotation="-90 0 0" scale="360 180 0" material="color: yellow; shader: flat" geojson="src: #geo-json; topologyObject: countries; projection: geoEquirectangular" class="not-clickable"></a-entity>'
    +'\n<a-entity id="rig" movement-controls position="0 4 5">\n<a-entity camera look-controls="pointerLockEnabled: true">\n<a-cursor id="cursor" color="#3B3B3B" raycaster="objects: .clickable">'
    +'\n<a-text position="0 0.2 0" width="1" color="white" align="center" id="texthud1" value="Land" visible="false">'
    +'\n<a-text position="0 -0.05 0" width="1" color="white" align="center" id="texthud2" value="Hoehe" visible="false"></a-text>'
    +'\n</a-text>\n</a-cursor>\n</a-entity>\n</a-entity>')

    
    for row in csv_reader_object:
        country= row["Land"]
        footprint=row["Oekologischer_Fussabdruck"]
        footprint=str(round(float(footprint),3))
        factor=1.5
        bar_height=str(float(footprint)*factor)
        latitude=row["Breitengrade"]
        longitude=row["Laengengrade"]
        height_position=float(bar_height)/2
        text_position=str(height_position*(-1)+0.02)
        
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

        string='<a-cylinder color="'+ color +'" height='+bar_height+' radius="0.25" position="'+longitude+ ' '+str_height_position +' '+ latitude+'"'+'\n event-set__enter1="_event: mouseenter; _target: #texthud1; value:'+country+'; visible: true; "'+'\nevent-set__enter2= "_event: mouseenter; _target: #texthud2; value:'+footprint + ' gha/person'+'; visible: true;"'+'\nevent-set__leave1="_event: mouseleave; _target:#texthud1; visible:false;"'+'\nevent-set__leave2="_event: mouseleave; _target:#texthud2; visible:false;"'+'\nclass="clickable">\n<a-text position="0 ' + text_position +' 0.35" class="not-clickable" color="black" width="3" align="center" rotation="-90 0 0" value="'+country+'" visible="true" baseline="top" wrap-count="12"> \n</a-cylinder>'
        file.write(string+'\n')
        print(row)
    
    file.write('</a-scene>\n</body>\n</html>')
    #LICENSE
    file.write('\n<!------------------------------------------------------------------------------\nIn this software the Movement-Controls of A-Frame-Extras-Component by Don McCurdy was used for movement controls'
    	+'\nhttps://github.com/c-frame/aframe-extras\n\nThe A-Frame-Extras is licensed with MIT License:\n\nThe MIT License (MIT)\n\nCopyright (c) 2016 Don McCurdy'
    	+'\nPermission is hereby granted, free of charge, to any person obtaining a copy'
    	+'\nof this software and associated documentation files (the "Software"), to deal'
    	+'\nin the Software without restriction, including without limitation the rights'
    	+'\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell'
    	+'\ncopies of the Software, and to permit persons to whom the Software is'
    	+'\nfurnished to do so, subject to the following conditions:\n'
    	+'\nThe above copyright notice and this permission notice shall be included in all'
    	+'\ncopies or substantial portions of the Software.\n'
    	+'\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR'
    	+'\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,'
    	+'\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE'
    	+'\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER'
    	+'\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,'
    	+'\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE'
    	+'\nSOFTWARE.\n------------------------------------------------------------------------------->')
    file.close()

