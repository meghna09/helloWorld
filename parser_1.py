# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:57:56 2018

@author: mmadhusu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 08:53:29 2018

@author: mmadhusu
"""
import global_router_schematic
import math
import copy
import numpy as np
#netlist parser
ncount = 1

class MOSFET:
    type = ""
    x= "0"
    y= "0"
    g=""
    d=""
    s=""
    b="vss"
    id =""
    name = ""

MOSlist = [MOSFET() for count in range(ncount)]

#f= open('C:\\Users\\mmadhusu\\Desktop\\Work summary\\netlist_OTA_ADT1.txt','r')
#lines = f.readlines()
#f.close()
#i=0
#subckt = False
#for line in lines:
#    if "Cell name: ota_test_ADT" in line:
#        subckt = True
#    if subckt == True:
#        if "qn" in line:
#            MOSlist.append(MOSFET())
#            line = line.replace("(","")
#            line = line.replace(")","")
#            line =line.split(" ")
#            MOSlist[i].type = "NMOS"
#            MOSlist[i].d = line[1]
#            MOSlist[i].g= line[2]
#            MOSlist[i].s=line[3]
#            MOSlist[i].name=line[4]
#            MOSlist[i].id=i
#            i=i+1
#            #for part in line:
#             #   print("\n", part)
#            #print(line)
#        if "qp" in line:
#            MOSlist.append(MOSFET())
#            line = line.replace("(","")
#            line = line.replace(")","")
#            line =line.split(" ")
#            MOSlist[i].type = "PMOS"
#            MOSlist[i].d = line[1]
#            MOSlist[i].g= line[2]
#            MOSlist[i].s=line[3]
#            MOSlist[i].b=line[4]
#            MOSlist[i].name=line[5]
#            MOSlist[i].id=str(i)
#            i=i+1
#
#g= open('C:\\Users\\mmadhusu\\Desktop\\Work summary\\instance_position_schematic.txt','r')
#lines_1 = g.readlines()
#g.close()
#del MOSlist[i]
#i=0
#for line in lines_1:
#    line = line.replace("(","")
#    line = line.replace(")","")
#    line = line.split(" ")
#    MOSlist[i].x=str(math.floor((float(line[0])+2)*2.5))
#    #print(MOSlist[i].x)
#    MOSlist[i].y=str(math.floor((float(line[1])+2)*2.5))
#    i=i+1
#
#
#for m in range(len(MOSlist)):
#    print("\n",MOSlist[m].type,"\n", MOSlist[m].d,"\n", MOSlist[m].g,"\n", MOSlist[m].s,"\n", MOSlist[m].b,"\n", MOSlist[m].name, MOSlist[m].id, "\n", MOSlist[m].x, "\n", MOSlist[m].y)
#    
#if global_router_schematic.get_route_position():
#    print("get routes succeeded")
#else:
#    print("Failed")
##global router
##grid position - x and y
##name of nets and connection - d, g, s, b

class GridCell(object):
    def __init__(self, cost = 1, pred = "", reached = "False", x =0, y=0, pathcost = 1, obstacle = 0):
        self.cost = cost
        self.pred = pred
        self.reached = reached
        self.x = x
        self.y = y
        self.pathcost = pathcost
        self.obstacle = obstacle
    
class wavefront_cell(object):
    def __init__(self, pathcost=0, pred="",x=0,y=0):
        pathcost = pathcost
        pred = pred
        x = x
        y = y


grid = [GridCell() for count in range(ncount)] 

route_pathcost =[]
wavefront = [GridCell() for count in range(ncount)]
del wavefront[0]    
source = GridCell()
target = GridCell()
route_gr=[]

def route(wavefront, grid, source, target):
    if not wavefront:
        print("wavefront empty")
        return False
    i=0
    #print(len(wavefront), "before while")
    while(wavefront):
       # print("Hi")
       #print(len(wavefront),"in while")
       wavefront=sorted(wavefront, key=lambda cell: cell.pathcost, reverse=False)
       C = copy.deepcopy(wavefront[0])
        #print(C.x, C.y, "Hi")
       if(int(C.x)== int(target.x) and int(C.y) == int(target.y)):
           #print(target.x, target.y)
           #print(C.x, C.y)
           T= GridCell(1,"","False",0,0,1)
           T= copy.deepcopy(C)
           #print(T.pred, T.x, T.y, T.pathcost)
           route_gr.append([T.x, T.y])
           route_pathcost.append(T.pathcost)
           while(T.x != int(source.x) or T.y != int(source.y)):
               #print(type(T.pred),type(T.reached))
               #if T.pred == "W":
                   #print("XYZ")
               print(T.x, T.y, T.pred, source.x, source.y, source.pred)
               if T.pred == "S":
                   for X in range(len(grid)):
                       if grid[X].y == (int(T.y) -1) and grid[X].x == int(T.x) and grid[X].reached == "True":
                           route_gr.append([grid[X].x, grid[X].y])
                           T = copy.deepcopy(grid[X])
                           break
                           #print("MNO")
               elif T.pred == "N":
                   for X in range(len(grid)):
                       if grid[X].y == (int(T.y) +1) and grid[X].x == int(T.x) and grid[X].reached == "True":
                           route_gr.append([grid[X].x, grid[X].y])
                           T = copy.deepcopy(grid[X])
                           break
               elif T.pred == "W":
                   for X in range(len(grid)):
                       if grid[X].y == int(T.y) and grid[X].x == (int(T.x) - 1) and grid[X].reached == "True":
                           route_gr.append([grid[X].x, grid[X].y])
                           T = copy.deepcopy(grid[X])
                           break
               elif T.pred == "E":
                   for X in range(len(grid)):
                       if grid[X].y == int(T.y) and grid[X].x == (int(T.x) + 1) and grid[X].reached == "True":
                           route_gr.append([grid[X].x, grid[X].y])
                           T = copy.deepcopy(grid[X])
                           break
               #print("ABC")
               #print(T.x, T.y, T.pred, source.x, source.y, source.pred, grid[X].x, grid[X].y, grid[X].pred)
           return True
       for N in range(len(grid)):
           #if grid[N].obstacle == int(0):
              #print ("M", wavefront[0].reached,grid[N].reached, len(grid))
              #break
           if ((grid[N].x== int(C.x) + 1) and (grid[N].y  == int(C.y)) and grid[N].reached == "False" and grid[N].obstacle==int(0)):
              grid[N].pred="W"
              grid[N].pathcost = C.pathcost + grid[N].cost
              grid[N].reached="True"
              wavefront.append(grid[N])
              i = i + 1
              #print(i)
                #print("MM")
           elif grid[N].x==int(C.x) - 1 and grid[N].y  == int(C.y) and grid[N].reached == "False" and grid[N].obstacle==int(0):
              grid[N].pred="E"
              grid[N].pathcost = C.pathcost + grid[N].cost
              grid[N].reached="True"
              #print("IJKL")
              wavefront.append(grid[N])
           elif grid[N].y==int(C.y) + 1 and grid[N].x  == int(C.x) and grid[N].reached == "False" and grid[N].obstacle==int(0):
              grid[N].pred="S"
              grid[N].pathcost = C.pathcost + grid[N].cost
              grid[N].reached="True"
              wavefront.append(grid[N])
              #print("Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
           elif grid[N].y==int(C.y) - 1 and grid[N].x  == int(C.x) and grid[N].reached == "False" and grid[N].obstacle==int(0):
              grid[N].pred="N"
              grid[N].pathcost = C.pathcost + grid[N].cost
              grid[N].reached="True"
              wavefront.append(grid[N])
           #if grid[N].obstacle == int(1):
               #print (grid[N].x, grid[N].y)
              #print("helloooooooooooooo")
           
               #print(wavefront[0].x, wavefront[0].y, "Hello", wavefront[0].reached, wavefront[0].obstacle)
          #  else:
           #     print("Okay")
       del wavefront[0]
       #print(wavefront[0].x, wavefront[0].y, "Hello")
    return False
    
    

#for l in range(len(grid)):
 #   print(grid[l].x, grid[l].y)


xg = 10
yg = 10

for x in range(xg):
    for y in range(yg):
        grid.append(GridCell(1,"","False",x,y,1,0))

del grid[0]

def constraints(m,n):
    if(m.d==n.d or m.d==n.s or m.d==n.g or m.d==n.b):
        return True
    elif(m.s==n.d or m.s==n.s or m.s==n.g or m.s==n.b):
        return True
    elif(m.g==n.d or m.g==n.s or m.g==n.g or m.g==n.b):
        return True
    elif(m.b==n.d or m.b==n.s or m.b==n.g or m.b==n.b):
        return True
    else:
        return False

#routed both ways, redundancy present
#for k in range(len(MOSlist)):
#    for p in range(len(MOSlist)):
#        if(p!=k):
#            if constraints(MOSlist[k],MOSlist[p]):
#                #del grid[:]
#                #grid = [GridCell() for count in range(ncount)] 
##                for x in range(xg):
##                    for y in range(yg):
##                        grid.append(GridCell(1,"","False",x,y,1))
##
##                del grid[0]
#                del wavefront[:]
#                source = GridCell(1,"","True",MOSlist[k].x, MOSlist[k].y,1)
#                for X in range(len(grid)):
#                    if grid[X].x == int(source.x) and grid[X].y== int(source.y):
#                        grid[X].reached = "True"
#                target = GridCell(1,"","False",MOSlist[p].x, MOSlist[p].y,1)
#                print(source.x, source.y)
#                print(target.x, target.y)
#                wavefront.append(source)
#                print(wavefront[0].x, "Hi", wavefront[0].y, wavefront[0].obstacle)
#                if route(wavefront, grid, source, target):
#                    print("route succeeded")
#                    tempx=0
#                    tempy=0
#                    for x,y in route_gr:
#                        for M in range(len(grid)):
#                            grid[M].pred=""
#                            grid[M].pathcost = 1
#                            grid[M].reached = "False"
#                            if grid[M].x==x and grid[M].y==y:
#                                grid[M].obstacle = 1
#                                print(grid[M].x, grid[M].y, grid[M].obstacle)
#                        #if x != tempx and y == tempy:
#                        print("horizontal", x,y)
#                        #elif y != tempy and x == tempx:
#                        print("vertical", x, y)
#                        tempx = x
#                        tempy = y
#                else:
#                    print("route failed")
#            
#print("Grid", grid[19].x, grid[19].y)
#
for m in range(len(global_router_schematic.get_route_position.coordinates_source)):
    del wavefront[:]
    source = GridCell(1,"","True",global_router_schematic.get_route_position.coordinates_source[m][0], global_router_schematic.get_route_position.coordinates_source[m][1],1,0)
    target = GridCell(1,"","False",global_router_schematic.get_route_position.coordinates_target[m][0], global_router_schematic.get_route_position.coordinates_target[m][1],1,0)

    for X in range(len(grid)):
        if grid[X].x == int(source.x) and grid[X].y== int(source.y):
            grid[X].reached = "True"
            grid[X].obstacle = 0
        if grid[X].x == int(target.x) and grid[X].y == int(target.y):
            grid[X].obstacle = 0
            #grid[X].reached = "False"
        
    print(source.x, source.y)
    print(target.x, target.y)
    wavefront.append(source)
    print(wavefront[0].x, "Hi", wavefront[0].y, wavefront[0].obstacle)
    if route(wavefront, grid, source, target):
        print("route succeeded")
        tempx=0
        tempy=0
        for x,y in route_gr:
            for M in range(len(grid)):
                grid[M].pred=""
                grid[M].pathcost = 1
                grid[M].reached = "False"
                if grid[M].x==x and grid[M].y==y:
                    grid[M].obstacle = 1
                    #print(grid[M].x, grid[M].y, grid[M].obstacle)
            #if x != tempx and y == tempy:
            #print("horizontal", x,y)
            #elif y != tempy and x == tempx:
            #print("vertical", x, y)
            tempx = x
            tempy = y
        print(route_gr[:])
    else:
        print("route failed")


f= open('C:\\Users\\mmadhusu\\Desktop\\Work summary\\netlist_OTA_ADT1.txt','r+')
lines = f.readlines()
f.close()
f= open('C:\\Users\\mmadhusu\\Desktop\\Work summary\\netlist_OTA_ADT1.txt','w')
for line in lines:
    if 'Design Change Time Stamp' in line:
        #f.write("\n")
        f.write(line)
        for m in range(len(route_pathcost)):
            C=0.5*0.2*route_pathcost[m]
            #C= [("C"), m,' ('+global_router_schematic.get_route_position.netname[m]," ", "0)", "capacitor", "c=", str(0.5*0.2*route_pathcost[m]),"f"]
            #f.write(("C")+ str(m)+' ('+str(global_router_schematic.get_route_position.netname[m])+" "+ "0)"+ "capacitor"+ "c="+ str(C)+"f")
            #f.write("\n")
            print(route_pathcost[m], global_router_schematic.get_route_position.netname[m])
            f.write(("C")+ str(m)+' ('+str(global_router_schematic.get_route_position.netname[m])+" "+ "0)"+ " capacitor "+ "c="+ str(C)+"f"+"\n")
            #f.write(line)
    else:
        f.write(line)
        #line = line
#f.write(lines)
f.close()

