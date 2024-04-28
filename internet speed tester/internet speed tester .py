from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import speedtest,about
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("internet speed tester")
        self.إظهار1=qt.QLabel("سرعة التحميل")
        self.التحميل=qt.QLineEdit()
        self.التحميل.setReadOnly(True)
        self.التحميل.setAccessibleName("سرعة التحميل")
        self.إظهار2=qt.QLabel("سرعة الرفع")
        self.الرفع=qt.QLineEdit()
        self.الرفع.setReadOnly(True)
        self.الرفع.setAccessibleName("سرعة الرفع")        
        self.بدء=qt.QPushButton("بدء الاختبار")
        self.بدء.setDefault(True)
        self.بدء.clicked.connect(self.test)
        self.عن=qt.QPushButton("عن المطور")
        self.عن.setDefault(True)        
        self.عن.clicked.connect(self.about)
        l=qt.QVBoxLayout()        
        l.addWidget(self.إظهار1)
        l.addWidget(self.التحميل)
        l.addWidget(self.إظهار2)
        l.addWidget(self.الرفع)        
        l.addWidget(self.بدء)
        l.addWidget(self.عن)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)                
    def test(self):
        try:
            qt.QMessageBox.warning(self, "تنبيه","لقد بدأ الاختبار, يرجى الانتظار لأنه قد يأخذ بعض الوقت")
            st=speedtest.Speedtest()            
            download_speed=st.download() / 1000000
            upload_speed=st.upload() / 1000000            
            self.التحميل.setText(f"{download_speed} MB")
            self.الرفع.setText(f"{upload_speed} MB")
            self.التحميل.setFocus()
        except:
            qt.QMessageBox.warning(self, "تحذير", "حدث خطأ ما, تأكد من إتصالك بالإنترنت")
    def about(self):
        about.dialog(self).exec()
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()