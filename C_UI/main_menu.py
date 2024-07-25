import flet as ft
import time
import C_UI.MiniFunc.CoreFunctions as Core


class MainMenu:
    #---Выполняется при создании класса---
    def __init__(self, page: ft.Page, is_anim_from_start=True):
        self.page = page
        self.animations = Core.read_settings('animations')
        self.page.title = "Uncharted Sector: Main Menu"
        self.del_before()
        self.anim_start(is_anim_from_start)

    # ---Перед появлением все предыдущие меню стираются---
    def del_before(self):
        self.page.clean()

    #---Кнопка Выход---
    def exit_app(self, e):
        self.page.window.close()

    #---Главное меню --> Настройки---
    def to_settings(self, e):
        from C_UI.settings import Settings
        Settings(self.page)

    #---Создание кнопок и основного функционала---
    def create_btns(self):
        #---Заголовок---
        title_t = ft.Column([
            ft.Text(value="Uncharted Sector",
                    size=30,
                    weight=ft.FontWeight('bold')),

            ft.Text(value="Приложение для удобной и комфортной игры",
                    size=10,
                    italic=True),

            ft.Divider()
        ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            height=80)

        #---Кнопки меню---
        menu_btns = ft.Column([
            ft.OutlinedButton(text="Лист персонажа", scale=1.2, width=170),
            ft.OutlinedButton(text="Главная книга", scale=1.2, width=170),
            ft.OutlinedButton(text="Настройки", scale=1.2, width=170, on_click=self.to_settings),
            ft.OutlinedButton(text="Выйти", scale=1.2, width=170, on_click=self.exit_app)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            height=230)

        #---Вывод как переменная---
        return ft.Column([title_t, menu_btns], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # ---Спавн главного меню с анимацией---
    def anim_start(self, from_start=True):
        # ---Создание контейнера для дальнейших анимаций---
        def create_container():
            b_style = ft.BorderSide(width=1, color='cyan')
            border = ft.Border(top=b_style, bottom=b_style, left=b_style, right=b_style)

            return ft.Container(padding=10, margin=0, border=border)

        # ---Анимация если меню вызвано с нуля---
        def anim_from_start():
            # ---Начальные параметры контейнера---
            container = create_container()
            container.border_radius = 40
            container.height = 40
            container.width = 40
            container.animate_opacity = ft.animation.Animation(500, curve=ft.AnimationCurve.EASE)
            container.opacity = 0
            container.animate = ft.animation.Animation(300, curve=ft.AnimationCurve.EASE)
            self.page.add(container)

            # ---Появление---
            time.sleep(0.3)
            container.opacity = 1
            self.page.update()

            # ---Анимация ширины---
            time.sleep(0.5)
            container.width = 300
            container.border_radius = 10
            self.page.update()

            # ---Анимация высоты---
            time.sleep(0.3)
            container.height = 350
            self.page.update()

            # ---Анимация появления кнопок---
            btns = self.create_btns()
            btns.animate_opacity = ft.animation.Animation(500, curve=ft.AnimationCurve.EASE)
            btns.opacity = 0
            container.content = btns
            self.page.update()
            time.sleep(0.2)
            btns.opacity = 1
            self.page.update()

        def anim_not_from_start():
            # ---Начальные параметры контейнера---
            container = create_container()
            container.border_radius = 10
            container.height = 350
            container.width = 300
            self.page.add(container)

            # ---Анимация появления кнопок---
            btns = self.create_btns()
            btns.animate_opacity = ft.animation.Animation(500, curve=ft.AnimationCurve.EASE)
            btns.opacity = 0
            container.content = btns
            self.page.update()
            time.sleep(0.1)
            btns.opacity = 1
            self.page.update()

        if self.animations:
            if from_start:
                anim_from_start()
            else:
                anim_not_from_start()
        else:
            container = create_container()
            container.height = 350
            container.width = 300
            container.border_radius = 10
            btns = self.create_btns()
            container.content = btns
            self.page.add(container)