import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import networkx as nx
from scipy.spatial.distance import euclidean
import numpy as np

# CSUF map image
base_map_path = 'image/map.png'
base_map = mpimg.imread(base_map_path)

# Given positions for the nodes
positions = [
    (113.6, 727.4), # Nutwood Parking (Node 0)
    (170.2, 454.0), # Visual Arts (Node 1)
    (166.3, 304.8), # Titan Student Union (Node 2)
    (205.0, 108.9), # Recreation Center (Node 3)
    (344.3, 487.8), # Clayes Performing Arts Center (Node 4)
    (322.4, 291.9), # Titan Bookstore (Node 5)
    (427.8, 108.9), # Titan Gym (Node 6)
    (458.6, 708.5), # Dan Black Hall (Node 7)
    (492.4, 627.0), # McCarthy Hall (Node 8)
    (510.3, 350.5), # Pollack Library (Node 9)
    (633.6, 717.5), # Langsdorf Hall (Node 10)
    (663.5, 501.7), # Humanities (Node 11)
    (645.6, 359.5), # Education Classroom (Node 12)
    (656.5, 107.9), # Student Health (Node 13)
    (717.2, 775.2), # SGMH (Node 14)
    (711.2, 665.8), # Carls Jr (Node 15)
    (804.7, 498.7), # Lot F (Node 16)
    (787.8, 216.3), # Engineering Building (Node 17)
    (903.1, 90),    # Gastronome (Node 18)
    (965.8, 523.6), # East Side Parking Structure (Node 19)
]

# Map given positions to graph nodes
pos = {str(i): positions[i] for i in range(len(positions))}

edges_explicit = [
    ('0', '1'), ('0', '4'), ('0', '7'), ('0', '8'),
    ('1', '0'), ('1', '4'), ('1', '2'),
    ('2', '1'), ('2', '5'), ('2', '3'),
    ('3', '2'), ('3', '5'), ('3', '6'), ('3', '9'),
    ('4', '0'), ('4', '1'), ('4', '5'), ('4', '9'), ('4', '8'), ('4', '7'),
    ('5', '2'), ('5', '4'), ('5', '9'), ('5', '3'), ('5', '6'), ('5', '13'),
    ('6', '3'), ('6', '5'), ('6', '9'), ('6', '12'), ('6', '13'),
    ('7', '0'), ('7', '4'), ('7', '8'), ('7', '10'),
    ('8', '4'), ('8', '0'), ('8', '7'), ('8', '10'), ('8', '11'), ('8', '9'),
    ('9', '8'), ('9', '4'), ('9', '5'), ('9', '3'), ('9', '6'), ('9', '13'), ('9', '12'), ('9', '11'),
    ('10', '7'), ('10', '8'), ('10', '11'), ('10', '15'), ('10', '14'),
    ('11', '8'), ('11', '4'), ('11', '9'), ('11', '12'), ('11', '16'), ('11', '15'),
    ('12', '11'), ('12', '16'), ('12', '9'), ('12', '6'), ('12', '13'), ('12', '17'),
    ('13', '6'), ('13', '5'), ('13', '9'), ('13', '12'), ('13', '17'), ('13', '18'),
    ('14', '10'), ('14', '15'),
    ('15', '14'), ('15', '10'), ('15', '11'), ('15', '16'), ('15', '19'),
    ('16', '11'), ('16', '15'), ('16', '19'), ('16', '12'), ('16', '17'), ('16', '18'),
    ('17', '12'), ('17', '13'), ('17', '18'), ('17', '16'),
    ('18', '13'), ('18', '17'), ('18', '16'), ('18', '19'),
    ('19', '15'), ('19', '16'), ('19', '18')
]

# Labels for each node
if isinstance(positions[0], tuple) and len(positions[0]) > 2:
    labels = [pos[2] for pos in positions]
else:
    labels = [
        "Nutwood Parking",
        "Visual Arts",
        "Titan Student Union",
        "Recreation Center",
        "Clayes Performing Arts Center",
        "Titan Bookstore",
        "Titan Gym",
        "Dan Black Hall",
        "McCarthy Hall",
        "Pollack Library",
        "Langsdorf Hall",
        "Humanities",
        "Education Classroom",
        "Student Health",
        "SGMH",
        "Carls Jr",
        "Lot F",
        "Engineering Building",
        "Gastronome",
        "East Side Parking Structure"
    ]

# Create a dictionary for node positions and labels
pos = {str(i): positions[i] for i in range(len(positions))}
node_labels = {str(i): str(i) for i in range(len(positions))}

# Create a new graph and add the specified edges
G_explicit = nx.DiGraph()
G_explicit.add_edges_from(edges_explicit)

# Generate a unique color for each node for the legend
unique_colors = plt.cm.rainbow(np.linspace(0, 1, len(positions)))

# Set up the figure and axis for the map
fig, ax = plt.subplots(figsize=(12, 9))
ax.imshow(base_map)
ax.axis('off')

# Draw the nodes and edges
nx.draw_networkx(G_explicit.to_undirected(), pos, ax=ax, node_color=unique_colors, edge_color='black', width=2, node_size=300)

# Draw node labels (node numbers only)
nx.draw_networkx_labels(G_explicit, pos, labels=node_labels, font_color='black')

# Create a legend that matches node colors to their labels with numbers
legend_handles = [
    plt.Line2D([0], [0], marker='o', color='w', label=f" {idx}: {name}", 
               markersize=10, markerfacecolor=color)
    for idx, (name, color) in enumerate(zip(labels, unique_colors))
]

# Add the legend to the plot
legend_ax = fig.add_axes([0.74, 0.3, 0.2, 0.4])
legend_ax.axis('off')
legend_ax.legend(handles=legend_handles, loc='center', title='Directory')

# Adjust the layout to accommodate the legend
plt.subplots_adjust(right=0.7)

# Display the plot
plt.show()