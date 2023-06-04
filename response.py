import requests
from datetime import datetime
import random
import json


apikey = "token"
limit = 10
ckey = "My Project"  # set the client_key for the integration and use the same value for all API calls
#Retrieves GIF from site

def get_gif(searchTerm):

    r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (searchTerm, apikey, ckey,  limit))
    data =  json.loads(r.content)
    gif_choice = random.randint(0,9)
    url = data["results"][gif_choice]["url"]
    return url


def handle_response(message) -> str:
    today = datetime.today().strftime('%A')
    p_message = message.lower()
    if 'day' in p_message:
        return get_gif("it is asuka " + str(today) + " evangelion")
    if 'today' in p_message:
        return get_gif("it is asuka " + str(today) + " evangelion")
    if 'good bot' in p_message :
        return get_gif("asuka love evangelion")
    if 'bad bot' in p_message:
        return get_gif("asuka mad evangelion")
    if 'jackson' in p_message:
        return get_gif("jackson")
    else:
        pass
