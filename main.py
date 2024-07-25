import flet as ft
from screeninfo import get_monitors


def main(page: ft.Page):
    page.window.width = get_monitors()[0].width / 1.4
    page.window.height = get_monitors()[0].height / 1.4
    page.window.alignment = ft.Alignment(0, 0)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    import C_UI.MiniFunc.CoreFunctions as Core
    theme = Core.read_settings('theme_mode')
    if theme is not None:
        page.theme_mode = theme

    from C_UI.main_menu import MainMenu
    MainMenu(page)


ft.app(target=main)
