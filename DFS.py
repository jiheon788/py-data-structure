from collections import deque

class StationNode:
    """간단한 지하철 역 노드 클래스"""
    def __init__(self, station_name):
        self.station_name = station_name
        self.visited = 0  # 한 번도 본적 없을 때: 0, 스택에 있을 때: 1, 발견된 상태: 2
        self.adjacent_stations = []


    def add_connection(self, other_station):
        """지하철 역 노드 사이 엣지 저장하기"""
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)


def create_station_graph(input_file):
    """input_file에서 데이터를 읽어 와서 지하철 그래프 노드들을 리턴하는 함수"""
    stations = {}  # 지하철 역 노드들을 담을 딕셔너리

    # 파라미터로 받은 input_file 파일을 연다
    with open(input_file) as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            previous_station = None  # 엣지를 저장하기 위한 도우미 변수. 현재 보고 있는 역 전 역을 저장한다
            subway_line = line.strip().split("-")  # 앞 뒤 띄어쓰기를 없애고 "-"를 기준점으로 데이터를 나눈다

            for name in subway_line:
                station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기

                # 지하철 역 이름이 이미 저장한 key 인지 확인
                if station_name not in stations:
                    current_station = StationNode(station_name)  # 새로운 인스턴스를 생성하고
                    stations[station_name] = current_station  # dictionary에 역 이름은 key로, 역 인스턴스를 value로 저장한다

                else:
                    current_station = stations[station_name]  # 이미 저장한 역이면 stations에서 역 인스턴스를 갖고 온다

                if previous_station is not None:
                    current_station.add_connection(previous_station)  # 현재 역과 전 역의 엣지를 연결한다

                previous_station = current_station  # 현재 역을 전 역으로 저장

    return stations

def dfs(graph, start_node):
    """dfs 함수"""
    stack = deque()  # 빈 스택 생성

    # 모든 노드를 처음 보는 노드로 초기화
    for station_node in graph.values():
        station_node.visited = 0

    start_node.visited = 1
    stack.append(start_node)

    while stack:
      current_station = stack.pop()
      current_station.visited = 2
      for neighbor in current_station.adjacent_stations:
        if neighbor.visited == 0:
          neighbor.visited = 1
          stack.append(neighbor)




stations = create_station_graph("./stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
dfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)