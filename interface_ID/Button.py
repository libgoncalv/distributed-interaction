import pickle
import json
import os
import time

PERIODE = 1*60

class Button:
  def __init__(self, x, y, r, txt, c, f):
    self.pos = PVector(x, y)
    self.radius = r
    self.caption = txt
    self.col = c
    self.filename = f
    self.visible = True
    self.clicked = False

  def show(self, mouseX, mouseY):
    if(self.isOver(mouseX, mouseY)):
        fill(155)
    else:
        if(not os.path.isfile(self.filename)):
            fill(color(0, 0, 0))
        else:
            stat = os.stat(self.filename)
            if(stat.st_mtime + PERIODE < time.time()):
                fill(color(255, 0, 0))
            else:
                fill(self.col)
    strokeWeight(1)
    ellipse(self.pos.x, self.pos.y, self.radius * 2, self.radius * 2)
    fill(0)
    fontSize = self.radius * 0.33
    textSize(fontSize)
    tw = textWidth(self.caption)
    tx = self.pos.x - (tw/2)
    ty = self.pos.y + (fontSize / 2)
    text(self.caption, tx, ty)
    
    if(self.clicked and os.path.isfile(self.filename)):
        with open(self.filename, "rb") as f:
            config = json.loads(pickle.load(f))
        s = ""
        if "nombre" in config:
            for capteur in range(config["nombre"]):
                s = s + "Type : %s\nLocalisation : %s\nMoyenne : %s\n\n" % (config["type"][capteur], config["localisation"][capteur], config["moyenne"][capteur])
        else:
            for key in config:
                s = s + "%s : %s\n" % (key, config[key])
        textSize(20)
        fill(250)
        rect(820, 20, 360, 660)
        fill(0)
        text(s, 840, 60)

  def isOver(self, mouseX, mouseY):
    distX = self.pos.x - mouseX
    distY = self.pos.y - mouseY
    return sqrt(distX*distX + distY*distY) <= self.radius
