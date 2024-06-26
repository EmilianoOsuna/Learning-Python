import cv2 as cv

#VISUALIZAR UNA IMAGEN EN OTRA VENTANA

# img = cv.imread("Hanna\IMG_20230222_120954.jpg") #Convierte una imagen a un arreglo de pixeles
# cv.imshow("Hanna", img) #El parámetro es el nombre de la ventana y el arreglo de pixeles
# cv.waitKey(0) #Keybind para esperar que se presione una tecla (SI HAY UN CERO ES TIEMPO INFINITO)

#VISUALIZAR UN VIDEO EN OTRA VENTANA

capture = cv.VideoCapture(0) #Captura video

while True: #Bucle infinito para leer e imprimir cada frame del video
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(30) & 0xFF==ord("d"): #Break del ciclo presionando la tecla D o hasta que se acaben los frames
        break

capture.release() #Suelta el archivo o la cámara para poder usarla en otra instancia
cv.destroyAllWindows() #Cierra todas las ventanas creadas por los frames