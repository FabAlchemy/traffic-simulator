from classes import *

cross_list = C = []
cross_list.append(Cross((0,0)))
cross_list.append(Cross((100,0)))
cross_list.append(Cross((50,50)))


road_list = R = []
road_list.append(Road(C[0], C[1], 54/3.6))
R.append(Road(C[1], C[2], 54/3.6))
R.append(Road(C[2], C[0], 54/3.6))


for rd in road_list:
    print(rd)


C[0].define_priority_axis((R[0], R[2]))
C[1].define_priority_axis((R[0], R[1]))
C[2].define_priority_axis((R[1], R[2]))
C[0].sort_linked_roads()
C[1].sort_linked_roads()
C[2].sort_linked_roads()
