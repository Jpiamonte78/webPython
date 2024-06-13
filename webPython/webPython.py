"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from webPython.components.navbar import navbar
from webPython.views.header.header import header


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.vstack(
            navbar(),
            header(),
            width="100%"    
        )
   

app = rx.App()
app.add_page(index)
