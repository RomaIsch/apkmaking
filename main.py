from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class MainApp(MDApp):
    def build(self):
        screen = MDScreen()

        # Главное решение: используем MDLabel для текста
        label = MDLabel(
            text="Привет, KivyMD!",
            halign="center",  # Выравнивание по горизонтали
            font_style="Display",  # Предустановленный стиль Material Design (крупный)
            theme_text_color="Primary"  # Цвет текста по умолчанию для темы
        )

        screen.add_widget(label)
        return screen


if __name__ == '__main__':
    MainApp().run()