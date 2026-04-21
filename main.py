import flet as ft

def main(page: ft.Page):
    page.title = "Список покупок"

    items = []

    input_field = ft.TextField(label="Введите товар")

    list_view = ft.Column()

    def add_item(e):
        if input_field.value == "":
            return
        
        item = {
            "name": input_field.value,
            "done": False
        }

        items.append(item)

        update_list()
        input_field.value = ""
        page.update()

    def delete_item(item):
        items.remove(item)
        update_list()
        page.update()

    def toggle_done(e, item):
        item["done"] = e.control.value
        update_list()
        page.update()

    def update_list():
        list_view.controls.clear()

        for item in items:
            list_view.controls.append(
                ft.Row([
                    ft.Checkbox(
                        value=item["done"],
                        on_change=lambda e, i=item: toggle_done(e, i)
                    ),
                    ft.Text(item["name"]),
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        on_click=lambda e, i=item: delete_item(i)
                    )
                ])
            )

    add_button = ft.ElevatedButton("ADD", on_click=add_item)

    page.add(
        input_field,
        add_button,
        list_view
    )

ft.app(target=main)