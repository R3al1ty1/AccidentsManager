# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogInsurance.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_InsuranceDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(815, 543)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-3, -5, 821, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photos/imgonline-com-ua-Blur-2l4fVmT8e17N.jpg"))
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 541))
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 541))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 541))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.selRow = QtWidgets.QWidget()
        self.selRow.setObjectName("selRow")
        self.selBack = QtWidgets.QLabel(self.selRow)
        self.selBack.setGeometry(QtCore.QRect(-3, -5, 811, 521))
        self.selBack.setText("")
        self.selBack.setPixmap(QtGui.QPixmap("photos/imgonline-com-ua-Blur-2l4fVmT8e17N.jpg"))
        self.selBack.setObjectName("selBack")
        self.selTableinsurance = QtWidgets.QTableView(self.selRow)
        self.selTableinsurance.setGeometry(QtCore.QRect(40, 90, 721, 381))
        self.selTableinsurance.setStyleSheet("color: grey; background-color: rgba(255,255,255,175)\n"
"")
        self.selTableinsurance.setObjectName("selTableinsurance")
        self.selUpperBack = QtWidgets.QLabel(self.selRow)
        self.selUpperBack.setGeometry(QtCore.QRect(0, 0, 811, 61))
        self.selUpperBack.setStyleSheet("background-color: rgba(255,255,255,75)")
        self.selUpperBack.setText("")
        self.selUpperBack.setObjectName("selUpperBack")
        self.searchText = QtWidgets.QLineEdit(self.selRow)
        self.searchText.setGeometry(QtCore.QRect(10, 10, 301, 41))
        self.searchText.setStyleSheet("color: grey; background-color: rgba(255,255,255,100)")
        self.searchText.setObjectName("searchText")
        self.searchButton = QtWidgets.QPushButton(self.selRow)
        self.searchButton.setGeometry(QtCore.QRect(320, 10, 131, 41))
        self.searchButton.setObjectName("searchButton")
        self.selReturn = QtWidgets.QPushButton(self.selRow)
        self.selReturn.setGeometry(QtCore.QRect(660, 10, 131, 41))
        self.selReturn.setObjectName("selReturn")
        self.tabWidget.addTab(self.selRow, "")
        self.addRow = QtWidgets.QWidget()
        self.addRow.setObjectName("addRow")
        self.addBack = QtWidgets.QLabel(self.addRow)
        self.addBack.setGeometry(QtCore.QRect(-3, -5, 811, 521))
        self.addBack.setText("")
        self.addBack.setPixmap(QtGui.QPixmap("photos/imgonline-com-ua-Blur-2l4fVmT8e17N.jpg"))
        self.addBack.setObjectName("addBack")
        self.addUpperBack = QtWidgets.QLabel(self.addRow)
        self.addUpperBack.setGeometry(QtCore.QRect(0, 0, 811, 61))
        self.addUpperBack.setStyleSheet("background-color: rgba(255,255,255,75)")
        self.addUpperBack.setText("")
        self.addUpperBack.setObjectName("addUpperBack")
        self.addReturn = QtWidgets.QPushButton(self.addRow)
        self.addReturn.setGeometry(QtCore.QRect(660, 10, 131, 41))
        self.addReturn.setObjectName("addReturn")
        self.middleBack = QtWidgets.QLabel(self.addRow)
        self.middleBack.setGeometry(QtCore.QRect(10, 80, 781, 421))
        self.middleBack.setStyleSheet("background-color: rgba(255,255,255,150)")
        self.middleBack.setText("")
        self.middleBack.setObjectName("middleBack")
        self.addInsuranceIdInput = QtWidgets.QLineEdit(self.addRow)
        self.addInsuranceIdInput.setGeometry(QtCore.QRect(60, 100, 251, 41))
        self.addInsuranceIdInput.setAutoFillBackground(False)
        self.addInsuranceIdInput.setStyleSheet("color: grey; background-color: rgba(255,255,255,100)")
        self.addInsuranceIdInput.setInputMask("")
        self.addInsuranceIdInput.setText("")
        self.addInsuranceIdInput.setObjectName("addInsuranceIdInput")
        self.addInsuranceNameInput = QtWidgets.QLineEdit(self.addRow)
        self.addInsuranceNameInput.setGeometry(QtCore.QRect(480, 100, 251, 41))
        self.addInsuranceNameInput.setStyleSheet("color: grey; background-color: rgba(255,255,255,100)")
        self.addInsuranceNameInput.setObjectName("addInsuranceNameInput")
        self.addAccidensNumberInput = QtWidgets.QLineEdit(self.addRow)
        self.addAccidensNumberInput.setGeometry(QtCore.QRect(60, 150, 251, 41))
        self.addAccidensNumberInput.setStyleSheet("color: grey; background-color: rgba(255,255,255,100)")
        self.addAccidensNumberInput.setObjectName("addAccidensNumberInput")
        self.addClientsNumberInput = QtWidgets.QLineEdit(self.addRow)
        self.addClientsNumberInput.setGeometry(QtCore.QRect(480, 150, 251, 41))
        self.addClientsNumberInput.setStyleSheet("color: grey; background-color: rgba(255,255,255,100)")
        self.addClientsNumberInput.setObjectName("addClientsNumberInput")
        self.addTableInsurance = QtWidgets.QTableView(self.addRow)
        self.addTableInsurance.setGeometry(QtCore.QRect(30, 250, 741, 241))
        self.addTableInsurance.setStyleSheet("color: grey; background-color: rgba(255,255,255,175)")
        self.addTableInsurance.setObjectName("addTableInsurance")
        self.addInsert = QtWidgets.QPushButton(self.addRow)
        self.addInsert.setGeometry(QtCore.QRect(480, 200, 251, 41))
        self.addInsert.setObjectName("addInsert")
        self.addRatingInput = QtWidgets.QLineEdit(self.addRow)
        self.addRatingInput.setGeometry(QtCore.QRect(60, 200, 251, 41))
        self.addRatingInput.setStyleSheet("color: grey; background-color: rgba(255,255,255,100)")
        self.addRatingInput.setObjectName("addRatingInput")
        self.tabWidget.addTab(self.addRow, "")
        self.updRow = QtWidgets.QWidget()
        self.updRow.setObjectName("updRow")
        self.updBack = QtWidgets.QLabel(self.updRow)
        self.updBack.setGeometry(QtCore.QRect(-3, -5, 811, 521))
        self.updBack.setText("")
        self.updBack.setPixmap(QtGui.QPixmap("photos/imgonline-com-ua-Blur-2l4fVmT8e17N.jpg"))
        self.updBack.setObjectName("updBack")
        self.updUpperBack = QtWidgets.QLabel(self.updRow)
        self.updUpperBack.setGeometry(QtCore.QRect(0, 0, 811, 61))
        self.updUpperBack.setStyleSheet("background-color: rgba(255,255,255,75)")
        self.updUpperBack.setText("")
        self.updUpperBack.setObjectName("updUpperBack")
        self.updReturn = QtWidgets.QPushButton(self.updRow)
        self.updReturn.setGeometry(QtCore.QRect(660, 10, 131, 41))
        self.updReturn.setObjectName("updReturn")
        self.updMiddleBack = QtWidgets.QLabel(self.updRow)
        self.updMiddleBack.setGeometry(QtCore.QRect(10, 80, 781, 421))
        self.updMiddleBack.setStyleSheet("background-color: rgba(255,255,255,150)")
        self.updMiddleBack.setText("")
        self.updMiddleBack.setObjectName("updMiddleBack")
        self.updChange = QtWidgets.QPushButton(self.updRow)
        self.updChange.setGeometry(QtCore.QRect(480, 200, 251, 41))
        self.updChange.setObjectName("updChange")
        self.updTableInsurance = QtWidgets.QTableView(self.updRow)
        self.updTableInsurance.setGeometry(QtCore.QRect(30, 250, 741, 241))
        self.updTableInsurance.setStyleSheet("color: grey; background-color: rgba(255,255,255,175)")
        self.updTableInsurance.setObjectName("updTableInsurance")
        self.updInsuranceIdInput = QtWidgets.QLineEdit(self.updRow)
        self.updInsuranceIdInput.setGeometry(QtCore.QRect(60, 100, 251, 41))
        self.updInsuranceIdInput.setAutoFillBackground(False)
        self.updInsuranceIdInput.setStyleSheet("color: grey; background-color: rgba(255,255,255,100)")
        self.updInsuranceIdInput.setInputMask("")
        self.updInsuranceIdInput.setText("")
        self.updInsuranceIdInput.setObjectName("updInsuranceIdInput")
        self.updInsuranceNameInput = QtWidgets.QLineEdit(self.updRow)
        self.updInsuranceNameInput.setGeometry(QtCore.QRect(480, 100, 251, 41))
        self.updInsuranceNameInput.setStyleSheet("color: grey; background-color: rgba(255,255,255,100)")
        self.updInsuranceNameInput.setObjectName("updInsuranceNameInput")
        self.updAccidensNumberInput = QtWidgets.QLineEdit(self.updRow)
        self.updAccidensNumberInput.setGeometry(QtCore.QRect(60, 150, 251, 41))
        self.updAccidensNumberInput.setStyleSheet("color: grey; background-color: rgba(255,255,255,100)")
        self.updAccidensNumberInput.setObjectName("updAccidensNumberInput")
        self.updRatingInput = QtWidgets.QLineEdit(self.updRow)
        self.updRatingInput.setGeometry(QtCore.QRect(60, 200, 251, 41))
        self.updRatingInput.setStyleSheet("color: grey; background-color: rgba(255,255,255,100)")
        self.updRatingInput.setObjectName("updRatingInput")
        self.updClientsNumberInput = QtWidgets.QLineEdit(self.updRow)
        self.updClientsNumberInput.setGeometry(QtCore.QRect(480, 150, 251, 41))
        self.updClientsNumberInput.setStyleSheet("color: grey; background-color: rgba(255,255,255,100)")
        self.updClientsNumberInput.setObjectName("updClientsNumberInput")
        self.tabWidget.addTab(self.updRow, "")
        self.delRow = QtWidgets.QWidget()
        self.delRow.setObjectName("delRow")
        self.delBack = QtWidgets.QLabel(self.delRow)
        self.delBack.setGeometry(QtCore.QRect(-3, -5, 811, 521))
        self.delBack.setText("")
        self.delBack.setPixmap(QtGui.QPixmap("photos/imgonline-com-ua-Blur-2l4fVmT8e17N.jpg"))
        self.delBack.setObjectName("delBack")
        self.delUpperBack = QtWidgets.QLabel(self.delRow)
        self.delUpperBack.setGeometry(QtCore.QRect(0, 0, 811, 61))
        self.delUpperBack.setStyleSheet("background-color: rgba(255,255,255,75)\n"
"")
        self.delUpperBack.setText("")
        self.delUpperBack.setObjectName("delUpperBack")
        self.delReturn = QtWidgets.QPushButton(self.delRow)
        self.delReturn.setGeometry(QtCore.QRect(660, 10, 131, 41))
        self.delReturn.setObjectName("delReturn")
        self.delNameText = QtWidgets.QLineEdit(self.delRow)
        self.delNameText.setGeometry(QtCore.QRect(10, 10, 301, 41))
        self.delNameText.setStyleSheet("color: grey; background-color: rgba(255,255,255,100)")
        self.delNameText.setObjectName("delNameText")
        self.deleteButton = QtWidgets.QPushButton(self.delRow)
        self.deleteButton.setGeometry(QtCore.QRect(320, 10, 131, 41))
        self.deleteButton.setObjectName("deleteButton")
        self.delTableInsurance = QtWidgets.QTableView(self.delRow)
        self.delTableInsurance.setGeometry(QtCore.QRect(40, 90, 721, 381))
        self.delTableInsurance.setStyleSheet("color: grey; background-color: rgba(255,255,255,175)")
        self.delTableInsurance.setObjectName("delTableInsurance")
        self.tabWidget.addTab(self.delRow, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.searchText.setPlaceholderText(_translate("Dialog", "                          Название"))
        self.delNameText.setPlaceholderText(_translate("Dialog", "                          Название"))
        self.searchButton.setText(_translate("Dialog", "Поиск"))
        self.selReturn.setText(_translate("Dialog", "Назад"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selRow), _translate("Dialog", "Просмотр"))
        self.addReturn.setText(_translate("Dialog", "Назад"))
        self.addInsuranceIdInput.setPlaceholderText(_translate("Dialog", "                                 ID"))
        self.addInsuranceNameInput.setPlaceholderText(_translate("Dialog", "                          Название"))
        self.addAccidensNumberInput.setPlaceholderText(_translate("Dialog", "                    Оформлено ДТП"))
        self.addClientsNumberInput.setPlaceholderText(_translate("Dialog", "                     Число клиентов"))
        self.addInsert.setText(_translate("Dialog", "Добавить"))
        self.addRatingInput.setPlaceholderText(_translate("Dialog", "                            Рейтинг"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addRow), _translate("Dialog", "Добавление"))
        self.updReturn.setText(_translate("Dialog", "Назад"))
        self.updChange.setText(_translate("Dialog", "Изменить"))
        self.updInsuranceIdInput.setPlaceholderText(_translate("Dialog", "                                 ID"))
        self.updInsuranceNameInput.setPlaceholderText(_translate("Dialog", "                          Название"))
        self.updAccidensNumberInput.setPlaceholderText(_translate("Dialog", "                    Оформлено ДТП"))
        self.updRatingInput.setPlaceholderText(_translate("Dialog", "                            Рейтинг"))
        self.updClientsNumberInput.setPlaceholderText(_translate("Dialog", "                     Число клиентов"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.updRow), _translate("Dialog", "Обновление"))
        self.delReturn.setText(_translate("Dialog", "Назад"))
        self.deleteButton.setText(_translate("Dialog", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.delRow), _translate("Dialog", "Удаление"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_InsuranceDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())