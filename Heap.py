def swap(tree, index_1, index_2):
  """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
  temp = tree[index_1]
  tree[index_1] = tree[index_2]
  tree[index_2] = temp


def heapify(tree, index, tree_size):
  """heapify 함수"""

  # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
  left_child_index = 2 * index
  right_child_index = 2 * index + 1

  largest_index = index  # 일단 부모 노드의 값이 가장 크다고 설정

  # 왼쪽 자식 노드의 값과 비교
  if 0 < left_child_index < tree_size and tree[largest_index] < tree[left_child_index]:
    largest_index = left_child_index

      
  if 0 < right_child_index < tree_size and tree[largest_index] < tree[right_child_index]:
    largest_index = right_child_index

  if largest_index != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
    swap(tree, index, largest_index)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
    heapify(tree, largest_index, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를 대상으로 또 heapify 함수를 호출한다

def heapsort(tree):
    """힙 정렬 함수"""
    tree_size = len(tree)

    # 코드를 쓰세요
    for index in range(tree_size-1, 0, -1):
      heapify(tree, index, tree_size)
        
    for i in range(tree_size-1, 0, -1):
      swap(tree, 1, i)  # root 노드와 마지막 인덱스를 바꿔준 후
      heapify(tree, 1, i)  # root 노드에 heapify를 호출한다



######################################################################
######################################################################
######################################################################

# 실행 코드
# tree = [None, 8, 3, 12, 5, 14, 10, 6, 2, 1, 4]  # heapify하려고 하는 완전 이진 트리

tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 20]  # heapify하려고 하는 완전 이진 트리

print(f"함수 전: {tree}")

heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출

print(f"함수 후: {tree}") 

######################################################################
######################################################################
######################################################################
# 실행 코드
data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
print(f"정렬 전: {data_to_sort}")

heapsort(data_to_sort)
print(f"정렬 후: {data_to_sort}")
