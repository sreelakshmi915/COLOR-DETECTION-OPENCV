#importing libraries

import pandas as pd
import cv2

img_source = "doc/pic6.jpg"
color_source = "doc/colors.csv"
#Read file
head_name =['color', 'color_name', 'hex_value', 'R', 'G', 'B']
df = pd.read_csv(color_source, names=head_name, header=None)



image = cv2.imread(img_source)
image = cv2.resize(image, (900, 500))
is_click =False
b = g = r = x_pos = y_pos = 0

#to get the color name from the r g b value
def get_color_name(R, G, B):
	min = 1000
	for i in range(len(df)):
		d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
		if d <= min:
			min = d
			c_name = df.loc[i, 'color_name']

	return c_name
#to get the coordinates
def draw_function(event,x,y,flag,params):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global is_click,r,g,b,xpos,y_pos
        is_click=True
        x_pos = x
        y_pos = y
        b,g,r =image[y_pos,x_pos]
        b = int(b)
        g = int(g)
        r = int(r)


#to display we have to make a window
cv2.namedWindow('display')
cv2.setMouseCallback('display',draw_function)
while True:
    cv2.imshow('display', image)
    if is_click:
        cv2.rectangle(image,(20,20),(700,60),(b,g,r),-1)
        text = get_color_name(r,g,b) +'  R =' + str(r) + ' G =' + str(g) + ' B =' +str(b)
        cv2.putText(image, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)
        if r + g + b >= 300:
            cv2.putText(image, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    if cv2.waitKey(20)& 0xFF == 27 :
        break

cv2.destroyAllWindows()


