# Importar bibliotecas Agregar las que faltan
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtCore import Qt

# Subclase QMainWindow
class VentanaPrincipal(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Mi ventanita")

		edt_ejemplo = QLineEdit()
		edt_ejemplo.setMaxLength(10)
		# edt_ejemplo.setInputMask('000.000.000.000;_')
		edt_ejemplo.setPlaceholderText("Escribe algo")
		# edt_ejemplo.returnPressed.connect(self.return_pressed)
		# edt_ejemplo.selectionChanged.connect(self.selection_changed)
		edt_ejemplo.textChanged.connect(self.text_changed)
		# edt_ejemplo.textEdited.connect(self.text_edited)

		self.setCentralWidget(edt_ejemplo)

	def return_pressed(self):
		print("Presionado")
		self.centralWidget.setText("BOOM!")

	def selection_changed(self):
		print("Selecion cambiada")
		print(self.centralWidget().selectedText())

	def text_changed(self, s):
		print("Texto cambiado")
		print(s)

	def text_edited(self, s):
		print("Texto editado")
		print(s)

app = QApplication([])
window = VentanaPrincipal()
window.show()

app.exec_()