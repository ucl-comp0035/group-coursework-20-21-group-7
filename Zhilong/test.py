img_src='https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2739117239,1572755614&fm=26&gp=0.jpg'
import cv2
cap = cv2.VideoCapture(img_src)
if( cap.isOpened() ) :
  ret,img = cap.read()
  cv2.imshow("image",img)
  cv2.waitKey()