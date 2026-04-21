import flet as ft
from db.main import init
from db.queries import add_product, get_products, update_product, delete_product

def main(page: ft.Page):
    page.title = "Список покупок"
    
    init()

    input_field = ft.TextField(label="Новый товар")
    list_view = ft.Column()

    sort_type = ft.Dropdown(
        options=[
            ft.dropdown.Option("all", "Все"),
            ft.dropdown.Option("done", "Купленные"),
            ft.dropdown.Option("not_done", "Не купленные")
        ],
        value="all"
    )

    def load_products():
        list_view.controls.clear()
        products = get_products()

        for product in products:
            id, name, done = product

            if sort_type.value == "done" and not done:
                continue
            if sort_type.value == "not_done" and done:
                continue

            checkbox = ft.Checkbox(
                label=name,
                value=bool(done),
                on_change=lambda e, id=id:
                    toggle_done(id, e.control.value)
            )

            delete_btn = ft.IconButton(
                icon=ft.Icons.DELETE,
                on_click=lambda e, id=id:
                    delete(id)
            )

            row = ft.Row([checkbox, delete_btn])
            list_view.controls.append(row)

        page.update()


    def toggle_done(id, value):
        update_product(id, int(value))
        load_products()


    def delete(id):
        delete_product(id)
        load_products()


    def add(e):
        if input_field.value:
            add_product(input_field.value)
            input_field.value = ""
            load_products()


    add_btn = ft.ElevatedButton("Add", on_click=add)

    sort_type.on_change = lambda e: load_products()

    page.add(
        ft.Text("Список покупок", size=30),
        input_field,
        add_btn,
        sort_type,
        list_view
    )

    load_products()


ft.app(target=main)