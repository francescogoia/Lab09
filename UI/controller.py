import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._model.load_voli()
        self._model.load_aereoporti()

    def handleAnalizza(self,e):
        try:
            distanza = int(self._view._txtIn.value)
            self._model.build_graph(distanza)
            grafo = self._model.myGraph
            self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {grafo.number_of_nodes()} nodi"
                                                           f"Il grafo ha {grafo.number_of_edges()} archi"))
            for r in grafo.edges.data():
                self._view._txt_result.controls.append(ft.Text(f"{r}"))
        except:
            self._view.create_alert(ft.Text("Errore durante l'esecuzione"))

        self._view.update_page()
