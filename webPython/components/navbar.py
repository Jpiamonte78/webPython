import reflex as rx
import webPython.styles.style as styles

def navbar() ->rx.Component:
    return rx.hstack(
        rx.text("JimmyDev"),
        position="sticky",
        bg="lightblue",
        padding_x=styles.Spacer.DEFAULT,
        padding_y=styles.Spacer.SMALL,
        z_index = "999",
        top = "0"
        
    )