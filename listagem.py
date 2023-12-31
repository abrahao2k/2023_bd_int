# Form implementation generated from reading ui file 'listagem.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database = "escola")
cursor = conexao.cursor()
print("Conectado ao BD.")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(284, 234)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.listar)
        self.verticalLayout.addWidget(self.pushButton)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Listagem de Dados"))
        self.pushButton.setText(_translate("MainWindow", "LISTAR"))

    def listar(self):
        comando = "SELECT * FROM aluno"
        cursor.execute(comando)
        dados = cursor.fetchall()  #converte para lista
        texto = ""
        for linha in dados:
            texto += "Codigo: " + str(linha[0]) + "\n"
            texto += "Nome: "   + linha[1] + "\n"
            texto += "Curso: "  + linha[2] + "\n"
            texto += "Turno: "  + linha[3] + "\n"
            texto += "Atleta: " + linha[4] + "\n"
            texto += "Bolsista: " + linha[5] + "\n"
            texto += "Obs.: " + linha[6] + "\n\n"
        self.plainTextEdit.setPlainText(texto)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
