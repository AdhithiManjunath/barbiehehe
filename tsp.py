def get_p(arr, l, r):
    if l == r:
        return [arr[:]]
    else:
        perm = []
        for i in range(l, r + 1):
            arr[i], arr[l] = arr[l], arr[i]
            perm.extend(get_p(arr, l + 1, r))
            arr[l], arr[i] = arr[i], arr[l]
            
    return perm

def tsp(graph, start, cities):
    vertex = [i for i in range(cities) if i != start]
    permutations = get_p(vertex, 0, len(vertex) - 1)
    
    M = []
    
    for i in permutations:
        d = 0
        k = start
        flag = 0
        
        for j in i:
            if graph[k][j] == 0:
                break
            else:
                d += graph[k][j]
                k = j
                flag += 1
        
        if flag == 4:
            if graph[k][start]:
                d += graph[k][start]
                M.append(d)  # Append distance to M
                
    M.sort()
    return M[0]  # Move these lines outside the loop

cities = int(input("Enter number of cities: "))
graph = [
    [0, 2, 0, 12, 5],
    [2, 0, 4, 8, 0],
    [0, 4, 0, 3, 3],
    [12, 8, 3, 0, 10],
    [5, 0, 3, 10, 0]
]

start = int(input("Enter the start city: "))
min_dist = tsp(graph, start, cities)
print(min_dist)