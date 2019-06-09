import json
import random
import uuid
import datetime
from dateutils import relativedelta


complex_names = {
    "717 N Maple":  "717.jpeg",
    "Hikone 2724": "hikone.jpg",
    "1737 Green Rd": "green.jpg",
    "221 S 7th St": "7th.jpg",
    "727 Miller Ave": "miller.jpg"
}

complexes = [
    {
        "address": name,
        "id": str(uuid.uuid4()),
        "allowance": random.randint(150, 300),
        "image": image
    }
    for name, image in complex_names.items()
]


units = []
num_units_for_complex = 12
unit_allowances = {
    1: 100,
    2: 134,
    3: 167,
    4: 204,
    5: 227,
}
for complex in complexes:
    bed_numbers = random.randint(1, 5)
    units += [
        {
            "id": str(uuid.uuid4()),
            "unit_complex": complex['id'],
            "bed_number": bed_numbers,
            "address": complex['address'] + ' ' + str(random.randint(100, 500)),
            "allowance": unit_allowances[bed_numbers]
        }
        for _ in range(random.randint(5, num_units_for_complex))
    ]

gas_readings = []
electricity_readings = []

for day in range(365):
    date = datetime.datetime.now() - relativedelta(days=day)
    gas_readings += [
        {
            "id": str(uuid.uuid4()),
            "unit": str(unit['id']),
            "usage": random.randint(100,7000)/100,
            "reading_type": "GAS",
            "date": date.strftime("%Y-%m-%d")
        }
        for unit in units
    ]
    electricity_readings += [
        {
            "id": str(uuid.uuid4()),
            "unit": str(unit['id']),
            "usage": random.randint(100,7000)/100,
            "reading_type": "ELECTRICITY",
            "date": date.strftime("%Y-%m-%d")
        }
        for unit in units
    ]
    
readings = gas_readings + electricity_readings

monthly = []
for month in range(12):
    date = datetime.datetime.now() - relativedelta(months=month)
    monthly += [
        {
            "id": str(uuid.uuid4()),
            "unit": str(unit['id']),
            "usage": random.randint(1000,100000)/100,
            "reading_type": "TOTAL",
            "date": date.strftime("%Y-%m-%d")
        }
        for unit in units
    ]

complex_models = [
    {
      "model": "govrent.UnitComplex",
      "pk": complex['id'],
      "fields": {
        "address": complex['address'],
        "image": complex["image"]
      }
    }
    for complex in complexes
]


unit_models = [
    {
      "model": "govrent.Unit",
      "pk": unit['id'],
      "fields": {
        "unit_complex": unit['unit_complex'],
        "bed_number": unit['bed_number'],
        "address": unit['address'],
        "allowance": unit['allowance']
      }
    }
    for unit in units
]


reading_models = [
    {
      "model": "govrent.MeterReading",
      "pk": reading['id'],
      "fields": {
            "unit": reading['unit'],
            "usage": reading['usage'],
            "reading_type": reading['reading_type'],
            "date": reading['date']
      }
    }
    for reading in readings
]

user_models = [{
    "model": "auth.user",
    "pk": 1,
    "fields": {
        "password": "pbkdf2_sha256$120000$anSo2Ya1BEzF$Wx9VxuaTubT6ZXvzRjwUGoiUWzC/Pbcd8IVS+mA7Y2c=",
        "last_login": None,
        "is_superuser": True,
        "username": "kamal",
        "first_name": "",
        "last_name": "",
        "email": "kamal@clinc.com",
        "is_staff": True,
        "is_active": True,
        "date_joined": "2019-06-09T05:44:43.259Z",
        "groups": [],
        "user_permissions": []
    }
}]

data = {
    "complexes": complexes,
    "units": units,
    "meter_readings": gas_readings + electricity_readings,
    "monthly": monthly
}
with open("dummy.json", 'w') as fout:
    json.dump(data, fout, indent=4)

with open("fixtures.json", 'w') as fout:
    json.dump(complex_models+unit_models+reading_models+user_models, fout, indent=4)