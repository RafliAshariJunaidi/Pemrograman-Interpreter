import pandas as pd

gpuData = pd.read_csv("https://raw.githubusercontent.com/Shalahuddin-Abdul/Pemrograman-Interpreter/main/Praktikum/UTS/All_GPUs.csv")
cpuData = pd.read_csv("https://raw.githubusercontent.com/Shalahuddin-Abdul/Pemrograman-Interpreter/main/Praktikum/UTS/Intel_CPUs.csv")


gpuDedicated = gpuData.copy().loc[gpuData['Integrated']=='No']
pRateAvg = gpuDedicated["Pixel_Rate(GPixel/s)"].mean()
pRateMax = gpuDedicated["Pixel_Rate(GPixel/s)"].max()
pRateMin = gpuDedicated["Pixel_Rate(GPixel/s)"].min()
pRateSkew = gpuDedicated["Pixel_Rate(GPixel/s)"].skew()

needDict = {
    "Browsing" : 1,
    "Gaming Ringan" : 2,
    "Gaming Berat" : 3,
    "Mini PC" : 4,
    "Kerja" : 5,
    "Sekolah" : 6,
    "Video Editing" : 7
}

# def perfRating(i):
#     pRateRating = gpuDedicated["Pixel_Rate(GPixel/s)"][i]/pRateAvg*5
#     return int(pRateRating)
def filters(cat, x):
    # new = gpuDedicated.drop(cat, axis=1)
    output = gpuDedicated.copy().loc[gpuDedicated[cat]>x]
    print(output[["Name", cat]])

print(needDict)
x = input("Masukkan Kebutuhan anda: ")
category = "Memory(MB)"
compParam = 1
def gpuRec(x):
    if x == 1:
        filters("Memory(MB)", 1024) 
    elif x == 2:
        filters("Memory(MB)", 2048)
    elif x == 3:
        filters("Memory(MB)", 4096)
    elif x == 4:
        filters("Memory(MB)", 2048)

# print(gpuDedicated)
