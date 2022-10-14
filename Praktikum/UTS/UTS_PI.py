import pandas as pd

gpuData = pd.read_csv("All_GPUs.csv")
cpuData = pd.read_csv("Intel_CPUs.csv")

# print(gpuData)
for i in range(3406):
    if gpuData["Notebook_GPU"][i]=="No":
        if gpuData["TMUs"][i]>256:
            print(gpuData["Name"][i], "with", gpuData["Memory"][i], "and", gpuData["Pixel_Rate"][i])
