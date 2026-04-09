import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

layers = Layers()
keyboard.modules.append(layers)

keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.col_pins = (board.D4, board.D5, board.D6, board.D9, board.D8, board.D7)

keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.keymap = [

# Layer 0
[
KC.ESC, KC.Q, KC.W, KC.E, KC.R, KC.T,
KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G,
KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B,
KC.LCTRL, KC.LGUI, KC.LALT, KC.MO(1), KC.MO(2), KC.SPACE
],

# Layer 1 (Fn)
[
KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,
KC.TRNS, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.TRNS,
KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
KC.TRNS, KC.HOME, KC.END, KC.TRNS, KC.TRNS, KC.ENTER
],

# Layer 2
[
KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6,
KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
]

]


if __name__ == "__main__":
    keyboard.go()