import os
import flet as ft


def create_section(title: str, file_name: str):
    """
    Создает раздел книги с заданным названием и содержимым из файла.

    Args:
        title (str): Название раздела.
        file_name (str): Имя файла в папке "Book".
    """
    book_dir = os.path.join(os.path.dirname(__file__), "Book")
    file_path = os.path.join(book_dir, f"{file_name}.txt")

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        section = ft.Column(
            controls=[
                ft.Text(title, size=24, weight="bold"),
                ft.Divider(),
                ft.Markdown(content)
            ]
        )
        return section
    else:
        return ft.Text("Ошибка - файл не найден", color="red")


def main(page: ft.Page):
    page.title = "Uncharted Sector"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    section = create_section("Введение", "Введение")
    page.add(section)


ft.app(target=main)
