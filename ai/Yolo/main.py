import numpy as np
import cv2
import time

COLORS = [
    (0,255, 255),
    (255, 255, 0),
    (0,255, 0),
    (255, 0, 0)
]

class_names = []

with open("coco.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

#video cap
captura = cv2.VideoCapture(0)# 0 para usar webcam

#rede net
net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg")

model = cv2.dnn.DetectionModel(net)

#carrega padrao entrdada (resolução e escala)
model.setInputParams(size=(416,416), scale=1/255)

while True:
    x, frame = captura.read()

    start = time.time()

    classes, scores, boxes = model.detect(frame, 0.1, 0.3)

    end = time.time()

    #classid: objecto detectado, score: % certeza
    for (classid, score, box) in zip(classes, scores, boxes):
        color = COLORS[int(classid % len(COLORS))]

        label = f'{class_names[classid]}:{score}'

        cv2.rectangle(frame, box, color, 2)

        cv2.putText(frame, label, (box[0], box[1] -10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    fps_label = f'FPS: {round((1. / (end - start)), 2)}'

    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("detections", frame)

    if cv2.waitKey(1) == 27:
        break

captura.release()
cv2.destroyAllWindows()



if __name__ == "__main__":
    
    #print(*COLORS)
    #print(*class_names, sep='\n')
    pass
    