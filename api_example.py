from os import error
import requests
import gc 
from dotenv import load_dotenv
import os

total_cases = 0 # total across a state
aggregate_total = 0
counter_opinions = 0
counter_cases = 0

load_dotenv()

# parameters for request
page_size = 10000
date_min = '1980-01-01'
date_max = '2020-12-31'
region = 'midwest'
auth_token = os.getenv('CASELAW_KEY') # store in a private .env variable!
filename = f'{region}_opinions_1980-now.txt'

# regions
regions = {
    'northeast': {
        "conn":1, 
        "mass":1, 
        "me":1, 
        "nh":1, 
        "nj":1, 
        "ny":1, 
        "pa":1, 
        "ri":1, 
        "vt":1
    },
    'midwest': {
        "ill":1, 
        "ind":1, 
        "iowa":1, 
        "kan":1, 
        "mich":1, 
        "minn":1,
        "mo":1, 
        "nd":1, 
        "neb":1, 
        "ohio":1, 
        "sd":1, 
        "wis":1
    },
    'south': {
        "ala":1, 
        "ark":1, 
        "dc": 1,  
        "del": 1,  
        "fla": 1,  
        "ga": 1,  
        "ky": 1,  
        "la": 1,  
        "md": 1, 
        "miss": 1,  
        "nc": 1,  
        "okla": 1,  
        "sc": 1,  
        "tenn": 1,  
        "tex": 1,  
        "va": 1,  
        "w-va":1
    },
    'west': {
        "alaska": 1,  
        "ariz": 1,  
        "cal": 1,  
        "colo": 1,  
        "haw": 1,  
        "idaho": 1, 
        "mont": 1,  
        "nev": 1,  
        "nm": 1,  
        "or": 1,  
        "utah": 1,  
        "wash": 1,  
        "wyo": 1
    }

}

# TODO: start searching by each element in the region!! Add a loop around.

def parse_results(data, output):
    global counter_cases
    for case in data["results"]:
        for opinion in case["casebody"]["data"]["opinions"]:
            # Preprocess here
            text = opinion["text"].lower()
            output.append(text)
        
        counter_cases += 1

        if counter_cases % 10000 == 0:
            print(f'{counter_cases} of {total_cases} done')

def fetch_data(state):
    global total_cases
    global aggregate_total
    output = []
    url = f'https://api.case.law/v1/cases/?full_case=true&page_size={page_size}&decision_date_min={date_min}&decision_date_max={date_max}&jurisdiction={state}'
    first_page = True
    while url:
        s = requests.Session()
        s.headers.update({'Authorization': f'Token {auth_token}'})
        response = s.get(url)

        if response.ok:
            try:
                data = response.json()
            except Exception as e:
                print(e)
                return
            if first_page:
                first_page = False
                total_cases = data["count"]
                aggregate_total += total_cases
                print(total_cases)
            url = data["next"] # use for future tokens

            parse_results(data, output)
        else:
            break
    return output

def main():
    if auth_token is None:
        print(f'API key not found.')
        return

    global counter_cases
    missed_states = []
    print(f'Region selected: {region}')
    print(f'Time period selected: {date_min} to {date_max}')
    print(f'Output file name: {filename}')

    with open(filename, 'a') as output_file:

        for state in regions[region]:
            counter_cases = 0
            print(f"CURRENT STATE: {state}")
            output_list = fetch_data(state)

            if output_list is None:
                print(f'No results for {state}')
                missed_states.append(state)

            else:
                output_file.writelines(output_list)
                del output_list
                gc.collect()

        print(f'There were {aggregate_total} cases across the {region} region')
        print(missed_states)

main()
