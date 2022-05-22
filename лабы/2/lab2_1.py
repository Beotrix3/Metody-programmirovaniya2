import os.path as osp
def load_graph(file,is_bin=False):
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
