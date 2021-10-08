'''
Parsing example with case.law
'''

import lzma
import json

NUM_CASES = 0
PRINT_DATA = False
with lzma.open("data/ala_text_20210921/data/data.jsonl.xz") as in_file:
    for line in in_file:
        case = json.loads(str(line, 'utf8'))
        if PRINT_DATA:
            print(case['name']) # get the name of the specific case
            print(case['jurisdiction']['name_long']) # get the name of the jurisdiction
            print(case['casebody']['data']['opinions'][0]['text']) # get the text of the opinion
            print(case['casebody']['data']['opinions'][0]['author']) # get the author (challenge: often no first name)
            print(case['decision_date']) # this is the decision date in YYYY-MM-DD format
            print(case['decision_date'][:4]) # get just the year, could use this for filtering purposes
        NUM_CASES += 1

print(NUM_CASES)
