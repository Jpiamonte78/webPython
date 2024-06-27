from enum import Enum
import reflex as rx
from .colors import Color as Color
from .colors import TextColor as TextColor
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
    "background_color": Color.BACKGROUND.value,
    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":Spacer.SMALL.value,
        "border_radius":Spacer.DEFAULT.value,
        "color":TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover":{
            "background_color": Color.SECONDARY.value
        }
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
    font_size = Spacer.DEFAULT.value,
    Color = TextColor.HEADER.value
)

button_body_style = dict(
    font_size = Spacer.MEDIUM.value,
    color = TextColor.BODY.value
)

