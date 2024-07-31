from datetime import *
from dateutil.relativedelta import *

def print_hey():
    print('Hey!')

def print_date():
    now = datetime.now()
    print(now + relativedelta(months=1))