import numpy as np
import cv2
import tensorflow as tf

"""
    This func will load the model that we use. 
    Convert the input image and predict. 
    
    input: currenly image
    output: predicted letter
"""
def modeling(test_image, prediction = True, result = True):             
    model = tf.keras.models.load_model('demo_cnn_model.h5')             # load model.
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
                    'C': 2
                   }

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
