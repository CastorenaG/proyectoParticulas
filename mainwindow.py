from PySide2.QtWidgets import QMainWindow, QGraphicsScene
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from adminParticula import AdminParticulas
from particula import Particula
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtGui import QPen, QColor, QTransform
from pprint import pprint

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.adminParticula=AdminParticulas()

        self.scene = QGraphicsScene()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.ui.id_pushButton.clicked.connect(self.ordenar_por_id)
        self.ui.distancia_pushButton.clicked.connect(self.ordenar_por_distancia)
        self.ui.velocidad_pushButton.clicked.connect(self.ordenar_por_velocidad)

        self.ui.graphicsView.setScene(self.scene)
        self.ui.get_particulas_pushButton.clicked.connect(self.dibujar_particulas)
        self.ui.particulas_cercanas_pushButton.clicked.connect(self.dibujar_particulas_cercanas)

        self.ui.Djikstra_pushButton.clicked.connect(self.grafo_djikstra)
        self.ui.Prim_pushButton.clicked.connect(self.grafo_prim)
        self.ui.Kruskal_pushButton.clicked.connect(self.grafo_kruskal)

    @Slot ( )
    def click_agregar_inicio(self):
        print('Agregar inicio')
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origenx_spinBox.value()
        origen_y = self.ui.origenY_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.adminParticula.agregar_inicio(particula)



    @Slot ( )
    def click_agregar_final(self):
        print('Agregar final')
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origenx_spinBox.value()
        origen_y = self.ui.origenY_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.adminParticula.agregar_final(particula)

    @Slot ( )
    def click_mostrar(self):
        print('Mostrar')
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.adminParticula))

    @Slot ( )
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.', 
            'JSON (*.json)'
        )[0]
        if(self.adminParticula.abrir(ubicacion)):
            QMessageBox.information(
                self,
                "Exito",
            "Se puedo abrir el archivo" + ubicacion
            )
        else:
            QMessageBox.information(
                self,

                "Error",
                "No se pudo abrir el archivo" + ubicacion
            )

    @Slot ( )
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.adminParticula.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID","OrigenX","OrigenY","DestinoX","DestinoY","Velocidad","Red","Green","Blue","Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.adminParticula))
        row=0
        for particula in self.adminParticula:
            id_widget= QTableWidgetItem(str(particula.id))
            origenX_widget= QTableWidgetItem(str(particula.origen_x))
            origenY_widget= QTableWidgetItem(str(particula.origen_y))
            destinoX_widget= QTableWidgetItem(str(particula.destino_x))
            destinoY_widget= QTableWidgetItem(str(particula.destino_y))
            velocidad_widget= QTableWidgetItem(str(particula.velocidad))
            red_widget= QTableWidgetItem(str(particula.red))
            green_widget= QTableWidgetItem(str(particula.green))
            blue_widget= QTableWidgetItem(str(particula.blue))
            distancia_widget= QTableWidgetItem(str(particula.distancia))
            

            self.ui.tabla.setItem(row,0,id_widget)
            self.ui.tabla.setItem(row,1,origenX_widget)
            self.ui.tabla.setItem(row,2,origenY_widget)
            self.ui.tabla.setItem(row,3,destinoX_widget)
            self.ui.tabla.setItem(row,4,destinoY_widget)
            self.ui.tabla.setItem(row,5,velocidad_widget)
            self.ui.tabla.setItem(row,6,red_widget)
            self.ui.tabla.setItem(row,7,green_widget)
            self.ui.tabla.setItem(row,8,blue_widget)
            self.ui.tabla.setItem(row,9,distancia_widget)
            row += 1

    @Slot( )    
    def wheelEvent(self, event):
        print(event.delta())
        if event.delta()>0:
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8,0.8)

    @Slot()
    def buscar(self):
        id_buscar=self.ui.buscar_lineEdit.text()
        encontrado=False
        for particula in self.adminParticula:
            if id_buscar== str(particula.id):
                self.ui.tabla.clear()
                self.ui.tabla.setColumnCount(10)
                headers = ["ID","OrigenX","OrigenY","DestinoX","DestinoY","Velocidad","Red","Green","Blue","Distancia"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)
                self.ui.tabla.setRowCount(1)
                id_widget= QTableWidgetItem(str(particula.id))
                origenX_widget= QTableWidgetItem(str(particula.origen_x))
                origenY_widget= QTableWidgetItem(str(particula.origen_y))
                destinoX_widget= QTableWidgetItem(str(particula.destino_x))
                destinoY_widget= QTableWidgetItem(str(particula.destino_y))
                velocidad_widget= QTableWidgetItem(str(particula.velocidad))
                red_widget= QTableWidgetItem(str(particula.red))
                green_widget= QTableWidgetItem(str(particula.green))
                blue_widget= QTableWidgetItem(str(particula.blue))
                distancia_widget= QTableWidgetItem(str(particula.distancia))
                

                self.ui.tabla.setItem(0,0,id_widget)
                self.ui.tabla.setItem(0,1,origenX_widget)
                self.ui.tabla.setItem(0,2,origenY_widget)
                self.ui.tabla.setItem(0,3,destinoX_widget)
                self.ui.tabla.setItem(0,4,destinoY_widget)
                self.ui.tabla.setItem(0,5,velocidad_widget)
                self.ui.tabla.setItem(0,6,red_widget)
                self.ui.tabla.setItem(0,7,green_widget)
                self.ui.tabla.setItem(0,8,blue_widget)
                self.ui.tabla.setItem(0,9,distancia_widget)
                encontrado = True
        
                return
        if encontrado is False:
              QMessageBox.information(
                self,
                "Error",
                "No se encontro el id " + id_buscar
            )
              
    
    @Slot()
    def dibujar(self):
        for particula in self.adminParticula:
            pen=QPen()
            pen.setWidth(2)
            r=particula.red
            g=particula.green
            b=particula.blue
            origen_x=particula.origen_x
            origen_y=particula.origen_y
            destino_x=particula.destino_x
            destino_y=particula.destino_y
            color=QColor(r,g,b)
            pen.setColor(color)
            self.scene.addEllipse(origen_x,origen_y,6,6,pen)
            self.scene.addEllipse(destino_x,destino_y,6,6,pen)
            self.scene.addLine(origen_x+3,origen_y+3,destino_x+3,destino_y+3,pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot( )
    def ordenar_por_id(self):
        #print('ordenar por id')
        self.adminParticula.ordenar_id()
        
    @Slot( )
    def ordenar_por_velocidad(self):
        #print('ordenar por velocidad')
        self.adminParticula.ordenar_velocidad()

    @Slot( )
    def ordenar_por_distancia(self):
        #print('ordenar por distancia')
        self.adminParticula.ordenar_distancia()

    @Slot()
    def dibujar_particulas_cercanas(self):
        resultado=self.adminParticula.particulas_cercanas()
        pprint(resultado)
        for punto1 , punto2,r,g,b in resultado:
            pen=QPen()
            pen.setWidth(2)
            x1=punto1[0]
            y1=punto1[1]
            r=r
            g=g
            b=b
            x2=punto2[0]
            y2=punto2[1]
            
            
            color=QColor(r,g,b)
            pen.setColor(color)

            
            self.scene.addLine(x1+3,y1+3,x2+3,y2+3,pen)

    @Slot()
    def dibujar_particulas(self):
        self.particulas = self.adminParticula.get_particulas()
        pprint(self.particulas)
        for particula in self.adminParticula:
            pen=QPen()
            pen.setWidth(2)
            r=particula.red
            g=particula.green
            b=particula.blue
            origen_x=particula.origen_x
            origen_y=particula.origen_y
            destino_x=particula.destino_x
            destino_y=particula.destino_y
            color=QColor(r,g,b)
            pen.setColor(color)
            self.scene.addEllipse(origen_x,origen_y,6,6,pen)
            self.scene.addEllipse(destino_x,destino_y,6,6,pen)
