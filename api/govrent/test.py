import json
import datetime
import random
from dateutils import relativedelta
for i in range(4):
    first = datetime.datetime.now() - relativedelta(years=1)
    days = {}
    while (first < datetime.datetime.now()):
        elec = random.randint(300, 900)/100
        days[first.strftime("%Y-%m-%d")] = elec
        first += relativedelta(days=1)
    with open('data{}.json'.format(i+1), 'w') as fout:
        json.dump(days, fout, indent=4)

