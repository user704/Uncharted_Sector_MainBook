import flet as ft
from screeninfo import get_monitors


def main(page: ft.Page):
    #---Настройки окна---
    page.title = "Uncharted Sector Main Book"
    page.theme_mode = 'dark'
    page.window.width = get_monitors()[0].width / 1.25
    page.window.height = get_monitors()[0].height / 1.35
    page.window.alignment = ft.Alignment(0, 0)
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = True

    border = ft.Border(top=ft.BorderSide(width=1, color='#171a1a'),
                       bottom=ft.BorderSide(width=1, color='#171a1a'),
                       left=ft.BorderSide(width=1, color='#171a1a'),
                       right=ft.BorderSide(width=1, color='#171a1a')
                       )
    page.add(
        ft.Row(
            [
                ft.Container(
                    padding=10,
                    border=border,
                    bgcolor='#426b6b',
                    border_radius=10,
                    content=ft.Column(
                        [
                            ft.Text("Uncharted Sector"),
                            ft.ElevatedButton("Лист персонажа"),
                            ft.ElevatedButton("Правила"),
                            ft.ElevatedButton("Бестиарий"),
                            ft.Row([ft.IconButton(icon=ft.icons.SETTINGS), ft.IconButton(icon=ft.icons.TURNED_IN)],
                                   alignment=ft.MainAxisAlignment.SPACE_AROUND)
                        ], alignment=ft.MainAxisAlignment.CENTER
                    )
                )
            ]
        )
    )


ft.app(target=main)
