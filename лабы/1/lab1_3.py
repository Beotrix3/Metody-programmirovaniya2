from sys import argv
import graphlib as gr
if len(argv)>1:
    if argv[1]!='/?':
        filename=argv[1]
    else:
        print('Поиск в графе кратчайшего пути между заданными вершинами.\nlaba1.py [имя_файла_графа] (тип_файла /b-бинарный файл или /n -небинарный) (номер_начальной_вершины) (номер_конечной_вершины)')
        exit()
    if len(argv)>4:
        if argv[2]=='/b':
            is_bin=True
        else:
            is_bin=False
        start=int(argv[3])
        fin=int(argv[4])
    else:
        is_bin=False
        start=0
        fin=3
else:
    is_bin=False
    start=0
    fin=3
    filename='input.txt'
def graph_short_path_find(cpoint,tpoint,rebrs,length=0,dellst=[],lens=[],path=''):
    if length==0:
        lens=[]
    path+=str(cpoint)+'-'
    if cpoint==tpoint:
        lens.append(length)
        #print('Найден путь ',path[:-1],':',length)
        return None
    for num in dellst:
        rebrs.pop(num)
    dellst=[]
    for c,d in enumerate(rebrs):
        if (cpoint in rebrs[c]):
            dellst.append(c)
    dellst.reverse()
    for num in dellst:
        if rebrs[num][0]!=cpoint:
            nextp=rebrs[num][0]
        else:
            nextp=rebrs[num][1]
        graph_short_path_find(nextp,tpoint,rebrs[:],length+rebrs[num][2],dellst,lens,path)
    if not lens:
        otv='{} {} -1'.format(cpoint,tpoint)
    else:
        otv=min(lens)
    lens=''
    return otv
graph=gr.load_graph(filename,is_bin)
length=graph_short_path_find(start,fin,graph)
print(length)

class TestShortPath(unittest.TestCase):
    def test_1(self):
        self.assertEqual(graph_short_path_find(0,3,graph), 20)
    def test_2(self):
        self.assertEqual(graph_short_path_find(2,3,graph), 11)
    def test_3(self):
        self.assertEqual(graph_short_path_find(3,0,graph), 20)
    def test_4(self):
        self.assertEqual(graph_short_path_find(3,2,graph), 11)
    def test_5(self):
        self.assertEqual(graph_short_path_find(2,4,graph), '2 4 -1')
    def test_6(self):
        self.assertEqual(graph_short_path_find(4,2,graph), '4 2 -1')
    def test_7(self):
        self.assertEqual(graph_short_path_find(5,6,graph), '5 6 -1')
    def test_8(self):
        self.assertEqual(graph_short_path_find(6,5,graph), '6 5 -1')
    def test_9(self):
        self.assertEqual(graph_short_path_find(1,3,graph), 15)
    def test_10(self):
        self.assertEqual(graph_short_path_find(3,1,graph), 15)
if __name__ == "__main__":
    graph=gr.load_graph(filename,is_bin)
    unittest.main()

