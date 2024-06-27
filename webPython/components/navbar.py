import reflex as rx
import webPython.styles.style as styles
from webPython.styles.colors import Color as Color

def navbar() ->rx.Component:
    return rx.hstack(
        rx.text("JimmyDev"),
        position="sticky",
        bg=Color.PRIMARY.value,
        padding_x=styles.Spacer.DEFAULT,
        padding_y=styles.Spacer.SMALL,
        z_index = "999",
        top = "0"
    )