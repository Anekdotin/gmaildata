__author__ = 'ed'

import mailbox
from email.utils import parsedate
from dateutil.parser import parse
import itertools
import plotly.plotly as py
from plotly.graph_objs import *


#enter path to mbox file.  Download from google under your dashboard
path = '/home/ed/Development/Python/gmaildata/All mail Including Spam and Trash.mbox'

#open the mailbox
mbox = mailbox.mbox(path)


## turn dates of emails into a list per day

all_dates = []
mbox = mailbox.mbox(path)
for message in mbox:
    all_dates.append( str (parse( message['date'])). split (' ')[0])
    

