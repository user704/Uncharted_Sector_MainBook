import flet as ft
import os
import time


def edit_typewriter(r, d_time=0.1, text=""):

    while r.value != text:
        past_text = r.value
        for char in past_text:
            if char != " ":
                r.value = r.value.replace(char, "  ", 1)
                r.page.update()
                time.sleep(0.1)
            else:
                break
        for char in r.value:
            if char == " ":
                r.value = r.value[1:]
                time.sleep(0.01)
            else:
                break



def create_section(title: str, file_name: str):
    file_path = os.path.join(os.path.dirname(__file__), "Resources", title, f"{file_name}.md")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return ft.Markdown(content, selectable=True)
    else:
        return ft.Text("Ошибка - файл не найден", color="red")


def main(page: ft.Page):
    page.title = "Uncharted Sector"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text = create_section("Введение", "Введение")
    page.add(text)
    page.scroll = "AUTO"

    file_path = os.path.join(os.path.dirname(__file__), "Resources", "Введение", f"{Введение_без_воды}.md")
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    button = ft.ElevatedButton("Запустить анимацию", on_click=lambda _: edit_typewriter(text, d_time=2, text=content))
    button.bgcolor = "blue"
    button.color = "white"
    button.alignment = ft.MainAxisAlignment.START
    button.z_index = 1
    page.add(button)
    page.update()


ft.app(target=main)
