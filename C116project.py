import cv2
img=cv2.imread("Image/solar-system.jpg")
text="sun"
text1="Mercury"
text2="Venus"
text3="Earth"
text31="Moon"
text4="Mars"
text5="Jupiter"
text6="Saturn"
text7="Uranus"
text8="Neptune"

cv2.putText(img,text,(20,200),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.5,color=(255,0,0))
cv2.putText(img,text1,(120,230),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.5,color=(255,0,0))
cv2.putText(img,text2,(190,250),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.5,color=(255,0,0))
cv2.putText(img,text3,(270,250),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.5,color=(255,0,0))
cv2.putText(img,text31,(340,180),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.5,color=(255,0,0))
cv2.putText(img,text4,(400,250),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.5,color=(255,0,0))
cv2.putText(img,text5,(610,370),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.5,color=(255,0,0))
cv2.putText(img,text6,(820,310),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.5,color=(255,0,0))
cv2.putText(img,text7,(990,280),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.5,color=(255,0,0))
cv2.putText(img,text8,(1140,275),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.5,color=(255,0,0))

cv2.imshow("output",img)
cv2.waitKey(0)