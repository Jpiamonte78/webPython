import reflex as rx
import webPython.styles.style as style

def title(text:str) ->rx.Component:
    return rx.heading(
        text,
        style = style.title_style,
        _as="h2"
    )
