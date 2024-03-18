import heapq as hq
import sys

graph = {
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: [(3, 5)],
    7: [(7, 6), (9, 8)],
    8: [],
}


def dijkstra(graph, start_v, dest_v):
    distances = [sys.maxsize] * (len(graph) + 1)
    # 시작점 예약하기
    # 시작점: 1번노드 / 시작 비용: 0
    pq = []
    hq.heappush(pq, (0, start_v))
    distances[start_v] = 0

    while pq:
        cur_d, cur_v = hq.heappop(pq)
        if cur_d > distances[cur_v]:
            continue
        for next_cost, next_v in graph[cur_v]:
            next_d = cur_d + next_cost
            if next_d < distances[next_v]:
                hq.heappush(pq, (next_d, next_v))
                distances[next_v] = next_d
    print(distances)
    return distances[dest_v]


print(dijkstra(graph, 1, 8))
