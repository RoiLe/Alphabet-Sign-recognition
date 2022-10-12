import numpy as np
import cv2
import tensorflow as tf
import handTrackingModule
import time

"""
    The video is begin. 
    the main loop of the program will run from here.
"""
def process_program():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handTrackingModule.handDetector()
    prediction  = ''


    while True:
        success, img = cap.read()
        hands = img
        img = detector.findHands(img)
        lm_list = detector.findPosition(img) #to recognize the hand if its in the frame.
        cTime = time.time()
        fps = 1 / (cTime - pTime) #frame per second
        pTime = cTime

        img = cv2.rectangle(img, (150,150), (350,350), (0,0,255), 2) 
            
        if len(lm_list) != 0 :
            cropped_img = cropped_image(img)
            cv2.imshow("cropped image", cropped_img)
            prediction = modeling(cropped_img, prediction = False, result = False)
  
            
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3) 
        cv2.putText(img, prediction, (100,100), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 0),3) 
    
        cv2.imshow("Image", img)
        cv2.waitKey(1)
            
        ### END OF WHILE LOOP ### 
cv2.destroyAllWindows()


"""
    convert the image as the correct place and returns only the hand. 

"""
def modeling(test_image, prediction = True, result = True):             
    model = tf.keras.models.load_model('demo_cnn_model_version_3.h5')   # load model.
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
    letters_dict = {'a': 0,
                    'b': 1,
                    'c': 2,
                    'd': 3,
                    'f': 4,
                    'g': 5,
                    'h': 6,
                    'i': 7,
                    'j': 8,
                    'k': 9,
                    'l': 10,
                    'm': 11,
                    'n': 12,
                    'o': 13,
                    'p': 14,
                    'q': 15,
                    'r': 16,
                    's': 17,
                    't': 18,
                    'u': 19,
                    'v': 20,
                    'w': 21,
                    'x': 22,
                    'y': 23,
                    'z': 24}
 
                 
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

