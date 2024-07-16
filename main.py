import flet as ft
import os

def create_section(title: str, file_name: str):
    file_path = os.path.join(os.path.dirname(__file__), title, f"{file_name}.txt")

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return ft.Column(
            controls=[
                ft.Text(title, size=24, weight="bold"),
                ft.Divider(),
                #ft.Markdown(content)
            ]
        )
    else:
        return ft.Text("Ошибка - файл не найден", color="red")

def main(page: ft.Page):
    page.title = "Uncharted Sector"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(create_section("Введение", "Введение"))
    page.scroll = "AUTO"
    page.update()


ft.app(target=main)
