import LinkedList
import DoublyLinkedList

# 생성
my_list = LinkedList.LinkedList()

# 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

# 출력 (__str__ 메서드 호출)
print(f"전체 출력: {my_list}")

# 노드에 접근
print(f"노드 접근: {my_list.find_node_at(3).data}")

# 노드에 접근/수정
my_list.find_node_at(2).data = 13

print(f"2번 노드 변경 후: {my_list}")


# 데이터 2를 갖는 노드 탐색
node_with_2 = my_list.find_node_with_data(2)

if not node_with_2 is None:
    print(node_with_2.data)
else:
    print("2를 갖는 노드는 없습니다")

# 데이터 11을 갖는 노드 탐색
node_with_6 = my_list.find_node_with_data(6)

if not node_with_6 is None:
    print(node_with_6.data)
else:
    print("6를 갖는 노드는 없습니다")

node_2 = my_list.find_node_at(2)
my_list.insert_after(node_2, 6)

print(f"전체 출력: {my_list}")


head_node = my_list.head
my_list.insert_after(head_node, 9)

print(f"전체 출력: {my_list}")


my_list.prepend(20)

print(f"전체 출력: {my_list}")

node_2 = my_list.find_node_at(2)
my_list.delete_after(node_2)

print(f"전체 출력: {my_list}")

# 가장 앞 노드 계속 삭제
print(my_list.pop_left())
print(my_list.pop_left())

print(f"전체 출력: {my_list}")

print("----------이중연결리스트------------")

my_list = DoublyLinkedList.DoublyLinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(f"전체 출력: {my_list}")

tail_node = my_list.tail  # tail 노드
my_list.insert_after(tail_node, 6)  # tail 노드 뒤에 노드 추가
print(my_list)
print(my_list.tail.data)  # 새로운 tail 노드 데이터 출력

# 링크드 리스트 중간에 데이터 삽입
node_at_index_3 = my_list.find_node_at(3)  # 노드 접근
my_list.insert_after(node_at_index_3, 3)
print(my_list)

# 링크드 리스트 중간에 데이터 삽입
node_at_index_2 = my_list.find_node_at(2)  # 노드 접근
my_list.insert_after(node_at_index_2, 2)
print(my_list)

#  여러 데이터를 링크드 리스트 앞에 추가
my_list.prepend(20)
my_list.prepend(30)


print(my_list)  # 링크드 리스트 출력

# head, tail 노드가 제대로 설정됐는지 확인
print(my_list.head.data)
print(my_list.tail.data)

