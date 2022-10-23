import time
from loginFunct import login
from recFunct import filters
from recFunct import gpuRec

needDict = {
    1 : "Browsing",
    2 : "Gaming Ringan",
    3 : "Gaming Berat",
    4 : "Mini PC",
    5 : "Kerja",
    6 : "Sekolah",
    7 : "Video Editing"
}

login()
time.sleep(3)
print(needDict)
x = input("Masukkan Kebutuhan anda: ")
gpuRec(int(x))
