# confirmed - recovered - deaths is a better idea since i.e the active number of cases

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import shutil
from random import random

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

response = requests.get('https://api.covid19india.org/data.json')

npastdates = 20
nfuturedates = 20

cases = []
dates = []

for item in response.json()["cases_time_series"]:
    cases.append(item["totalconfirmed"])
    dates.append(item["date"].strip())
"""
pdate = dates[-1]
dates = dates[:-1]

for date in pd.date_range(pdate + " 2020", periods=nfuturedates, freq='d'):
    dates.append(str(date.day) + " " + str(date.month_name()))

realcases = cases
#cases = cases[-npastdates:]
days = list(range(len(cases)))

X = [[day] for day in days]
y = cases

X_pred = list(range(len(cases) + nfuturedates))
X_pred = [[x_pred] for x_pred in X_pred]

poly = PolynomialFeatures(3)

reg = LinearRegression().fit(poly.fit_transform(X), y)

y_pred = reg.predict(poly.fit_transform(X_pred))
"""
plt.scatter(dates, cases,  color='black')
#plt.plot(X_pred, y_pred, color='blue', linewidth=3)
#plt.xticks(())
#plt.yticks(())
plt.show()

"""

allcases = realcases
for item in y_pred[-20:]:
    allcases.append(int(item))
    
datecases = []
for i in range(len(dates)):
    datecases.append([dates[i], allcases[i]])

jsondata = []
for item in [{"date": date, "confirmed": confirmed} for [date, confirmed] in datecases]:
    jsondata.append(item)

jsondata = str({"India" : jsondata}).replace("'", '"')
#print(y_pred)

with open("jsons/current.json", 'w') as f:
    f.write(json.dumps(json.loads(jsondata), indent=2, sort_keys=True))

shutil.copyfile("jsons/current.json", "jsons/" + pdate + ".json")
"""
