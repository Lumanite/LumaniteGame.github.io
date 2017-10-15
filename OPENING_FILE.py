#OPENING FILE
from tkinter import *
from GUI_FILE import canvas, root
__name__ = "OPENING_FILE.py"


#Can't open logo.gif
PIlogo = PhotoImage(file="logo.gif")
LOGO = canvas.create_image(650, 380, image=PIlogo)

LLText = canvas.create_text(650, 100, fill="purple", text="Lumanite",
                            font=("Fixedsys", 72))
#IN CASE...
def hide(obj):
    canvas.itemconfigure(obj, state="hidden")

def show(obj):
    canvas.itemconfigure(obj, state="normal")
