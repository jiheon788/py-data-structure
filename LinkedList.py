from hashlib import new

class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data
        self.next = None  # 다음 노드 레퍼런스

class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메서드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head

        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next

        return None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None:  # 비어있는경우
            self.head = new_node
            self.tail = new_node
        else:  # 비어있지 않은 경우
            self.tail.next = new_node
            self.tail = new_node

    def insert_after(self, previous_node, data):
        """주어진 노드 뒤 삽입 연산"""
        new_node = Node(data)

        if previous_node is self.tail: #가장 마지막 순서 삽입
            self.tail.next = new_node
            self.tail = new_node
        else: #두 노드 사이에 삽입
            new_node.next = previous_node.next
            previous_node.next = new_node

    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_after(self, previous_node):
        """삭제 연산"""
        data = previous_node.next.data

        if previous_node.next is self.tail: # 지우려는 노드가 tail일 떄
            previous_node.next = None
            self.tail = previous_node 
        else: #두 노드 사이 노드를 지울 때 
            previous_node.next = previous_node.next.next     

        return data

    def pop_left(self):
        """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다"""
        data = self.head.data
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return data

    def __str__(self):
        """링크드 리스트를 문자열로 리턴"""
        res_str = "|"
        iterator = self.head

        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next

        return res_str






