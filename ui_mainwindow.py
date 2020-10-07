# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(351, 605)
        MainWindow.setStyleSheet(u"")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionVer = QAction(MainWindow)
        self.actionVer.setObjectName(u"actionVer")
        self.actionDibujar = QAction(MainWindow)
        self.actionDibujar.setObjectName(u"actionDibujar")
        self.actionProfundidad = QAction(MainWindow)
        self.actionProfundidad.setObjectName(u"actionProfundidad")
        self.actionPrim = QAction(MainWindow)
        self.actionPrim.setObjectName(u"actionPrim")
        self.actionKrustal = QAction(MainWindow)
        self.actionKrustal.setObjectName(u"actionKrustal")
        self.actionDijkstra = QAction(MainWindow)
        self.actionDijkstra.setObjectName(u"actionDijkstra")
        self.actionAmplitud = QAction(MainWindow)
        self.actionAmplitud.setObjectName(u"actionAmplitud")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 351, 571))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.velocidad = QLineEdit(self.tab)
        self.velocidad.setObjectName(u"velocidad")

        self.gridLayout.addWidget(self.velocidad, 14, 0, 1, 1)

        self.mostrar = QPushButton(self.tab)
        self.mostrar.setObjectName(u"mostrar")

        self.gridLayout.addWidget(self.mostrar, 23, 0, 1, 1)

        self.color_r = QSpinBox(self.tab)
        self.color_r.setObjectName(u"color_r")
        self.color_r.setMaximum(250)

        self.gridLayout.addWidget(self.color_r, 20, 0, 1, 1)

        self.color_b = QSpinBox(self.tab)
        self.color_b.setObjectName(u"color_b")
        self.color_b.setMaximum(250)

        self.gridLayout.addWidget(self.color_b, 16, 0, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 11, 0, 1, 1)

        self.id = QLineEdit(self.tab)
        self.id.setObjectName(u"id")

        self.gridLayout.addWidget(self.id, 2, 0, 1, 1)

        self.destinoy = QLineEdit(self.tab)
        self.destinoy.setObjectName(u"destinoy")

        self.gridLayout.addWidget(self.destinoy, 12, 0, 1, 1)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 19, 0, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)

        self.color_g = QSpinBox(self.tab)
        self.color_g.setObjectName(u"color_g")
        self.color_g.setMaximum(250)

        self.gridLayout.addWidget(self.color_g, 18, 0, 1, 1)

        self.origenx = QLineEdit(self.tab)
        self.origenx.setObjectName(u"origenx")

        self.gridLayout.addWidget(self.origenx, 5, 0, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 15, 0, 1, 1)

        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 13, 0, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.destinox = QLineEdit(self.tab)
        self.destinox.setObjectName(u"destinox")

        self.gridLayout.addWidget(self.destinox, 10, 0, 1, 1)

        self.origeny = QLineEdit(self.tab)
        self.origeny.setObjectName(u"origeny")

        self.gridLayout.addWidget(self.origeny, 7, 0, 1, 1)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 21, 0, 1, 1)

        self.agregar = QPushButton(self.tab)
        self.agregar.setObjectName(u"agregar")
        self.agregar.setStyleSheet(u"")

        self.gridLayout.addWidget(self.agregar, 22, 0, 1, 1)

        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 17, 0, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout.addWidget(self.salida, 2, 1, 22, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 7pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout = QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.horizontalLayout.addWidget(self.buscar_lineEdit)

        self.buscar = QPushButton(self.tab_2)
        self.buscar.setObjectName(u"buscar")

        self.horizontalLayout.addWidget(self.buscar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.verticalLayout.addWidget(self.tabla)

        self.mostar_tabla = QPushButton(self.tab_2)
        self.mostar_tabla.setObjectName(u"mostar_tabla")

        self.verticalLayout.addWidget(self.mostar_tabla)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(9, 9, 321, 361))
        self.gridLayoutWidget = QWidget(self.tab_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 380, 311, 161))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.ordenarV = QPushButton(self.gridLayoutWidget)
        self.ordenarV.setObjectName(u"ordenarV")

        self.gridLayout_2.addWidget(self.ordenarV, 1, 0, 1, 1)

        self.dibujar = QPushButton(self.gridLayoutWidget)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_2.addWidget(self.dibujar, 0, 0, 1, 1)

        self.mas_cercano = QPushButton(self.gridLayoutWidget)
        self.mas_cercano.setObjectName(u"mas_cercano")

        self.gridLayout_2.addWidget(self.mas_cercano, 2, 1, 1, 1)

        self.origenX = QLineEdit(self.gridLayoutWidget)
        self.origenX.setObjectName(u"origenX")

        self.gridLayout_2.addWidget(self.origenX, 4, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 5, 0, 1, 1)

        self.destinoX = QLineEdit(self.gridLayoutWidget)
        self.destinoX.setObjectName(u"destinoX")

        self.gridLayout_2.addWidget(self.destinoX, 6, 0, 1, 1)

        self.ordenarD = QPushButton(self.gridLayoutWidget)
        self.ordenarD.setObjectName(u"ordenarD")

        self.gridLayout_2.addWidget(self.ordenarD, 1, 1, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 5, 1, 1, 1)

        self.limpiar = QPushButton(self.gridLayoutWidget)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_2.addWidget(self.limpiar, 0, 1, 1, 1)

        self.puntos = QPushButton(self.gridLayoutWidget)
        self.puntos.setObjectName(u"puntos")

        self.gridLayout_2.addWidget(self.puntos, 2, 0, 1, 1)

        self.origenY = QLineEdit(self.gridLayoutWidget)
        self.origenY.setObjectName(u"origenY")

        self.gridLayout_2.addWidget(self.origenY, 4, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 3, 1, 1, 1)

        self.destinoY = QLineEdit(self.gridLayoutWidget)
        self.destinoY.setObjectName(u"destinoY")

        self.gridLayout_2.addWidget(self.destinoY, 6, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 351, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuGrafos = QMenu(self.menubar)
        self.menuGrafos.setObjectName(u"menuGrafos")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuGrafos.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuGrafos.addAction(self.actionVer)
        self.menuAlgoritmos.addAction(self.actionProfundidad)
        self.menuAlgoritmos.addAction(self.actionAmplitud)
        self.menuAlgoritmos.addAction(self.actionPrim)
        self.menuAlgoritmos.addAction(self.actionKrustal)
        self.menuAlgoritmos.addAction(self.actionDijkstra)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionVer.setText(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.actionDibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.actionProfundidad.setText(QCoreApplication.translate("MainWindow", u"Recorrido Profundidad", None))
        self.actionPrim.setText(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.actionKrustal.setText(QCoreApplication.translate("MainWindow", u"Krustal", None))
        self.actionDijkstra.setText(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.actionAmplitud.setText(QCoreApplication.translate("MainWindow", u"Recorrido Amplitud", None))
        self.mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Color RGB</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Velocidad</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Origen</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Destino</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Captura de Particulas</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostar_tabla.setText(QCoreApplication.translate("MainWindow", u"Mostrar Tabla", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.ordenarV.setText(QCoreApplication.translate("MainWindow", u"Ordenar Velocidad", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.mas_cercano.setText(QCoreApplication.translate("MainWindow", u"Particulas m\u00e1s Cercana", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.ordenarD.setText(QCoreApplication.translate("MainWindow", u"Ordenar Distancia", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.puntos.setText(QCoreApplication.translate("MainWindow", u"Puntos", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Grafica", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuGrafos.setTitle(QCoreApplication.translate("MainWindow", u"Grafos", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
    # retranslateUi

