import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.myGraph = nx.Graph()
        self.diz_voli = {}
        self.diz_aereoporti = {}
        self.list_media_distanze = []


    def load_voli(self):
        for v in DAO.get_all_flights():
            self.diz_voli[v._id] = v
        self.list_voli = DAO.get_all_flights()
        self.list_media_distanze = DAO.get_medie_aereoporti()
    def load_aereoporti(self):
        for a in DAO.get_all_airport():
            self.diz_aereoporti[a._id] = a
        self.list_aereoporti = DAO.get_all_airport()

    def build_graph(self, distanza):
        self.myGraph.add_nodes_from(self.diz_aereoporti.values())
        for t in self.list_media_distanze:
            if t[0] > distanza:
                a_partenza = self.diz_aereoporti[t[1]]
                a_arrivo = self.diz_aereoporti[t[2]]
                print((a_partenza, a_arrivo))
                self.myGraph.add_edge(a_partenza, a_arrivo, weight = t[0])
        print(f"Nodi: {self.myGraph.number_of_nodes()}, archi: {self.myGraph.number_of_edges()}")


