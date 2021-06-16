import cv2
import os
cam = cv2.VideoCapture(0)

cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def main():
# For each person, enter one numeric face id
    face_id = input('\n Enter User Id And Press <return> ==>  ')
    print("\n [INFO] Initializing face capture. Look the camera and wait")
# Initialize individual sampling face count
    count = 0
    while True:
        ret, img = cam.read()
        if ret == True:
#Converts the colr image to the gray image
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Shows the gray Image
            cv2.imshow('Gray Image', gray)
            
#detects the face from the image
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                cv2.putText(img, "Image No: "+str(count), (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))
                count += 1
                
# Save the captured image into the datasets folder
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
                cv2.imshow('image', img)
                
# Press 'ESC' for exiting video
            if cv2.waitKey(100) & 0xff == 27:
                break
            elif count >= 30: # Take 30 face sample and stop video
                 break
# Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()