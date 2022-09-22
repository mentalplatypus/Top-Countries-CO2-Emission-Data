import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn")

# data taken from https://github.com/owid/co2-data
data = pd.read_csv("data.csv").fillna(0)
year = np.unique(data['year'].values)

cn = [0.0]*(271 - len((data[data['country'] == "China"]['co2']).tolist())) + (data[data['country'] == "China"]['co2']).tolist()
us = [0.0]*(271 - len((data[data['country'] == "United States"]['co2']).tolist())) + (data[data['country'] == "United States"]['co2']).tolist()
ind = [0.0]*(271 - len((data[data['country'] == "India"]['co2']).tolist())) + (data[data['country'] == "India"]['co2']).tolist()
ru = [0.0]*(271 - len((data[data['country'] == "Russia"]['co2']).tolist())) + (data[data['country'] == "Russia"]['co2']).tolist()
jp = [0.0]*(271 - len((data[data['country'] == "Japan"]['co2']).tolist())) + (data[data['country'] == "Japan"]['co2']).tolist()
ir = [0.0]*(271 - len((data[data['country'] == "Iran"]['co2']).tolist())) + (data[data['country'] == "Iran"]['co2']).tolist()
ge = [0.0]*(271 - len((data[data['country'] == "Germany"]['co2']).tolist())) + (data[data['country'] == "Germany"]['co2']).tolist()
sk = [0.0]*(271 - len((data[data['country'] == "South Korea"]['co2']).tolist())) + (data[data['country'] == "South Korea"]['co2']).tolist()
sa = [0.0]*(271 - len((data[data['country'] == "Saudi Arabia"]['co2']).tolist())) + (data[data['country'] == "Saudi Arabia"]['co2']).tolist()
ida = [0.0]*(271 - len((data[data['country'] == "Indonesia"]['co2']).tolist())) + (data[data['country'] == "Indonesia"]['co2']).tolist()

palette = sns.color_palette("Spectral", 10).as_hex()
colors = ','.join(palette)
labels = ("China", "United States", "India", "Russia", "Japan", "Iran", "Germany", "South Korea", "Saudi Arabia",
          "Indonesia")

plt.figure(figsize=(10, 6))
plt.stackplot(year, cn, us, ind, ru, jp, ir, ge, sk, sa, ida, colors=colors, labels=labels)
plt.title("Annual Production-Based CO2 Emissions of Top 10 Countries from 1750-2020")
plt.xlabel("Year")
plt.ylabel("Production-Based CO2 Emissions (in MMT)")
plt.legend(loc="upper left", shadow=True, ncol=1)
plt.xticks(np.arange(1750, 2021, step=10), rotation=45)
plt.margins(x=0)

plt.show()
