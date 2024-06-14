import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.hstack(
        rx.text(f"Copyright {datetime.date.today().year}"),
        rx.image(src="favicon.ico")
    )