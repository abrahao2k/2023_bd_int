# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 136)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_soma = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_soma.setObjectName("pushButton_soma")
        self.pushButton_soma.clicked.connect(self.soma)
        self.horizontalLayout.addWidget(self.pushButton_soma)
        self.pushButton_subtracao = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_subtracao.setObjectName("pushButton_subtracao")
        self.pushButton_subtracao.clicked.connect(self.subtracao)
        self.horizontalLayout.addWidget(self.pushButton_subtracao)
        self.pushButton_multiplicacao = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_multiplicacao.setObjectName("pushButton_multiplicacao")
        self.pushButton_multiplicacao.clicked.connect(self.multiplicacao)
        self.horizontalLayout.addWidget(self.pushButton_multiplicacao)
        self.pushButton_divisao = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_divisao.setObjectName("pushButton_divisao")
        self.pushButton_divisao.clicked.connect(self.divisao)
        self.horizontalLayout.addWidget(self.pushButton_divisao)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.lineEdit_valor1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_valor1.setObjectName("lineEdit_valor1")
        self.gridLayout.addWidget(self.lineEdit_valor1, 0, 1, 1, 1)
        self.label_valor1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_valor1.setObjectName("label_valor1")
        self.gridLayout.addWidget(self.label_valor1, 0, 0, 1, 1)
        self.lineEdit_valor2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_valor2.setObjectName("lineEdit_valor2")
        self.gridLayout.addWidget(self.lineEdit_valor2, 1, 1, 1, 1)
        self.label_valor2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_valor2.setObjectName("label_valor2")
        self.gridLayout.addWidget(self.label_valor2, 1, 0, 1, 1)
        self.label_total = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_total.setObjectName("label_total")
        self.gridLayout.addWidget(self.label_total, 3, 0, 1, 1)
        self.lineEdit_total = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_total.setObjectName("lineEdit_total")
        self.gridLayout.addWidget(self.lineEdit_total, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora"))
        self.pushButton_soma.setText(_translate("MainWindow", "+"))
        self.pushButton_subtracao.setText(_translate("MainWindow", "-"))
        self.pushButton_multiplicacao.setText(_translate("MainWindow", "*"))
        self.pushButton_divisao.setText(_translate("MainWindow", "/"))
        self.label_valor1.setText(_translate("MainWindow", "Valor 1:"))
        self.label_valor2.setText(_translate("MainWindow", "Valor 2:"))
        self.label_total.setText(_translate("MainWindow", "Total:"))
    
    def soma(self):
        valor1 = float(self.lineEdit_valor1.text())
        valor2 = float(self.lineEdit_valor2.text())
        total  = valor1 + valor2
        self.lineEdit_total.setText(str(total))
        
    def subtracao(self):
        valor1 = float(self.lineEdit_valor1.text())
        valor2 = float(self.lineEdit_valor2.text())
        total  = valor1 - valor2
        self.lineEdit_total.setText(str(total))
    
    def multiplicacao(self):
        valor1 = float(self.lineEdit_valor1.text())
        valor2 = float(self.lineEdit_valor2.text())
        total  = valor1 * valor2
        self.lineEdit_total.setText(str(total))
    
    def divisao(self):
        valor1 = float(self.lineEdit_valor1.text())
        valor2 = float(self.lineEdit_valor2.text())
        total  = valor1 / valor2
        self.lineEdit_total.setText(str(total))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())