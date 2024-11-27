from faker import Faker
import random as rn
import pandas as pd #type:ignore
import numpy as np  #type:ignore

fake=Faker()

num_rows=200

def generate_data():
    data={
        'customer_id':[id for id in range(1000,1201)],
        'customer_name' : [fake.name() for _ in range(num_rows)],  # _ indicates throwaway variable
        'product_id' : [rn.randint(1,20) for _ in range(num_rows)],
        'purchase_date' : [fake.date_between(start_date="-1y",end_date="today") for _ in range(num_rows)], # date_between helps generate fake data from today to past 1 year
        'quantity' : [rn.randint(1,10) for _ in range(num_rows)],
        'price_per_unit' : [round(rn.uniform(10.0,100.0),2) for _ in range(num_rows)],
        'region' : [rn.choice("North","South","East","West") for _ in range(num_rows)]
    }

    return data



