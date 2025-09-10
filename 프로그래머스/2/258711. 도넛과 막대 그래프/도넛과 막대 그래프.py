def solution(edges):
    answer = [0,0,0,0] #생성 정점, 도넛, 막대, 8자
    max_vertex_num = max(map(max, edges)) + 1
    outs = [0] * max_vertex_num
    ins = [0] * max_vertex_num
    
    for out_v, in_v in edges:
        outs[out_v] += 1
        ins[in_v] += 1
    # print(outs, ins)
    # print(max_vertex_num)
    total_graph_count = 0
    for node in range(1, max_vertex_num):
        if outs[node] >= 2 and ins[node] == 0: #생성한 정점 조건
            answer[0] = node
            total_graph_count = outs[node]
        # 1개 이상 들어오고 나가는게 없는 정점의 개수가 막대 그래프 개수
        if ins[node] >= 1 and outs[node] == 0:
            answer[2] += 1
        # 2개 이상 들어오고 나가는게 2개면 8자 그래프 개수
        if ins[node] >= 2 and outs[node] == 2:
            answer[3] += 1
    # 도넛
    answer[1] = total_graph_count - answer[3] - answer[2]
    
    # print(total_graph_count)
    return answer