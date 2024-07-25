import flet as ft
import time
import C_UI.MiniFunc.CoreFunctions as Core


class Main_Book:

    # ---Инициализация класса---
    def __init__(self, page: ft.Page):
        self.page = page
        self.container = None
        self.left_container = None
        self.down_container = None
        self.btns1 = None
        self.btns2 = None
        self.btns3 = None
        self.animations = Core.read_settings('animations')
        self.page.title = "Uncharted Sector: MainBook"
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

    #---Главная книга --> Главное меню---
    def back_to_menu(self, e):
        self.animate_spawn(True)
        from C_UI.main_menu import MainMenu
        MainMenu(self.page, False)

    #---Главная книга --> Главное меню---
    def back_to_settings(self, e):
        self.animate_spawn(True)
        from C_UI.settings import Settings
        Settings(self.page)

    # ---Спавн меню настроек с анимацией---
    def animate_spawn(self, end=False):
        # ---Создание контейнера для дальнейших анимаций---
        def create_container():
            b_style = ft.BorderSide(width=1, color='cyan')
            border = ft.Border(top=b_style, bottom=b_style, left=b_style, right=b_style)

            return ft.Container(padding=10, margin=0, border=border, alignment=ft.Alignment(0, 0))

        if not self.animations:
            #Первый контейнер
            self.container = create_container()
            self.container.border_radius = 10
            self.container.width = 900
            self.container.height = 500
            self.container.border_radius = ft.BorderRadius(top_left=0, top_right=10,
                                                           bottom_left=0, bottom_right=0)
            #Контент контейнера
            self.btns1 = self.create_book()
            self.container.content = self.btns1

            #Второй контейнер
            self.left_container = create_container()
            self.left_container.border_radius = 10
            self.left_container.width = 150
            self.left_container.height = 500
            self.left_container.border_radius = ft.BorderRadius(top_left=10, top_right=0,
                                                                bottom_left=0, bottom_right=0)
            #Контент контейнера
            self.btns2 = self.create_shelf()
            self.left_container.content = self.btns2

            #Третий контейнер
            self.down_container = create_container()
            self.down_container.border_radius = 10
            self.down_container.width = 1060
            self.down_container.height = 80
            self.down_container.border_radius = ft.BorderRadius(top_left=0, top_right=0,
                                                                bottom_left=10, bottom_right=10)
            #Контент контейнера
            self.btns3 = self.create_row()
            self.down_container.content = self.btns3

            self.page.add(ft.Row([self.left_container, self.container], alignment=ft.MainAxisAlignment.CENTER),
                          self.down_container)
            return

        if not end:
            #Создаём контейнер
            self.container = create_container()
            self.container.border_radius = 10
            self.container.height = 350
            self.container.width = 300
            self.container.animate = ft.animation.Animation(300, curve=ft.AnimationCurve.EASE)
            self.page.add(self.container)

            #Анимация ширины
            time.sleep(0.1)
            self.container.width = 900
            self.page.update()

            #Анимация высоты и радиуса
            time.sleep(0.2)
            self.container.height = 500
            self.container.border_radius = ft.BorderRadius(top_left=0, top_right=10,
                                                           bottom_left=0, bottom_right=0)
            self.page.update()

            #Создаём контент
            self.btns1 = self.create_book()
            self.btns1.animate_opacity = ft.Animation(500, ft.AnimationCurve.EASE)
            self.btns1.opacity = 0
            self.container.content = self.btns1
            self.page.update()

            #Анимация появления
            time.sleep(0.2)
            self.btns1.opacity = 1
            self.page.update()

            #Создаём второй контейнер
            self.left_container = create_container()
            self.left_container.border_radius = 10
            self.left_container.height = 10
            self.left_container.width = 10
            self.left_container.animate = ft.animation.Animation(300, curve=ft.AnimationCurve.EASE)

            #Добавляем контейнер на экран
            time.sleep(0.1)
            self.page.clean()
            self.page.add(ft.Row([self.left_container, self.container],
                                 alignment=ft.MainAxisAlignment.CENTER))

            #Анимация ширины
            time.sleep(0.1)
            self.left_container.width = 150
            self.page.update()

            #Анимация высоты и радиуса
            time.sleep(0.2)
            self.left_container.height = 500
            self.left_container.border_radius = ft.BorderRadius(top_left=10, top_right=0,
                                                                bottom_left=0, bottom_right=0)
            self.page.update()

            #Создаём контент
            self.btns2 = self.create_shelf()
            self.btns2.animate_opacity = ft.Animation(500, ft.AnimationCurve.EASE)
            self.btns2.opacity = 0
            self.left_container.content = self.btns2
            self.page.update()

            time.sleep(0.2)
            self.btns2.opacity = 1
            self.page.update()

            #Создаём третий контейнер
            self.down_container = create_container()
            self.down_container.border_radius = 10
            self.down_container.height = 10
            self.down_container.width = 10
            self.down_container.animate = ft.animation.Animation(300, curve=ft.AnimationCurve.EASE)
            self.page.add(ft.Row([self.down_container], alignment=ft.MainAxisAlignment.CENTER))

            #Анимация ширины
            time.sleep(0.1)
            self.down_container.width = 1060
            self.page.update()

            #Анимация высоты
            time.sleep(0.2)
            self.down_container.height = 80
            self.down_container.border_radius = ft.BorderRadius(top_left=0, top_right=0,
                                                                bottom_left=10, bottom_right=10)
            self.page.update()

            #Создаём контент
            self.btns3 = self.create_row()
            self.btns3.animate_opacity = ft.Animation(500, ft.AnimationCurve.EASE)
            self.btns3.opacity = 0
            self.down_container.content = self.btns3
            self.page.update()

            time.sleep(0.2)
            self.btns3.opacity = 1
            self.page.update()
        else:
            self.btns3.opacity = 0
            self.down_container.border_radius = 10
            self.page.update()

            time.sleep(0.2)
            self.down_container.height = 10
            self.page.update()

            time.sleep(0.2)
            self.down_container.width = 10
            self.page.update()

            time.sleep(0.2)
            self.page.controls.pop(1)
            self.btns2.opacity = 0
            self.left_container.border_radius = 10
            self.page.update()

            time.sleep(0.2)
            self.left_container.width = 10
            self.page.update()

            time.sleep(0.2)
            self.left_container.height = 10
            self.page.update()

            time.sleep(0.1)
            self.btns1.opacity = 0
            self.page.clean()
            self.page.add(self.container)
            self.container.border_radius = 10
            self.page.update()

            time.sleep(0.1)
            self.container.width = 300
            self.page.update()

            time.sleep(0.2)
            self.container.height = 350
            self.page.update()
            return

    # ---Создание виджетов---
    def create_book(self):
        a = ft.Text("Test", size=20)
        return ft.ListView([a, a, a, a, a, a, a, a, a, a, a, a, a, a], auto_scroll=True)

    # ---Создание виджетов---
    def create_shelf(self):
        a = ft.Text("Test", size=20)
        return ft.ListView([a, a, a, a, a, a, a, a, a, a, a, a, a, a], auto_scroll=True)

    # ---Создание виджетов---
    def create_row(self):
        return ft.Row([ft.OutlinedButton("В главное меню", scale=1.2, on_click=self.back_to_menu),
                       ft.OutlinedButton("Настройки", on_click=self.back_to_settings, scale=1.2)], alignment=ft.MainAxisAlignment.SPACE_AROUND)
