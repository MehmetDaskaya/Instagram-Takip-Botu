import pyautogui
import random
import time
import cv2
 
takipEdilen = []
dil = input("Diliniz nedir?\n")
saniye = float(input("Takipler arası süre varsayılan olarak rastgele 10-35 saniye arasında bir değer ile yapılır. Buna ek süre olarak kaç saniye eklemek istersin?\n"))
time.sleep(1)
print("Takip işlemi başladı\n")

while True:

    if dil =="türkçe":
        def takip_et():
            takipet = pyautogui.locateCenterOnScreen(r"C:\instagram_bot_images\takipet.png", confidence=0.8)
            time.sleep(0.3)
            if not takipet:
                pyautogui.scroll(-350)
            else:
                time.sleep(random.randint(10,35)+saniye)
                pyautogui.click(takipet)
                pyautogui.scroll(-60)
                time.sleep(2)
                takipEdilen.append("a")
                print("Şimdiye kadar takip edilen kişi sayısı: " + str(len(takipEdilen)))
        
        while True:
            takip_et()

    elif dil =="ingilizce":
        def takip_et():
            takipet = pyautogui.locateCenterOnScreen(r"C:\instagram_bot_images\follow.png", confidence=0.8)
            time.sleep(0.3)
            if not takipet:
                pyautogui.scroll(-350)
            else:
                time.sleep(random.randint(10,35)+saniye)
                pyautogui.click(takipet)
                pyautogui.scroll(-60)
                time.sleep(2)
                takipEdilen.append("a")
                print("Şimdiye kadar takip edilen kişi sayısı: " + str(len(takipEdilen)))
        
        while True:
            takip_et()
    else:
        continue