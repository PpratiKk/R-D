for j in range(16):
     #inner loop for drawing 18 shapes
         for j in range(18):
             #get the color using HSV to RGB conversion
                 c=colorsys.hsv_to_rgb(h,1,1)
                 color(c)
                 #increment hue for the next color
                 h+=0.005
                 #Draw shapes
                 right(90)
                 circle(150-j*6,90)
                 left(90)
circle(150-j*6,90)
                 right(180)
circle(40,24)
                 #complete the drawing