import os
import cv2
import time
import handTrackingModule   
import letterPrediction



def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handTrackingModule.handDetector() #for future developments.
    input_folder = 'alphabet letters'
    prediction  = ''

    #the video is start .
    if status == False:
        while True:
            success, img = cap.read()
            hands = img
            img = detector.findHands(img)
            lm_list = detector.findPosition(img) #to recognize the hand if its in the frame.
            cTime = time.time()
            fps = 1 / (cTime - pTime) #frame per second
            pTime = cTime

            #rectangle to position the hands.
            img = cv2.rectangle(img, (150,150), (350,350), (0,0,255), 2) 
            
            if len(lm_list) != 0 :
                cropped_img = letterPrediction.cropped_image(img)
                cv2.imshow("cropped image", cropped_img)
                prediction = letterPrediction.modeling(cropped_img, prediction = False, result = False)
    
            
            cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3) 
            cv2.putText(img, prediction, (100,100), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 0),3) 
    
    
            cv2.imshow("Image", img)
            cv2.waitKey(1)
        
        ### END OF WHILE LOOP ### 
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()  
    
