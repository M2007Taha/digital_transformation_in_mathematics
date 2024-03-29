"""
@author: m2007taha
digital_transformation_in_mathematics v1.0
"""
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
import math
import numpy

class main():
    def __init__(self,gui):
        self.gui = gui
    def func(self):
        self.gui.factorial_button.clicked.connect(self.clear)
        self.gui.factorial_button.clicked.connect(self.factorial_func)
        self.gui.trigonometry_button.clicked.connect(self.clear)
        self.gui.trigonometry_button.clicked.connect(self.trigonometry_func)
        self.gui.fibonacci_button.clicked.connect(self.clear)
        self.gui.fibonacci_button.clicked.connect(self.fibonacci_func)
        self.gui.exponentiation_button.clicked.connect(self.clear)
        self.gui.exponentiation_button.clicked.connect(self.exponentiation_func)
        self.gui.absolute_button.clicked.connect(self.clear)
        self.gui.absolute_button.clicked.connect(self.absolute_func)
        self.gui.gcd_lcm_button.clicked.connect(self.clear)
        self.gui.gcd_lcm_button.clicked.connect(self.gcd_lcm_func)
    #functions
    def fibonacci_func(self):
        try:
            print("fibonacci function run")
            counter = int(self.gui.fibonacci_input.text())
            a, b = 0, 1
            for _ in range(1,counter):
                self.gui.fibonacci_out.append(f"{a}\n")
                print(a, end=" ")
                a, b = b, a+b
            print()
        except:
            print('Error')
    def factorial_func(self):
        try:
            print("factorial function run")
            pin = self.gui.factorial_input.text()
            if '-' in pin:
                number = int(pin.replace('-',''))
                tmp = '-'
            else:
                number = int(pin)
                tmp = ''
            print(f"user input : {number}")
            factor = number * (number-1)
            for i in range(number-2,0,-1):
                factor *= i
            self.gui.factorial_out.append(f'{tmp}{factor}')
            print(f'out put : {tmp}{factor}')
        except:
            print('Error')
    def trigonometry_func(self):
        try:
            print("trigonometry function run")
            Input = self.gui.trigonometry_input.text()
            angle = math.radians(int(Input))
            print(f"user input : {angle}")
            sin = round(math.sin(angle),5)
            cos = round(math.cos(angle),5)
            tan = round(math.tan(angle),5)
            if tan != 0 :
                cot = round((1 / tan),5)
            else: 
                cot = 'Undefinde - تعریف نشده'
            result = f"sin{Input}∘ : {sin}\ncos{Input}∘ : {cos}\ntan{Input}∘ : {tan}\ncot{Input}∘ : {cot}"
            self.gui.trigonometry_out.append(f'{result}')
            print(f'out put :\n{result}')
        except:
            print('Error')
    def exponentiation_func(self):
        try:
            print("exponentiation function run")
            exponent = float(self.gui.exponentiation_exponent_input.text())
            base = float(self.exponentiation_base_input.text())
            print(f"user input:\nexponent : {exponent}\nbase : {base}")
            result = pow(base,exponent)
            self.gui.exponentiation_out.append(f"{result}")
            print(f"out put : {result}")
        except:
            print('Error')
    def absolute_func(self):
        try:
            print("absolute function run")
            number = float(self.gui.absolute_input.text())
            print(f"user input : {number}")
            result = abs(number)
            self.gui.absolute_out.append(f'{result}')
            print(f"out put : {result}")
        except:
            print('Error')
    def gcd_lcm_func(self):
        try:
            print("gcd_lcm function run")
            number1 = int(self.gui.gcd_lcm_input1.text())
            number2 = int(self.gui.gcd_lcm_input2.text())
            print(f"user input : {number1},{number2}")
            gcd = math.gcd(number1,number2)
            lcm = math.lcm(number1,number2)
            result = f"GCD({number1},{number2}) = {gcd}\nLCM({number1},{number2}) = {lcm}"
            self.gui.gcd_lcm_out.append(result)
            print(f"out put : {result}")
        except:
            print('Error')
    def clear(self):
        print('clear function run')
        self.gui.trigonometry_out.clear()
        self.gui.factorial_out.clear()
        self.gui.fibonacci_out.clear()
        self.gui.exponentiation_out.clear()
        self.gui.absolute_out.clear()
        self.gui.gcd_lcm_out.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file = QFile('14march.ui')
    if not ui_file.open(QIODevice.ReadOnly):
        sys.exit('error: cannot open *.ui file')
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        sys.exit(loader.errorString())
    window.show()
    
    a = main(window)
    a.func()

    sys.exit(app.exec())
