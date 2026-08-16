import math
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_FILE = os.path.join(BASE_DIR, "NotoSansBengali-Regular.ttf")

if os.path.exists(FONT_FILE):
    LabelBase.register(name="BanglaFont", fn_regular=FONT_FILE)
    BANGLA_FONT = "BanglaFont"
else:
    BANGLA_FONT = "Roboto"

BANGLA = "০১২৩৪৫৬৭৮৯"
ENGLISH = "0123456789"
TO_BANGLA = str.maketrans(ENGLISH, BANGLA)
TO_ENGLISH = str.maketrans(BANGLA, ENGLISH)

def to_bangla(value):
    return str(value).translate(TO_BANGLA)

def to_english(value):
    return str(value).translate(TO_ENGLISH)

class CalculatorApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shift = False
        self.memory = 0
        self.answer = 0

    def build(self):
        root = BoxLayout(orientation="vertical", padding=8, spacing=6)
        self.display = TextInput(
            text="", font_name=BANGLA_FONT, font_size=28,
            readonly=True, multiline=False, halign="right",
            size_hint_y=None, height=72
        )
        root.add_widget(self.display)

        grid = GridLayout(cols=5, spacing=5)
        buttons = [
            "SHIFT","AC","DEL","(",")",
            "sin","cos","tan","√","π",
            "x²","x³","xʸ","1/x","n!",
            "log","ln","e","ANS","%",
            "BIN","DEC","OCT","HEX","÷",
            "৭","৮","৯","×","−",
            "৪","৫","৬","+","=",
            "১","২","৩",".","M+",
            "০","M−","MR","MC","HIS"
        ]
        for text in buttons:
            font = BANGLA_FONT if text in BANGLA else "Roboto"
            b = Button(text=text, font_name=font, font_size=17)
            b.bind(on_press=self.press)
            grid.add_widget(b)
        root.add_widget(grid)
        return root

    def press(self, instance):
        value = instance.text

        if value == "SHIFT":
            self.shift = not self.shift
            instance.text = "SHIFT ON" if self.shift else "SHIFT"
            return
        if value == "AC":
            self.display.text = ""
            return
        if value == "DEL":
            self.display.text = self.display.text[:-1]
            return
        if value == "=":
            self.calculate()
            return

        if value in ("sin", "cos", "tan"):
            fn = {"sin":"sin", "cos":"cos", "tan":"tan"}[value]
            if self.shift:
                fn = {"sin":"asin", "cos":"acos", "tan":"atan"}[value]
            self.display.text += fn + "("
            return

        if value == "√":
            self.display.text += "sqrt("
            return
        if value == "π":
            self.display.text += "pi"
            return
        if value == "x²":
            self.display.text += "^2"
            return
        if value == "x³":
            self.display.text += "^3"
            return
        if value == "xʸ":
            self.display.text += "^"
            return
        if value == "1/x":
            self.display.text += "inv("
            return
        if value == "n!":
            self.display.text += "fact("
            return
        if value == "log":
            self.display.text += "log("
            return
        if value == "ln":
            self.display.text += "ln("
            return
        if value == "e":
            self.display.text += "e"
            return
        if value == "ANS":
            self.display.text += str(self.answer)
            return

        if value in ("BIN","DEC","OCT","HEX"):
            self.convert_number(value)
            return

        if value == "M+":
            try:
                self.memory += float(self.get_current_value())
                self.display.text = "M+"
            except:
                self.display.text = "ভুল মান!"
            return
        if value == "M−":
            try:
                self.memory -= float(self.get_current_value())
                self.display.text = "M-"
            except:
                self.display.text = "ভুল মান!"
            return
        if value == "MR":
            self.display.text = to_bangla(self.memory)
            return
        if value == "MC":
            self.memory = 0
            self.display.text = "MC"
            return
        if value == "HIS":
            self.display.text = to_bangla(self.answer)
            return

        self.display.text += value

    def get_current_value(self):
        expression = to_english(self.display.text)
        expression = expression.replace("×","*").replace("÷","/").replace("−","-")
        expression = expression.replace("^","**").replace("%","/100")
        try:
            return eval(expression, {"__builtins__": {}}, {"pi":math.pi,"e":math.e})
        except:
            return 0

    def convert_number(self, mode):
        try:
            value = to_english(self.display.text).strip()
            number = int(float(value))
            if mode == "DEC":
                result = str(number)
            elif mode == "BIN":
                result = bin(number)[2:]
            elif mode == "OCT":
                result = oct(number)[2:]
            else:
                result = hex(number)[2:].upper()
            self.display.text = to_bangla(result)
        except:
            self.display.text = "ভুল মান!"

    def calculate(self):
        try:
            expression = to_english(self.display.text)
            expression = expression.replace("×","*").replace("÷","/")
            expression = expression.replace("−","-").replace("^","**")
            expression = expression.replace("%","/100")

            def sin(x): return math.sin(math.radians(x))
            def cos(x): return math.cos(math.radians(x))
            def tan(x): return math.tan(math.radians(x))
            def asin(x): return math.degrees(math.asin(x))
            def acos(x): return math.degrees(math.acos(x))
            def atan(x): return math.degrees(math.atan(x))
            def inv(x): return 1/x
            def fact(x):
                if x < 0 or int(x) != x:
                    raise ValueError
                return math.factorial(int(x))
            def ln(x): return math.log(x)

            allowed = {
                "sin":sin,"cos":cos,"tan":tan,
                "asin":asin,"acos":acos,"atan":atan,
                "sqrt":math.sqrt,"log":math.log10,"ln":ln,
                "inv":inv,"fact":fact,"pi":math.pi,"e":math.e
            }
            result = eval(expression, {"__builtins__": {}}, allowed)

            if isinstance(result, float):
                if not math.isfinite(result):
                    raise ValueError
                result = int(result) if result.is_integer() else round(result,10)

            self.answer = result
            self.display.text = to_bangla(result)
            self.shift = False
        except ZeroDivisionError:
            self.display.text = "শূন্য দিয়ে ভাগ করা যাবে না"
        except ValueError:
            self.display.text = "ভুল মান!"
        except:
            self.display.text = "ভুল হিসাব!"

if __name__ == "__main__":
    CalculatorApp().run()
