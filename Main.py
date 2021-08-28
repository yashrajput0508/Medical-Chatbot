# Medical chatbot which gives the answer for your question
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox
from frames.loginform import *
from frames.Registeration import *
from frames.chat import *
from frames.Report import *
import Database as db
import pandas as pd
import sys, webbrowser



class model: # It handles the modeling  and predicting phase
    def __init__(self):
        self.training=pd.read_csv('data/Training.csv')
        self.length=len(self.training.columns)-1
        self.modeling()

    def modeling(self): # It models the algorithm
        # Slicing and Dicing the dataset to separate features from predictions
        X = self.training.iloc[:, 0:132].values
        Y = self.training.iloc[:, -1].values

        # Dimensionality Reduction for removing redundancies
        self.dimensionality_reduction = self.training.groupby(self.training['prognosis']).max()

        # Encoding String values to integer constants
        from sklearn.preprocessing import LabelEncoder
        self.labelencoder = LabelEncoder()
        y = self.labelencoder.fit_transform(Y)
        # Splitting the dataset into training set and test set
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
        # Implementing the Decision Tree Classifier
        from sklearn.tree import DecisionTreeClassifier
        self.classifier = DecisionTreeClassifier()
        self.classifier.fit(X_train, y_train)

    def prediction(self,value): # It predict the result of your answer
        l=[]
        v=self.classifier.predict([value])
        disease=self.labelencoder.inverse_transform(v)
        red_cols = self.dimensionality_reduction.columns
        symptoms_given = red_cols[self.dimensionality_reduction.loc[disease].values[0].nonzero()]
        l.extend([disease[0],symptoms_given])
        return l

class report(QWidget):  # It handles the report frames which gives the result to the user
    def __init__(self,value):
        super().__init__()
        self.ui=Ui_Form_2()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.backtochat)
        self.ui.pushButton_2.clicked.connect(self.location)
        self.value=value
        self.datas()

    def datas(self): # it takes the prediction from model
        try:
            self.list=[0]*work.model.length
            if self.value<=work.model.length:
                self.list[self.value]=1
            self.ans=work.model.prediction(self.list)
            self.addFeature()
        except Exception as e:
            print(e)

    def addFeature(self): # it show the report to the user
        self.ui.name.setText(work.Name)
        self.ui.number.setText(work.Contactno)
        self.ui.disease.setText(str(self.ans[0]))
        self.ui.symptomspresent.setText(work.Symtoms)
        self.ui.symptomsgiven.setText(",".join(list(self.ans[1])))
        self.doctors=pd.read_csv('data/doctor_dataset.csv')
        row = self.doctors[self.doctors['disease'] == self.ans[0]]
        self.ui.consultant.setText(str(row['name'].values[0]))
        self.ui.link.setText("<a href={}>{}</a>".format(str(row['link'].values[0]),str(row['link'].values[0])))
        data = pd.read_csv("data/symptom_precaution.csv")
        self.ui.precations.setText(", ".join(data[data['disease'] == "Allergy"].values[0]))

    def backtochat(self): # it return to the chatting app
        work.chat()
        work.destroyreport()

    def location(self): #IT shows the nearest hospital from house
        webbrowser.open("https://www.google.com/maps/search/hospitals/@28.4455837,79.4113011,12.21z/data=!4m8!2m7!3m6!1shospitals!2sSRMS+College+of+Engineering,Technology+%26+Research,Bareilly,+Ram+Murti+Puram,+Bareilly+-+Nainital+Rd,+Highway,+Bhoji+Pura,+Uttar+Pradesh+243202!3s0x39a008efd314c97d:0x9d39830912ec26b9!4m2!1d79.4352386!2d28.4754361")

class qna(QWidget): # it handles the qna frame
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form1()
        self.ui.setupUi(self)
        self.length=work.model.length
        self.i=0
        self.ui.username.setText("Do you have " + work.model.training.columns[self.i] + "?")
        self.i=1
        self.ui.submit.clicked.connect(self.next)
        self.ui.restart.clicked.connect(self.restart)
        self.ui.quit.clicked.connect(self.quit)

    def next(self): # it shows the question to user one by one
        if self.ui.no.isChecked():
            self.ui.no.setChecked(False)
            if self.i<=self.length:
                self.ui.username.setText("Do you have "+work.model.training.columns[self.i]+"?")
                self.i+=1
            else:
                work.report(self.i)
                work.destroychat()
        elif self.ui.yes.isChecked():
            self.ui.yes.setChecked(False)
            work.Symtoms=work.model.training.columns[self.i-1]
            work.report(self.i-1)
            work.destroychat()
        else:
            QMessageBox.warning(self.parent(),"warning","Please select any option")

    def restart(self): # it restart the frame
        self.i = 0
        self.ui.username.setText("Do you have " + work.model.training.columns[self.i] + "?")
        self.i = 1

    def quit(self):
        work.destroychat()

class Registering(QWidget): # it handles the registering frame
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.Register.clicked.connect(self.submit)

    def submit(self): # it register the username,email,contact,password to the database
        name=self.ui.username.text()
        email=self.ui.emailid_2.text()
        contact=self.ui.contactnumber.text()
        if name=="":
            QMessageBox.warning(self.parent(),"Warning","Please enter your name")
        elif email=="":
            QMessageBox.warning(self.parent(),"Warning","Please enter your email")
        elif contact=="":
            QMessageBox.warning(self.parent(),"Warning","Please enter your contact")
        elif self.ui.password.text()=="":
            QMessageBox.warning(self.parent(),"Warning","Please enter your password")
        elif self.ui.password.text()!=self.ui.password_7.text():
            QMessageBox.warning(self.parent(),"Warning","Password Not matched")
        else:
            db.updatedatabase(name,email,contact,self.ui.password.text())
            QMessageBox.information(self.parent(),"Success","Successful SignIn")
            work.Name=name
            work.Contactno=contact
            work.chat()
            work.destroyRegister()


class LoginForm(QMainWindow): # It handle the login form
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Register.clicked.connect(self.login)
        self.ui.Register_2.clicked.connect(self.register)
        db.database()

    def login(self): # it check the username or password
        username=self.ui.username.text()
        password=self.ui.password.text()
        lists=[]
        for i in db.getlist(username):
            lists.append(i[0])
        if lists!=[]:
            if password in lists:
                work.Name=username
                work.Contactno=db.getnumber(username,password)[0][0]
                work.chat()
                work.destroyLogin()
                # Login
            else:
                self.ui.warning.setText("Login Details are wrong try again")
        else:
            self.ui.warning.setText("User not found please register yourself")

    def register(self): # It open the register frame work
        work.registered()
        work.destroyLogin()

class MainWork(): # it is the main class handles all the frames
    def __init__(self):
        self.model=model()
        self.login=LoginForm()
        self.login.show()
        self.Name = ""
        self.Contactno = ""
        self.Symtoms = ""

    def destroyLogin(self): # it destroy the login frame
        self.login.close()

    def registered(self): # it shows the register frame
        self.reg = Registering()
        self.reg.show()

    def destroyRegister(self): # it destroy the register frame
        self.reg.close()

    def chat(self): # it show the qna frame
        self.qna=qna()
        self.qna.show()

    def destroychat(self): # it destroy the qna frame
        self.qna.close()

    def report(self,i): # it show the report frame
        self.rep=report(i)
        self.rep.show()

    def destroyreport(self): # it destroy the report frame
        self.rep.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    work = MainWork()
    sys.exit(app.exec_())