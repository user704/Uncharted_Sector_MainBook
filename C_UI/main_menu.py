# main_menu.py

import flet as ft


class MainMenu:
    def __init__(self, page: ft.Page):
        self.page = page
        self.del_before()
        self.create_widgets()

    def deletee(self,e):
        self.page.add(ft.Text(value="Блять"))

    def del_before(self):
        self.page.clean()

    def create_widgets(self):
        b_style = ft.BorderSide(width=1, color='#171a1a')
        border = ft.Border(top=b_style, bottom=b_style, left=b_style, right=b_style)

        title_t = [
            ft.Text(value="Uncharted Sector",
                    color='#a5d1d1',
                    size=30,
                    weight=ft.FontWeight('bold')),

            ft.Text(value="Приложение для удобной и комфортной игры",
                    color='#a5d1d1',
                    size=10,
                    italic=True)
        ]

        menu_btns = [
            ft.OutlinedButton(text="Лист персонажа", scale=1.2),
            ft.OutlinedButton(text="а", scale=1.2, on_click=self.deletee),
            ft.OutlinedButton(text="Бестиарий", scale=1.2),
            ft.OutlinedButton(text="Бестиарий", scale=1.2),
            ft.OutlinedButton(text="Бестиарий", scale=1.2)
        ]

        menu_ctr = ft.Container()
        menu_ctr.padding = 10
        menu_ctr.margin = 0
        menu_ctr.border = border
        menu_ctr.bgcolor = '#426b6b'
        menu_ctr.border_radius = 10
        menu_ctr.height = 300
        menu_ctr.width = 300
        menu_ctr.content = ft.Column(title_t + [ft.Divider()] + menu_btns,
                                     horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        self.page.add(menu_ctr)
