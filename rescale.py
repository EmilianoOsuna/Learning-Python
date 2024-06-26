import cv2 as cv

#Función que sirve para reescalar un video o una imagen
def rescaleFrame(frame, scale = 0.50):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# VISUALIZAR UN VIDEO EN OTRA VENTANA

# capture = cv.VideoCapture(0) #Captura video

# while True: #Bucle infinito para leer e imprimir cada frame del video
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame)
#     cv.imshow("Video", frame)
#     cv.imshow("Video resized", frame_resized)

#     if cv.waitKey(27) & 0xFF==ord("d"): #Break del ciclo presionando la tecla D o hasta que se acaben los frames CV.WAITKEY controla los frames
#         break

# capture.release() #Suelta el archivo o la cámara para poder usarla en otra instancia
# cv.destroyAllWindows() #Cierra todas las ventanas creadas por los frames

# VISUALIZAR UNA IMAGEN EN OTRA VENTANA

img = cv.imread("Hanna\IMG_20230222_120954.jpg ") #Convierte una imagen a un arreglo de pixeles
resized_img = rescaleFrame(img)
cv.imshow("Hanna", resized_img) #El parámetro es el nombre de la ventana y el arreglo de pixeles
cv.waitKey(0) #Keybind para esperar que se presione una tecla (SI HAY UN CERO ES TIEMPO INFINITO)