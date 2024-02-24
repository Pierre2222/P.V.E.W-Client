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
            curr = Functions.Air_Quality()
            post_label = qtw.QLabel(f""""
            {Functions.check_wind(entry.text)}
            {Functions.check_temp(entry.text)}
            {Functions.check_rain(entry.text)}
            {curr.check_air(entry.text)}
                                    """)
            self.layout().addWidget(post_label)
            

            
app = qtw.QApplication([])
mw = MainWindow()

app.exec_()

