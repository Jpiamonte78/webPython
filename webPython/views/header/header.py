import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback = "Jimmy Piamonte", size = "9", radius = "full"),
        rx.text("@jpiamontedev"),
        rx.text("Hola Mi nombre es Jimmy Piamonte"),
        rx.text("""Soy Ingeniero de Sistemas, esta es mi primera web
                desarrollada con Python""")
    )