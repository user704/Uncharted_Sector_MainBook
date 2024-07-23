import flet as ft


# ЛИСТ ВИЕВ

class Settings:

    # ---Инициализация класса---
    def __init__(self, page: ft.Page):
        self.page = page
        self.del_before()
        self.create_widgets()

    #---Удаление предыдущего окна---
    def del_before(self):
        self.page.clean()

    #---Переключение темы---
    def change_theme(self, e):
        if self.page.theme_mode == 'light':
            self.page.theme_mode = 'dark'
        else:
            self.page.theme_mode = 'light'
        self.page.update()

    #---Настройки --> Главное меню---
    def back_to_menu(self, e):
        from C_UI.main_menu import MainMenu
        MainMenu(self.page)

    # ---Создание виджетов---
    def create_widgets(self):
        self.page.title = "Uncharted Sector: Settings"
        b_style = ft.BorderSide(width=1, color='#171a1a')
        border = ft.Border(top=b_style, bottom=b_style, left=b_style, right=b_style)

        #---Список настроек---
        w_change_theme = ft.Row([ft.Text("Тема", scale=1.2),
                                 ft.IconButton(
                                     icon=ft.icons.SUNNY if self.page.theme_mode == 'light' else ft.icons.DARK_MODE,
                                     on_click=self.change_theme)], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

        settings_list = ft.ListView(
            [
                w_change_theme,
                ft.Divider(opacity=0.3, color='black'),
                w_change_theme,
                ft.Divider(opacity=0.3, color='black')
            ], height=520, padding=20
        )

        #---Нижняя панель---
        bottom_row = ft.Row([
            ft.ElevatedButton(text="В главное меню",
                              scale=1.2,
                              width=170,
                              color='#85c7c7',
                              on_click=self.back_to_menu)
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND)

        #---Контейнер---
        menu_ctr = ft.Container()
        menu_ctr.padding = 10
        menu_ctr.margin = 0
        menu_ctr.border = border
        menu_ctr.bgcolor = '#426b6b'
        menu_ctr.border_radius = 10
        menu_ctr.height = 600
        menu_ctr.width = 1000
        menu_ctr.content = ft.Column([settings_list, bottom_row], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.page.add(menu_ctr)
