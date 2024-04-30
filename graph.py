# Graph representation of 20 Csuf locations and paths between them
Campus_graph = {
         'Nutwood Parking': [['Dan Black Hall',815],['McCarthy Hall',896],['Clayes Performing Arts Center',747],['Visual Arts',667]],
         'Visual Arts': [['Clayes Performing Arts Center',421],['Titan Student Union',357],['Nutwood Parking',667]],
         'Titan Student Union': [['Visual Arts',357],['Titan Bookstore',337],['Recreation Center',480]],
         'Recreation Center': [['Titan Student Union',480],['Titan Gym',500],['Titan Bookstore',526],['Pollack Library',930]],
         'Clayes Performing Arts Center': [['Visual Arts',421],['Titan Bookstore',490],['Pollack Library',536],['Humanities',746],['McCarthy Hall',439],['Dan Black Hall',574],['Nutwood Parking',747]],
         'Titan Bookstore': [['Titan Student Union',337],['Recreation Center',526],['Titan Gym',465],['Student Health',887],['Pollack Library',472],['Clayes Performing Arts Center',490]],
         'Titan Gym': [['Recreation Center',500],['Titan Bookstore',465],['Student Health',500],['Pollack Library',605],['Education Classroom',787]],
         'Dan Black Hall': [['Nutwood Parking',815],['Langsdorf Hall',411],['Clayes Performing Arts Center',574],['McCarthy Hall',165],['Pollack Library',855],['Humanities',679]],
         'McCarthy Hall': [['Humanities',453],['Dan Black Hall',165],['Nutwood Parking',896]],
         'Pollack Library': [['Dan Black Hall',855],['Clayes Performing Arts Center',536],['Titan Bookstore',472],['Recreation Center',930],['Titan Gym',580],['Student Health',647],['Education Classroom',600],['Humanities',528]],
         'Langsdorf Hall': [['Dan Black Hall',411],['SGMH',227],['Carls Jr',228],['Humanities',520],['McCarthy Hall',353]],
         'Humanities': [['Education Classroom',337],['Pollack Library',528],['Clayes Performing Arts Center',746],['McCarthy Hall',453],['Dan Black Hall',679],['Langsdorf Hall',520],['Carls Jr',413],['Lot F',338]],
         'Education Classroom': [['Humanities',337],['Pollack Library',600],['Titan Gym',787],['Student Health',600],['Engieering Building',477],['Lot F',497]],
         'Student Health': [['Titan Gym',500],['Gastronome',586],['Engieering Building',409],['Education Classroom',600],[ 'Pollack Library',647],['Titan Bookstore',464]],
         'SGMH': [['Carls Jr',256],['Langsdorf Hall',227]],
         'Carls Jr': [['SGMH',256],['Langsdorf Hall',228],['Lot F',461,],['East Side Parking Structure',694],['Humanities',413]],
         'Lot F': [['Carls Jr',461],['East Side Parking Structure',380],['Gastronome',985],['Engieering Building',677],['Education Classroom',497],['Humanities',338]],
         'Engieering Building': [['Lot F',677],['Gastronome',416],['Student Health',409],['Education Classroom',477]],
         'Gastronome': [['Engieering Building',416],['Student Health',586],['Lot F',985],['East Side Parking Structure',1045]],
         'East Side Parking Structure': [['Carls Jr',694],['Lot F',380],['Gastronome',1045]]
         }



def dfs(visited, graph, node,search):  #function for dfs 
    global distance
    if node not in visited:
        if node == search:
           dfs_stack.append(node)
           return True
        
        visited.add(node)
        for neighbour in graph[node]:
            if dfs(visited, graph, neighbour[0],search):
                #when a target node is found we start appending the nodes to the list
                dfs_stack.append(node)
                distance += neighbour[1]
                return True
        
        return False




############## DFS #########################################
distance = 0
dfs_visited = set() # Set to keep track of visited nodes of graph.
dfs_stack = [] #tracks path

### CHOOSE START/END 
dfs(dfs_visited,Campus_graph,'Titan Gym','Visual Arts')
dfs_stack.reverse()#reverses stack to represent path


#adds the total distance covered
#for i in range(len(dfs_stack)-1):
    #distance += dfs_stack[i][1]

print(dfs_stack)
print(distance)



############ BFS ######################
from collections import deque

def bfs_all(graph, start, goal):

    queue = deque([(start, [start], 0)])                        # Queue for BFS (node, path, distance)
    bfs_visited = set()
    all_paths = []
    
    while queue:
        current_node, path, total_distance = queue.popleft()

        if current_node == goal:
            all_paths.append((path, total_distance))            # Store path & distance if a possible path is found
            continue                                            # Continue to next node
        
        bfs_visited.add(current_node)                           # Mark current node as visited

        for neighbor, distance in graph[current_node]:          # Queue adjacent nodes
            if neighbor not in bfs_visited:
                new_path = path + [neighbor]
                new_distance = total_distance + distance
                queue.append((neighbor, new_path, new_distance))

    return all_paths                                            # Return all possible paths & their distances

# BFS test
all_paths = bfs_all(Campus_graph, 'Titan Gym', 'Visual Arts')
for path, distance in all_paths:
    print("Path:", path)
    print("Distance:", distance)


############## Dijkstra's ###############