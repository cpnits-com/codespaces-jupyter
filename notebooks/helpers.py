import pytz
import time
import datetime

def nu(waar: str) -> str:
    t = time.time()
    s = "%d-%m-%Y %H:%M:%S"
    return datetime.datetime.fromtimestamp(t, pytz.timezone(waar)).strftime(s)