import reflex as rx 
import webPython.components.link_icon as link_icon
import webPython.styles.style as style
from webPython.styles.colors import TextColor as TextColor



def header() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.avatar(fallback = "JP", size = "7", radius = "full"),
                rx.vstack(
                    rx.text("@jpiamontedev",color=TextColor.HEADER.value),
                    rx.text("Hola Mi nombre es Jimmy Piamonte",color=TextColor.BODY.value),
                    rx.hstack(
                        link_icon.link_icon("https://www.facebook.com/jimmy.j.piamonte"),
                        link_icon.link_icon("https://www.instagram.com/jpiamonte"),
                        link_icon.link_icon("https://www.youtube.com/channel/UC2iKwxe6Aqgc49k5AXTig9A")
                    )
                    
                )
            ),
            rx.text("""Soy Ingeniero de Sistemas, esta es mi primera web
                    desarrollada con Python""",
                    color=TextColor.BODY.value),
            spacing="7"
        )
    )
        