#program python pengulangan
# Menggunakan program turtle

import turtle

night = turtle.Turtle()

for i in range(100):
    night.forward(20 + i* 3)
    night.right(135)

night.done()