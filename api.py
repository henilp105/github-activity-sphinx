import json
import requests
from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt
import datetime

info = requests.get('https://contributor-overtime-api.apiseven.com/monthly-contributor?repo=fortran-lang/fpm').text
print(info)
