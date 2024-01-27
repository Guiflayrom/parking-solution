import cv2
import numpy as np
import random
import pandas as pd

intervalo = 5

ret = True
save = False

positions = []
load = False

if load:
	positions = np.load('positions.npy')
	positions = positions.tolist()
	
def get_event(event, x, y, flags, param):
	global positions
	if event == cv2.EVENT_LBUTTONDOWN:
		positions.append([x,y])
	if event == cv2.EVENT_MBUTTONDOWN:

		positions.pop(-1)

def draw(frame):
	global positions, save


	tamanho = len(positions)
	black = np.zeros_like(frame)
	for x,y in positions:
		cv2.circle(frame, (x,y), 2,[255,255,255],-1, cv2.LINE_AA)
	
	if tamanho > 3:
		np.save('positions.npy', positions)
		lista_temporaria = []
		prop = tamanho // 4
		for i in range(0,prop):
			a = positions[((i*4)-4)]
			b = positions[((i*4)-4)+1]
			c = positions[((i*4)-4)+2]
			d = positions[((i*4)-4)+3]
			lista_temporaria.append([a,b,c,d])
		positions_arr = np.array(lista_temporaria)
		for e in range(0,prop):
			a = positions[(e*4)]
			b = positions[(e*4)+1]
			c = positions[(e*4)+2]
			d = positions[(e*4)+3]
			x_,y_,w_,h_ = 100000,100000,0,0
			a,b,c,d = reversed([a,b,c,d])
			for item in [a,b,c,d]:
				if item[0] < x_:
					x_ = item[0]
				if item[1] < y_:
					y_ = item[1]
				if item[0]>w_:
					w_ = item[0]
				if item[1]>h_:
					h_ = item[1]
			
			center_x = int(x_ + ((w_-x_)//2))
			center_y = int(y_ + ((h_-y_)//2))
			
			arr = np.array([a,b,c,d])
			t_black = np.zeros_like(frame)
			cv2.fillPoly(black, [arr], [255,255,255]) 
			cv2.fillPoly(t_black, [arr], [255,255,255]) 
			cv2.putText(black, str(e), (center_x,center_y), cv2.FONT_HERSHEY_SIMPLEX,  .5, [0,0,0], 2, cv2.LINE_AA)
			resultado_t = np.where(t_black > 0 , copy, 0)
			mini = resultado_t[y_:h_,x_:w_]
			name = random.randint(0,99999999)
			sname = str(name).zfill(11)
			mini = cv2.resize(mini, (100,100))
			if save:
				cv2.imwrite('vagas/{}.jpg'.format(sname),mini)
		save = False

	return black
		
cv2.namedWindow("Main")
cv2.setMouseCallback("Main", get_event)



url = '1CW5FXYBIDXC6YZT8.jpg'
# exemplo: rtsp://199.234.167.151:554/onvif/profile1/media.smp
count = 0
while ret:
	count += 1
	frame = cv2.imread(url)
	copy = frame.copy()
	black = draw(frame)
	resultado = np.where(black > 0 , copy, 0)

	final = cv2.addWeighted(frame,1,black,.6,1)
	cv2.imshow("Main",final)
	k = cv2.waitKey(1)
	if count % intervalo == 0 or k == ord('s'):
		save = True


		
	if k == ord('n'):
		save = False
	if k == ord('q'):
		exit()
	
