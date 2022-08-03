from ensurepip import version
from turtle import left
import numpy as np
import cv2
import numpy as np

import tensorflow as tf

"""
    convert the image as the correct place and returns only the hand. 
    
"""
def modeling(test_image, prediction = True, result = True):
    model = tf.keras.models.load_model('cnn_model_4.h5')                # load model.
    cv2.imwrite('img.jpg', test_image)                                  # resize for the model size.
    image = tf.keras.utils.load_img('img.jpg', target_size = (64, 64))
    test_image = tf.image.resize(image,[64, 64])
    test_image = tf.keras.utils.img_to_array(test_image)                # convert to array
    test_image = np.expand_dims(test_image, axis = 0)
    array_result = model.predict(test_image)                            # prediction 
    if prediction: print(array_result)
    letter_result = result_to_letter(array_result)
    if result: print(letter_result)

    return letter_result

"""
    From the vector array we get the letter by the dictioniory.  
"""
def result_to_letter(result):
    letter_position = 0
    letters_dict = {'A': 0,
                    'B': 1,
                    'C': 2,
                    'D': 3,
                    'E': 4,
                    'F': 5,
                    'G': 6,
                    'H': 7,
                    'I': 8,
                    'J': 9,
                    'K': 10,
                    'L': 11,
                    'M': 12,
                    'N': 13,
                    'O': 14,
                    'P': 15,
                    'Q': 16,
                    'R': 17,
                    'S': 18,
                    'T': 19,
                    'U': 20,
                    'V': 21,
                    'W': 22,
                    'X': 23,
                    'Y': 24,
                    'Z': 25,
                    'space': 26}
    for i in result[0]:   
        if i != 0:
            position = list(letters_dict.values()).index(letter_position)
            return list(letters_dict.keys())[position]
        letter_position += 1
    return None

"""
     Cut the emphasis area. 
"""
def cropped_image(img):
    # Cropping an image
    cropped_image = img[152:348, 152:348]
    return cropped_image

"""
    
"""
def preprocess(img):        
    hands = cropped_image(img)                                      # only the hand frame.   
    img_gray = cv2.cvtColor(hands, cv2.COLOR_BGR2GRAY)              # Convert to graycsale            
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)                 # Blur the image for better edge detection
    edges = cv2.Canny(image=img_blur, threshold1=40, threshold2=40)# Canny Edge Detection 
    return edges