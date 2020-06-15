class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        queue = []
        visited = dict()
        for item in flights:
            if item[0] == src:
                queue.append((item[1],item[2],0))
                visited[item[1]] = item[2]
        min_cost = 1000000000
        while queue:
            current_city,current_cost,current_stop = queue.pop(0)
            #print(current_city)
            if current_city == dst:
                min_cost = min(min_cost,current_cost)
            if current_stop >= k:
                continue
            for item in flights:
                if item[0] == current_city and item[1] == dst:
                    min_cost = min(min_cost,current_cost + item[2])
                if item[0] == current_city and item[1] not in visited:
                    queue.append((item[1],item[2]+current_cost,current_stop+1))
                    visited[item[1]] = current_cost+item[2]
                if item[0] == current_city and visited[item[1]] > item[2]+current_cost:
                    queue.append((item[1],item[2]+current_cost,current_stop+1))
                    visited[item[1]] = current_cost+item[2]
        if min_cost != 1000000000:
            return min_cost
        return -1