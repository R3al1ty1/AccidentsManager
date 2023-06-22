import sys
from datetime import datetime
from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import *
import psycopg2
from adminui import Ui_AdminMainWindow
from userui import Ui_UserMainWindow
from dialogOfficer import Ui_OfficerDialog
from accidentFinalUi import Ui_AccidentDialog
from dialogInsurance import Ui_InsuranceDialog
from dialogParticipant import Ui_ParticipantDialog
from dialogVehicle import Ui_VehicleDialog
from dialogUserAccident import Ui_UserAccidentDialog
from dialogUserInsurance import Ui_UserInsuranceDialog
from dialogUserVehicle import Ui_UserVehicleDialog
import consts
from CRUDs import accidentsCRUD, officerCRUD, insuranceCRUD, participantCRUD, vehicleCRUD

conn = psycopg2.connect(
    host="localhost",
    database="Accidents",
    user=consts.user,
    port=consts.port,
    password=consts.password
)

USER_PWD = {
    'admin': 'admin',
    'user': 'user'
}

class SigninPage(QDialog):
    def __init__(self):
        super(SigninPage, self).__init__()
        self.signInUserLabel = QLabel('Login')
        self.signInPwdLabel = QLabel('Password')
        self.signInPwd2Label = QLabel('Password')
        self.signInUserLine = QLineEdit()
        self.signInPwdLine = QLineEdit()
        self.signInPwd2Line = QLineEdit()
        self.signInButton = QPushButton('Sign in')

        self.user_h_layout = QHBoxLayout()
        self.pwd_h_layout = QHBoxLayout()
        self.pwd2_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.lineedit_init()
        self.pushbutton_init()
        self.layout_init()

    def layout_init(self):
        self.user_h_layout.addWidget(self.signInUserLabel)
        self.user_h_layout.addWidget(self.signInUserLine)
        self.pwd_h_layout.addWidget(self.signInPwdLabel)
        self.pwd_h_layout.addWidget(self.signInPwdLine)
        self.pwd2_h_layout.addWidget(self.signInPwd2Label)
        self.pwd2_h_layout.addWidget(self.signInPwd2Line)

        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.pwd2_h_layout)
        self.all_v_layout.addWidget(self.signInButton)

        self.setLayout(self.all_v_layout)

    def lineedit_init(self):
        self.signInPwdLine.setEchoMode(QLineEdit.EchoMode.Password)
        self.signInPwd2Line.setEchoMode(QLineEdit.EchoMode.Password)

        self.signInUserLine.textChanged.connect(self.check_input_func)
        self.signInPwdLine.textChanged.connect(self.check_input_func)
        self.signInPwd2Line.textChanged.connect(self.check_input_func)

    def pushbutton_init(self):
        self.signInButton.setEnabled(False)
        self.signInButton.clicked.connect(self.check_signin_func)

    def check_input_func(self):
        if self.signInUserLine.text() and \
                self.signInPwdLine.text() and \
                self.signInPwd2Line.text():
            self.signInButton.setEnabled(True)
        else:
            self.signInButton.setEnabled(False)

    def check_signin_func(self):
        if self.signInPwdLine.text() != self.signInPwd2Line.text():
            QMessageBox.critical(self, 'Wrong', 'Two Passwords Typed Are Not Same!')

        self.signInUserLine.clear()
        self.signInPwdLine.clear()
        self.signInPwd2Line.clear()

class WindowAdmin(QMainWindow):
    def __init__(self):
        super(WindowAdmin, self).__init__()
        self.ui = Ui_AdminMainWindow()
        self.ui.setupUi(self)
        self.returnButtonClicked()
        self.dialogButtonClicked()
        self.setBestOfficer()
        self.shortInfo()

    def returnButtonClicked(self):
        self.ui.buttonQuit.clicked.connect(self.openLoginDialog)
    def dialogButtonClicked(self):
        self.ui.buttonOfficer.clicked.connect(self.openOfficerDialog)
        self.ui.buttonTransport.clicked.connect(self.openTransportDialog)
        self.ui.buttonParticipants.clicked.connect(self.openParticipantDialog)
        self.ui.buttonInsurance.clicked.connect(self.openInsuranceDialog)
        self.ui.buttonAccdient.clicked.connect(self.openAccidentDialog)
    def openLoginDialog(self):
        self.Login = Login()
        self.Login.show()
        self.close()
    def openOfficerDialog(self):
        self.OfficerDialog = Officer()
        self.OfficerDialog.show()
        self.close()

    def openParticipantDialog(self):
        self.ParticipantDialog = Participant()
        self.ParticipantDialog.show()
        self.close()

    def openInsuranceDialog(self):
        self.InsuranceDialog = Insurance()
        self.InsuranceDialog.show()
        self.close()

    def setBestOfficer(self):
        cur = conn.cursor()
        cur.execute("SELECT officer_id, COUNT(*) AS count FROM accident GROUP BY officer_id ORDER BY count DESC LIMIT 1;")
        answer = cur.fetchall()
        cur.execute("SELECT officer.full_name, officer.photo_path FROM officer WHERE officer_id = (%s) GROUP BY officer.full_name, officer.photo_path", (answer[0][0],))
        res = cur.fetchall()
        self.ui.officerName.setText(res[0][0])
        self.ui.photoOfficer.setPixmap(QtGui.QPixmap(res[0][1]))
        cur.close()

    def shortInfo(self):
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM accident;")
        res = cur.fetchall()
        cur.execute("SELECT city, COUNT(*) AS count FROM accident GROUP BY city ORDER BY count DESC LIMIT 1;")
        answer = cur.fetchall()
        self.ui.accCityInput.setText(answer[0][0])
        self.ui.accAmountInput.setText(str(res[0][0]))
        now = datetime.now()
        current_time = now.time()
        current_time = str(current_time)
        current_time = current_time.split('.')
        self.ui.dateInput.setText(current_time[0])

    def openTransportDialog(self):
        self.TransportDialog = Vehicle()
        self.TransportDialog.show()
        self.close()

    def openAccidentDialog(self):
        self.AccidentDialog = Accident()
        self.AccidentDialog.show()
        self.close()

class WindowUser(QMainWindow):
    def __init__(self):
        super(WindowUser, self).__init__()
        self.ui = Ui_UserMainWindow()
        self.ui.setupUi(self)
        self.returnButtonClicked()
        self.dialogButtonClicked()
        self.shortInfo()

    def returnButtonClicked(self):
        self.ui.buttonQuit.clicked.connect(self.openLoginDialog)

    def openLoginDialog(self):
        self.Login = Login()
        self.Login.show()
        self.close()

    def shortInfo(self):
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM accident;")
        res = cur.fetchall()
        cur.execute("SELECT city, COUNT(*) AS count FROM accident GROUP BY city ORDER BY count DESC LIMIT 1;")
        answer = cur.fetchall()
        self.ui.accCityInput.setText(answer[0][0])
        self.ui.accAmountInput.setText(str(res[0][0]))
        now = datetime.now()
        current_time = now.time()
        current_time = str(current_time)
        current_time = current_time.split('.')
        self.ui.dateInput.setText(current_time[0])

    def dialogButtonClicked(self):
        self.ui.buttonAutoDamage.clicked.connect(self.openUserTransportDialog)
        self.ui.buttonInsurance.clicked.connect(self.openUserInsuranceDialog)
        self.ui.buttonAccident.clicked.connect(self.openUserAccidentDialog)

    def openUserInsuranceDialog(self):
        self.UserInsuranceDialog = UserInsurance()
        self.UserInsuranceDialog.show()
        self.close()

    def openUserTransportDialog(self):
        self.UserTransportDialog = UserVehicle()
        self.UserTransportDialog.show()
        self.close()

    def openUserAccidentDialog(self):
        self.UserAccidentDialog = UserAccident()
        self.UserAccidentDialog.show()
        self.close()

class Officer(QWidget):
    def __init__(self):
        super(Officer, self).__init__()
        self.ui = Ui_OfficerDialog()
        self.ui.setupUi(self)
        self.returnButtonClicked()
        self.inputData()

    def returnButtonClicked(self):
        self.ui.selReturn.clicked.connect(self.openAdminWindow)
        self.ui.updReturn.clicked.connect(self.openAdminWindow)
        self.ui.delReturn.clicked.connect(self.openAdminWindow)
        self.ui.addReturn.clicked.connect(self.openAdminWindow)
        self.ui.searchButton.clicked.connect(self.showDistinct)
        self.ui.deleteButton.clicked.connect(self.deleteDistinct)
        self.ui.updChange.clicked.connect(self.updateDistinct)
        self.ui.addInsert.clicked.connect(self.createDistinct)
        self.ui.searchAccButton.clicked.connect(self.goToAccidents)

    def openAdminWindow(self):
        self.WindowAdmin = WindowAdmin()
        self.WindowAdmin.show()
        self.close()
    def inputData(self):
        rows = officerCRUD.select_all(conn)
        selTableView = self.ui.selTableOfficer
        addTableView = self.ui.addTableOfficer
        updTableView = self.ui.updTableOfficer
        delTableView = self.ui.delTableOfficer

        model = QStandardItemModel()
        model.setColumnCount(4)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "ФИО")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Фото")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Дата рождения")

        for row in rows:
            lst = []
            for elem in row:
                lst.append(elem)
            lst[0] = str(lst[0])
            date = lst[3]
            date = str(date)
            lst.pop()
            lst.append(date)
            model.appendRow([QStandardItem(data) for data in lst])
            selTableView.setModel(model)
            addTableView.setModel(model)
            updTableView.setModel(model)
            delTableView.setModel(model)
    def goToAccidents(self):
        self.AccidentDialog = Accident()
        self.AccidentDialog.show()
        full_name = self.ui.searchText.text()
        Accident.testFunc(self.AccidentDialog, full_name)
        self.close()

    def showDistinct(self):
        inp = self.ui.searchText.text()
        ans = officerCRUD.select(inp, conn)
        self.ui.searchAccButton.clicked.connect(self.goToAccidents)
        selTableView = self.ui.selTableOfficer
        model = QStandardItemModel()
        model.setColumnCount(4)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "ФИО")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Фото")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Дата рождения")

        for row in ans:
            lst = []
            for elem in row:
                lst.append(elem)
            lst[0] = str(lst[0])
            date = lst[3]
            date = str(date)
            lst.pop()
            lst.append(date)
            model.appendRow([QStandardItem(data) for data in lst])
            selTableView.setModel(model)

    def deleteDistinct(self):
        toDelete = self.ui.delNameText.text()
        print(toDelete)
        officerCRUD.delete(toDelete, conn)
        self.inputData()

    def updateDistinct(self):
        changeId = self.ui.updOfficerIdInput.text()
        changePath = self.ui.updPhotoPathInput.text()
        changeName = self.ui.updFullNameInput.text()
        changeBDay = self.ui.updBdayInput.text()
        officerCRUD.update(changeId, changeName, changePath, changeBDay, conn)
        self.inputData()

    def createDistinct(self):
        createId = self.ui.addOfficerIdInput.text()
        createPath = self.ui.addPhotoPathInput.text()
        createName = self.ui.addFullNameInput.text()
        createBDay = self.ui.addBdayInput.text()
        officerCRUD.insert(createId, createName, createPath, createBDay, conn)
        self.inputData()

class UserAccident(QWidget):
    def __init__(self):
        super(UserAccident, self).__init__()
        self.ui = Ui_UserAccidentDialog()
        self.ui.setupUi(self)
        self.returnButtonClicked()
        self.inputData()

    def returnButtonClicked(self):
        self.ui.returnButton.clicked.connect(self.openUserWindow)
        self.ui.searchButton.clicked.connect(self.showDistinct)

    def openUserWindow(self):
        self.UserWindow = WindowUser()
        self.UserWindow.show()
        self.close()

    def inputData(self):
        rows = accidentsCRUD.select_all(conn)
        TableView = self.ui.tableView

        model = QStandardItemModel()
        model.setColumnCount(5)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Условия")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Дата")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Место")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Город")

        for row in rows:
            lst = []
            for elem in row:
                lst.append(elem)
            date = lst[2]
            date = str(date)
            lst[0] = str(lst[0])
            lst[2] = date
            lst[4] = lst[5]
            lst.pop()
            print(lst)
            model.appendRow([QStandardItem(data) for data in lst])
            TableView.setModel(model)

    def showDistinct(self):
        accDate = self.ui.searchDate.text()
        place = date = self.ui.searchPlace.text()
        ans = accidentsCRUD.select(accDate, place, conn)
        TableView = self.ui.tableView
        model = QStandardItemModel()
        model.setColumnCount(6)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Условия")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Дата")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Место")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "ID сотрудника")
        model.setHeaderData(5, Qt.Orientation.Horizontal, "Город")

        for row in ans:
            lst = []
            for elem in row:
                lst.append(elem)
            date = lst[2]
            date = str(date)
            lst[0] = str(lst[0])
            lst[2] = date
            lst[4] = str(lst[4])
            model.appendRow([QStandardItem(data) for data in lst])
            TableView.setModel(model)

class Accident(QWidget):
    def __init__(self):
        super(Accident, self).__init__()
        self.ui = Ui_AccidentDialog()
        self.ui.setupUi(self)
        self.returnButtonClicked()
        self.inputData()

    def returnButtonClicked(self):
        self.ui.selReturn.clicked.connect(self.openAdminWindow)
        self.ui.updReturn.clicked.connect(self.openAdminWindow)
        self.ui.delReturn.clicked.connect(self.openAdminWindow)
        self.ui.addReturn.clicked.connect(self.openAdminWindow)
        self.ui.searchButton.clicked.connect(self.showDistinct)
        self.ui.deleteButton.clicked.connect(self.deleteDistinct)
        self.ui.updChange.clicked.connect(self.updateDistinct)
        self.ui.addInsert.clicked.connect(self.createDistinct)
        self.ui.addInsert_2.clicked.connect(self.goToParticipant)

    def openAdminWindow(self):
        self.WindowAdmin = WindowAdmin()
        self.WindowAdmin.show()
        self.close()
    def goToParticipant(self):
        self.ParticipantDialog = Participant()
        self.ParticipantDialog.show()
        self.close()

    def testFunc(self, full_name):
        cur = conn.cursor()
        cur.execute("SELECT * FROM accident WHERE officer_id = (SELECT officer_id FROM officer WHERE full_name = (%s))", (full_name,))
        ans = cur.fetchall()
        selTableView = self.ui.selTableAccident
        addTableView = self.ui.addTableAccident
        updTableView = self.ui.updTableAccident
        delTableView = self.ui.delTableAccident

        model = QStandardItemModel()
        model.setColumnCount(5)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Условия")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Дата")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Место")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Город")

        for row in ans:
            lst = []
            for elem in row:
                lst.append(elem)
            date = lst[2]
            date = str(date)
            lst[0] = str(lst[0])
            lst[2] = date
            lst[4] = lst[5]
            lst.pop()
            model.appendRow([QStandardItem(data) for data in lst])
            selTableView.setModel(model)
            addTableView.setModel(model)
            updTableView.setModel(model)
            delTableView.setModel(model)

    def inputData(self):
        rows = accidentsCRUD.select_all(conn)
        selTableView = self.ui.selTableAccident
        addTableView = self.ui.addTableAccident
        updTableView = self.ui.updTableAccident
        delTableView = self.ui.delTableAccident

        model = QStandardItemModel()
        model.setColumnCount(5)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Условия")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Дата")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Место")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Город")

        for row in rows:
            lst = []
            for elem in row:
                lst.append(elem)
            date = lst[2]
            date = str(date)
            lst[0] = str(lst[0])
            lst[2] = date
            lst[4] = lst[5]
            lst.pop()
            model.appendRow([QStandardItem(data) for data in lst])
            selTableView.setModel(model)
            addTableView.setModel(model)
            updTableView.setModel(model)
            delTableView.setModel(model)

    def showDistinct(self):
        accDate = self.ui.searchDate.text()
        place = date = self.ui.searchPlace.text()
        if place == '':
            cur = conn.cursor()
            cur.execute("SELECT * FROM accident WHERE accident_date = (%s)", (accDate,))
            ans = cur.fetchall()
            print(ans)
        elif accDate == '':
            cur = conn.cursor()
            cur.execute("SELECT * FROM accident WHERE place = (%s)", (place,))
            ans = cur.fetchall()
            print(ans)
        else:
            ans = accidentsCRUD.select(accDate, place, conn)
        selTableView = self.ui.selTableAccident
        model = QStandardItemModel()
        model.setColumnCount(6)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Условия")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Дата")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Место")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "ID сотрудника")
        model.setHeaderData(5, Qt.Orientation.Horizontal, "Город")

        for row in ans:
            lst = []
            for elem in row:
                lst.append(elem)
            date = lst[2]
            date = str(date)
            lst[0] = str(lst[0])
            lst[2] = date
            lst[4] = str(lst[4])
            model.appendRow([QStandardItem(data) for data in lst])
            selTableView.setModel(model)

    def deleteDistinct(self):
        toDelete = self.ui.delNameText.text()
        accidentsCRUD.delete(toDelete, conn)
        self.inputData()

    def updateDistinct(self):
        changeId = self.ui.updAccidentIdInput.text()
        changeDate = self.ui.updAccidentDateInput.text()
        changeOfficerId = self.ui.updOfficerIdInput.text()
        changeConditions = self.ui.updConditionsInput.text()
        changePlace = self.ui.updPlaceInput.text()
        changeCity = self.ui.updCityInput.text()
        accidentsCRUD.update(changeId,changeConditions, changeDate, changePlace, changeOfficerId, changeCity, conn)
        self.inputData()

    def createDistinct(self):
        createId = self.ui.addAccidentIdInput.text()
        createDate = self.ui.addAccidentDateInput.text()
        createOfficerId = self.ui.addOfficerIdInput.text()
        createConditions = self.ui.addConditionsInput.text()
        createPlace = self.ui.addPlaceInput.text()
        createCity = self.ui.addCityInput.text()
        accidentsCRUD.insert(createId, createConditions, createDate, createPlace, createOfficerId, createCity, conn)
        self.inputData()

class UserInsurance(QWidget):
    def __init__(self):
        super(UserInsurance, self).__init__()
        self.ui = Ui_UserInsuranceDialog()
        self.ui.setupUi(self)
        self.returnButtonClicked()
        self.inputData()

    def returnButtonClicked(self):
        self.ui.returnButton.clicked.connect(self.openUserWindow)
        self.ui.searchButton.clicked.connect(self.showDistinct)

    def openUserWindow(self):
        self.UserWindow = WindowUser()
        self.UserWindow.show()
        self.close()

    def inputData(self):
        rows = insuranceCRUD.select_all(conn)
        TableView = self.ui.tableView

        model = QStandardItemModel()
        model.setColumnCount(5)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Название")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Число оформлений")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Число клиентов")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Рейтинг")

        for row in rows:
            lst = []
            for elem in row:
                lst.append(elem)
            lst[0] = str(lst[0])
            lst[2] = str(lst[2])
            lst[3] = str(lst[3])
            temp = str(lst[4])
            lst.pop()
            lst.append(temp)
            model.appendRow([QStandardItem(data) for data in lst])
            TableView.setModel(model)

    def showDistinct(self):
        inp = self.ui.searchText.text()
        ans = insuranceCRUD.select(inp, conn)
        TableView = self.ui.tableView
        model = QStandardItemModel()
        model.setColumnCount(5)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Название")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Число оформлений")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Число клиентов")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Рейтинг")

        for row in ans:
            lst = []
            for elem in row:
                lst.append(elem)
            lst[0] = str(lst[0])
            lst[2] = str(lst[2])
            lst[3] = str(lst[3])
            temp = str(lst[4])
            lst.pop()
            lst.append(temp)
            model.appendRow([QStandardItem(data) for data in lst])
            TableView.setModel(model)

class Insurance(QWidget):
    def __init__(self):
        super(Insurance, self).__init__()
        self.ui = Ui_InsuranceDialog()
        self.ui.setupUi(self)
        self.returnButtonClicked()
        self.inputData()

    def returnButtonClicked(self):
        self.ui.selReturn.clicked.connect(self.openAdminWindow)
        self.ui.updReturn.clicked.connect(self.openAdminWindow)
        self.ui.delReturn.clicked.connect(self.openAdminWindow)
        self.ui.addReturn.clicked.connect(self.openAdminWindow)
        self.ui.searchButton.clicked.connect(self.showDistinct)
        self.ui.deleteButton.clicked.connect(self.deleteDistinct)
        self.ui.updChange.clicked.connect(self.updateDistinct)
        self.ui.addInsert.clicked.connect(self.createDistinct)

    def openAdminWindow(self):
        self.WindowAdmin = WindowAdmin()
        self.WindowAdmin.show()
        self.close()

    def inputData(self):
        rows = insuranceCRUD.select_all(conn)
        selTableView = self.ui.selTableinsurance
        addTableView = self.ui.addTableInsurance
        updTableView = self.ui.updTableInsurance
        delTableView = self.ui.delTableInsurance

        model = QStandardItemModel()
        model.setColumnCount(5)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Название")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Число оформлений")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Число клиентов")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Рейтинг")

        for row in rows:
            lst = []
            for elem in row:
                lst.append(elem)
            lst[0] = str(lst[0])
            lst[2] = str(lst[2])
            lst[3] = str(lst[3])
            temp = str(lst[4])
            lst.pop()
            lst.append(temp)
            model.appendRow([QStandardItem(data) for data in lst])
            selTableView.setModel(model)
            addTableView.setModel(model)
            updTableView.setModel(model)
            delTableView.setModel(model)

    def showDistinct(self):
        inp = self.ui.searchText.text()
        ans = insuranceCRUD.select(inp, conn)
        selTableView = self.ui.selTableinsurance
        model = QStandardItemModel()
        model.setColumnCount(5)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Название")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Число оформлений")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Число клиентов")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Рейтинг")

        for row in ans:
            lst = []
            for elem in row:
                lst.append(elem)
            lst[0] = str(lst[0])
            lst[2] = str(lst[2])
            lst[3] = str(lst[3])
            temp = str(lst[4])
            lst.pop()
            lst.append(temp)
            model.appendRow([QStandardItem(data) for data in lst])
            selTableView.setModel(model)

    def deleteDistinct(self):
        toDelete = self.ui.delNameText.text()
        insuranceCRUD.delete(toDelete, conn)
        self.inputData()

    def updateDistinct(self):
        changeId = self.ui.updInsuranceIdInput.text()
        changeName = self.ui.updInsuranceNameInput.text()
        changeAccidentsNumber = self.ui.updAccidensNumberInput.text()
        changeRating = self.ui.updRatingInput.text()
        changeClientsNumber = self.ui.updClientsNumberInput.text()
        insuranceCRUD.update(changeId, changeName, changeAccidentsNumber, changeClientsNumber, changeRating, conn)
        self.inputData()

    def createDistinct(self):
        createId = self.ui.addInsuranceIdInput.text()
        createName = self.ui.addInsuranceNameInput.text()
        createAccidentsNumber = self.ui.addAccidensNumberInput.text()
        createRating = self.ui.addRatingInput.text()
        createClientsNumber = self.ui.addClientsNumberInput.text()
        insuranceCRUD.insert(createId, createName, createAccidentsNumber, createClientsNumber, createRating, conn)
        self.inputData()
class Participant(QWidget):
    def __init__(self):
        super(Participant, self).__init__()
        self.ui = Ui_ParticipantDialog()
        self.ui.setupUi(self)
        self.returnButtonClicked()
        self.inputData()

    def returnButtonClicked(self):
        self.ui.selReturn.clicked.connect(self.openAdminWindow)
        self.ui.updReturn.clicked.connect(self.openAdminWindow)
        self.ui.delReturn.clicked.connect(self.openAdminWindow)
        self.ui.addReturn.clicked.connect(self.openAdminWindow)
        self.ui.searchButton.clicked.connect(self.showDistinct)
        self.ui.deleteButton.clicked.connect(self.deleteDistinct)
        self.ui.updChange.clicked.connect(self.updateDistinct)
        self.ui.addInsert.clicked.connect(self.createDistinct)

    def openAdminWindow(self):
        self.WindowAdmin = WindowAdmin()
        self.WindowAdmin.show()
        self.close()

    def inputData(self):
        rows = participantCRUD.select_all(conn)
        selTableView = self.ui.selTableParticipant
        addTableView = self.ui.addTableParticipant
        updTableView = self.ui.updTableParticipant
        delTableView = self.ui.delTableParticipant

        model = QStandardItemModel()
        model.setColumnCount(8)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Телефон")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Дата рождения")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "ФИО")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Номер ВУ")
        model.setHeaderData(5, Qt.Orientation.Horizontal, "Номер страховки")
        model.setHeaderData(6, Qt.Orientation.Horizontal, "Пол")
        model.setHeaderData(7, Qt.Orientation.Horizontal, "Мед. обследование")

        for row in rows:
            lst = []
            for elem in row:
                lst.append(elem)
            date = lst[2]
            date = str(date)
            lst[0] = str(lst[0])
            lst[2] = date
            lst[7] = str(lst[7])
            model.appendRow([QStandardItem(data) for data in lst])
            selTableView.setModel(model)
            addTableView.setModel(model)
            updTableView.setModel(model)
            delTableView.setModel(model)

    def showDistinct(self):
        inp = self.ui.searchText.text()
        ans = participantCRUD.select(inp, conn)
        selTableView = self.ui.selTableParticipant
        model = QStandardItemModel()
        model.setColumnCount(8)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Телефон")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Дата рождения")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "ФИО")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Номер ВУ")
        model.setHeaderData(5, Qt.Orientation.Horizontal, "Номер страховки")
        model.setHeaderData(6, Qt.Orientation.Horizontal, "Пол")
        model.setHeaderData(7, Qt.Orientation.Horizontal, "Мед. обследование")

        for row in ans:
            lst = []
            for elem in row:
                lst.append(elem)
            date = lst[2]
            date = str(date)
            lst[0] = str(lst[0])
            lst[2] = date
            lst[7] = str(lst[7])
            model.appendRow([QStandardItem(data) for data in lst])
            selTableView.setModel(model)

    def updateDistinct(self):
        changeId = self.ui.updParticipantIdInput.text()
        changePhone = self.ui.updPhoneInput.text()
        changeDLNumber = self.ui.updDLNumberPathInput.text()
        changeInsuranceNumber = self.ui.updInsuranceNumberInput.text()
        changeFullName= self.ui.updFullNameInput.text()
        changeBDay = self.ui.updBdayInput.text()
        changeSex = self.ui.updSexInput.text()
        changeTreatmentNeed = self.ui.updTreatmentNeededInput.text()
        participantCRUD.update(changeId, changePhone, changeBDay, changeFullName, changeDLNumber, changeInsuranceNumber, changeSex,changeTreatmentNeed, conn)
        self.inputData()
    def deleteDistinct(self):
        toDelete = self.ui.delNameText.text()
        participantCRUD.delete(toDelete, conn)
        self.inputData()


    def createDistinct(self):
        createId = self.ui.addParticipantIdInput.text()
        createPhone = self.ui.addPhoneInput.text()
        createDLNumber = self.ui.addDLNumberPathInput.text()
        createInsuranceNumber = self.ui.addInsuranceNumberInput.text()
        createFullName = self.ui.addFullNameInput.text()
        createBDay = self.ui.addBdayInput.text()
        createSex = self.ui.addSexInput.text()
        createTreatmentNeed = self.ui.addTreatmentNeededInput.text()
        participantCRUD.insert(createId, createPhone, createBDay, createFullName, createDLNumber, createInsuranceNumber, createSex, createTreatmentNeed, conn)
        self.inputData()

class UserVehicle(QWidget):
    def __init__(self):
        super(UserVehicle, self).__init__()
        self.ui = Ui_UserVehicleDialog()
        self.ui.setupUi(self)
        self.returnButtonClicked()
        self.inputData()

    def returnButtonClicked(self):
        self.ui.returnButton.clicked.connect(self.openUserWindow)
        self.ui.searchButton.clicked.connect(self.showDistinct)

    def openUserWindow(self):
        self.UserWindow = WindowUser()
        self.UserWindow.show()
        self.close()

    def inputData(self):
        rows = vehicleCRUD.select_all(conn)
        TableView = self.ui.tableView

        model = QStandardItemModel()
        model.setColumnCount(13)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Моторизованное?")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Наименование")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Цвет")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Марка")
        model.setHeaderData(5, Qt.Orientation.Horizontal, "Модель")
        model.setHeaderData(6, Qt.Orientation.Horizontal, "Год")
        model.setHeaderData(7, Qt.Orientation.Horizontal, "VIN")
        model.setHeaderData(8, Qt.Orientation.Horizontal, "ПТС")
        model.setHeaderData(9, Qt.Orientation.Horizontal, "СТС")
        model.setHeaderData(10, Qt.Orientation.Horizontal, "Кол-во ДТП")
        model.setHeaderData(11, Qt.Orientation.Horizontal, "ID страховой")
        model.setHeaderData(12, Qt.Orientation.Horizontal, "Цена ремонта")


        for row in rows:
            lst = []
            for elem in row:
                lst.append(elem)
            date = lst[6]
            date = str(date)
            lst[0] = str(lst[0])
            lst[1] = str(lst[1])
            lst[6] = date
            lst[7] = str(lst[7])
            lst[10] = str(lst[10])
            lst[11] = str(lst[11])
            lst[12] = str(lst[12])
            model.appendRow([QStandardItem(data) for data in lst])
            TableView.setModel(model)

    def showDistinct(self):
        inp = self.ui.searchText.text()
        ans = vehicleCRUD.select(inp, conn)
        TableView = self.ui.tableView
        model = QStandardItemModel()
        model.setColumnCount(13)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Моторизованное?")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Наименование")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Цвет")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Марка")
        model.setHeaderData(5, Qt.Orientation.Horizontal, "Модель")
        model.setHeaderData(6, Qt.Orientation.Horizontal, "Год")
        model.setHeaderData(7, Qt.Orientation.Horizontal, "VIN")
        model.setHeaderData(8, Qt.Orientation.Horizontal, "ПТС")
        model.setHeaderData(9, Qt.Orientation.Horizontal, "СТС")
        model.setHeaderData(10, Qt.Orientation.Horizontal, "Кол-во ДТП")
        model.setHeaderData(11, Qt.Orientation.Horizontal, "ID страховой")
        model.setHeaderData(12, Qt.Orientation.Horizontal, "Цена ремонта")

        for row in ans:
            lst = []
            for elem in row:
                lst.append(elem)
            date = lst[6]
            date = str(date)
            lst[0] = str(lst[0])
            lst[1] = str(lst[1])
            lst[6] = date
            lst[7] = str(lst[7])
            lst[10] = str(lst[10])
            lst[11] = str(lst[11])
            lst[12] = str(lst[12])
            model.appendRow([QStandardItem(data) for data in lst])
            TableView.setModel(model)

class Vehicle(QWidget):
    def __init__(self):
        super(Vehicle, self).__init__()
        self.ui = Ui_VehicleDialog()
        self.ui.setupUi(self)
        self.returnButtonClicked()
        self.inputData()

    def returnButtonClicked(self):
        self.ui.selReturn.clicked.connect(self.openAdminWindow)
        self.ui.updReturn.clicked.connect(self.openAdminWindow)
        self.ui.delReturn.clicked.connect(self.openAdminWindow)
        self.ui.addReturn.clicked.connect(self.openAdminWindow)
        self.ui.searchButton.clicked.connect(self.showDistinct)
        self.ui.deleteButton.clicked.connect(self.deleteDistinct)
        self.ui.updChange.clicked.connect(self.updateDistinct)
        self.ui.addInsert.clicked.connect(self.createDistinct)

    def openAdminWindow(self):
        self.WindowAdmin = WindowAdmin()
        self.WindowAdmin.show()
        self.close()

    def inputData(self):
        rows = vehicleCRUD.select_all(conn)
        selTableView = self.ui.selTableVehicle
        addTableView = self.ui.addTableVehicle
        updTableView = self.ui.updTableVehicle
        delTableView = self.ui.delTableVehicle

        model = QStandardItemModel()
        model.setColumnCount(13)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Моторизованное?")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Наименование")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Цвет")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Марка")
        model.setHeaderData(5, Qt.Orientation.Horizontal, "Модель")
        model.setHeaderData(6, Qt.Orientation.Horizontal, "Год")
        model.setHeaderData(7, Qt.Orientation.Horizontal, "VIN")
        model.setHeaderData(8, Qt.Orientation.Horizontal, "ПТС")
        model.setHeaderData(9, Qt.Orientation.Horizontal, "СТС")
        model.setHeaderData(10, Qt.Orientation.Horizontal, "Кол-во ДТП")
        model.setHeaderData(11, Qt.Orientation.Horizontal, "ID страховой")
        model.setHeaderData(12, Qt.Orientation.Horizontal, "Цена ремонта")


        for row in rows:
            lst = []
            for elem in row:
                lst.append(elem)
            date = lst[6]
            date = str(date)
            lst[0] = str(lst[0])
            lst[1] = str(lst[1])
            lst[6] = date
            lst[7] = str(lst[7])
            lst[10] = str(lst[10])
            lst[11] = str(lst[11])
            lst[12] = str(lst[12])
            model.appendRow([QStandardItem(data) for data in lst])
            selTableView.setModel(model)
            addTableView.setModel(model)
            updTableView.setModel(model)
            delTableView.setModel(model)

    def showDistinct(self):
        inp = self.ui.searchVIN.text()
        ans = vehicleCRUD.select(inp, conn)
        selTableView = self.ui.selTableVehicle
        model = QStandardItemModel()
        model.setColumnCount(13)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "Id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Моторизованное?")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Наименование")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Цвет")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Марка")
        model.setHeaderData(5, Qt.Orientation.Horizontal, "Модель")
        model.setHeaderData(6, Qt.Orientation.Horizontal, "Год")
        model.setHeaderData(7, Qt.Orientation.Horizontal, "VIN")
        model.setHeaderData(8, Qt.Orientation.Horizontal, "ПТС")
        model.setHeaderData(9, Qt.Orientation.Horizontal, "СТС")
        model.setHeaderData(10, Qt.Orientation.Horizontal, "Кол-во ДТП")
        model.setHeaderData(11, Qt.Orientation.Horizontal, "ID страховой")
        model.setHeaderData(12, Qt.Orientation.Horizontal, "Цена ремонта")

        for row in ans:
            lst = []
            for elem in row:
                lst.append(elem)
            date = lst[6]
            date = str(date)
            lst[0] = str(lst[0])
            lst[1] = str(lst[1])
            lst[6] = date
            lst[7] = str(lst[7])
            lst[10] = str(lst[10])
            lst[11] = str(lst[11])
            lst[12] = str(lst[12])
            model.appendRow([QStandardItem(data) for data in lst])
            selTableView.setModel(model)

    def deleteDistinct(self):
        toDelete = self.ui.delVINText.text()
        vehicleCRUD.delete(toDelete, conn)
        self.inputData()

    def updateDistinct(self):
        changeId = self.ui.updVehicleIdInput.text()
        changeName = self.ui.updVehicleNameInput.text()
        changeColor = self.ui.updColorInput.text()
        changeMotored = self.ui.updMotoredInput.text()
        changeBrand = self.ui.updBrandInput.text()
        changeModel = self.ui.updModelInput.text()
        changeYearProd = self.ui.updYearProdInput.text()
        changeDamageCost = self.ui.updDamageCostInput.text()
        changeVIN = self.ui.updVINInput.text()
        changePassport = self.ui.updPassportInput.text()
        changeRegistration = self.ui.updRegistrationInput.text()
        changeAccidentNumber = self.ui.updAccidentNumberInput.text()
        changeInsuranceID = self.ui.updInsuranceIDInput.text()
        vehicleCRUD.update(changeId, changeMotored, changeName, changeColor, changeBrand, changeModel, changeYearProd, changeVIN, changePassport, changeRegistration, changeAccidentNumber, changeInsuranceID, changeDamageCost, conn)
        self.inputData()

    def createDistinct(self):
        createId = self.ui.addVehicleIdInput.text()
        createName = self.ui.addVehicleNameInput.text()
        createColor = self.ui.addColorInput.text()
        createMotored = self.ui.addMotoredInput.text()
        createBrand = self.ui.addBrandInput.text()
        createModel = self.ui.addModelInput.text()
        createYearProd = self.ui.addYearProdInput.text()
        createDamageCost = self.ui.addDamageCostInput.text()
        createVIN = self.ui.addVINInput.text()
        createPassport = self.ui.addPassportInput.text()
        createRegistration = self.ui.addRegistrationInput.text()
        createAccidentNumber = self.ui.addAccidentNumberInput.text()
        createInsuranceID = self.ui.addInsuranceIDInput.text()
        vehicleCRUD.insert(createId, createMotored, createName, createColor, createBrand, createModel, createYearProd, createVIN, createPassport, createRegistration, createAccidentNumber, createInsuranceID,createDamageCost, conn)
        self.inputData()
class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.resize(300, 100)

        self.user_label = QLabel('Login:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.user_line.setClearButtonEnabled(True)
        self.pwd_line = QLineEdit(self)
        self.pwd_line.setClearButtonEnabled(True)
        self.login_button = QPushButton('Войти', self)

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.lineedit_init()
        self.pushbutton_init()
        self.layout_init()
        self.signin_page = SigninPage()

    def layout_init(self):
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.h_layout.addWidget(self.login_button)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def lineedit_init(self):
        self.user_line.setPlaceholderText('login..')
        self.pwd_line.setPlaceholderText('password..')
        self.pwd_line.setEchoMode(QLineEdit.EchoMode.Password)

        self.user_line.textChanged.connect(self.check_input_func)
        self.pwd_line.textChanged.connect(self.check_input_func)

    def pushbutton_init(self):
        self.login_button.setEnabled(False)
        self.login_button.clicked.connect(self.check_login_func)

    def check_login_func(self):
        password = USER_PWD.get(self.user_line.text())
        if password != self.pwd_line.text():
            QMessageBox.critical(self, 'Wrong', 'Wrong Username or Password!')
            return

        user = self.user_line.text().split('@')[0]
        if user == 'admin':
            self.windowAdmin = WindowAdmin()
            self.windowAdmin.show()
        else:
            self.windowUser = WindowUser()
            self.windowUser.show()

        self.close()

    def show_signin_page_func(self):
        self.signin_page.exec()

    def check_input_func(self):
        if self.user_line.text() and self.pwd_line.text():
            self.login_button.setEnabled(True)
        else:
            self.login_button.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Login()
    w.show()
    sys.exit(app.exec())