import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QHBoxLayout,QVBoxLayout,QPushButton
from PyQt5.QtCore import Qt,QTime,QTimer

class Stop_watch(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,300,200)
        self.time = QTime(0,0,0,0)
        self.timelabel = QLabel("00:00:00:00",self)
        self.startbutton = QPushButton("Start",self)
        self.stopbutton = QPushButton("stop",self)
        self.resetbutton = QPushButton("Reset",self)
        self.timer = QTimer(self)
        self.InitUi()

    def InitUi(self):
        self.setWindowTitle("STOPWATCH")

        vbox = QVBoxLayout()
        
        vbox.addWidget(self.timelabel)

        self.timelabel.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.startbutton)
        hbox.addWidget(self.stopbutton)
        hbox.addWidget(self.resetbutton)

        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setStyleSheet("""
                           
           QPushButton,QLabel{
                           padding: 20px;
                           font-weight:bold;
                           font-family:calibri;
                           }
           QPushButton{
                           font-size:30px;}

           QLabel{
                           font-size:40px;
                           background-color:hsl(194, 100%, 82%);
                           border-radius:30px;}

        """)

        self.startbutton.clicked.connect(self.start)
        self.stopbutton.clicked.connect(self.stop)
        self.resetbutton.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.timelabel.setText(self.format_time(self.time))

    def format_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.timelabel.setText(self.format_time(self.time))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    watch = Stop_watch()
    watch.show()
    sys.exit(app.exec_())