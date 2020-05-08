import pandas as pd
data = pd.read_csv("C:/Users/Albert/OneDrive/Documents/channels_data.txt", sep="|")
print(data.head())
print(data.shape)
print(data.dtypes)
print(data.groupby(["GroupID", "ChannelName"]).sum())
x = dir(pd)
print(x)