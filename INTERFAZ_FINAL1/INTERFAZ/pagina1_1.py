import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QLabel, QLineEdit, QVBoxLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Crear los grupos
        groupBox_gastos = QGroupBox("PROPUESTA DE GASTOS")
        groupBox_tarjeta = QGroupBox("LA TARJETA PERFECTA PARA TI")

        # Crear layouts verticales para cada grupo
        vbox_gastos = QVBoxLayout()
        vbox_tarjeta = QVBoxLayout()

        # Agregar elementos al grupo de gastos
        label_categoria = QLabel("Categoría:")
        self.line_edit_categoria = QLineEdit()
        label_monto = QLabel("Monto:")
        self.line_edit_monto = QLineEdit()
        button_agregar_gasto = QPushButton("Agregar Gasto")

        vbox_gastos.addWidget(label_categoria)
        vbox_gastos.addWidget(self.line_edit_categoria)
        vbox_gastos.addWidget(label_monto)
        vbox_gastos.addWidget(self.line_edit_monto)
        vbox_gastos.addWidget(button_agregar_gasto)

        # Agregar elementos al grupo de tarjeta (ejemplo simplificado)
        label_recomendacion = QLabel("Recomendación:")
        self.label_tarjeta_recomendada = QLabel("Aún no hay recomendaciones")
        vbox_tarjeta.addWidget(label_recomendacion)
        vbox_tarjeta.addWidget(self.label_tarjeta_recomendada)

        # Asignar los layouts a los grupos
        groupBox_gastos.setLayout(vbox_gastos)
        groupBox_tarjeta.setLayout(vbox_tarjeta)

        # Crear el layout principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(groupBox_gastos)
        main_layout.addWidget(groupBox_tarjeta)

        self.setLayout(main_layout)

        # Conectar la señal del botón "Agregar Gasto" a una función (a implementar)
        button_agregar_gasto.clicked.connect(self.agregar_gasto)

    def agregar_gasto(self):
        # Aquí se implementará la lógica para agregar un nuevo gasto
        # Por ejemplo, guardar los datos en una lista o base de datos
        categoria = self.line_edit_categoria.text()
        monto = self.line_edit_monto.text()
        print(f"Se agregó un gasto de {monto} en la categoría {categoria}")

        # Actualizar la recomendación (ejemplo simplificado)
        self.label_tarjeta_recomendada.setText("Tarjeta de crédito recomendada: Platinum")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())   