### RANDOM URLS ###

random_json_urls = [
    "https://api.quotable.io/quotes/random", # get a random quote
    "https://opentdb.com/api.php?amount=1", # random trivia question
    "http://api.open-notify.org/astros.json", # people currently in space
    "https://api.data.gov.sg/v1/environment/air-temperature", #singapore weather
    "https://fakerapi.it/api/v1/credit_cards?_quantity=1", # fake credit card data
    "https://randomuser.me/api/", # random user data
    "https://celestrak.org/NORAD/elements/gp.php?INTDES=2023-015&FORMAT=JSON-PRETTY", # satellite data
    "https://www.asterank.com/api/skymorph/search?target=J99TS7A", # astroids, minor planets, and other objects
    "https://inspirehep.net/api/literature/451647", # scholarly information about high energy physics
    "https://cat-fact.herokuapp.com/facts/random", # random fact about cats
    "https://vpic.nhtsa.dot.gov/api/vehicles/GetVehicleTypesForMake/merc?format=json", # vehicle types
    "https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json", # US Congress Stock transactions
    "https://binaryjazz.us/wp-json/genrenator/v1/genre/1", # random music genre
    "https://api.themotivate365.com/stoic-quote", # random stoic quote
    "https://quote-garden.onrender.com/api/v3/quotes?limit=1", # random quote
    "https://api.kanye.rest/", # random kanye quote
    "https://www.affirmations.dev/", # random affirmation
    "https://official-joke-api.appspot.com/random_joke", # random joke
]

from random import randint

random_url = f"https://api.fisenko.net/v1/quotes/en?query=string&offset={randint(0, 500)}&limit=1" # random quote
random_json_urls.append(random_url)

random_html_urls = [
    "https://loripsum.net/api/10/short/headers", # absolute gibberish html
    "https://api.fbi.gov/wanted/v1/list", # FBIs most wanted
    ]