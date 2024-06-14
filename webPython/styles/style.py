from enum import Enum
import reflex as rx
# Constantes
MAX_WIDTH = "550px"

#Tamaños
class Spacer(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"

#estilos base
BASE_STYLE = {
    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":Spacer.SMALL.value,
        "border_radius":Spacer.DEFAULT.value
    },
    rx.link:{
        "text_decoration":"none",
        "_hover":{}
    }
    
}

title_style=dict(
    size = "md",
    width = "100%",
    padding_top = Spacer.DEFAULT.value
)
button_title_style=dict(
    font_size = Spacer.DEFAULT.value
)

button_body_style = dict(
    font_size = Spacer.MEDIUM.value
)

