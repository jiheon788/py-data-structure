# Data Structure Using Python

## Linked List

## Doubly Linked List

## Hash Table

## Queue
* FIFO (First-in, First-Out)
* 먼저 들어간 데이터가 먼저 나온다.
* e.g. 은행 줄서기

## Stack
* LIFO (Last-in, First-Out)
* 마지막에 들어간 데이터가 처음에 나온다.
* e.g. 접시쌓기


## Tree
### Full Binary Tree (정 이진 트리)
* 모든 노드가 2개 또는 0개의 자식을 갖는 이진 트리
* 자식이 하나인 노드가 존재하면 안됨

### Complete Binary Tree (완전 이진 트리)
* 마지막 레벨 제외 모든 노드가 채워짐
* 마지막 레벨은 왼쪽에서 오른쪽 방향으로는 다 채워짐


### Perfect Binary Tree (포화 이진 트리)
* 모든 레벨이 빠짐없이 채워짐

## Heap
* Complete Binary Tree && **모든 부모 노드는 자식 노들들의 데이터 보다 크거나 같다.**
* 힙 정렬 & 우선순위 큐를 구현하기 위하여 사용
* 힙은 완전 정렬된 상태가 아니다.

### Heapify
* 완전이진트리를 정렬을 통하여 Heap으로 만들어줌
* 가장 마지막 노드부터 root 노드까지 역순으로 heapify() 해주어야 함


### 힙 정렬
1. 리스트를 힙으로 만든다.
2. root 노드와 마지막 노드의 위치를 바꿉니다. 마지막 위치로 간 기존의 root 노드는 이제 힙에서 없다고 가정합니다.
3. 새로운 root 노드가 힙 속성을 지킬 수 있게 heapify합니다.
4. 힙에 남아있는 노드가 없도록 단계 2 ~ 3을 반복합니다.
