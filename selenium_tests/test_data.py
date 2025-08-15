import json
import random
def test_data():
    filepath= "C:\\Users\\akash\\PycharmProjects\\Practicepython\\selenium_tests\\test_data.json"
    with open(filepath,"r") as file:
        data = json.load(file)
    return random.choice(data)
def test_login_data():
    filepath= "C:\\Users\\akash\\PycharmProjects\\Practicepython\\selenium_tests\\test_login_data.json"
    with open(filepath,"r") as file:
        data = json.load(file)
    return data
def contact_us():
    filepath= "C:\\Users\\akash\\PycharmProjects\\Practicepython\\selenium_tests\\contact_us_data.json"
    with open(filepath,"r") as file:
        data = json.load(file)
    return data