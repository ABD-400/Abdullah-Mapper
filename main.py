with open('main.py', 'w') as f:
    f.write('''
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder

# تصميم الواجهة
Builder.load_string("""
<MainLayout>:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: (0.05, 0.05, 0.05, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: "Abdullah Ultimate Mapper"
        font_size: '32sp'
        bold: True
        color: (0, 0.7, 1, 1)
    Label:
        id: status
        text: "انتظار ضغطة زر من اليد أو الكيبورد..."
        font_size: '18sp'
""")

class MainLayout(BoxLayout):
    def init(self, **kwargs):
        super().init(**kwargs)
        # الاستماع لضغطات المفاتيح (كيبورد + يد تحكم)
        Window.bind(on_key_down=self.on_input)

    def on_input(self, window, key, scancode, codepoint, modifier):
        self.ids.status.text = f"تم رصد الزر! الكود هو: {scancode}"
        return True

class AbdullahMapperApp(App):
    def build(self):
        return MainLayout()

if name == "main":
    AbdullahMapperApp().run()
''')
