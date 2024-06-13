import reflex as rx

def navbar() ->rx.Component:
    return rx.hstack(
        rx.text("JimmyDev",height="40px"),
        position="sticky",
        bg="blue",
        padding="16px",
        z_index = "999"
    )