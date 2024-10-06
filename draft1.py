#Written and copyrighted by Rudra
#Roll Number - 240041031
# As soon as I learnt about how to plot a line, I thought sphere can be plotted By 
# just plotting large number of circles with geometric constrain.
# 
# Hence I did it , you can see it. I thought it would be differnt from others, (my own style).
# 

import numpy as num
import matplotlib.pyplot as plt
import mpl_toolkits as mp3d

axe = plt.axes(projection = "3d")

axe.set_xlabel("X - axis")
axe.set_ylabel("Y - axis")
axe.set_zlabel("Z - axis")

theata = num.arange(0, 2 * num.pi, 0.01) # Creating a array of line points to make circle

z = -1

# Plotting sphere by loop of circles.
while (z<=1) :
    a = (1-z**2)**0.5 # Here a is radius of circle

    x_data = a * num.cos(theata)
    y_data = a * num.sin(theata)

    axe.plot(x_data, y_data, z, color = 'b', alpha = 0.07) # Plotting a circle
    z +=0.01
axe.scatter(0,0,[-1,1],color='b', alpha = 0.1, s = 3)
axe.plot(0, 0, [-1,1], linewidth = 2, color = 'g')

axe.text(0,0,1,"|0>", fontsize = 15)
axe.text(0,0,-1,"|1>", fontsize = 15)
state_vector_x = num.cos(num.pi/4)
state_vector_z = num.sin(num.pi/4) * (-1)

#Plotting state vector - 
axe.quiver(0, 0, 0, state_vector_x, 0, state_vector_z, color = 'r')

#Now we are done with task, hopefully (I mean from my side, don't know how quantum god will react!)

#As we have some time so lets try to make it more beautiful

axe.set_title("My First Sphere Yeee")
axe.set_xlim([-1,1])
axe.set_ylim([-1,1])
axe.set_zlim([-1,1])

axe.plot([-1,1], 0, 0, color = 'black')
axe.plot(0, [-1,1], 0, color = 'black')

axe.text(0.5,0,0,'X - Axis', fontsize = 12)
axe.text(0,-0.9,0,'Y - Axis', fontsize = 12)

print('Thank You')
plt.show()