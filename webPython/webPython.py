"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import webPython.styles.style as styles
from rxconfig import config
from webPython.components.navbar import navbar
from webPython.views.header.header import header
from webPython.views.links.links import links
from webPython.components.footer import footer

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width = "100%",
                margin_y=styles.Spacer.BIG
            )
        ),
        footer()
    )
    
    
   

app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)

