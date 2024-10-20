import folium
import networkx as nx
from nodes import nodes
from edges import links

# -------------------- BUILD NETWORK GRAPH --------------------

# Create a geographic graph
G = nx.Graph()

# Add all nodes to the graph with positions
for node, attributes in nodes.items():
    G.add_node(attributes.uid, pos=attributes.position)

# Add all links to the graph
for link in links:
    G.add_edge(link.start_uid, link.end_uid, label=link.label, length=link.length, transmission=link.transmission, link_type=link.link_type)

# -------------------- CREATE FOLIUM MAP --------------------

# Create a Folium map centered around Boston
m = folium.Map(location=[42.3601, -71.0589], zoom_start=5, tiles='cartodb positron')

# Add nodes to the map with detailed labels
for node, attributes in nodes.items():
    lat, lon = attributes.position
    info = (
        f"{attributes.name}<br>"
        f"Memory type: {attributes.memory_type}<br>"
        f"Cooling: {attributes.cooling}<br>"
        f"T2: {attributes.T2}<br>"
        f"Status: {attributes.status}<br>"
        f"Participants: {attributes.participants}<br>"
        f"Technologies: {', '.join(attributes.technologies)}"
    )
    folium.Marker(location=[lat, lon], popup=info, icon=folium.Icon(color='blue')).add_to(m)

# Add edges to the map with curved lines
def add_curved_edge(start, end, label, color='blue', dash_array=None):
    start_node = G.nodes[start]
    end_node = G.nodes[end]

    # Create a curved line effect by adding intermediary points
    mid_point = [(start_node['pos'][0] + end_node['pos'][0]) / 2, (start_node['pos'][1] + end_node['pos'][1]) / 2 + 0.01]  # Adjust for curvature
    locations = [start_node['pos'], mid_point, end_node['pos']]

    folium.PolyLine(locations=locations, color=color, weight=2.5, dash_array=dash_array, popup=label).add_to(m)

# Add existing links (solid blue lines)
for edge in G.edges(data=True):
    add_curved_edge(edge[0], edge[1], edge[2]['label'], color='blue')

# Add planned links (dashed red lines)
add_curved_edge("FH576-A", "UA", "Planned Link: Joint Device Development", color='red', dash_array='5, 5')

# -------------------- ADD LEGEND --------------------

# Create a legend for the map
legend_html = """
<div style="position: fixed;
     bottom: 50px; left: 50px; width: 200px; height: auto;
     background-color: white; border:2px solid grey; z-index:9999;
     font-size:14px; padding: 10px;">
&emsp;<b>Legend</b><br>
&emsp;<i style="color:blue;">&#9679;</i>&nbsp;Existing Edge<br>
&emsp;<i style="color:red;">&#9679;</i>&nbsp;Planned Link<br>
&emsp;<i style="color:gray;">&#9679;</i>&nbsp;Fiber Connection<br>
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))

# Save the map
m.save("boston_network_map.html")
