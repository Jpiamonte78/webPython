import reflex as rx
import datetime
from webPython.styles.colors import TextColor as TextColor
from webPython.styles.colors import Color as Color


def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(src="favicon.ico"),    
            rx.text(f"Copyright {datetime.date.today().year}",color=TextColor.FOOTER.value),
            bg = Color.SECONDARY.value,
            width="100%"
        )
    )
