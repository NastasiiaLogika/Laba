from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math
import sys


class QWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python")
        self.setGeometry(100, 100, 560, 450)
        self.UiComponents()
        self.show()

    def UiComponents(self):

        self.label = QLabel(self)

        self.label.setGeometry(5, 5, 550, 70)

        self.label.setWordWrap(True)

        self.label.setStyleSheet("QLabel"
                                "{"
                                "border : 4px solid black;"
                                "background : white;"
                                "}")

        self.label.setAlignment(Qt.AlignRight)

        self.label.setFont(QFont('Arial', 15))

        push1 = QPushButton("1", self)

        push1.setGeometry(5, 150, 140, 40)

        push2 = QPushButton("2", self)

        push2.setGeometry(150, 150, 140, 40)

        push3 = QPushButton("3", self)

        push3.setGeometry(295, 150, 140, 40)

        push4 = QPushButton("4", self)

        push4.setGeometry(5, 200, 140, 40)

        push5 = QPushButton("5", self)

        push5.setGeometry(150, 200, 140, 40)

        push6 = QPushButton("6", self)

        push6.setGeometry(295, 200, 140, 40)

        push7 = QPushButton("7", self)

        push7.setGeometry(5, 250, 140, 40)

        push8 = QPushButton("8", self)

        push8.setGeometry(150, 250, 140, 40)

        push9 = QPushButton("9", self)

        push9.setGeometry(295, 250, 140, 40)

        push0 = QPushButton("0", self)

        push0.setGeometry(5, 300, 140, 40)
        
        push_equal = QPushButton("=", self)

        push_equal.setGeometry(440, 300, 115, 40)

        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)

        push_plus = QPushButton("+", self)

        push_plus.setGeometry(440, 250, 115, 40)

        push_minus = QPushButton("-", self)

        push_minus.setGeometry(440, 200, 115, 40)

        push_mul = QPushButton("*", self)

        push_mul.setGeometry(440, 150, 115, 40)

        push_div = QPushButton("/", self)

        push_div.setGeometry(295, 300, 140, 40)

        push_point = QPushButton(".", self)

        push_point.setGeometry(150, 300, 140, 40)

        push_cos = QPushButton("cos", self)

        push_cos.setGeometry(5, 350, 140, 40)

        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)

        push_sin = QPushButton("sin", self)

        push_sin.setGeometry(150, 350, 140, 40)

        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)

        push_tg = QPushButton("tg", self)

        push_tg.setGeometry(295, 350, 140, 40)

        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)

        push_sqrt = QPushButton("√", self)

        push_sqrt.setGeometry(440, 350, 115, 40)

        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)

        push_clear = QPushButton("Clear", self)
        push_clear.setGeometry(5, 100, 260, 40)
        
        push_del = QPushButton("Del", self)
        push_del.setGeometry(275, 100, 280, 40)

        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push0.clicked.connect(self.action0)
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        push_div.clicked.connect(self.action_div)
        push_mul.clicked.connect(self.action_mul)
        push_plus.clicked.connect(self.action_plus)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
        push_del.clicked.connect(self.action_del)
        push_cos.clicked.connect(self.action_cos)
        push_sin.clicked.connect(self.action_sin)
        push_sqrt.clicked.connect(self.action_sqrt)
        push_tg.clicked.connect(self.action_tg)
        
    def action_equal(self):
        equation = self.label.text()
        try:
            ans = eval(equation)
            self.label.setText(str(ans))

        except:
            self.label.setText("Wrong Input")

    def action_plus(self):
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_minus(self):
        text = self.label.text()
        self.label.setText(text + " - ")

    def action_div(self):
        text = self.label.text()
        self.label.setText(text + " / ")

    def action_mul(self):
        text = self.label.text()
        self.label.setText(text + " * ")

    def action_point(self):
        text = self.label.text()
        self.label.setText(text + ".")

    def action0(self):
        text = self.label.text()
        self.label.setText(text + "0")

    def action1(self):
        text = self.label.text()
        self.label.setText(text + "1")

    def action2(self):
        text = self.label.text()
        self.label.setText(text + "2")

    def action3(self):
        text = self.label.text()
        self.label.setText(text + "3")

    def action4(self):
        text = self.label.text()
        self.label.setText(text + "4")

    def action5(self):
        text = self.label.text()
        self.label.setText(text + "5")

    def action6(self):
        text = self.label.text()
        self.label.setText(text + "6")

    def action7(self):
        text = self.label.text()
        self.label.setText(text + "7")

    def action8(self):
        text = self.label.text()
        self.label.setText(text + "8")

    def action9(self):
         text = self.label.text()
         self.label.setText(text + "9")

    def action_clear(self):
        self.label.setText("")

    def action_del(self):
        text = self.label.text()
        print(text[:len(text) - 1])
        self.label.setText(text[:len(text) - 1])

    def action_cos(self):
        text = self.label.text()
        value = float(text)
        cos_value = math.cos(math.radians(value))

        self.label.setText("cos " +text+" = "+ str(cos_value))

    def action_sin(self):
        text = self.label.text()
        value = float(text)
        sin_value = math.sin(math.radians(value))

        self.label.setText("sin " + text + " = " + str(sin_value))

    def action_sqrt(self):
        text = self.label.text()
        value = float(text)
        sqrt_value = math.sqrt(value)

        self.label.setText("sqrt " + text + " = " + str(sqrt_value))

    def action_tg(self):
        text = self.label.text()
        value = float(text)
        tg_value = math.tan(math.radians(value))

        self.label.setText("tg " + text + " = " + str(tg_value))
        

App = QApplication(sys.argv)
window = QWindow()
sys.exit(App.exec())