from datetime import datetime
import pytz
import json
import requests
from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt

fortran_monthly =[]
fortran_commits =[]
fpm_monthly =[]
fpm_commits =[]
stdlib_monthly =[]
stdlib_commits =[]

months = ["Unknown", "January","Febuary","March", "April","May","June","July","August","September","October","November","December"]
def monthly_graph(repo):
  info = requests.get('https://api.github.com/repos/fortran-lang/'+repo+'/stats/code_frequency').text
  d = json.loads(info)
  c = 0
  monthly_commits=[]
  commits=[]
  for i in range(0,len(d),4):
    for j in range(4):
      try:
        c = c + d[i+j][1]
      except:
       print("")
    date_time = datetime.fromtimestamp(d[i][0])
    monthly = str(months[date_time.month])+" "+str(date_time.year)
    commits.append(c)
    monthly_commits.append(monthly)
    c=0
  test_chart = {"data": [
          {
           "x": monthly_commits,
           "y": commits,
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
  if repo =='fortran-lang.org':
    fortran_monthly = monthly_commits
    fortran_commits = commits
  if repo =='fpm':
    fpm_monthly = monthly_commits
    fpm_commits = commits
    print(fpm_monthly , fpm_commits)
  if repo =='stdlib':
    stdlib_monthly = monthly_commits
    stdlib_commits = commits
    print(stdlib_monthly , stdlib_commits)
  with open(repo+".json", "w") as f:
    json.dump(test_chart, f)

 
graphs =["fortran-lang.org","fpm","stdlib"]
for i in graphs:
  monthly_graph(i)
