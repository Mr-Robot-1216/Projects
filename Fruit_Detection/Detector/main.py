# -*- coding: utf-8 -*-
"""

Author:: Kale Akhila <akhila.kale.3@gmail.com> <https://www.linkedin.com/in/kale-akhila-46aaa4192/>

"""

## **Importing Layers**

from tensorflow.keras.models import model_from_json
import numpy as np
import cv2

"""# **Loading the files**"""

model = model_from_json(open("model.json","r").read()) # load model
model.load_weights('fruits_copy1.hdf5') # load weights

# start the camera for video capturing
cap = cv2.VideoCapture(0) #('video.mkv')

# set the start and end points for image capturing

start_point = (100,100)
end_point = (300,300)

color = (255,0,0)

# set the points for cropping the image
x = start_point[0]
y = start_point[1]
w = end_point[0]-start_point[0]
h = end_point[1]-start_point[1]

"""# **Cropping the image and predicting the item**"""

while(cap.isOpened()):
    ret, frame = cap.read() # captures frame and returns boolean value and captured image
   
    image = cv2.rectangle(frame,start_point,end_point,color,2)
    croped_image = image[y:y+w,x:x+h] # cropping the image required i.e item area from the image
    resized_image = cv2.resize(croped_image,(100,100))
    image_array = np.array(resized_image,dtype='float32') / 255.0 
    image_array = np.expand_dims(image_array, axis=0)
    predictions = model.predict(image_array)

    # finding maximum indexed array
    max_index=np.argmax(predictions[0])

    items = ('Apple Braeburn', 'Apple Crimson Snow', 'Apple Golden 1',
       'Apple Golden 2', 'Apple Golden 3', 'Apple Granny Smith',
       'Apple Pink Lady', 'Apple Red 1', 'Apple Red 2', 'Apple Red 3',
       'Apple Red Delicious', 'Apple Red Yellow 1', 'Apple Red Yellow 2',
       'Apricot', 'Avocado', 'Avocado ripe', 'Banana',
       'Banana Lady Finger', 'Banana Red', 'Beetroot', 'Blueberry',
       'Cactus fruit', 'Cantaloupe 1', 'Cantaloupe 2', 'Carambula',
       'Cauliflower', 'Cherry 1', 'Cherry 2', 'Cherry Rainier',
       'Cherry Wax Black', 'Cherry Wax Red', 'Cherry Wax Yellow',
       'Chestnut', 'Clementine', 'Cocos', 'Corn', 'Corn Husk',
       'Cucumber Ripe', 'Cucumber Ripe 2', 'Dates', 'Eggplant', 'Fig',
       'Ginger Root', 'Granadilla', 'Grape Blue', 'Grape Pink',
       'Grape White', 'Grape White 2', 'Grape White 3', 'Grape White 4',
       'Grapefruit Pink', 'Grapefruit White', 'Guava', 'Hazelnut',
       'Huckleberry', 'Kaki', 'Kiwi', 'Kohlrabi', 'Kumquats', 'Lemon',
       'Lemon Meyer', 'Limes', 'Lychee', 'Mandarine', 'Mango',
       'Mango Red', 'Mangostan', 'Maracuja', 'Melon Piel de Sapo',
       'Mulberry', 'Nectarine', 'Nectarine Flat', 'Nut Forest',
       'Nut Pecan', 'Onion Red', 'Onion Red Peeled', 'Onion White',
       'Orange', 'Papaya', 'Passion Fruit', 'Peach', 'Peach 2',
       'Peach Flat', 'Pear', 'Pear 2', 'Pear Abate', 'Pear Forelle',
       'Pear Kaiser', 'Pear Monster', 'Pear Red', 'Pear Stone',
       'Pear Williams', 'Pepino', 'Pepper Green', 'Pepper Orange',
       'Pepper Red', 'Pepper Yellow', 'Physalis', 'Physalis with Husk',
       'Pineapple', 'Pineapple Mini', 'Pitahaya Red', 'Plum', 'Plum 2',
       'Plum 3', 'Pomegranate', 'Pomelo Sweetie', 'Potato Red',
       'Potato Red Washed', 'Potato Sweet', 'Potato White', 'Quince',
       'Rambutan', 'Raspberry', 'Redcurrant', 'Salak', 'Strawberry',
       'Strawberry Wedge', 'Tamarillo', 'Tangelo', 'Tomato 1', 'Tomato 2',
       'Tomato 3', 'Tomato 4', 'Tomato Cherry Red', 'Tomato Heart',
       'Tomato Maroon', 'Tomato Yellow', 'Tomato not Ripened', 'Walnut',
       'Watermelon')
    predicted_item = items[max_index]
    cv2.putText(frame, predicted_item, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    img = cv2.resize(image, (1240,720), interpolation =cv2.INTER_AREA)

    # display the resulting frame
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the capture
cap.release()
cv2.destroyAllWindows()