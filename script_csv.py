import numpy as np 
import pyautogui as auto 
import keyboard 
import os 
from pynput.mouse import Button, Controller 
def main(): 
    def endProgram(): 
        keyboard.unhook_all_hotkeys() 
        print('Ending program in between') 
        os._exit(0) 
    keyboard.add_hotkey('Esc+q', endProgram,suppress=True) 
    mouse = Controller() 
    auto.moveTo( x=1820.1171875, y=11.1953125,duration=1.0) 
    auto.sleep(1.0) 
    auto.mouseDown(button='left', x=1820.1171875, y=11.1953125, duration = 2) 
    auto.moveTo( x=1820.1171875, y=11.1953125,duration=1.142071008682251) 
    auto.mouseUp(button='left', x=1820.1171875, y=11.1953125, duration = 0.14207100868225098) 
    keyboard.press("f") 
    auto.sleep(1.0) 
    keyboard.release("f") 
    auto.sleep(1.0) 
    keyboard.press("i") 
    auto.sleep(1.0) 
    keyboard.release("i") 
    auto.sleep(1.0) 
    keyboard.press("n") 
    auto.sleep(1.0) 
    keyboard.release("n") 
    auto.sleep(1.0) 
    keyboard.press("d") 
    auto.sleep(1.0) 
    keyboard.release("d") 
    auto.sleep(1.0) 
    keyboard.press("e") 
    auto.sleep(1.0) 
    keyboard.press("r") 
    auto.sleep(1.0) 
    keyboard.release("e") 
    auto.sleep(1.0) 
    keyboard.release("r") 
    auto.sleep(1.0) 
    keyboard.press("enter") 
    auto.sleep(1.0) 
    keyboard.release("enter") 
    auto.sleep(1.0) 
    auto.moveTo( x=913.3125, y=555.4921875,duration=5.129266262054444) 
    auto.mouseDown(button='left', x=913.3125, y=555.4921875, duration = 4.129266262054444) 
    auto.moveTo( x=913.3125, y=555.91015625,duration=1.2527947425842285) 
    auto.moveTo( x=913.3125, y=555.91015625,duration=0.01) 
    auto.moveTo( x=913.3125, y=556.19921875,duration=0.01) 
    auto.moveTo( x=913.3125, y=558.3828125,duration=0.01) 
    auto.moveTo( x=913.3125, y=559.1328125,duration=0.01) 
    auto.moveTo( x=913.3125, y=559.8828125,duration=0.01) 
    auto.moveTo( x=913.3125, y=561.26171875,duration=0.01) 
    auto.moveTo( x=913.76953125, y=562.640625,duration=0.01) 
    auto.moveTo( x=914.3125, y=564.82421875,duration=0.01) 
    auto.moveTo( x=915.40234375, y=567.0078125,duration=0.01) 
    auto.moveTo( x=915.9453125, y=569.19140625,duration=0.01) 
    auto.moveTo( x=916.48828125, y=571.375,duration=0.01) 
    auto.moveTo( x=917.03125, y=573.55859375,duration=0.01) 
    auto.moveTo( x=918.12109375, y=575.7421875,duration=0.01) 
    auto.moveTo( x=918.578125, y=577.12109375,duration=0.01) 
    auto.moveTo( x=919.03515625, y=578.5,duration=0.01) 
    auto.moveTo( x=919.4921875, y=579.87890625,duration=0.01) 
    auto.moveTo( x=919.94921875, y=581.2578125,duration=0.01) 
    auto.moveTo( x=920.8671875, y=582.63671875,duration=0.01) 
    auto.moveTo( x=921.2421875, y=583.38671875,duration=0.01) 
    auto.moveTo( x=921.6171875, y=584.13671875,duration=0.01) 
    auto.moveTo( x=922.07421875, y=585.515625,duration=0.01) 
    auto.moveTo( x=922.44921875, y=586.265625,duration=0.01) 
    auto.moveTo( x=922.82421875, y=587.015625,duration=0.01) 
    auto.moveTo( x=923.19921875, y=587.765625,duration=0.01) 
    auto.moveTo( x=923.57421875, y=588.515625,duration=0.01) 
    auto.moveTo( x=923.94921875, y=589.265625,duration=0.01) 
    auto.moveTo( x=924.40625, y=590.64453125,duration=0.01) 
    auto.moveTo( x=924.78125, y=591.39453125,duration=0.01) 
    auto.moveTo( x=925.0703125, y=591.68359375,duration=0.01) 
    auto.moveTo( x=925.4453125, y=592.43359375,duration=0.01) 
    auto.moveTo( x=925.734375, y=592.72265625,duration=0.01) 
    auto.moveTo( x=926.109375, y=593.47265625,duration=0.01) 
    auto.moveTo( x=926.484375, y=594.22265625,duration=0.01) 
    auto.moveTo( x=926.859375, y=594.97265625,duration=0.01) 
    auto.moveTo( x=927.1484375, y=595.26171875,duration=0.01) 
    auto.moveTo( x=927.4375, y=595.55078125,duration=0.01) 
    auto.moveTo( x=927.8125, y=596.30078125,duration=0.01) 
    auto.moveTo( x=928.1015625, y=596.58984375,duration=0.01) 
    auto.moveTo( x=928.390625, y=596.87890625,duration=0.01) 
    auto.moveTo( x=928.6796875, y=597.16796875,duration=0.01) 
    auto.moveTo( x=928.96875, y=597.45703125,duration=0.01) 
    auto.moveTo( x=928.96875, y=597.74609375,duration=0.01) 
    auto.moveTo( x=929.2578125, y=598.03515625,duration=0.01) 
    auto.moveTo( x=929.546875, y=598.32421875,duration=0.01) 
    auto.moveTo( x=929.8359375, y=598.61328125,duration=0.01) 
    auto.moveTo( x=930.125, y=598.90234375,duration=0.01) 
    auto.moveTo( x=930.875, y=599.27734375,duration=0.01) 
    auto.moveTo( x=931.625, y=599.65234375,duration=0.01) 
    auto.moveTo( x=933.00390625, y=600.5703125,duration=0.01) 
    auto.moveTo( x=933.37890625, y=601.3203125,duration=0.01) 
    auto.moveTo( x=934.12890625, y=601.6953125,duration=0.01) 
    auto.moveTo( x=935.765625, y=603.33203125,duration=0.01) 
    auto.moveTo( x=936.515625, y=604.08203125,duration=0.01) 
    auto.moveTo( x=937.265625, y=604.45703125,duration=0.01) 
    auto.moveTo( x=938.015625, y=605.20703125,duration=0.01) 
    auto.moveTo( x=938.765625, y=605.95703125,duration=0.01) 
    auto.moveTo( x=939.140625, y=606.70703125,duration=0.01) 
    auto.moveTo( x=939.890625, y=607.08203125,duration=0.01) 
    auto.moveTo( x=940.640625, y=607.83203125,duration=0.01) 
    auto.moveTo( x=941.390625, y=608.58203125,duration=0.01) 
    auto.moveTo( x=942.140625, y=609.33203125,duration=0.01) 
    auto.moveTo( x=942.890625, y=609.70703125,duration=0.01) 
    auto.moveTo( x=943.640625, y=610.45703125,duration=0.01) 
    auto.moveTo( x=945.01953125, y=610.9140625,duration=0.01) 
    auto.moveTo( x=945.76953125, y=611.6640625,duration=0.01) 
    auto.moveTo( x=947.1484375, y=612.58203125,duration=0.01) 
    auto.moveTo( x=947.8984375, y=613.33203125,duration=0.01) 
    auto.moveTo( x=949.27734375, y=614.25,duration=0.01) 
    auto.moveTo( x=950.02734375, y=615.0,duration=0.01) 
    auto.moveTo( x=950.77734375, y=615.75,duration=0.01) 
    auto.moveTo( x=951.52734375, y=616.5,duration=0.01) 
    auto.moveTo( x=952.27734375, y=617.25,duration=0.01) 
    auto.moveTo( x=953.02734375, y=618.0,duration=0.01) 
    auto.moveTo( x=953.77734375, y=618.75,duration=0.01) 
    auto.moveTo( x=954.5234375, y=619.49609375,duration=0.01) 
    auto.moveTo( x=955.2734375, y=620.24609375,duration=0.01) 
    auto.moveTo( x=956.0234375, y=620.99609375,duration=0.01) 
    auto.moveTo( x=956.94140625, y=622.375,duration=0.01) 
    auto.moveTo( x=957.69140625, y=623.125,duration=0.01) 
    auto.moveTo( x=958.609375, y=624.50390625,duration=0.01) 
    auto.moveTo( x=959.359375, y=625.25390625,duration=0.01) 
    auto.moveTo( x=960.27734375, y=626.6328125,duration=0.01) 
    auto.moveTo( x=961.9140625, y=628.26953125,duration=0.01) 
    auto.moveTo( x=963.55078125, y=629.90625,duration=0.01) 
    auto.moveTo( x=964.46875, y=631.28515625,duration=0.01) 
    auto.moveTo( x=965.84765625, y=632.203125,duration=0.01) 
    auto.moveTo( x=968.37109375, y=634.09375,duration=0.01) 
    auto.moveTo( x=970.0078125, y=635.73046875,duration=0.01) 
    auto.moveTo( x=972.53125, y=637.62109375,duration=0.01) 
    auto.moveTo( x=975.0546875, y=639.51171875,duration=0.01) 
    auto.moveTo( x=977.578125, y=642.03515625,duration=0.01) 
    auto.moveTo( x=980.1015625, y=643.92578125,duration=0.01) 
    auto.moveTo( x=982.625, y=646.44921875,duration=0.01) 
    auto.moveTo( x=985.1484375, y=648.97265625,duration=0.01) 
    auto.moveTo( x=987.0390625, y=651.49609375,duration=0.01) 
    auto.moveTo( x=989.5625, y=653.38671875,duration=0.01) 
    auto.moveTo( x=991.19921875, y=655.0234375,duration=0.01) 
    auto.moveTo( x=993.08984375, y=657.546875,duration=0.01) 
    auto.moveTo( x=993.83984375, y=658.296875,duration=0.01) 
    auto.moveTo( x=994.7578125, y=659.67578125,duration=0.01) 
    auto.moveTo( x=995.046875, y=659.96484375,duration=0.01) 
    auto.moveTo( x=995.421875, y=660.71484375,duration=0.01) 
    auto.moveTo( x=995.7109375, y=661.00390625,duration=0.01) 
    auto.moveTo( x=996.0, y=661.29296875,duration=0.01) 
    auto.moveTo( x=996.2890625, y=661.58203125,duration=0.01) 
    auto.moveTo( x=996.2890625, y=661.87109375,duration=0.01) 
    auto.moveTo( x=996.2890625, y=662.09765625,duration=0.01) 
    auto.moveTo( x=996.578125, y=662.09765625,duration=0.01) 
    auto.moveTo( x=996.578125, y=662.38671875,duration=0.01) 
    auto.moveTo( x=996.578125, y=662.67578125,duration=0.01) 
    auto.moveTo( x=996.578125, y=662.96484375,duration=0.01) 
    auto.moveTo( x=996.578125, y=663.25390625,duration=0.01) 
    auto.moveTo( x=996.578125, y=663.54296875,duration=0.01) 
    auto.moveTo( x=996.8671875, y=663.83203125,duration=0.01) 
    auto.moveTo( x=996.8671875, y=664.58203125,duration=0.01) 
    auto.moveTo( x=996.8671875, y=664.87109375,duration=0.01) 
    auto.moveTo( x=996.8671875, y=665.62109375,duration=0.01) 
    auto.moveTo( x=996.8671875, y=666.37109375,duration=0.01) 
    auto.moveTo( x=996.8671875, y=666.66015625,duration=0.01) 
    auto.moveTo( x=997.2421875, y=667.41015625,duration=0.01) 
    auto.moveTo( x=997.2421875, y=668.7890625,duration=0.01) 
    auto.moveTo( x=997.2421875, y=669.5390625,duration=0.01) 
    auto.moveTo( x=997.2421875, y=670.91796875,duration=0.01) 
    auto.moveTo( x=997.2421875, y=672.296875,duration=0.01) 
    auto.moveTo( x=997.2421875, y=673.67578125,duration=0.01) 
    auto.moveTo( x=997.2421875, y=675.859375,duration=0.01) 
    auto.moveTo( x=997.2421875, y=677.23828125,duration=0.01) 
    auto.moveTo( x=997.2421875, y=679.421875,duration=0.01) 
    auto.moveTo( x=997.2421875, y=681.60546875,duration=0.01) 
    auto.moveTo( x=997.2421875, y=683.7890625,duration=0.01) 
    auto.moveTo( x=997.2421875, y=685.16796875,duration=0.01) 
    auto.moveTo( x=997.2421875, y=687.3515625,duration=0.01) 
    auto.moveTo( x=997.2421875, y=689.53515625,duration=0.01) 
    auto.moveTo( x=997.2421875, y=690.9140625,duration=0.01) 
    auto.moveTo( x=996.78125, y=692.29296875,duration=0.01) 
    auto.moveTo( x=996.40234375, y=693.04296875,duration=0.01) 
    auto.moveTo( x=995.48046875, y=694.421875,duration=0.01) 
    auto.moveTo( x=994.7265625, y=695.171875,duration=0.01) 
    auto.moveTo( x=993.97265625, y=695.921875,duration=0.01) 
    auto.moveTo( x=993.05078125, y=697.30078125,duration=0.01) 
    auto.moveTo( x=992.296875, y=698.05078125,duration=0.01) 
    auto.moveTo( x=991.54296875, y=698.42578125,duration=0.01) 
    auto.moveTo( x=990.7890625, y=699.17578125,duration=0.01) 
    auto.moveTo( x=990.49609375, y=699.46484375,duration=0.01) 
    auto.moveTo( x=990.203125, y=699.75390625,duration=0.01) 
    auto.moveTo( x=989.91015625, y=700.04296875,duration=0.01) 
    auto.moveTo( x=989.6171875, y=700.33203125,duration=0.01) 
    auto.moveTo( x=989.32421875, y=700.62109375,duration=0.01) 
    auto.moveTo( x=989.32421875, y=700.91015625,duration=0.01) 
    auto.moveTo( x=989.0703125, y=700.91015625,duration=0.01) 
    auto.moveTo( x=989.0703125, y=701.16015625,duration=0.01) 
    auto.moveTo( x=989.0703125, y=701.3671875,duration=0.01) 
    auto.moveTo( x=988.31640625, y=701.7421875,duration=0.01) 
    auto.moveTo( x=988.31640625, y=702.4921875,duration=0.01) 
    auto.moveTo( x=987.9375, y=703.2421875,duration=0.01) 
    auto.moveTo( x=987.64453125, y=703.53125,duration=0.01) 
    auto.moveTo( x=986.890625, y=704.28125,duration=0.01) 
    auto.moveTo( x=986.59765625, y=704.5703125,duration=0.01) 
    auto.moveTo( x=986.3046875, y=704.859375,duration=0.01) 
    auto.moveTo( x=986.01171875, y=705.1484375,duration=0.01) 
    auto.moveTo( x=985.71875, y=705.4375,duration=0.01) 
    auto.moveTo( x=985.42578125, y=705.7265625,duration=0.01) 
    auto.moveTo( x=985.42578125, y=706.015625,duration=0.01) 
    auto.moveTo( x=985.171875, y=706.015625,duration=0.01) 
    auto.moveTo( x=985.171875, y=706.234375,duration=0.01) 
    auto.mouseUp(button='left', x=985.171875, y=706.234375, duration = 0.3176450729370117) 
