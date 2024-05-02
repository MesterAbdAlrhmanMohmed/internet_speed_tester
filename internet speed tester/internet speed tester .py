from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import speedtest,about
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("internet speed tester")
        self.إظهار1=qt.QLabel("سرعة التحميل في الثانية")
        self.التحميل=qt.QLineEdit()
        self.التحميل.setReadOnly(True)
        self.التحميل.setAccessibleName("سرعة التحميل في الثانية")
        self.إظهار2=qt.QLabel("سرعة الرفع في الثانية")
        self.الرفع=qt.QLineEdit()
        self.الرفع.setReadOnly(True)
        self.الرفع.setAccessibleName("سرعة الرفع في الثانية")
        self.إظهار3=qt.QLabel("البينج")
        self.بينج=qt.QLineEdit()
        self.بينج.setReadOnly(True)
        self.بينج.setAccessibleName("البينج")
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
        l.addWidget(self.إظهار3)
        l.addWidget(self.بينج)
        l.addWidget(self.بدء)
        l.addWidget(self.عن)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)                
    def test(self):
        try:
            qt.QMessageBox.warning(self, "تنبيه","لقد بدأ الاختبار, يرجى الانتظار لأنه قد يأخذ بعض الوقت")
            السرعة=speedtest.Speedtest()
            سرعة_التحميل=السرعة.download() / 1000000
            سرعة_الرفع=السرعة.upload() / 1000000
            البينج=السرعة.results.ping
            self.التحميل.setText(f"{سرعة_التحميل} MB")
            self.الرفع.setText(f"{سرعة_الرفع} MB")
            self.بينج.setText(str(البينج))
            self.التحميل.setFocus()            
        except:
            qt.QMessageBox.warning(self, "تحذير", "حدث خطأ ما, تأكد من إتصالك بالإنترنت, وإذا إستمرت المشكلة قم بإعادة تشغيل الكمبيوتر")
    def about(self):
        about.dialog(self).exec()
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()