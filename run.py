import cv2

def mail():

    import time
    import smtplib
    from email.message import EmailMessage
    Address = "27-17-43/1, Sector 12, Navi Mumbai"
    msg = EmailMessage()
    msg["Subject"] = "Fire Outbreak Detected"
    msg["From"] = "goosezenv@gmail.com"
    msg["To"] = "anushreddydasari@gmail.com"
    msg.set_content(f"I'm FireDetectionSys,\nData:\nAddress - {Address}\nTime - {time.ctime()}")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("goosezenv@gmail.com", "test1234test")
        smtp.send_message(msg)
        smtp.close()

def alarm():

    from playsound import playsound
    print("Fire Detected")
    playsound("Alert.mp3")


def shutdown():

    import time
    import sys
    print("System Shutting Down in ETA: 3s")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("Shutting Down...")
    sys.exit()

if __name__ == '__main__':

    firedetector = cv2.CascadeClassifier('FDSys.xml')

    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    capture.set(3,640)
    capture.set(4,480)

    while (True):
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fire = firedetector.detectMultiScale(frame, 1.2, 5)

        for (x,y,w,h) in fire:
            cv2.destroyAllWindows()
            alarm()
            mail()
            shutdown()

        cv2.imshow('window', frame)
        if cv2.waitKey(1) == ord('q'):
            break