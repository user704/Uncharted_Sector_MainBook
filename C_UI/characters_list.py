import flet as ft


class MainMenu:
    def __init__(self, page: ft.Page):
        self.page = page
        self.del_before()
        self.create_widgets()

    def del_before(self):
        self.page.clean()

    def exit_app(self, e):
        self.page.window.close()

    def create_widgets(self):
        self.page.title = "Uncharted Sector Main Menu"
        b_style = ft.BorderSide(width=1, color='#171a1a')
        border = ft.Border(top=b_style, bottom=b_style, left=b_style, right=b_style)

        #---Заголовок---
        title_t = ft.Column([
            ft.Text(value="Uncharted Sector",
                    color='#a5d1d1',
                    size=30,
                    weight=ft.FontWeight('bold')),

            ft.Text(value="Приложение для удобной и комфортной игры",
                    color='#a5d1d1',
                    size=10,
                    italic=True),

            ft.Divider()
        ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            height=80)

        #---Кнопки меню---
        menu_btns = ft.Column([
            ft.ElevatedButton(text="Лист персонажа", scale=1.2, width=170, color='#85c7c7'),
            ft.ElevatedButton(text="Главная книга", scale=1.2, width=170, color='#85c7c7'),
            ft.ElevatedButton(text="Настройки", scale=1.2, width=170, color='#85c7c7'),
            ft.ElevatedButton(text="Выйти", scale=1.2, width=170, color='#85c7c7', on_click=self.exit_app)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        #---Разметка---
        layout = ft.Column([title_t, menu_btns],
                           horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        #---Контейнер---
        menu_ctr = ft.Container()
        menu_ctr.padding = 10
        menu_ctr.margin = 0
        menu_ctr.border = border
        menu_ctr.bgcolor = '#426b6b'
        menu_ctr.border_radius = 10
        menu_ctr.height = 350
        menu_ctr.width = 300
        menu_ctr.content = layout

        self.page.add(menu_ctr)
