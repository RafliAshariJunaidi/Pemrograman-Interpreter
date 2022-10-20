import pandas as pd

gpuData = pd.read_csv("https://raw.githubusercontent.com/Shalahuddin-Abdul/Pemrograman-Interpreter/main/Praktikum/UTS/All_GPUs.csv")
cpuData = pd.read_csv("https://raw.githubusercontent.com/Shalahuddin-Abdul/Pemrograman-Interpreter/main/Praktikum/UTS/Intel_CPUs.csv")


gpuDedicated = gpuData.copy().loc[gpuData['Integrated']=='No']
pRateAvg = gpuDedicated["Pixel_Rate(GPixel/s)"].mean()
pRateMax = gpuDedicated["Pixel_Rate(GPixel/s)"].max()
pRateMin = gpuDedicated["Pixel_Rate(GPixel/s)"].min()
pRateSkew = gpuDedicated["Pixel_Rate(GPixel/s)"].skew()

def perfRating(i):
    pRateRating = gpuDedicated["Pixel_Rate(GPixel/s)"][i]/pRateAvg*5
    return int(pRateRating)

# perfRating(24)

# print(gpuData)
for i in range(3406):
    if gpuData["Notebook_GPU"][i]=="No":
        if gpuData["TMUs"][i]>256:
            print(gpuData["Name"][i], "with", gpuData["Memory"][i], "and", gpuData["Pixel_Rate"][i])
