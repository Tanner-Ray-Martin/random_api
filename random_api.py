from random import choice

import helpers
from constants import random_json_urls

api_url = choice(random_json_urls)

api_response = helpers.hit_api(api_url)

for key, value in helpers.iter_data(api_response, parent=">>> "):
    print(key.split(".")[-1]+":", value)