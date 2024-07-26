import flet as ft
import time
import C_UI.MiniFunc.CoreFunctions as Core

class Settings:

    # ---Инициализация класса---
    def __init__(self, page: ft.Page):
        self.container = None
        self.btns = None
        self.page = page
        self.animations = Core.read_settings('animations')
        self.page.title = "Uncharted Sector: Settings"
        self.del_before()
        self.animate_spawn()

    #---Удаление предыдущего окна---
    def del_before(self):
        self.page.clean()

    #---Переключение темы---
    def change_theme(self, e):
        if self.page.theme_mode == 'dark':
            Core.write_settings('theme_mode', 'light')
        else:
            Core.write_settings('theme_mode', 'dark')
        self.page.theme_mode = Core.read_settings('theme_mode')

        self.page.update()

    #---Переключение анимаций---
    def change_animations(self, e):
        if Core.read_settings('animations'):
            Core.write_settings('animations', False)
        else:
            Core.write_settings('animations', True)
        self.animations = Core.read_settings('animations')
        self.page.update()

    #---Настройки --> Главное меню---
    def back_to_menu(self, e):
        self.animate_spawn(True)
        from C_UI.main_menu import MainMenu
        MainMenu(self.page, False)

    # ---Настройки --> Главное меню---
    def back_to_main_book(self, e):
        self.animate_spawn(True)
        from C_UI.main_book import Main_Book
        Main_Book(self.page)

    # ---Спавн меню настроек с анимацией---
    def animate_spawn(self, end=False):
        # ---Создание контейнера для дальнейших анимаций---
        def create_container():
            b_style = ft.BorderSide(width=1, color='cyan')
            border = ft.Border(top=b_style, bottom=b_style, left=b_style, right=b_style)

            return ft.Container(padding=10, margin=0, border=border)
        if not self.animations:
            self.container = create_container()
            self.container.animate = ft.animation.Animation(300, curve=ft.AnimationCurve.EASE)
            self.container.border_radius = 10
            self.container.width = 1000
            self.container.height = 600
            self.btns = self.create_widgets()
            self.btns.animate_opacity = ft.animation.Animation(500, curve=ft.AnimationCurve.EASE)
            self.container.content = self.btns
            self.page.add(self.container)
            return

        if not end:
            # ---Начальные параметры контейнера---
            self.container = create_container()
            self.container.border_radius = 10
            self.container.height = 350
            self.container.width = 300
            self.container.animate = ft.animation.Animation(300, curve=ft.AnimationCurve.EASE)
            self.page.add(self.container)

            # ---Анимация ширины---
            time.sleep(0.1)
            self.container.width = 1000
            self.page.update()

            # ---Анимация высоты---
            time.sleep(0.3)
            self.container.height = 600
            self.page.update()

            # ---Анимация появления кнопок---
            self.btns = self.create_widgets()
            self.btns.animate_opacity = ft.animation.Animation(500, curve=ft.AnimationCurve.EASE)
            self.btns.opacity = 0
            self.container.content = self.btns
            self.page.update()
            time.sleep(0.2)
            self.btns.opacity = 1
            self.page.update()
        else:
            # ---Анимация исчезания кнопок---
            time.sleep(0.2)
            self.btns.opacity = 0
            # self.container.content = None
            self.page.update()

            # ---Анимация ширины---
            time.sleep(0.1)
            self.container.width = 300
            self.page.update()

            # ---Анимация высоты---
            time.sleep(0.3)
            self.container.height = 350
            self.page.update()
            time.sleep(0.2)

    # ---Создание виджетов---
    def create_widgets(self):

        #---Заголовок раздела настроек---
        def section_title(title=''):
            text = ft.Text(title, size=20, weight=ft.FontWeight('bold'))

            return [ft.Column([ft.Divider(thickness=2), text, ft.Divider(thickness=2)],
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER, width=100)]

        #---Пункт настроек - тумблер---
        def settings_switch(name='', current_value=False, event=None):
            text = ft.Text(name, scale=1.2, text_align=ft.TextAlign.CENTER, offset=ft.Offset(x=0.15, y=0))
            switch = ft.Switch(value=current_value, on_change=event)
            row = ft.Row([text, switch], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

            return [row, ft.Divider()]

        #---Список настроек---
        settings_list = ft.ListView(
            section_title('Визуальные настройки') +
            settings_switch(name="Переключить тему",
                            current_value=Core.read_settings('theme_mode') == 'light',
                            event=self.change_theme) +
            settings_switch(name="Анимации",
                            current_value=Core.read_settings('animations'),
                            event=self.change_animations)
            , height=520, padding=0
        )

        #---Нижняя панель---
        bottom_row = ft.Row([
            ft.OutlinedButton(text="В главное меню",
                              scale=1.2,
                              width=170,
                              on_click=self.back_to_menu),
            ft.OutlinedButton(text="Правила и сеттинг",
                              scale=1.2,
                              width=180,
                              on_click=self.back_to_main_book),
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND)

        return ft.Column(controls=[settings_list, bottom_row], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
