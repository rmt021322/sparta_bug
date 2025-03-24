import sys
sys.stdin = open("algo2_sample_in.txt", "r")  # 파일로부터 입력을 받음

def preorder(tree, idx, result):
    if idx >= len(tree):
        return
    result.append(tree[idx])
    preorder(tree, 2 * idx + 1, result)  # 왼쪽 자식
    preorder(tree, 2 * idx + 2, result)  # 오른쪽 자식

def inorder(tree, idx, result):
    if idx >= len(tree):
        return
    inorder(tree, 2 * idx + 1, result)  # 왼쪽 자식
    result.append(tree[idx])
    inorder(tree, 2 * idx + 2, result)  # 오른쪽 자식

def postorder(tree, idx, result):
    if idx >= len(tree):
        return
    postorder(tree, 2 * idx + 1, result)  # 왼쪽 자식
    postorder(tree, 2 * idx + 2, result)  # 오른쪽 자식
    result.append(tree[idx])

def solve():
    T = int(input())  # 테스트 케이스 개수
    for _ in range(T):
        N = int(input())  # 정점의 개수
        tree = list(map(int, input().split()))  # 트리 정점의 값들

        # 각 순회 방식으로 트리 순회
        preorder_result = []
        inorder_result = []
        postorder_result = []
        
        preorder(tree, 0, preorder_result)
        inorder(tree, 0, inorder_result)
        postorder(tree, 0, postorder_result)
        
        # 순회 결과를 이진수 문자열로 만들기
        preorder_binary = ''.join(map(str, preorder_result))
        inorder_binary = ''.join(map(str, inorder_result))
        postorder_binary = ''.join(map(str, postorder_result))
        
        # 이진수를 10진수로 변환하여 최댓값 찾기
        max_value = max(int(preorder_binary, 2), int(inorder_binary, 2), int(postorder_binary, 2))
        
        # 결과 출력
        print(max_value)

# solve() 함수를 호출하여 실행
solve()
