import reflex as rx
from webPython.components.link_button import link_button
from webPython.components.title import title
def links() ->rx.Component:
    return rx.vstack(
        title("Portafolio"),
        link_button("Codifer","Página web de codifer", "https://www.codifer.com"),
        link_button("Sanptec","Sitio web de sanptec","https://www.sanptec.com"),
        link_button("Coovestido","Sitio web de coovestido","https://www.coovestido.com"),
        link_button("Dra. Carol Ramirez","Sitio web Ortodoncia","https://www.dracarolramirez.com/"),
        width="100%"
    )