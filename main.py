import os
import cv2
import time
import handTrackingModule
import letterPrediction
from dataPreProccess import preproccess
import gui

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handTrackingModule.handDetector()
    input_folder = 'alphabet letters'
    prediction  = ''
    counter = 0
    imageName = 'img_'

    #status = preproccess(input_folder, action = True)
    status = False
    #print("PreProcess is done")
    # recognition is start.
    if status == False:
        while True:
            success, img = cap.read()
            hands = img
            img = detector.findHands(img)
            lm_list = detector.findPosition(img) #to recognize the hand if its in the frame.
            cTime = time.time()
            fps = 1 / (cTime - pTime) #frame per second
            pTime = cTime
            
           
            imagePath = ''

            #rectangle to position the hands.
            img = cv2.rectangle(img, (150,150), (350,350), (0,0,255), 2) 
            
            if len(lm_list) != 0 :
                #edges = letterPrediction.edge_detect(img)
                #cv2.imshow("edge detect image", edges)
                #imageName = imageName+str(counter)+'.jpg'
                #imagePath = os.path.join('testImages' , imageName) 
                cropped_img = letterPrediction.cropped_image(img)
                cv2.imshow("cropped image", cropped_img)
                    #cv2.imwrite(imagePath, edges)
                prediction = letterPrediction.modeling(cropped_img, prediction = False, result = False)
                
                #print(imagePath)
                #imageName = imageName[:4]
                #counter += 1
    
            
            cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3) 
            cv2.putText(img, prediction, (100,100), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 0),3) 
    
    
            cv2.imshow("Image", img)
            cv2.waitKey(1)
        
        ### END OF WHILE LOOP ### 
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()  
    