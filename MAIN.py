import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import Functions

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PVEW: Environment Viewer")
        self.setLayout(qtw.QVBoxLayout())
        PVEW_label = qtw.QLabel("PVEW")
        PVEW_label.setFont(qtg.QFont('Black Hans Sans', 30))
        self.layout().addWidget(PVEW_label)

        entry = qtw.QLineEdit()
        entry.setObjectName("Email_Grabber")
        entry.setText("Enter Your Email")
        self.layout().addWidget(entry)

        button = qtw.QPushButton("Confirm", clicked = lambda: Button_Press())
        self.layout().addWidget(button)
        self.show()
        def Button_Press():
            return entry.text
            
app = qtw.QApplication([])
mw = MainWindow()

app.exec_()

email = mw.Butt_Press()
print(email)

