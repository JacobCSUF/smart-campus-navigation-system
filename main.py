import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import numpy as np
from PIL import Image, ImageTk
from pathfinding import dfs_path, bfs_path, dijkstra_path
from graph_data import edges_distances, edges_explicit, positions

# Constants for walking speed
WALKING_SPEED_MPH = 2.5
FEET_PER_MILE = 5280

# Initialize the Tkinter root window first
root = tk.Tk()
root.title("Smart Campus Navigation System")

# CSUF map image
base_map_path = 'image/map.png'
base_image = Image.open(base_map_path)

# Convert the image for Tkinter use
tk_image = ImageTk.PhotoImage(base_image, master=root)

# Map given positions to graph nodes
pos = {str(i): positions[i] for i in range(len(positions))}

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

# Create a directed graph and define edges with distances
G = nx.DiGraph()

# Use the imported edge distances
G.add_weighted_edges_from(edges_distances)  

# Set DPI for the figure
dpi = 75

# Calculate the size in inches (1920x1080 pixels)
fig_width = 1280 / dpi
fig_height = 720 / dpi

# Create the figure with the specified size
fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi)
ax.imshow(base_image)
ax.axis('off')

# Create a FigureCanvasTkAgg object
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill='both', expand=True)

# GUI components for node and algorithm selection
start_var = tk.StringVar(value='Nutwood Parking')
end_var = tk.StringVar(value='Visual Arts')
algorithm_var = tk.StringVar(value="DFS")

# Label setup for displaying results
results_var = tk.StringVar()
results_var.set("Select start, end, and algorithm then press 'Calculate Path'")

# Define a larger font for better visibility
large_font = ('Helvetica', 14)
text_color = "blue"  # You can use color names or hexadecimal color codes

# Dropdown and label placement
ttk.Label(root, text="Start Node:", font=large_font, foreground=text_color).pack()
start_dropdown = ttk.Combobox(root, textvariable=start_var, values=labels, font=large_font, width=20)
start_dropdown.pack()

ttk.Label(root, text="End Node:", font=large_font, foreground=text_color).pack()
end_dropdown = ttk.Combobox(root, textvariable=end_var, values=labels, font=large_font, width=20)
end_dropdown.pack()

ttk.Label(root, text="Algorithm:", font=large_font, foreground=text_color).pack()
algorithm_dropdown = ttk.Combobox(root, textvariable=algorithm_var, values=["DFS", "BFS", "Dijkstra"], font=large_font, width=20)
algorithm_dropdown.pack()

# List to store results for display
results_list = []

# Draw labels colors
nx.draw_networkx_labels(G, pos={node: positions[labels.index(node)] for node in G}, labels={node: node for node in G},
                        font_color='blue', font_size=12, ax=ax,
                        bbox=dict(facecolor='white', alpha=0.1, edgecolor='none'))

# Function to update the graph based on user selections
def update_graph():
    start_node = start_var.get()
    end_node = end_var.get()
    algorithm = algorithm_var.get()
    path = None

    # Calling the all algorithms from pathfinding.py
    if algorithm == "DFS":
        path = dfs_path(G, start_node, end_node)
    elif algorithm == "BFS":
        path = bfs_path(G, start_node, end_node)
    else:
        path = dijkstra_path(G, start_node, end_node) 

    # Calculate the total distance and time of the path
    if path:
        total_distance = sum(G[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
        time_in_minutes = (total_distance / FEET_PER_MILE) / WALKING_SPEED_MPH * 60
        result_text = f"Algorithm: {algorithm}, Distance: {total_distance:.2f} ft, Time: {time_in_minutes:.2f} min"
        
        ax.clear()
        ax.imshow(base_image)

        # Specific colors for start and end nodes, and one color for all other nodes
        node_colors = ['lime' if node == path[0] else 'red' if node == path[-1] else 'yellow' for node in path]

        # Start and End nodes are larger
        node_sizes = [300 if node == path[0] or node == path[-1] else 150 for node in path]

        # Draw the network
        nx.draw_networkx(G, pos={node: positions[labels.index(node)] for node in G}, ax=ax, nodelist=path,
                        edgelist=list(zip(path, path[1:])), node_color=node_colors, edge_color='black', width=2, node_size=node_sizes)

        # Draw labels colors
        nx.draw_networkx_labels(G, pos={node: positions[labels.index(node)] for node in G}, labels={node: node for node in G},
                                font_color='blue', font_size=12, ax=ax,
                                bbox=dict(facecolor='white', alpha=0.1, edgecolor='none'))

        canvas.draw()
        print(f"Path: {path}, Distance: {total_distance} feet, Time: {time_in_minutes:.2f} minutes")
    else:
        print("No path found.")

    # Update the list of results and maintain only the last three entries
    results_list.append(result_text)
    if len(results_list) > 3:
        results_list.pop(0)  # Remove the oldest result if more than three

    # Update the results display
    results_var.set("\n\n".join(results_list))
    
# Button to update the graph based on user selections, making it larger with a larger font
update_button = ttk.Button(root, text="Calculate Path", command=update_graph, style='Large.TButton')
update_button.pack(pady=10)

results_display = ttk.Label(root, textvariable=results_var, font=large_font)
results_display.pack(pady=20)

# Apply a style to enlarge button text
style = ttk.Style()
style.configure('Large.TButton', font=('Helvetica', 16))

root.mainloop()
