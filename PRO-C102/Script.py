#Setup
from CloudStorage import TranferData
import cv2
import time
import os

def main(accToken):
    access_token = accToken
    trnfr = TranferData(access_token)

    srcList = 'Folder1'
    
    for file in os.listdir(srcList):
        src = srcList+'/'+file
        dst = '/Atharva\'s Files/'+file
        trnfr.upload_file(src, dst)
        print(f'File {file} has moved')
    print('All files have been moved!')

def tksnpsht():    
    videoCaptureObject = cv2.VideoCapture(0)
    counter = 5

    while(counter>0):
        ret,frame = videoCaptureObject.read()
        time.sleep(3)
        cv2.imwrite(f"Folder1/NewPicture{counter}.jpg",frame)
        counter=counter - 1

    videoCaptureObject.release()
    cv2.destroyAllWindows()
    main() #Enter Access Token

#Display
for i in range(1, 2):
    print("\n")
    
    try:
        tksnpsht()
    except:
        print('Access token not entered (in Script.py line 32)')

for i in range(1, 2):
    print("\n")