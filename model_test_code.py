### pip install ultralytics 

from ultralytics import YOLO

model = YOLO("yolov8m_custom_drone_aeroplane.pt")

model.predict(source=0, show=True, save=True, conf=0.5)

'''

### pip install ultralytics 



### Training
yolo task=detect mode=train epochs=100 data=data_custom.yaml model=yolov8m.pt imgsz=640


### Testing

-- Drone
yolo task=detect mode=predict model=yolov8m_custom.pt show=True conf=0.5 source=testing_model\000033.jpg

--aeroplane
yolo task=detect mode=predict model=yolov8m_custom.pt show=True conf=0.5 source=testing_model\aero_57.jpg

-- detection in yolo format (get labels files)
yolo task=detect mode=predict model=yolov8m_custom.pt show=True conf=0.5 source=testing_model\aero_57.jpg save_txt=True

line_thickness=1 
save_crop=True
hide_labels=True
hide_conf=True
classes=[0]   ... detect only drone
classes=[0, 1, ...]   ... detect only drone

input as camera the source=0
ip camera source=https://...

### Export the Model in other format:

yolo task=detect mode=export model=yolov8m_custom.pt format=onnx 
yolo task=detect mode=export model=yolov8m_custom.pt format=tflite 

'''