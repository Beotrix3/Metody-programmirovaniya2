dellst=[]
    for c,d in enumerate(rebrs):
        if (cpoint in rebrs[c]):
            dellst.append(c)
    dellst.reverse()
    for num in dellst:
        if rebrs[num][0]!=cpoint:
            nextp=rebrs[num][0]
        else:
    
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
