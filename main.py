import flet as ft

from db.main_db import init_db
from db.queries import add_product, get_products, toggle_done, delete_product


def main(page: ft.Page):
    page.title = "Список покупок"
    page.window_width = 400
    page.window_height = 600

    init_db()

    name_input = ft.TextField(label="Товар")
    qty_input = ft.TextField(label="Количество", value="1")
    list_view = ft.Column()
    counter = ft.Text("Куплено: 0")

    current_filter = {"value": "all"}

    def load_products():
        list_view.controls.clear()
        products = get_products()
        done_count = 0

        for p in products:
            pid, name, qty, done = p

            if done:
                done_count += 1

            if current_filter["value"] == "done" and not done:
                continue
            if current_filter["value"] == "not_done" and done:
                continue

            def change(e, pid=pid):
                toggle_done(pid, e.control.value)
                load_products()

            def remove(e, pid=pid):
                delete_product(pid)
                load_products()

            row = ft.Row([
                ft.Checkbox(value=bool(done), on_change=change),
                ft.Text(f"{name} ({qty})"),
                ft.IconButton(ft.Icons.DELETE, on_click=remove)
            ])

            list_view.controls.append(row)

        counter.value = f"Куплено: {done_count}"
        list_view.update()
        counter.update()

    def set_filter(value):
        current_filter["value"] = value
        load_products()

    btn_all = ft.ElevatedButton("Все", on_click=lambda e: set_filter("all"))
    btn_done = ft.ElevatedButton("Купленные", on_click=lambda e: set_filter("done"))
    btn_not_done = ft.ElevatedButton("Не купленные", on_click=lambda e: set_filter("not_done"))

    def add(e):
        if name_input.value:
            add_product(name_input.value, int(qty_input.value or 1))
            name_input.value = ""
            qty_input.value = "1"
            name_input.update()
            qty_input.update()
            load_products()

    add_btn = ft.ElevatedButton("Добавить", on_click=add)

    page.add(
        ft.Row([name_input, qty_input, add_btn]),
        ft.Row([btn_all, btn_done, btn_not_done]),
        counter,
        list_view
    )

    load_products()


ft.app(target=main)