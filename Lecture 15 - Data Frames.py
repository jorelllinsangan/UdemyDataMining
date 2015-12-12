import numpy as np
import pandas as pd
import webbrowser

from pandas import Series, DataFrame


# website ='http://en.wikipedia.org/wiki/NFL_win-loss_records'

# webbrowser.open(website)
# nfl_frame = DataFrame(columns=  ('Rank', 'Team', 'Won', 'Lost', 'Tied', 'Pct.', 'First Season', 'Total Games', 'Conference'))
nfl_frame = pd.read_clipboard()

print nfl_frame, 

print nfl_frame.columns