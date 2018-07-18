# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:01:37 2018

@author: mmadhusu
"""
import math
import copy
import numpy as np

def get_route_position():
    g= open('C:\\Users\\mmadhusu\\Desktop\\Work summary\\schematic_instance_position2.txt','r')
    lines1 = g.readlines()
    g.close()
    
    f= open('C:\\Users\\mmadhusu\\Desktop\\Work summary\\global_routing_schematic2.txt','r')
    lines = f.readlines()
    f.close()
    ncount =1
    class MOS(object):
        def __init__(self, name="", x=0, y=0):
            self.name=name
            self.x=x
            self.y=y
    
    class NETs(object):
        def __init__(self, netname="", inst=[]):
            self.netname=netname
            self.inst=inst
    #    def __init__(self, netname="",x1=0,y1=0,x2=0,y2=0,node1="",node2=""):
    #        self.netname=netname
    #        self.x1=x1
    #        self.y1=y1
    #        self.x2=x2
    #        self.y2=y2
    
    I = [MOS() for count in range(ncount)]
    net = [NETs() for count in range(ncount)]
    i=0
    del(I[0])
    del(net[0])
    for line in lines1:
        I.append(MOS())
        line = line.replace("(", " ")
        line = line.replace('"',"")
        line = line.replace(")","")
        line = line.split(" ")
        I[i].x=str(math.floor((float(line[1])+2)*2.5))
        #print(MOSlist[i].x)
        I[i].y=str(math.floor((float(line[2])+2)*2.5))
        I[i].name = line[0]
        i=i+1
    
    i=0
    #for line in lines:
        #print (line)
       # print ("XXMXXX")
    #lines = f.split("\n")
    for line in lines:
        line = line.replace("(", " ")
        line = line.replace('"',"")
        line = line.replace(")","")
        line = line.replace("\n","")
        #print(line)
        #print("XXXX")
        #print(i)
        #line=line.replace("\n","")
        line = line.split(" ")
        net.append(NETs())
        net[i].netname = line[0]
        del line[0]
        net[i].inst=line
        #print(net[i].inst)
        #del line[0]
    #    for m in range(len(line)-1):
    #        #print (m)
    #        net[i].inst.append(line[m+1])
        i=i+1
    
    for x in range(len(net)):
        print(net[x].inst[:], net[x].netname)
    print("\n")
    for x in range(len(I)):
        print(I[x].name, I[x].x, I[x].y)
    
    for x in range(len(net)):
        #for l in range(len(net[x].inst)):
        #inst=[]
        #net[x].inst = np.unique(net[x].inst).tolist()
        #for inst in net[x].inst:
        #    if not inst.startswith("q"):
        i=0
        while(i<len(net[x].inst)):
            if not net[x].inst[i].startswith("q"):
                print (net[x].inst[i])
                del net[x].inst[i]
            else:
                i = i+1
       # net[x].inst.remove(net[x].inst[i] if not net[x].inst.startswith("q") else i++)
        #
    get_route_position.coordinates_source=[]
    get_route_position.coordinates_target=[]
    for x in range(len(net)):
        print(net[x].inst[:], net[x].netname)
    get_route_position.netname=[]
    for x in range(len(net)):
        if len(net[x].inst) > 1 and net[x].netname != 'gnd!' and net[x].netname != 'vdd!':
            for l in range(len(net[x].inst)-1):
                #print(len(net[x].inst)-1)
                if net[x].inst[l] != net[x].inst[l+1]:
                    for y in range(len(I)):
                        if I[y].name == net[x].inst[l]:
                            print(net[x].inst[l])
                            get_route_position.coordinates_source.append([I[y].x, I[y].y])
                    for m in range(len(I)):
                        if I[m].name == net[x].inst[l+1]:
                            print(net[x].inst[l+1])
                            get_route_position.coordinates_target.append([I[m].x, I[m].y])
                            get_route_position.netname.append(net[x].netname)
#        if len(net[x].inst)==2:
#            for y in range(len(I)):
#                if I[y].name == net[x].inst[0]:
#                    get_route_position.coordinates_source.append([I[y].x, I[y].y])
#            for m in range(len(I)):
#                if I[m].name == net[x].inst[1]:
#                    get_route_position.coordinates_target.append([I[m].x, I[m].y])
#    
    for l in range(len(get_route_position.coordinates_source)):
        print(get_route_position.coordinates_source[l])
    print("Hi")
    for j in range(len(get_route_position.coordinates_target)):
        print(get_route_position.coordinates_target[j])
    print(get_route_position.netname[:])
    return True


get_route_position()
