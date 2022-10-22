import pandas as pd
gpuData = pd.read_csv("gpuData.csv")
cpuData = pd.read_csv("Intel_CPUs.csv")

gpuDedicated = gpuData.copy().loc[gpuData['Integrated']=='No']

def filters(cat, x):
    output = gpuDedicated[(gpuDedicated[cat]>x)].copy().head(10)
    print(output[["Name", cat]])

def gpuRec(x):
    if x == 1:
        filters("Memory(MB)", 1024) 
    elif x == 2:
        filters("Memory(MB)", 4096)
    elif x == 3:
        filters("Pixel_Rate(GPixel/s)", 100)
    elif x == 4:
        filters("Memory(MB)", 3072)
    elif x == 5:
        filters("Memory(MB)", 2048)
    elif x == 6:
        filters("Memory(MB)", 1024)    
    elif x == 7:
        filters("Texture_Rate(GTexel/s)", 100)