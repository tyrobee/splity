import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

layers = Layers()
keyboard.modules.append(layers)

keyboard.row_pins = (
    board.D0,
    board.D1,
    board.D2,
    board.D3
)

keyboard.col_pins = (
    board.D4,
    board.D5,
    board.D6,
    board.D7,
    board.D8,
    board.D9
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW
# KEYMAP
keyboard.debug_enabled = True

keyboard.keymap = [
# Layer 0
[
KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC,
KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT,
KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLSH, KC.ENT,
KC.SPC, KC.MO(1), KC.MO(2), KC.GRV, KC.MINS, KC.NO
],
# Layer 1 (symbols/navigation)
[
KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.K0,
KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.NO, KC.NO,
KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
],

# Layer 2 (function keys)
[
KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6,
KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
]

]


if __name__ == "__main__":
    keyboard.go()