import flet as ft
from screeninfo import get_monitors


def main(page: ft.Page):
    page.window.width = get_monitors()[0].width / 1.4
    page.window.height = get_monitors()[0].height / 1.4
    page.window.alignment = ft.Alignment(0, 0)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(ft.Container(bgcolor='yellow', width=100, height=100),
             ft.Container(bgcolor='blue', width=100, height=100),ft.Container(bgcolor='yellow', width=100, height=100),
             ft.Container(bgcolor='blue', width=100, height=100),ft.Container(bgcolor='yellow', width=100, height=100),
             ft.Container(bgcolor='blue', width=100, height=100))


ft.app(target=main)
