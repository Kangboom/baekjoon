def del_tree(root, n):
    # root를 삭제하면 무조건 0리턴
    if root == n:
        return 0
    
    cnt = 0
    stack = []
    stack.append(root)

    while stack:
        v = stack.pop()
        
        # 자식들 중 지울 노드가 아닌 노드만 stack에 추가
        for child in childs[v]:
            if( child != n):    
                stack.append(child)

        # 자신의 자식 중에 지울 노드가 있다면 삭제
        if n in childs[v]:
            childs[v].remove(n)    

        # 자신이 리프 노드인지 아닌지 검사, 맞으면 cnt +1 
        if not childs[v] :
            cnt += 1

    return cnt   

N = int(input())
tree = list(map(int, input().split()))
del_num = int(input())
root = 0
# 자식 정보를 가지고 있는 리스트 생성
childs = [[] for _ in range(N)]

# 자신의 자식들을 정리한 childs 리스트 생성
for i, p in enumerate(tree):
    if p == -1 : # 루트는 따로 기록함. 무조건 0번 노드가 루트가 아님!
        root = i 
        continue
    childs[p].append(i) # 부모가 적혀있는 tree 리스트를 토대로 childs 리스트 작성

print(del_tree(root, del_num))
