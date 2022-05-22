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
