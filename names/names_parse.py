import csv

with open('firstnames.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    NUM_ROWS = 0
    AVG_OBS = 0
    for row in reader:
        NUM_ROWS += 1
        AVG_OBS += int(row['obs'])
        # should we add a filter for obs (number of observances). Maybe > 300?
        # may need to tune these parameters
        if int(row['obs']) > 50 and float(row['pctblack']) > 40:
            print(row['firstname'])


        #print(row['firstname'])
    print('Summary statistics')
    print(NUM_ROWS)
    print(AVG_OBS)
    print(AVG_OBS / NUM_ROWS)
