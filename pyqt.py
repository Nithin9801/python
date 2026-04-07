# clock

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel
from PyQt5.QtCore import QTime,QTimer,Qt
from PyQt5.QtGui import QFont,QFontDatabase

class clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.time = QTimer(self)
        self.Initui()

    def Initui(self):
        self.setWindowTitle("DIGITAL CLOCK")
        self.setGeometry(700,300,300,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("color:green;" \
        "font-size:150px;")

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family,150)
        self.time_label.setFont(my_font)

        self.setStyleSheet("background-color:black;")

        self.time.timeout.connect(self.Update_time)
        self.time.start(1000)

        self.Update_time()

    def Update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


def main():
    app = QApplication(sys.argv)
    window = clock()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()