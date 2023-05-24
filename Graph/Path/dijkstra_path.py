def dijkstra(self,start_node,end_node):
        #crea un dizionario in cui tutte le distanze sono settate ad infinito
        distances={i:float('inf') for i in self.__graph}
        pathes={i:None for i in self.__graph}

        #setta la distanza del nodo di partenza a 0 in quanto per arrivare dal nodo di partenza al nodo di partenza il costo è zero.
        distances[start_node] = 0
        priority_queue = [(0,start_node)]
        print(pathes)
        while len(priority_queue) > 0:
            
            current_distance,current_node = self.min_pop(priority_queue)

            print('Current node: ',current_node)

            for neighbor, peso in self.__graph[current_node].items():
                print('Vicino: ',neighbor)
                evaluate_distance = current_distance + peso

                if evaluate_distance < distances[neighbor]:
                    distances[neighbor] = evaluate_distance
                    #crea un dizionario in cui la chiave indica il nodo e il valore indica da quale nodo passare
                    pathes[neighbor] = current_node
                    priority_queue.append((evaluate_distance,neighbor))
            print(pathes)
                
                
        path=[end_node]
        current = end_node

        while current is not start_node:
            print(current)
            current = pathes[current]
            path += [current]
        
        print(distances)

        return path,distances[end_node]
