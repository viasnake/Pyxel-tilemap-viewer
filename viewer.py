import pyxel

class Main:
    def __init__(self):
        pyxel.init(256, 256, caption="Pyxel tilemap viewer", fps=30)
        pyxel.load('tm.pyxres', True, True, False, False)

        self.tm = 0
        self.tm_u = 0
        self.tm_v = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_W):
            self.tm_v -= 8
        if pyxel.btnp(pyxel.KEY_S):
            self.tm_v += 8
        if pyxel.btnp(pyxel.KEY_A):
            self.tm_u -= 8
        if pyxel.btnp(pyxel.KEY_D):
            self.tm_u += 8
        if pyxel.btnp(pyxel.KEY_0):
            self.tm = 0
            self.tm_u = 0
            self.tm_v = 0
        if pyxel.btnp(pyxel.KEY_1):
            self.tm = 1
            self.tm_u = 0
            self.tm_v = 0
        if pyxel.btnp(pyxel.KEY_2):
            self.tm = 2
            self.tm_u = 0
            self.tm_v = 0
        if pyxel.btnp(pyxel.KEY_3):
            self.tm = 3
            self.tm_u = 0
            self.tm_v = 0
        if pyxel.btnp(pyxel.KEY_4):
            self.tm = 4
            self.tm_u = 0
            self.tm_v = 0
        if pyxel.btnp(pyxel.KEY_5):
            self.tm = 5
            self.tm_u = 0
            self.tm_v = 0
        if pyxel.btnp(pyxel.KEY_6):
            self.tm = 6
            self.tm_u = 0
            self.tm_v = 0
        if pyxel.btnp(pyxel.KEY_7):
            self.tm = 7
            self.tm_u = 0
            self.tm_v = 0
        print("Current: " + str(self.tm_u) + ", " + str(self.tm_v) + "  Tilemap: " + str(self.tm))

    def draw(self):
        pyxel.cls(0)

        pyxel.bltm(0, 0, self.tm, self.tm_u, self.tm_v, 256, 256)
        pyxel.text(2, 2, "({0}, {1})".format(self.tm_u, self.tm_v), 7)

Main()