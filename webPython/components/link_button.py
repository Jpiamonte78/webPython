import reflex as rx

import webPython.styles.style as style

def link_button(title:str,body:str,url:str) ->rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon( 
                        tag="camera",
                        width=style.Spacer.BIG.value,
                        height = style.Spacer.BIG.value),
                rx.vstack(
                    rx.text(title,style=style.button_title_style),
                    rx.text(body,style=style.button_body_style)
                )
            )
        ),
        href = url,
        is_external = True,
        width = "100%"
    )