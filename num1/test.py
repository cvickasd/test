import json
import datetime
import time

target_seconds = 30

def print_str(time):
    if time==target_seconds:
        print("Its time")

def time_call(time):   
    print(current_seconds)
    
while True:
    current_seconds = datetime.datetime.now().time().second
    time_call(current_seconds)
    print_str(current_seconds)
    time.sleep(1)