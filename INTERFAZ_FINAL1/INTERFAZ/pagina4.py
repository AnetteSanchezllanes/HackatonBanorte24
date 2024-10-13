import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import webbrowser
from PyQt6.QtGui import QPixmap

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        # Crear el botón
        self.btn_face = QPushButton("Compartir a Facebookr", self)

        # Conectar la señal de clic del botón con la función abrir_facebook
        self.btn_face.clicked.connect(self.abrir_facebook)
        pixmap = QPixmap("ruta/a/tu/imagen.jpg")  # Reemplaza con la ruta de tu imagen

        # Crear un QLabel y asignarle la imagen
        label = label_imagen(self)
        label.setPixmap(pixmap)

        # Ajustar el tamaño del QLabel (opcional)
        label.resize(pixmap.width(), pixmap.height())
        # ... (resto del código para crear la interfaz)

    def abrir_facebook(self):
        url = 'https://www.facebook.com/'
        webbrowser.open(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
    