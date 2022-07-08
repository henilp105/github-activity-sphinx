import yaml
from pathlib import Path
from collections import Counter
import json
import requests
import datetime

def Sort_Tuple(tup):
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst-i-1):
            if (tup[j][0] > tup[j + 1][0]):
                temp = tup[j]
                tup[j]= tup[j + 1]
                tup[j + 1]= temp
    return tup

def plot_graphs(graph):
  a=[]
  login=[]
  contributions=[]
  info = requests.get('https://api.github.com/repos/fortran-lang/'+graph+'/contributors').text
  d = json.loads(info)
  for i in range(len(d)):
        try:
            a.append((d[i]['login'],d[i]['contributions']))
        except KeyError:
            print("")
  Sort_Tuple(a)
  for i in a:
    login.append(i[0])
    contributions.append(i[1])
  test_chart = {"data": [
      {
        "x": login,
        "y": contributions,
      }
    ],
    "layout": {
      "margin": {
        "t": 15,
        "b": 30,
        "r": 15,
        "l": 35
      }
    }
  }
  print(test_chart)
  with open(graph+".json", "w") as f:
    json.dump(test_chart, f)
graphs =["fortran-lang.org","fpm","stdlib"]
for i in graphs:
  plot_graphs(i)
