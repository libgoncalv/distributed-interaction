from Button import Button
import pickle

foyer = Button(351, 131, 15, "", color(0, 255, 0), "../foyer.ser")
bureau19 = Button(137, 281, 15, "", color(0, 255, 0), "../bureau19.ser")
slot = Button(100, 573, 15, "", color(0, 255, 0), "../meteo.ser")

def setup():
    global img
    size(800, 700)
    img = loadImage("upssitech.png")
    img.resize(800, 700)
    image(img, 0, 0)
    foyer.show(mouseX, mouseY)
    bureau19.show(mouseX, mouseY)
    slot.show(mouseX, mouseY)

def draw():
    image(img, 0, 0)
    foyer.show(mouseX, mouseY)
    bureau19.show(mouseX, mouseY)
    slot.show(mouseX, mouseY)
    
def mousePressed():
    if(foyer.isOver(mouseX, mouseY)):
        if(foyer.clicked):
            this.surface.setSize(800, 700)
        else:
            this.surface.setSize(1200, 700)
        foyer.clicked = not foyer.clicked
        bureau19.clicked = False
        slot.clicked = False
    elif(bureau19.isOver(mouseX, mouseY)):
        if(bureau19.clicked):
            this.surface.setSize(800, 700)
        else:
            this.surface.setSize(1200, 700)
        bureau19.clicked = not bureau19.clicked
        foyer.clicked = False
        slot.clicked = False
    elif(slot.isOver(mouseX, mouseY)):
        if(slot.clicked):
            this.surface.setSize(800, 700)
        else:
            this.surface.setSize(1200, 700)
        slot.clicked = not slot.clicked
        foyer.clicked = False
        bureau19.clicked = False
