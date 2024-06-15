import reflex as rx 
import webPython.components.link_icon as link_icon



def header() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.avatar(fallback = "JP", size = "7", radius = "full"),
                rx.vstack(
                    rx.text("@jpiamontedev"),
                    rx.text("Hola Mi nombre es Jimmy Piamonte"),
                    link_icon.link_icon()
                )
            ),
            rx.text("""Soy Ingeniero de Sistemas, esta es mi primera web
                    desarrollada con Python""")
        )
    )
        