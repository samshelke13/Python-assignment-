#!/usr/bin/env python
# coding: utf-8



port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
x1=list(port1.keys())
x2=list(port1.values())
port2={  x2[i]:x1[i]  for i in range(len(x1)) }
print(port2)

Output:{'FTP': 21, 'SSH': 22, 'telnet': 23, 'http': 80}


    
    

list1=[(1,2),(3,4),(5,6),(4,5)]
res=[ sum(i)  for i in list1 ]
print(res)


output :[3, 7, 11, 9]


    
    
    
lis=[(1,2,3),[1,2],['a','hit','less']]
res=[]
for i in lis: 
    if type(i)==type(lis): 
        res=res+i
    elif type(i)==tuple:
        res.extend(i)
    else: 
        res.append(i)

print(res)


output:[1, 2, 3, 1, 2, 'a', 'hit', 'less']




