# Quantum Network Simulation

This repository contains a simulation of a quantum network involving various institutions, fiber hubs, and quantum technologies.

created for CQN review 2024

## File Descriptions

- **nodes.py**: Contains definitions for nodes in the network, including their properties.
- **edges.py**: Contains definitions for links in the network, including properties like length, transmission loss, and link type.
- **main.py**: The main script that builds the network graph and creates a Folium map for visualization.
- **requirements.txt**: Lists the required Python packages to run the simulation.

## How to Run

1. Install the required packages using:
pip install -r requirements.txt

2. Run the main script:
python main.py


3. Open the generated `boston_network_map.html` file in a web browser to view the network visualization.



<!DOCTYPE html>
<html>
<head>
    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_3587f2379f9b3cbb89e1e2e0f34318c9 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            </style>
        
</head>
<body>
    
    
<div style="position: fixed;
     bottom: 50px; left: 50px; width: 200px; height: auto;
     background-color: white; border:2px solid grey; z-index:9999;
     font-size:14px; padding: 10px;">
&emsp;<b>Legend</b><br>
&emsp;<i style="color:blue;">&#9679;</i>&nbsp;Existing Edge<br>
&emsp;<i style="color:red;">&#9679;</i>&nbsp;Planned Link<br>
&emsp;<i style="color:gray;">&#9679;</i>&nbsp;Fiber Connection<br>
</div>
    
            <div class="folium-map" id="map_3587f2379f9b3cbb89e1e2e0f34318c9" ></div>
        
</body>
<script>
    
    
            var map_3587f2379f9b3cbb89e1e2e0f34318c9 = L.map(
                "map_3587f2379f9b3cbb89e1e2e0f34318c9",
                {
                    center: [42.3601, -71.0589],
                    crs: L.CRS.EPSG3857,
                    zoom: 5,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_fbf34d43503b01662364ab40c44d5725 = L.tileLayer(
                "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
                {"attribution": "\u0026copy; \u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors \u0026copy; \u003ca href=\"https://carto.com/attributions\"\u003eCARTO\u003c/a\u003e", "detectRetina": false, "maxNativeZoom": 20, "maxZoom": 20, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abcd", "tms": false}
            );
        
    
            tile_layer_fbf34d43503b01662364ab40c44d5725.addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var marker_66c7b77dc1eeacbbff944eaa312ea83e = L.marker(
                [42.3619, -71.0903],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_633e1904e1198842682fc807fd1bc437 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_66c7b77dc1eeacbbff944eaa312ea83e.setIcon(icon_633e1904e1198842682fc807fd1bc437);
        
    
        var popup_072ede03b63acb290a1b7dd911c90fbd = L.popup({"maxWidth": "100%"});

        
            
                var html_f1bc9c2e3105725e06715a9ca6eefd01 = $(`<div id="html_f1bc9c2e3105725e06715a9ca6eefd01" style="width: 100.0%; height: 100.0%;">Fiber Hub 576-A<br>Memory type: N/A<br>Cooling: 4K<br>T2: N/A<br>Status: Online<br>Participants: CQN<br>Technologies: </div>`)[0];
                popup_072ede03b63acb290a1b7dd911c90fbd.setContent(html_f1bc9c2e3105725e06715a9ca6eefd01);
            
        

        marker_66c7b77dc1eeacbbff944eaa312ea83e.bindPopup(popup_072ede03b63acb290a1b7dd911c90fbd)
        ;

        
    
    
            var marker_f0b4ba95986c9780116acec40540eb41 = L.marker(
                [42.3656, -71.1032],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_5fb5005df7a2489ee7bbe3606754d7d5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_f0b4ba95986c9780116acec40540eb41.setIcon(icon_5fb5005df7a2489ee7bbe3606754d7d5);
        
    
        var popup_cd69f400ff7dfd768272640cf40838c1 = L.popup({"maxWidth": "100%"});

        
            
                var html_f9c3f4bc51bd46e85f2bcacd27eab282 = $(`<div id="html_f9c3f4bc51bd46e85f2bcacd27eab282" style="width: 100.0%; height: 100.0%;">Harvard<br>Memory type: SiV<br>Cooling: 1K<br>T2: >1ms<br>Status: Installed<br>Participants: MIT-LL<br>Technologies: Quantum Frequency Conversion</div>`)[0];
                popup_cd69f400ff7dfd768272640cf40838c1.setContent(html_f9c3f4bc51bd46e85f2bcacd27eab282);
            
        

        marker_f0b4ba95986c9780116acec40540eb41.bindPopup(popup_cd69f400ff7dfd768272640cf40838c1)
        ;

        
    
    
            var marker_323cbd38899175f69404619841812179 = L.marker(
                [42.4464, -71.2258],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_21ffadf45093323221f1f80e8d50f5c8 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_323cbd38899175f69404619841812179.setIcon(icon_21ffadf45093323221f1f80e8d50f5c8);
        
    
        var popup_46d956c5929d2575154ce6e5f40cf7d2 = L.popup({"maxWidth": "100%"});

        
            
                var html_04b2d735ed971dc8c0585752fe30be56 = $(`<div id="html_04b2d735ed971dc8c0585752fe30be56" style="width: 100.0%; height: 100.0%;">Lincoln Lab<br>Memory type: SiV<br>Cooling: 0.3K<br>T2: >1ms<br>Status: Under Construction<br>Participants: Startup<br>Technologies: Quantum Frequency Conversion</div>`)[0];
                popup_46d956c5929d2575154ce6e5f40cf7d2.setContent(html_04b2d735ed971dc8c0585752fe30be56);
            
        

        marker_323cbd38899175f69404619841812179.bindPopup(popup_46d956c5929d2575154ce6e5f40cf7d2)
        ;

        
    
    
            var marker_0080f5d79bc77f4c03be029fbd3d1016 = L.marker(
                [42.3619, -71.0903],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_ee73030b1eb3869e00c4207768829876 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_0080f5d79bc77f4c03be029fbd3d1016.setIcon(icon_ee73030b1eb3869e00c4207768829876);
        
    
        var popup_5c5538a39d0a73c1646816a29d91bfe3 = L.popup({"maxWidth": "100%"});

        
            
                var html_828e6f80544e7858ddf936b43d21d00c = $(`<div id="html_828e6f80544e7858ddf936b43d21d00c" style="width: 100.0%; height: 100.0%;">Fiber Hub 576-B<br>Memory type: N/A<br>Cooling: 4K<br>T2: ?<br>Status: Online<br>Participants: CQN<br>Technologies: </div>`)[0];
                popup_5c5538a39d0a73c1646816a29d91bfe3.setContent(html_828e6f80544e7858ddf936b43d21d00c);
            
        

        marker_0080f5d79bc77f4c03be029fbd3d1016.bindPopup(popup_5c5538a39d0a73c1646816a29d91bfe3)
        ;

        
    
    
            var marker_b4faf5a673691ce3248b218947e2d8c4 = L.marker(
                [42.3646, -71.1028],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_93e6c7498b95e7594b8c957d8ea1a7e3 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_b4faf5a673691ce3248b218947e2d8c4.setIcon(icon_93e6c7498b95e7594b8c957d8ea1a7e3);
        
    
        var popup_02107ee2637d563b140cc1a917f4654d = L.popup({"maxWidth": "100%"});

        
            
                var html_aa9b35b39ac33e15823185731d46ff16 = $(`<div id="html_aa9b35b39ac33e15823185731d46ff16" style="width: 100.0%; height: 100.0%;">26-465<br>Memory type: SiV<br>Cooling: 1K<br>T2: >1ms<br>Status: Installed<br>Participants: MIT-LL<br>Technologies: </div>`)[0];
                popup_02107ee2637d563b140cc1a917f4654d.setContent(html_aa9b35b39ac33e15823185731d46ff16);
            
        

        marker_b4faf5a673691ce3248b218947e2d8c4.bindPopup(popup_02107ee2637d563b140cc1a917f4654d)
        ;

        
    
    
            var marker_9854bbb928daef5db9869d53682297d9 = L.marker(
                [42.3593, -71.0957],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_eefae389ade42067f016953829848dfc = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_9854bbb928daef5db9869d53682297d9.setIcon(icon_eefae389ade42067f016953829848dfc);
        
    
        var popup_92bc3a58afaac95ce0cdb307b091f304 = L.popup({"maxWidth": "100%"});

        
            
                var html_c4075aed5a702d0fd87b4d51130fe06e = $(`<div id="html_c4075aed5a702d0fd87b4d51130fe06e" style="width: 100.0%; height: 100.0%;">38-177 SE Wall<br>Memory type: laser cooled Rb atom array<br>Cooling: <5 $\mu$K<br>T2: ?<br>Status: under construction<br>Participants: MIT, with Harvard and DARPA and QuEra<br>Technologies: </div>`)[0];
                popup_92bc3a58afaac95ce0cdb307b091f304.setContent(html_c4075aed5a702d0fd87b4d51130fe06e);
            
        

        marker_9854bbb928daef5db9869d53682297d9.bindPopup(popup_92bc3a58afaac95ce0cdb307b091f304)
        ;

        
    
    
            var marker_b0af62916789ff05b5ffa3afca35c616 = L.marker(
                [42.3646, -71.1028],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_c87ca8b88945ae67466f2cae40c05802 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_b0af62916789ff05b5ffa3afca35c616.setIcon(icon_c87ca8b88945ae67466f2cae40c05802);
        
    
        var popup_c685f2d5232e4855a68fe969c2d30edf = L.popup({"maxWidth": "100%"});

        
            
                var html_b220b395dcbf304d606b019536d5fb43 = $(`<div id="html_b220b395dcbf304d606b019536d5fb43" style="width: 100.0%; height: 100.0%;">26-368<br>Memory type: SnV<br>Cooling: 4K<br>T2: ?<br>Status: Online<br>Participants: CQN<br>Technologies: </div>`)[0];
                popup_c685f2d5232e4855a68fe969c2d30edf.setContent(html_b220b395dcbf304d606b019536d5fb43);
            
        

        marker_b0af62916789ff05b5ffa3afca35c616.bindPopup(popup_c685f2d5232e4855a68fe969c2d30edf)
        ;

        
    
    
            var marker_76dac82763b6b41d7b3894cdda1bbea1 = L.marker(
                [42.3619, -71.0903],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_86c4bfdbe492aa4b7b181981c1adb211 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_76dac82763b6b41d7b3894cdda1bbea1.setIcon(icon_86c4bfdbe492aa4b7b181981c1adb211);
        
    
        var popup_16ee696adbf48aef31cdd77662949026 = L.popup({"maxWidth": "100%"});

        
            
                var html_64e738d436de8701da216425c2f075ad = $(`<div id="html_64e738d436de8701da216425c2f075ad" style="width: 100.0%; height: 100.0%;">36-576<br>Memory type: SnV, SiV, silicon G-center<br>Cooling: 1K<br>T2: ?<br>Status: Installed<br>Participants: MIT-LL<br>Technologies: </div>`)[0];
                popup_16ee696adbf48aef31cdd77662949026.setContent(html_64e738d436de8701da216425c2f075ad);
            
        

        marker_76dac82763b6b41d7b3894cdda1bbea1.bindPopup(popup_16ee696adbf48aef31cdd77662949026)
        ;

        
    
    
            var marker_627fe525e13578bd23a511df0ed05e14 = L.marker(
                [42.3646, -71.1028],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_617b13eab896f1b9319e686d8b3461a9 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_627fe525e13578bd23a511df0ed05e14.setIcon(icon_617b13eab896f1b9319e686d8b3461a9);
        
    
        var popup_7ad5696b642a1ca72c0c11fd1529c9c8 = L.popup({"maxWidth": "100%"});

        
            
                var html_058c84798e9bbb143dd9fdacdae42ee9 = $(`<div id="html_058c84798e9bbb143dd9fdacdae42ee9" style="width: 100.0%; height: 100.0%;">Notaros Lab<br>Memory type: N/A<br>Cooling: 0.3K<br>T2: N/A<br>Status: Online<br>Participants: Startup<br>Technologies: </div>`)[0];
                popup_7ad5696b642a1ca72c0c11fd1529c9c8.setContent(html_058c84798e9bbb143dd9fdacdae42ee9);
            
        

        marker_627fe525e13578bd23a511df0ed05e14.bindPopup(popup_7ad5696b642a1ca72c0c11fd1529c9c8)
        ;

        
    
    
            var marker_7bbed4a2c2cf27a661d0d7ae8bcda650 = L.marker(
                [42.3593, -71.0957],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_0fac10b20ba63ad3a7f8fda4b4616547 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_7bbed4a2c2cf27a661d0d7ae8bcda650.setIcon(icon_0fac10b20ba63ad3a7f8fda4b4616547);
        
    
        var popup_65a0b0909ff9e88c878fb3d93eedfb27 = L.popup({"maxWidth": "100%"});

        
            
                var html_f25502b929f7e5a60704e21b08ad4e23 = $(`<div id="html_f25502b929f7e5a60704e21b08ad4e23" style="width: 100.0%; height: 100.0%;">38-185<br>Memory type: SnV<br>Cooling: 1K<br>T2: >2ms<br>Status: Online<br>Participants: CQN<br>Technologies: </div>`)[0];
                popup_65a0b0909ff9e88c878fb3d93eedfb27.setContent(html_f25502b929f7e5a60704e21b08ad4e23);
            
        

        marker_7bbed4a2c2cf27a661d0d7ae8bcda650.bindPopup(popup_65a0b0909ff9e88c878fb3d93eedfb27)
        ;

        
    
    
            var marker_8afea32bc5fe8478f6d44a43d9ff7508 = L.marker(
                [32.2319, -110.9501],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_c48c5ad5630de914533176ed28be1b56 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_8afea32bc5fe8478f6d44a43d9ff7508.setIcon(icon_c48c5ad5630de914533176ed28be1b56);
        
    
        var popup_dfd41d37051b05f29ed75016aa36f96e = L.popup({"maxWidth": "100%"});

        
            
                var html_d904710f07ceea2d598b6c25834c7a17 = $(`<div id="html_d904710f07ceea2d598b6c25834c7a17" style="width: 100.0%; height: 100.0%;">University of Arizona<br>Memory type: SnV<br>Cooling: 4K<br>T2: N/A<br>Status: Online<br>Participants: CQN<br>Technologies: </div>`)[0];
                popup_dfd41d37051b05f29ed75016aa36f96e.setContent(html_d904710f07ceea2d598b6c25834c7a17);
            
        

        marker_8afea32bc5fe8478f6d44a43d9ff7508.bindPopup(popup_dfd41d37051b05f29ed75016aa36f96e)
        ;

        
    
    
            var marker_10f02e5539a8cec2984122aacad6e999 = L.marker(
                [53.349805, -6.26031],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_89e3254a476f54d9a98fbe6a0af885a4 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_10f02e5539a8cec2984122aacad6e999.setIcon(icon_89e3254a476f54d9a98fbe6a0af885a4);
        
    
        var popup_ac2ed525a63e5fbff11bff142fa00b3d = L.popup({"maxWidth": "100%"});

        
            
                var html_8e9f2bf7cd38474dec72f57f288c56c4 = $(`<div id="html_8e9f2bf7cd38474dec72f57f288c56c4" style="width: 100.0%; height: 100.0%;">CoQreate (Ireland)<br>Memory type: SnV<br>Cooling: N/A<br>T2: 50ms<br>Status: Installed<br>Participants: MIT-LL<br>Technologies: </div>`)[0];
                popup_ac2ed525a63e5fbff11bff142fa00b3d.setContent(html_8e9f2bf7cd38474dec72f57f288c56c4);
            
        

        marker_10f02e5539a8cec2984122aacad6e999.bindPopup(popup_ac2ed525a63e5fbff11bff142fa00b3d)
        ;

        
    
    
            var marker_7ebba24f170f2a4787fecd9d0054ea04 = L.marker(
                [42.4464, -71.2258],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_5ca4b41153a72e17845136af0c82163a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_7ebba24f170f2a4787fecd9d0054ea04.setIcon(icon_5ca4b41153a72e17845136af0c82163a);
        
    
        var popup_4e3f79bfc852cb4631ab339004e27e8e = L.popup({"maxWidth": "100%"});

        
            
                var html_3ceef873c209cdb4829033c84b979b9b = $(`<div id="html_3ceef873c209cdb4829033c84b979b9b" style="width: 100.0%; height: 100.0%;">MIT Lincoln Lab<br>Memory type: SiV<br>Cooling: 0.1K<br>T2: >1ms<br>Status: Under Construction<br>Participants: Startup<br>Technologies: Quantum Frequency Conversion</div>`)[0];
                popup_4e3f79bfc852cb4631ab339004e27e8e.setContent(html_3ceef873c209cdb4829033c84b979b9b);
            
        

        marker_7ebba24f170f2a4787fecd9d0054ea04.bindPopup(popup_4e3f79bfc852cb4631ab339004e27e8e)
        ;

        
    
    
            var marker_e29a0bfaae1ac22a0ec2ec53d87dac05 = L.marker(
                [42.3601, -71.0589],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_734e3a3b85f0de42d31834e31a67350d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_e29a0bfaae1ac22a0ec2ec53d87dac05.setIcon(icon_734e3a3b85f0de42d31834e31a67350d);
        
    
        var popup_b88a62b13d301372bb6c6ab2c5f1b437 = L.popup({"maxWidth": "100%"});

        
            
                var html_9b44ec4c48a8ecdad05b31a0f7af16a2 = $(`<div id="html_9b44ec4c48a8ecdad05b31a0f7af16a2" style="width: 100.0%; height: 100.0%;">QuNet<br>Memory type: SiV<br>Cooling: 4K<br>T2: n/a<br>Status: Online<br>Participants: CQN<br>Technologies: </div>`)[0];
                popup_b88a62b13d301372bb6c6ab2c5f1b437.setContent(html_9b44ec4c48a8ecdad05b31a0f7af16a2);
            
        

        marker_e29a0bfaae1ac22a0ec2ec53d87dac05.bindPopup(popup_b88a62b13d301372bb6c6ab2c5f1b437)
        ;

        
    
    
            var marker_04f1aeba6f0eb10b5429eae5f90e47c7 = L.marker(
                [44.0445, -123.0122],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_4fb080d4271db7b15fc02cb55309335e = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_04f1aeba6f0eb10b5429eae5f90e47c7.setIcon(icon_4fb080d4271db7b15fc02cb55309335e);
        
    
        var popup_ea798d4fdec1d63f881a74e18fa1b55d = L.popup({"maxWidth": "100%"});

        
            
                var html_a44a4b95c011d34e75a4510e9392f53c = $(`<div id="html_a44a4b95c011d34e75a4510e9392f53c" style="width: 100.0%; height: 100.0%;">University of Oregon<br>Memory type: N/A<br>Cooling: 1K<br>T2: N/A<br>Status: Installed<br>Participants: MIT-LL<br>Technologies: </div>`)[0];
                popup_ea798d4fdec1d63f881a74e18fa1b55d.setContent(html_a44a4b95c011d34e75a4510e9392f53c);
            
        

        marker_04f1aeba6f0eb10b5429eae5f90e47c7.bindPopup(popup_ea798d4fdec1d63f881a74e18fa1b55d)
        ;

        
    
    
            var marker_3df8057e3ddfdd6c6a4ba50d1d794346 = L.marker(
                [40.2338, -111.6584],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_ff9984c9343132a743f7d25f5fb57a9b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_3df8057e3ddfdd6c6a4ba50d1d794346.setIcon(icon_ff9984c9343132a743f7d25f5fb57a9b);
        
    
        var popup_a4f5cd3979fb4a1f672ca60a927cabaa = L.popup({"maxWidth": "100%"});

        
            
                var html_766e9dcf6fe28fc584e5b2827620ba33 = $(`<div id="html_766e9dcf6fe28fc584e5b2827620ba33" style="width: 100.0%; height: 100.0%;">BYU<br>Memory type: N/A<br>Cooling: 0.3K<br>T2: N/A<br>Status: Online<br>Participants: Startup<br>Technologies: </div>`)[0];
                popup_a4f5cd3979fb4a1f672ca60a927cabaa.setContent(html_766e9dcf6fe28fc584e5b2827620ba33);
            
        

        marker_3df8057e3ddfdd6c6a4ba50d1d794346.bindPopup(popup_a4f5cd3979fb4a1f672ca60a927cabaa)
        ;

        
    
    
            var marker_985f64e58314e6988b098c09ec1db4b5 = L.marker(
                [38.9175, -77.0189],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_add0fc3d98a0007e24319903c3ee160d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_985f64e58314e6988b098c09ec1db4b5.setIcon(icon_add0fc3d98a0007e24319903c3ee160d);
        
    
        var popup_71b038772c327d76fc7a1f6ab3f26359 = L.popup({"maxWidth": "100%"});

        
            
                var html_25724caf4acb302966c41562e391757f = $(`<div id="html_25724caf4acb302966c41562e391757f" style="width: 100.0%; height: 100.0%;">Howard University<br>Memory type: N/A<br>Cooling: 4K<br>T2: N/A<br>Status: Online<br>Participants: CQN<br>Technologies: </div>`)[0];
                popup_71b038772c327d76fc7a1f6ab3f26359.setContent(html_25724caf4acb302966c41562e391757f);
            
        

        marker_985f64e58314e6988b098c09ec1db4b5.bindPopup(popup_71b038772c327d76fc7a1f6ab3f26359)
        ;

        
    
    
            var marker_7325875d6a19271d45ae5e2fe8659531 = L.marker(
                [42.3902, -72.5297],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_fa0b002a3830330d8f7d5bae21ef68d8 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_7325875d6a19271d45ae5e2fe8659531.setIcon(icon_fa0b002a3830330d8f7d5bae21ef68d8);
        
    
        var popup_6bf3bd491727bc7f44f7843648f599de = L.popup({"maxWidth": "100%"});

        
            
                var html_f7522861036a546fb44518ab502786ce = $(`<div id="html_f7522861036a546fb44518ab502786ce" style="width: 100.0%; height: 100.0%;">UMass Amherst<br>Memory type: N/A<br>Cooling: 1K<br>T2: N/A<br>Status: Installed<br>Participants: MIT-LL<br>Technologies: </div>`)[0];
                popup_6bf3bd491727bc7f44f7843648f599de.setContent(html_f7522861036a546fb44518ab502786ce);
            
        

        marker_7325875d6a19271d45ae5e2fe8659531.bindPopup(popup_6bf3bd491727bc7f44f7843648f599de)
        ;

        
    
    
            var marker_21194309381abe9c029c75725043d433 = L.marker(
                [38.9856, -76.9426],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_cba01ef7130f39d1d698c17f78b745dc = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_21194309381abe9c029c75725043d433.setIcon(icon_cba01ef7130f39d1d698c17f78b745dc);
        
    
        var popup_b6e4ba8a4441d1af67cfb6dc0de63e01 = L.popup({"maxWidth": "100%"});

        
            
                var html_eb5e642504b96e361bff5ad356651509 = $(`<div id="html_eb5e642504b96e361bff5ad356651509" style="width: 100.0%; height: 100.0%;">University of Maryland<br>Memory type: trapped ions<br>Cooling: RT<br>T2: >1 s<br>Status: Online<br>Participants: Startup<br>Technologies: </div>`)[0];
                popup_b6e4ba8a4441d1af67cfb6dc0de63e01.setContent(html_eb5e642504b96e361bff5ad356651509);
            
        

        marker_21194309381abe9c029c75725043d433.bindPopup(popup_b6e4ba8a4441d1af67cfb6dc0de63e01)
        ;

        
    
    
            var marker_fba466e1ce5b75e18a05badde4c61fff = L.marker(
                [53.3434, -6.254],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_4ccae8f31f3e2b276912a2da431ee96f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_fba466e1ce5b75e18a05badde4c61fff.setIcon(icon_4ccae8f31f3e2b276912a2da431ee96f);
        
    
        var popup_404c512a60379d974bf3285991c82520 = L.popup({"maxWidth": "100%"});

        
            
                var html_732c071a56f413cb7f657ca413de2d4d = $(`<div id="html_732c071a56f413cb7f657ca413de2d4d" style="width: 100.0%; height: 100.0%;">Trinity College (Ireland)<br>Memory type: SnV<br>Cooling: <1K<br>T2: ?<br>Status: Online<br>Participants: CQN<br>Technologies: </div>`)[0];
                popup_404c512a60379d974bf3285991c82520.setContent(html_732c071a56f413cb7f657ca413de2d4d);
            
        

        marker_fba466e1ce5b75e18a05badde4c61fff.bindPopup(popup_404c512a60379d974bf3285991c82520)
        ;

        
    
    
            var marker_87f2a2f4b68ab720ff0c2eb66ee7d246 = L.marker(
                [42.350876, -71.106918],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_9b7ba334a24270f3a3948c31f1169238 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_87f2a2f4b68ab720ff0c2eb66ee7d246.setIcon(icon_9b7ba334a24270f3a3948c31f1169238);
        
    
        var popup_a6a80491a3a8c233fd11e40de529ca16 = L.popup({"maxWidth": "100%"});

        
            
                var html_8bb1899ff5a239921df7489ad2757c1b = $(`<div id="html_8bb1899ff5a239921df7489ad2757c1b" style="width: 100.0%; height: 100.0%;">Boston University Photonics Incubator<br>Memory type: SiV<br>Cooling: <1K<br>T2: ?<br>Status: Installed<br>Participants: QuNETT<br>Technologies: </div>`)[0];
                popup_a6a80491a3a8c233fd11e40de529ca16.setContent(html_8bb1899ff5a239921df7489ad2757c1b);
            
        

        marker_87f2a2f4b68ab720ff0c2eb66ee7d246.bindPopup(popup_a6a80491a3a8c233fd11e40de529ca16)
        ;

        
    
    
            var marker_dcfc46468aaf9384340b33f3437f2e67 = L.marker(
                [42.3633196, -71.0925566],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_31089865a5c31eef27747fc4a983be94 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_dcfc46468aaf9384340b33f3437f2e67.setIcon(icon_31089865a5c31eef27747fc4a983be94);
        
    
        var popup_2ef838e5870c55c2a6c940f850ee0bcf = L.popup({"maxWidth": "100%"});

        
            
                var html_365f84e679b51c936f4dbff011a141ed = $(`<div id="html_365f84e679b51c936f4dbff011a141ed" style="width: 100.0%; height: 100.0%;">AT&T Fiber Hub<br>Memory type: N/A<br>Cooling: N/A<br>T2: N/A<br>Status: Online<br>Participants: AT&T<br>Technologies: </div>`)[0];
                popup_2ef838e5870c55c2a6c940f850ee0bcf.setContent(html_365f84e679b51c936f4dbff011a141ed);
            
        

        marker_dcfc46468aaf9384340b33f3437f2e67.bindPopup(popup_2ef838e5870c55c2a6c940f850ee0bcf)
        ;

        
    
    
            var marker_b8760d2e0ab24d49f478920e5506ea50 = L.marker(
                [42.3615, -71.093],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_8e19a0cdc8ff6b046374540778a963d3 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_b8760d2e0ab24d49f478920e5506ea50.setIcon(icon_8e19a0cdc8ff6b046374540778a963d3);
        
    
        var popup_61c51c3ab69d8470829ece24f8928e1c = L.popup({"maxWidth": "100%"});

        
            
                var html_579cef3af49186773469bbdec1776f42 = $(`<div id="html_579cef3af49186773469bbdec1776f42" style="width: 100.0%; height: 100.0%;">Englund Lab (36-575)<br>Memory type: SiV, SnV<br>Cooling: 4K<br>T2: N/A<br>Status: Online<br>Participants: MIT<br>Technologies: </div>`)[0];
                popup_61c51c3ab69d8470829ece24f8928e1c.setContent(html_579cef3af49186773469bbdec1776f42);
            
        

        marker_b8760d2e0ab24d49f478920e5506ea50.bindPopup(popup_61c51c3ab69d8470829ece24f8928e1c)
        ;

        
    
    
            var marker_8fd264ba09f39a226f483e37822c252e = L.marker(
                [42.3897538, -71.1475561],
                {}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
            var icon_2bca38be1bb92ef8f7ed983f4f0efaf8 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_8fd264ba09f39a226f483e37822c252e.setIcon(icon_2bca38be1bb92ef8f7ed983f4f0efaf8);
        
    
        var popup_ac32e0aef0c6c9b9338e199fb35dc04d = L.popup({"maxWidth": "100%"});

        
            
                var html_52d13985d670fd7b050ef2b5f99f91d3 = $(`<div id="html_52d13985d670fd7b050ef2b5f99f91d3" style="width: 100.0%; height: 100.0%;">BBN Raytheon<br>Memory type: N/A<br>Cooling: <100mK<br>T2: N/A<br>Status: Online<br>Participants: BBN<br>Technologies: </div>`)[0];
                popup_ac32e0aef0c6c9b9338e199fb35dc04d.setContent(html_52d13985d670fd7b050ef2b5f99f91d3);
            
        

        marker_8fd264ba09f39a226f483e37822c252e.bindPopup(popup_ac32e0aef0c6c9b9338e199fb35dc04d)
        ;

        
    
    
            var poly_line_12c334e3b7c9091f6f874fc4125b476c = L.polyline(
                [[42.3619, -71.0903], [42.363749999999996, -71.08675], [42.3656, -71.1032]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_cdd2ea38a1d313acf6e2c0fdd1f200bc = L.popup({"maxWidth": "100%"});

        
            
                var html_e03456fe2516ac158d12c010277116ab = $(`<div id="html_e03456fe2516ac158d12c010277116ab" style="width: 100.0%; height: 100.0%;">2 SMF-28</div>`)[0];
                popup_cdd2ea38a1d313acf6e2c0fdd1f200bc.setContent(html_e03456fe2516ac158d12c010277116ab);
            
        

        poly_line_12c334e3b7c9091f6f874fc4125b476c.bindPopup(popup_cdd2ea38a1d313acf6e2c0fdd1f200bc)
        ;

        
    
    
            var poly_line_d26b4b03b080c606834c360c3f5ba3cb = L.polyline(
                [[42.3619, -71.0903], [42.40415, -71.14805], [42.4464, -71.2258]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_3f7713fd6c2dca0d44aa98202bc8da67 = L.popup({"maxWidth": "100%"});

        
            
                var html_c251e0383f873f942300645cb58a5e1b = $(`<div id="html_c251e0383f873f942300645cb58a5e1b" style="width: 100.0%; height: 100.0%;">2 SMF-28</div>`)[0];
                popup_3f7713fd6c2dca0d44aa98202bc8da67.setContent(html_c251e0383f873f942300645cb58a5e1b);
            
        

        poly_line_d26b4b03b080c606834c360c3f5ba3cb.bindPopup(popup_3f7713fd6c2dca0d44aa98202bc8da67)
        ;

        
    
    
            var poly_line_eac45d0455752c5ac451da1799b2979d = L.polyline(
                [[42.3619, -71.0903], [42.356387999999995, -71.08860899999999], [42.350876, -71.106918]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_67094782a5407b39945b8b81500b1a15 = L.popup({"maxWidth": "100%"});

        
            
                var html_93cd6db6c76596dd2f6c313d6b3515ce = $(`<div id="html_93cd6db6c76596dd2f6c313d6b3515ce" style="width: 100.0%; height: 100.0%;">1 SMF-28</div>`)[0];
                popup_67094782a5407b39945b8b81500b1a15.setContent(html_93cd6db6c76596dd2f6c313d6b3515ce);
            
        

        poly_line_eac45d0455752c5ac451da1799b2979d.bindPopup(popup_67094782a5407b39945b8b81500b1a15)
        ;

        
    
    
            var poly_line_5add92535d99ec6d608845a2127b9854 = L.polyline(
                [[42.3656, -71.1032], [42.3644598, -71.08787829999999], [42.3633196, -71.0925566]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_f56e767d2b7a3ba57531d0806fc0bc73 = L.popup({"maxWidth": "100%"});

        
            
                var html_3ec6eb6189e03469d877356a23ef867c = $(`<div id="html_3ec6eb6189e03469d877356a23ef867c" style="width: 100.0%; height: 100.0%;">3 SMF-28</div>`)[0];
                popup_f56e767d2b7a3ba57531d0806fc0bc73.setContent(html_3ec6eb6189e03469d877356a23ef867c);
            
        

        poly_line_5add92535d99ec6d608845a2127b9854.bindPopup(popup_f56e767d2b7a3ba57531d0806fc0bc73)
        ;

        
    
    
            var poly_line_d15c0c711ab103d1ba22935d8f010f14 = L.polyline(
                [[42.4464, -71.2258], [42.40415, -71.14805], [42.3619, -71.0903]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_d938408816791968312b9f44ea5b4025 = L.popup({"maxWidth": "100%"});

        
            
                var html_f6569c5864b3fed85cb49e049fc8c382 = $(`<div id="html_f6569c5864b3fed85cb49e049fc8c382" style="width: 100.0%; height: 100.0%;">2 ?</div>`)[0];
                popup_d938408816791968312b9f44ea5b4025.setContent(html_f6569c5864b3fed85cb49e049fc8c382);
            
        

        poly_line_d15c0c711ab103d1ba22935d8f010f14.bindPopup(popup_d938408816791968312b9f44ea5b4025)
        ;

        
    
    
            var poly_line_19916d0d022d6d27a218675160b1386a = L.polyline(
                [[42.3619, -71.0903], [42.36325, -71.08655], [42.3646, -71.1028]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_7dec3844adcde0cb761f9ca3ad5a5b77 = L.popup({"maxWidth": "100%"});

        
            
                var html_c3c22587ed8bfbebe7df40833c979a12 = $(`<div id="html_c3c22587ed8bfbebe7df40833c979a12" style="width: 100.0%; height: 100.0%;">2 SM600</div>`)[0];
                popup_7dec3844adcde0cb761f9ca3ad5a5b77.setContent(html_c3c22587ed8bfbebe7df40833c979a12);
            
        

        poly_line_19916d0d022d6d27a218675160b1386a.bindPopup(popup_7dec3844adcde0cb761f9ca3ad5a5b77)
        ;

        
    
    
            var poly_line_3148701780e695f31372127240ea42af = L.polyline(
                [[42.3646, -71.1028], [42.3646, -71.0928], [42.3646, -71.1028]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_315c727e4e4e2dd1d8c49cb89fd28d5b = L.popup({"maxWidth": "100%"});

        
            
                var html_9fec2b3e23d0642f2fa8dbfba76a674a = $(`<div id="html_9fec2b3e23d0642f2fa8dbfba76a674a" style="width: 100.0%; height: 100.0%;">4 SMF28</div>`)[0];
                popup_315c727e4e4e2dd1d8c49cb89fd28d5b.setContent(html_9fec2b3e23d0642f2fa8dbfba76a674a);
            
        

        poly_line_3148701780e695f31372127240ea42af.bindPopup(popup_315c727e4e4e2dd1d8c49cb89fd28d5b)
        ;

        
    
    
            var poly_line_64c94d3c98ec2a4a8d62d88e8afe2fc2 = L.polyline(
                [[42.3646, -71.1028], [42.36325, -71.08655], [42.3619, -71.0903]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_02388acba39ce48eac8308f519a5ab58 = L.popup({"maxWidth": "100%"});

        
            
                var html_899b32abdfbd660b5f28804f63eb33cd = $(`<div id="html_899b32abdfbd660b5f28804f63eb33cd" style="width: 100.0%; height: 100.0%;">2 PM40-U40D</div>`)[0];
                popup_02388acba39ce48eac8308f519a5ab58.setContent(html_899b32abdfbd660b5f28804f63eb33cd);
            
        

        poly_line_64c94d3c98ec2a4a8d62d88e8afe2fc2.bindPopup(popup_02388acba39ce48eac8308f519a5ab58)
        ;

        
    
    
            var poly_line_bbd79e60283fd583c45ac18106d75c49 = L.polyline(
                [[42.3646, -71.1028], [42.36195, -71.08924999999999], [42.3593, -71.0957]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_da1ed10fc684610ad90981b702de96b0 = L.popup({"maxWidth": "100%"});

        
            
                var html_91790bad7224259ee8a0d3c500b6c248 = $(`<div id="html_91790bad7224259ee8a0d3c500b6c248" style="width: 100.0%; height: 100.0%;">6 SMF28</div>`)[0];
                popup_da1ed10fc684610ad90981b702de96b0.setContent(html_91790bad7224259ee8a0d3c500b6c248);
            
        

        poly_line_bbd79e60283fd583c45ac18106d75c49.bindPopup(popup_da1ed10fc684610ad90981b702de96b0)
        ;

        
    
    
            var poly_line_14552088fadf33185e9f7fab9d8fd04d = L.polyline(
                [[42.3646, -71.1028], [42.3646, -71.0928], [42.3646, -71.1028]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_1b1760e11874196952fb9adf1fb497f6 = L.popup({"maxWidth": "100%"});

        
            
                var html_578f2c5106d95d74fb8ad1d530ec05e4 = $(`<div id="html_578f2c5106d95d74fb8ad1d530ec05e4" style="width: 100.0%; height: 100.0%;">2 SMF-28</div>`)[0];
                popup_1b1760e11874196952fb9adf1fb497f6.setContent(html_578f2c5106d95d74fb8ad1d530ec05e4);
            
        

        poly_line_14552088fadf33185e9f7fab9d8fd04d.bindPopup(popup_1b1760e11874196952fb9adf1fb497f6)
        ;

        
    
    
            var poly_line_30f6b33632b2bc6d32790790d9e08235 = L.polyline(
                [[53.349805, -6.26031], [53.3466025, -6.247154999999999], [53.3434, -6.254]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_fc608a47f29499e9fdf6fb344d20c6e0 = L.popup({"maxWidth": "100%"});

        
            
                var html_cc7f7493f03816762f43a2fd0c03e215 = $(`<div id="html_cc7f7493f03816762f43a2fd0c03e215" style="width: 100.0%; height: 100.0%;">1 SMF-28</div>`)[0];
                popup_fc608a47f29499e9fdf6fb344d20c6e0.setContent(html_cc7f7493f03816762f43a2fd0c03e215);
            
        

        poly_line_30f6b33632b2bc6d32790790d9e08235.bindPopup(popup_fc608a47f29499e9fdf6fb344d20c6e0)
        ;

        
    
    
            var poly_line_922f3fc09a3eb3c3fc0682ad12200561 = L.polyline(
                [[42.4464, -71.2258], [42.4048598, -71.1491783], [42.3633196, -71.0925566]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_cae99cc296dae63e24b06bc0067a53c9 = L.popup({"maxWidth": "100%"});

        
            
                var html_231cc2c3696327572ac4e1642e1852bb = $(`<div id="html_231cc2c3696327572ac4e1642e1852bb" style="width: 100.0%; height: 100.0%;">3 SMF-28</div>`)[0];
                popup_cae99cc296dae63e24b06bc0067a53c9.setContent(html_231cc2c3696327572ac4e1642e1852bb);
            
        

        poly_line_922f3fc09a3eb3c3fc0682ad12200561.bindPopup(popup_cae99cc296dae63e24b06bc0067a53c9)
        ;

        
    
    
            var poly_line_842127ab4c0a94cac06777b757842d82 = L.polyline(
                [[44.0445, -123.0122], [43.217349999999996, -97.76095], [42.3902, -72.5297]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_0c0a5e5f826d71dc3603cc7ba6c31df1 = L.popup({"maxWidth": "100%"});

        
            
                var html_d5f12b2bb097e3dde037102ffc686f53 = $(`<div id="html_d5f12b2bb097e3dde037102ffc686f53" style="width: 100.0%; height: 100.0%;">2 SMF-28</div>`)[0];
                popup_0c0a5e5f826d71dc3603cc7ba6c31df1.setContent(html_d5f12b2bb097e3dde037102ffc686f53);
            
        

        poly_line_842127ab4c0a94cac06777b757842d82.bindPopup(popup_0c0a5e5f826d71dc3603cc7ba6c31df1)
        ;

        
    
    
            var poly_line_3e7cbfe4ce71cf974051af337f42db1b = L.polyline(
                [[38.9175, -77.0189], [38.95155, -76.97075], [38.9856, -76.9426]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_e4694116b96901666edb5b571fbe431f = L.popup({"maxWidth": "100%"});

        
            
                var html_b7f411f835e523d5ba8d887c3aefbb72 = $(`<div id="html_b7f411f835e523d5ba8d887c3aefbb72" style="width: 100.0%; height: 100.0%;">1 SMF-28</div>`)[0];
                popup_e4694116b96901666edb5b571fbe431f.setContent(html_b7f411f835e523d5ba8d887c3aefbb72);
            
        

        poly_line_3e7cbfe4ce71cf974051af337f42db1b.bindPopup(popup_e4694116b96901666edb5b571fbe431f)
        ;

        
    
    
            var poly_line_0562384a7d78313334e6cb93f0e75e55 = L.polyline(
                [[38.9856, -76.9426], [40.668238, -74.01475899999998], [42.350876, -71.106918]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_bd8e17965b0e8e97498cf67225d1f106 = L.popup({"maxWidth": "100%"});

        
            
                var html_02eb5ea32d98cbaa15b65cf293c7f5c0 = $(`<div id="html_02eb5ea32d98cbaa15b65cf293c7f5c0" style="width: 100.0%; height: 100.0%;">2 SMF-28</div>`)[0];
                popup_bd8e17965b0e8e97498cf67225d1f106.setContent(html_02eb5ea32d98cbaa15b65cf293c7f5c0);
            
        

        poly_line_0562384a7d78313334e6cb93f0e75e55.bindPopup(popup_bd8e17965b0e8e97498cf67225d1f106)
        ;

        
    
    
            var poly_line_524d145a20c93b82a7d0baabaff06412 = L.polyline(
                [[42.3633196, -71.0925566], [42.362409799999995, -71.08277829999999], [42.3615, -71.093]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_aaaefd5fce10e9c0df6613b083400e84 = L.popup({"maxWidth": "100%"});

        
            
                var html_98b4065104d68dd028cb954cf0a442ac = $(`<div id="html_98b4065104d68dd028cb954cf0a442ac" style="width: 100.0%; height: 100.0%;">2 SMF-28</div>`)[0];
                popup_aaaefd5fce10e9c0df6613b083400e84.setContent(html_98b4065104d68dd028cb954cf0a442ac);
            
        

        poly_line_524d145a20c93b82a7d0baabaff06412.bindPopup(popup_aaaefd5fce10e9c0df6613b083400e84)
        ;

        
    
    
            var poly_line_a7747f9ef409d1e89471bb77c4b40426 = L.polyline(
                [[42.3633196, -71.0925566], [42.3765367, -71.11005635], [42.3897538, -71.1475561]],
                {"bubblingMouseEvents": true, "color": "blue", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "blue", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_d9f2a809bbe0a8cd9205fe901370779e = L.popup({"maxWidth": "100%"});

        
            
                var html_305fd5b9aa4b0fcfdc2b6eed9271ea8d = $(`<div id="html_305fd5b9aa4b0fcfdc2b6eed9271ea8d" style="width: 100.0%; height: 100.0%;">3 SMF-28</div>`)[0];
                popup_d9f2a809bbe0a8cd9205fe901370779e.setContent(html_305fd5b9aa4b0fcfdc2b6eed9271ea8d);
            
        

        poly_line_a7747f9ef409d1e89471bb77c4b40426.bindPopup(popup_d9f2a809bbe0a8cd9205fe901370779e)
        ;

        
    
    
            var poly_line_7656d4177e1ca1c9b11a606a29400a4a = L.polyline(
                [[42.3619, -71.0903], [37.2969, -91.0102], [32.2319, -110.9501]],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": "5, 5", "dashOffset": null, "fill": false, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 1.0, "smoothFactor": 1.0, "stroke": true, "weight": 2.5}
            ).addTo(map_3587f2379f9b3cbb89e1e2e0f34318c9);
        
    
        var popup_62c7c33cf6ed20ea17ed662f8f03fd40 = L.popup({"maxWidth": "100%"});

        
            
                var html_dad0789bac9a26559353ee6e4284d3f8 = $(`<div id="html_dad0789bac9a26559353ee6e4284d3f8" style="width: 100.0%; height: 100.0%;">Planned Link: Joint Device Development</div>`)[0];
                popup_62c7c33cf6ed20ea17ed662f8f03fd40.setContent(html_dad0789bac9a26559353ee6e4284d3f8);
            
        

        poly_line_7656d4177e1ca1c9b11a606a29400a4a.bindPopup(popup_62c7c33cf6ed20ea17ed662f8f03fd40)
        ;

        
    
</script>
</html>
