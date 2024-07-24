import flet as ft
import time


class Settings:

    # ---Инициализация класса---
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Uncharted Sector: Settings"
        self.del_before()
        self.anim_start()

    #---Удаление предыдущего окна---
    def del_before(self):
        self.page.clean()

    #---Сохранение настройки в файл---
    @staticmethod
    def save_to_file(key, value):
        #Поиск абсолютного пути
        from os import path
        file_path = path.abspath(path.dirname(__file__))
        file_path = path.join(file_path, '..', "Data", "settings.json")
        #Перезаписываем файл настроек
        import json
        with open(file_path, 'w', encoding='UTF-8') as file:
            json.dump({key: value}, file)

    #---Переключение темы---
    def change_theme(self, e):
        if self.page.theme_mode == 'light':
            self.page.theme_mode = 'dark'
        else:
            self.page.theme_mode = 'light'
        self.page.update()
        self.save_to_file('theme_mode', value=self.page.theme_mode)

    #---Настройки --> Главное меню---
    def back_to_menu(self, e):
        from C_UI.main_menu import MainMenu
        MainMenu(self.page)

    # ---Спавн меню настроек с анимацией---
    def anim_start(self):
        # ---Создание контейнера для дальнейших анимаций---
        def create_container():
            b_style = ft.BorderSide(width=1, color='cyan')
            border = ft.Border(top=b_style, bottom=b_style, left=b_style, right=b_style)

            return ft.Container(padding=10, margin=0, border=border)

        # ---Начальные параметры контейнера---
        container = create_container()
        container.border_radius = 10
        container.height = 350
        container.width = 300
        container.animate = ft.animation.Animation(300, curve=ft.AnimationCurve.EASE)
        self.page.add(container)

        # ---Анимация ширины---
        time.sleep(0.5)
        container.width = 300
        self.page.update()

        # ---Анимация высоты---
        time.sleep(0.3)
        container.height = 350
        self.page.update()

        # ---Анимация появления кнопок---
        btns = self.create_widgets()
        btns.animate_opacity = ft.animation.Animation(500, curve=ft.AnimationCurve.EASE)
        btns.opacity = 0
        container.content = btns
        self.page.update()
        time.sleep(0.2)
        btns.opacity = 1
        self.page.update()

    # ---Создание виджетов---
    def create_widgets(self):

        #---Заголовок раздела настроек---
        def section_title(title=''):
            row = ft.Row([ft.Text(title, size=20, weight=ft.FontWeight('bold'))], alignment=ft.MainAxisAlignment.CENTER)

            return [ft.Divider(thickness=2), row, ft.Divider(thickness=2)]

        #---Пункт настроек - тумблер---
        def settings_switch(name='', current_value=False, event=None):
            text = ft.Text(name, scale=1.2, text_align=ft.TextAlign.CENTER, offset=ft.Offset(x=0.15, y=0))
            switch = ft.Switch(value=current_value, on_change=event)
            row = ft.Row([text, switch], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

            return [row, ft.Divider()]

        #---Список настроек---
        settings_list = ft.ListView(
            section_title('Визуальные настройки') +
            settings_switch(name="Тёмная / Светлая тема",
                            current_value=self.page.theme_mode == 'light',
                            event=self.change_theme)
            , height=520, padding=0
        )

        #---Нижняя панель---
        bottom_row = ft.Row([
            ft.OutlinedButton(text="В главное меню",
                              scale=1.2,
                              width=170,
                              on_click=self.back_to_menu)
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND)

        return ft.Column(controls=[settings_list, bottom_row], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
