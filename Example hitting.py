import numpy as np
import pandas as pd
import pybaseball as bb
from pybaseball import statcast
from pybaseball import batting_leaders
from pybaseball import batting_stats_range
from pybaseball import pitching_leaders
from pybaseball import pitching_stats_range

print('Dates must be entered as Year-Month-Day')
x = input('Enter First Date:') 
y = input('Enter Second Date:')
print('H = Hits', 'HR = Home Runs', 'AVG = Batting Average', 'SLG = Sluggling %', 'OPS = On Base + SLG' )
z = input('Enter requested Stat:')

data = batting_stats_range(x, y)
sorted_d1 = data.sort_values(by=z, ascending=False)
#sorted_hr = sorted_d1('Name', 'HR')
sorted_d1.head(5)

