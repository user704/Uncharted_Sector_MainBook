import flet as ft


class Settings:

    # ---Инициализация класса---
    def __init__(self, page: ft.Page):
        self.page = page
        self.del_before()
        self.create_widgets()

    #---Удаление предыдущего окна---
    def del_before(self):
        self.page.clean()

    #---Сохранение настройки в файл---
    def save_to_file(self, key, value):
        from os import path
        file_path = path.abspath(path.dirname(__file__))
        file_path = path.join(file_path, '..', "Data", "settings.json")

        import json
        with open(file_path, 'w', encoding='UTF-8') as file:
            json.dump({key : value}, file)

    #---Переключение темы---
    def change_theme(self, e):
        if self.page.theme_mode == 'light':
            self.page.theme_mode = 'dark'
        else:
            self.page.theme_mode = 'light'
        self.page.update()
        self.save_to_file('theme_mode', value= self.page.theme_mode)

    #---Настройки --> Главное меню---
    def back_to_menu(self, e):
        from C_UI.main_menu import MainMenu
        MainMenu(self.page)

    # ---Создание виджетов---
    def create_widgets(self):

        def section_title(title=''):
            row = ft.Row([ft.Text(title)], alignment=ft.MainAxisAlignment.CENTER)

            return [ft.Divider(), row, ft.Divider()]

        def settings_switch(name='', current_value=False, event=None):
            text = ft.Text(name, scale=1.2, text_align=ft.TextAlign.CENTER, offset=ft.Offset(x=0.15, y=0))
            switch = ft.Switch(value=current_value, on_change=event)
            row = ft.Row([text, switch], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

            return [row, ft.Divider()]

        self.page.title = "Uncharted Sector: Settings"
        b_style = ft.BorderSide(width=1, color='cyan')
        border = ft.Border(top=b_style, bottom=b_style, left=b_style, right=b_style)

        settings_list = ft.ListView(
            section_title('Визуальные настройки') +
            settings_switch(name="Тёмная / Светлая тема",
                            current_value=self.page.theme_mode == 'light',
                            event=self.change_theme)
            , height=520, padding=0
        )

        #---Нижняя панель---
        bottom_row = ft.Row([
            ft.OutlinedButton(text="В главное меню",
                              scale=1.2,
                              width=170,
                              on_click=self.back_to_menu)
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND)

        #---Контейнер---
        menu_ctr = ft.Container()
        menu_ctr.padding = 10
        menu_ctr.margin = 0
        menu_ctr.border = border
        menu_ctr.border_radius = 10
        menu_ctr.height = 600
        menu_ctr.width = 1000
        menu_ctr.content = \
            ft.Column(controls=[settings_list, bottom_row],
                      horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.page.add(menu_ctr)
