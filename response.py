import requests
import random
import json
import pytz
import datetime


apikey = # click to set to your apikey
limit = 10
ckey = "My Project"  # set the client_key for the integration and use the same value for all API calls
#Retrieves GIF from site

def get_gif(searchTerm):

    r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (searchTerm, apikey, ckey,  limit))
    data =  json.loads(r.content)
    gif_choice = random.randint(0,9)
    url = data["results"][gif_choice]["url"]
    return url

def num_to_day(num):
    if num == 0:
        return "Monday"
    if num == 1:
        return "Tuesday"
    if num == 2:
        return "Wednesday"
    if num == 3:
        return "Thursday"
    if num == 4:
        return "Friday"
    if num == 5:
        return "Saturday"
    if num == 6:
        return "Sunday"
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
def handle_response(message) -> str:
    cst = pytz.timezone('US/Central')
    cst_date = datetime.datetime.now(cst)
    num = cst_date.weekday()
    today = num_to_day(num)
    p_message = message.lower()
    if p_message in days:
        pass
    elif 'yesterday' in p_message:
        num = (num - 1) % 7
        today = num_to_day(num)
        return get_gif("it is asuka " + str(today) + " evangelion")
    elif 'tomorrow' in p_message:
        num = (num + 1) % 7
        today = num_to_day(num)
        return get_gif("it is asuka " + str(today) + " evangelion")
    elif 'day' in p_message:
        return get_gif("it is asuka " + str(today) + " evangelion")
    elif 'today' in p_message:
        return get_gif("it is asuka " + str(today) + " evangelion")
    elif 'good bot' in p_message :
        return get_gif("asuka love evangelion")
    elif 'bad bot' in p_message:
        return get_gif("asuka mad evangelion")
    elif 'jackson' in p_message:
        return get_gif("jackson")
    else:
        pass
