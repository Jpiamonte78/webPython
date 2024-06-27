import reflex as rx
import webPython.styles.style as style
from webPython.styles.colors import TextColor as TextColor

def title(text:str) ->rx.Component:
    return rx.heading(
        text,
        style = style.title_style,
        color = TextColor.HEADER.value,
        _as="h2"
    )
