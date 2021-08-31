from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    
    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()
        if city not in cache:
            answer += 5
            
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.popleft(),
                cache.append(city)
        
        elif city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        
    return answer

test_case = [
    [3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]],
    [3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]],
    [2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]],
    [5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]],
    [2, ["Jeju", "Pangyo", "NewYork", "newyork"]],
    [0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]]
]

for t1, t2 in test_case:
    print(solution(t1, t2))