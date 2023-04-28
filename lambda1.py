# first lambda function it will generate mock data for second lambda function and it will generate data in random index fashion

import json
import random


name_list=["waman","kalpesh","pankaj","anant","prthmesh","sahil"]
age_list=[26,27,25,26,23,25]
salary_list=[75000,55000,44000,25000,60000,35000]


def lambda_handler(event, context):
    # TODO implement
    
    #whenever my lambda fucntion execute it will generate random index from 0 to 5
    random_index=random.randint(0,5)
    payload={}
    
    payload["emp_name"]=name_list[random_index]
    payload["emp_age"]=age_list[random_index]
    payload["emp_salary"]=salary_list[random_index]
    
    #print(payload)
    
    
    return payload
