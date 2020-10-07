from PySide2.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox, QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
from queue import PriorityQueue
import math
import json
import pprint
from PySide2.QtGui import QPen, QColor, QTransform

class MainWindow(QMainWindow):
    particulas = []
    grafo = dict()
    def __init__ (self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
            #Conexiones entre Python y Qt Designer
        self.ui.agregar.clicked.connect(self.agregar)
        self.ui.mostrar.clicked.connect(self.mostrar)

        self.ui.actionAbrir.triggered.connect(self.abrir)
        self.ui.actionGuardar.triggered.connect(self.guardar)

        self.ui.mostar_tabla.clicked.connect(self.click_mostrar_tabla)
        self.ui.buscar.clicked.connect(self.buscar)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.ordenarV.clicked.connect(self.click_ordenar_velocidad)
        self.ui.ordenarD.clicked.connect(self.click_ordenar_distancia)

        self.ui.puntos.clicked.connect(self.click_Puntos)
        self.ui.mas_cercano.clicked.connect(self.click_Mas_Cercanos)

        self.ui.actionVer.triggered.connect(self.grafoMostrar)

        self.ui.actionAmplitud.triggered.connect(self.recorrido_amplitud)
        self.ui.actionProfundidad.triggered.connect(self.recorrido_profunidad)

        self.ui.actionPrim.triggered.connect(self.PrimAlg)
        self.ui.actionKrustal.triggered.connect(self.KrusAlg)
        self.ui.actionDijkstra.triggered.connect(self.DijsAlg)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)
    @Slot()
    def DijsAlg(self):
        pen = QPen()
        pen.setWidth(5)
        grafo = dict()
        dicc = dict()
        camino = dict()
        pq = PriorityQueue()
        coorxy = (int(self.ui.origenX.text()), int(self.ui.origenY.text()))
        destino = (int(self.ui.destinoX.text()), int(self.ui.destinoY.text()))
        dicc[coorxy] = 0
        for a in self.particulas:
            nueva = math.sqrt(((a['destino']['x'] - a['origen']['x']) ** 2) + \
                              ((a['destino']['y'] - a['origen']['y']) ** 2))
            nodo = (a['origen']['x'],  a['origen']['y'])
            nodo2 = (a['destino']['x'], a['destino']['y'])
            arista_d = (nodo2, nueva)
            arista_o = (nodo, nueva)
            if nodo in grafo:
                grafo[nodo].append(arista_d)
            else:
                grafo[nodo] = [arista_d]
            if nodo2 in grafo:
                grafo[nodo2].append(arista_o)
            else:
                grafo[nodo2] = [arista_o]
            if nodo not in dicc:
                dicc[nodo] = 10000000000
            if nodo2 not in dicc:
                dicc[nodo2] = 10000000000
            if nodo not in camino:
                camino[nodo] = ''
            if nodo2 not in camino:
                camino[nodo2] = ''
        pq.put((0, coorxy))

        while not pq.empty():
            aux = pq.get()
            adyacente = grafo[aux[1]]
            for a in adyacente:
                if aux[0] + a[1] < dicc[a[0]]:
                    dicc[a[0]] = aux[0] + a[1]
                    camino[a[0]] = aux[1]
                    pq.put((a[1] + aux[0], a[0]))
        pen.setColor(QColor(228, 0, 124))
        while True:
            aux = camino[destino]
            print(camino)
            self.scene.addLine(destino[0], destino[1], aux[0], aux[1], pen)
            destino = aux
            if destino == coorxy:
                break
        self.ui.origenX.clear()
        self.ui.origenY.clear()
        self.ui.destinoX.clear()
        self.ui.destinoY.clear()

    @Slot()
    def KrusAlg(self):
        ListaOrdenada = PriorityQueue()
        Disjoint = []
        Resultado = []
        for a in self.particulas:
            ponderacion = a['velocidad'] * (-1)
            vertice_O = (a['origen']['x'], a['origen']['y'])
            vertice_D = (a['destino']['x'], a['destino']['y'])
            arista = [ponderacion, vertice_O, vertice_D]
            ListaOrdenada.put(arista)
            if [vertice_O] not in Disjoint:
                o = [vertice_O]
                Disjoint.append(o)
            if [vertice_D] not in Disjoint:
                d = [vertice_D]
                Disjoint.append(d)

        pos = pos2 = 0
        while not ListaOrdenada.empty():
            elem = ListaOrdenada.get()
            ori = elem[1]
            des = elem[2]
            cont = 0
            for i in Disjoint:
                if ori in i:
                    pos = cont
                if des in i:
                    pos2 = cont
                cont += 1

            if pos != pos2:
                Resultado.append(elem)
                for elem in Disjoint[pos2]:
                    Disjoint[pos].append(elem)
                Disjoint.pop(pos2)

        pen = QPen()
        pen.setWidth(5)
        pen.setColor(QColor(255, 0, 212))
        for i in Resultado:
            self.scene.addLine(i[1][0], i[1][1], i[2][0], i[2][1], pen)


    @Slot()
    def PrimAlg(self):
        grafo = dict()  # {}
        for a in self.particulas:
            nueva = math.sqrt(((a['destino']['x'] - a['origen']['x']) ** 2) + \
                              ((a['destino']['y'] - a['origen']['y']) ** 2))
            nodo = (a['origen']['x'], a['origen']['y'])
            nodo2 = (a['destino']['x'], a['destino']['y'])
            arista_d = (nodo2, nueva)
            arista_o = (nodo, nueva)
            if nodo in grafo:
                grafo[nodo].append(arista_d)
            else:
                grafo[nodo] = [arista_d]
            if nodo2 in grafo:
                grafo[nodo2].append(arista_o)
            else:
                grafo[nodo2] = [arista_o]
            solucion = []
            visitado = []
            pq = PriorityQueue()
            pen = QPen()
            pen.setWidth(5)
            coorx = int(self.ui.origenX.text())
            coory = int(self.ui.origenY.text())
            root = (coorx, coory)
            visitado.append(root)

            for x in grafo[root]:
                des = x[0]
                pon = x[1]
                ari = (pon, root, des)
                pq.put(ari)
            while not pq.empty():
                minimo = pq.get()
                d = minimo[2]
                if d not in visitado:
                    visitado.append(d)
                    solucion.append(minimo)
                    for i in grafo[d]:
                        vertice = i[0]
                        weight = i[1]
                        adyacente = (weight, d, vertice)
                        if vertice not in visitado:
                            pq.put(adyacente)

        for i in solucion:
            pen.setColor(QColor(255, 0, 212))
            self.scene.addLine(i[1][0], i[1][1], i[2][0], i[2][1], pen)
        self.ui.origenX.clear()
        self.ui.origenY.clear()



    @Slot()
    def recorrido_amplitud(self):
        self.ui.salida.clear()
        coorx = int(self.ui.origenX.text())
        coory = int(self.ui.origenY.text())
        origen = (coorx, coory)
        cola = []
        visitados = []
        cola.append(origen)
        while cola:
            actual = cola.pop(0)
            if actual not in visitados:
                visitados.append(actual)
            for adyacente, peso, in self.grafo[actual]:
                if adyacente not in visitados:
                    cola.append(adyacente)
        s = pprint.pformat(visitados, width=40)
        self.ui.salida.insertPlainText("Amplitud: ")
        self.ui.salida.insertPlainText(s)
                    
    @Slot()
    def recorrido_profunidad(self):
        self.ui.salida.clear()
        coorx = int(self.ui.origenX.text())
        coory = int(self.ui.origenY.text())
        origen = (coorx, coory)
        pila = []
        visitados = []
        pila.append(origen)
        visitados.append(origen)
        while pila:
            actual = pila.pop()
            for adyacente, peso, in self.grafo[actual]:
                if adyacente not in visitados:
                    pila.append(adyacente)
                    visitados.append(adyacente)
        s = pprint.pformat(visitados, width=40)
        self.ui.salida.insertPlainText("Profunidad: ")
        self.ui.salida.insertPlainText(s)

    @Slot()
    def grafoMostrar(self):
        self.ui.salida.clear()
        for a in self.particulas:
            dist = math.sqrt(((a['destino']['x'] - a['origen']['x']) ** 2) + \
                                  ((a['destino']['y'] - a['origen']['y']) ** 2))
            dist = int(dist)
            nodo = (a['origen']['x'], a['origen']['y'])
            nodo2 = (a['destino']['x'], a['destino']['y'])
            arista_d = (nodo2, dist)
            arista_o = (nodo, dist)
            if nodo in self.grafo:
                self.grafo[nodo].append(arista_d)
            else:
                self.grafo[nodo] = [arista_d]
            if nodo2 in self.grafo:
                self.grafo[nodo2].append(arista_o)
            else:
                self.grafo[nodo2] = [arista_o]
        s = pprint.pformat(self.grafo, width=40)
        self.ui.salida.insertPlainText(s)

    @Slot()
    def click_Puntos(self):
        pen = QPen()
        pen.setWidth(2)
        for particulas in self.particulas:
            r = particulas['color']['red']
            g = particulas['color']['green']
            b = particulas['color']['blue']

            color = QColor(r, g, b)
            pen.setColor(color)

            x_origen = particulas['origen']['x']
            y_origen = particulas['origen']['y']
            x_destino = particulas['destino']['x']
            y_destino = particulas['destino']['y']

            self.scene.addEllipse(x_origen, y_origen, 3, 3, pen)
            self.scene.addEllipse(x_destino, y_destino, 3, 3, pen)

    @Slot()
    def click_Mas_Cercanos(self):
        point=[]
        for particulas in self.particulas:
            P={
                'x':particulas['origen']['x'],
                'y':particulas['origen']['y'],
                'r':particulas['color']['red'],
                'g':particulas['color']['green'],
                'b':particulas['color']['blue']
            }
            point.append(P)
            P={
                'x':particulas['destino']['x'],
                'y':particulas['destino']['y'],
                'r':particulas['color']['red'],
                'g':particulas['color']['green'],
                'b':particulas['color']['blue']
            }
            point.append(P)
        pen = QPen()
        pen.setWidth(2)
        for i in point:
            min = 1000
            for j in point:
                aux = math.sqrt(((j['x'] - i['x']) ** 2) + ((j['y'] - i['y']) ** 2))
                if aux != 0 and aux < min:
                    min = aux
                    savex = j['x']
                    savey = j['y']

            r = i['r']
            g = i['g']
            b = i['b']
            color = QColor(r, g, b)
            pen.setColor(color)
            self.scene.addLine(i['x'] + 1.5, i['y'] + 1.5, savex + 1.5, savey + 1.5, pen)

    @Slot()
    def click_ordenar_velocidad(self):
        self.particulas.sort(key = lambda particulas: int(particulas['velocidad']))
        pen = QPen()
        pen.setWidth(2)
        aux = 0
        for particulas in self.particulas:
            dist = math.sqrt(((particulas['destino']['x'] - particulas['origen']['x']) ** 2) + \
                             ((particulas['destino']['y'] - particulas['origen']['y']) ** 2))
            r = particulas['color']['red']
            g = particulas['color']['green']
            b = particulas['color']['blue']

            color = QColor(r, g, b)
            pen.setColor(color)

            x_origen = 0
            y_origen = aux
            x_destino = dist
            y_destino = aux

            self.scene.addEllipse(x_origen, y_origen, 3, 3, pen)
            self.scene.addEllipse(x_destino, y_destino, 3, 3, pen)
            self.scene.addLine(x_origen + 1.5, y_origen + 1.5, x_destino + 1.5, y_destino + 1.5, pen)
            aux += 6

    @Slot()
    def click_ordenar_distancia(self):
        self.particulas.sort(key=lambda particulas: math.sqrt(((particulas['destino']['x'] - particulas['origen']['x']) ** 2) + \
                                  ((particulas['destino']['y'] - particulas['origen']['y']) ** 2)),reverse=True)
        pen = QPen()
        pen.setWidth(2)
        aux=0
        for particulas in self.particulas:
            dist = math.sqrt(((particulas['destino']['x'] - particulas['origen']['x']) ** 2) + \
                             ((particulas['destino']['y'] - particulas['origen']['y']) ** 2))
            r = particulas['color']['red']
            g = particulas['color']['green']
            b = particulas['color']['blue']

            color = QColor(r, g, b)
            pen.setColor(color)

            x_origen = 0
            y_origen = aux
            x_destino = dist
            y_destino = aux

            self.scene.addEllipse(x_origen, y_origen, 3, 3, pen)
            self.scene.addEllipse(x_destino, y_destino, 3, 3, pen)
            self.scene.addLine(x_origen + 1.5, y_origen + 1.5, x_destino + 1.5, y_destino + 1.5, pen)
            aux+=6

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)
        for particulas in self.particulas:

            r = particulas['color']['red']
            g = particulas['color']['green']
            b = particulas['color']['blue']

            color =QColor(r, g, b)
            pen.setColor(color)

            x_origen = particulas['origen']['x']
            y_origen = particulas['origen']['y']
            x_destino = particulas['destino']['x']
            y_destino = particulas['destino']['y']

            self.scene.addEllipse(x_origen, y_origen, 3, 3, pen)
            self.scene.addEllipse(x_destino, y_destino, 3, 3, pen)
            self.scene.addLine(x_origen + 1.5, y_origen + 1.5, x_destino + 1.5, y_destino + 1.5, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()
        self.ui.graphicsView.setTransform(QTransform())

    @Slot()
    def buscar(self):
        particulas = []
        id = int(self.ui.buscar_lineEdit.text())
        for particula in self.particulas:
            if id == particula['id']:
                particulas.append(particula)
        if len(particulas) == 0:
            QMessageBox.information(self, "Particulas", "No Hubo Coincidencias")
        else:
            self.particulas_tabla(particulas)

    @Slot()
    def click_mostrar_tabla(self):
        self.particulas_tabla(self.particulas)

    def particulas_tabla(self, particulas):

        self.ui.tabla.clear()
        self.ui.tabla.setColumnCount(6)
        self.ui.tabla.setRowCount(len(particulas))

        labels = ['id','origen', 'destino', 'velocidad', 'color', 'distancia']
        self.ui.tabla.setHorizontalHeaderLabels(labels)

        row = 0
        for particulas in particulas:
            dist = math.sqrt(((particulas['destino']['x'] - particulas['origen']['x']) ** 2) + \
                                  ((particulas['destino']['y'] - particulas['origen']['y']) ** 2))
            id = QTableWidgetItem(str(particulas['id']))
            origen = QTableWidgetItem(str(particulas['origen']))
            destino = QTableWidgetItem(str(particulas['destino']))
            velocidad = QTableWidgetItem(str(particulas['velocidad']))
            color = QTableWidgetItem(str(particulas['color']))
            distancia = QTableWidgetItem(str(dist))

            self.ui.tabla.setItem(row, 0, id)
            self.ui.tabla.setItem(row, 1, origen)
            self.ui.tabla.setItem(row, 2, destino)
            self.ui.tabla.setItem(row, 3, velocidad)
            self.ui.tabla.setItem(row, 4, color)
            self.ui.tabla.setItem(row, 5, distancia)
            row += 1

    @Slot()
    def agregar(self):
        id = self.ui.id.text()
        origenx = int(self.ui.origenx.text())
        origeny = int(self.ui.origeny.text())
        destinox = int(self.ui.destinox.text())
        destinoy = int(self.ui.destinoy.text())
        velocidad = int(self.ui.velocidad.text())

        color_r = self.ui.color_r.value()
        color_g = self.ui.color_g.value()
        color_b = self.ui.color_b.value()

        particula ={
            'id' : id,
            'origen':{'x':origenx, 'y':origeny},
            'destino':{'x':destinox, 'y':destinoy},
            'velocidad ':velocidad,
            'color':{'red':color_r, 'green':color_g, 'blue':color_b}

        }
        self.particulas.append(particula)

        self.ui.id.clear()
        self.ui.origenx.clear()
        self.ui.origeny.clear()
        self.ui.destinox.clear()
        self.ui.destinoy.clear()
        self.ui.velocidad.clear()
        self.ui.color_r.setValue(0)
        self.ui.color_g.setValue(0)
        self.ui.color_b.setValue(0)

    @Slot()
    def mostrar(self):
        self.ui.salida.clear()
        for particula in self.particulas:
            distancia = math.sqrt(((particula['destino']['x'] - particula['origen']['x']) ** 2) + \
                                  ((particula['destino']['y'] - particula['origen']['y']) ** 2))
            distancia = str(distancia)

            for key, value in particula.items():
                if type(value) is int:
                    value = str(value)
                if type(value) is dict:
                    value = str(value)
                self.ui.salida.insertPlainText(key+":"+value+'\n')
            self.ui.salida.insertPlainText("distancia: " + distancia + '\n' + '\n')

    @Slot()
    def abrir(self):
        ubicacion = QFileDialog.getOpenFileName(self, "Abrir Archivo", ".", "JSON (*.json)")
        with open(ubicacion[0], 'r') as archivo:
            self.particulas = json.load(archivo)

    @Slot()
    def guardar(self):
        ubicacion = QFileDialog.getSaveFileName(self, "Guardar Particulas", ".", "JSON (*.json")

        with open(ubicacion[0], 'w') as archivo:
            json.dump(self.particulas, archivo, indent=5)



