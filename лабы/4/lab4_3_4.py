import os.path as osp, numpy as np
def cruscall(file,is_bin=False):
    if is_bin:
        graph=open(file,'rb')
        fsize=osp.getsize(file)
        reblist=[]
        for e in range(int(fsize/12)):
            temp=[]
            for k in range(3):
                temp.append(int.from_bytes(graph.read(4),'little'))
            reblist.append(temp)
    else:
        graph=open(file,'r')
        reblist=[[int(k) for k in e.split()] for e in graph.readlines()]
    graph.close()
    return reblist
def save_graph(graph,file_name,is_bin=False):
    if is_bin:
        newf=open(file_name,'wb')
        for e in graph:
            newf.write(e[0].to_bytes(4, byteorder='little'))
            newf.write(e[1].to_bytes(4, byteorder='little'))
            newf.write(e[2].to_bytes(4, byteorder='little'))
    else:
        newf=open(file_name,'w')
        for e in graph:
            newf.write('∫▒〖{}={}~{}〗 \n'.format(e[0],e[1],e[2]))
    newf.close()
