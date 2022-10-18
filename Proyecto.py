# importamos bibliotecas
from  PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QLineEdit, QWidget, QGraphicsColorizeEffect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import sys
#subclase para QMainWindow
class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proyecto Python")
        #texto de arriba
        #texto_centro = QLabel("Aqui va el contenido de mi proyecto")
        #texto_centro.setAlignment(Qt.AlignBottom)
        self.Texto_arriba = QLabel("Este es el avance del proyecto", self)
        self.Texto_arriba.setGeometry(60, 50, 50, 60)
        self.Texto_arriba.setStyleSheet("border: 1px solid black;")
        self.Texto_arriba.setFont(QFont('Times', 20))
        self.Texto_arriba.setAlignment(Qt.AlignTop)
        efecto_color = QGraphicsColorizeEffect()
        efecto_color.setColor(Qt.darkGreen)
        self.Texto_arriba.setGraphicsEffect(efecto_color)

        layout = QVBoxLayout()

        layout.addWidget(self.Texto_arriba)
        layout.addWidget(QLineEdit())


        contenedor = QWidget()
        contenedor.setLayout(layout)

        self.setCentralWidget(contenedor)



app = QApplication([])

ventana = ventanaPrincipal()
ventana.resize(1024, 800)
ventana.setStyleSheet("background-color: cyan;")
ventana.show()

app.exec_()