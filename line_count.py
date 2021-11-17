# count number of lines

curr_file = open(r'/Users/Firebolt/Documents/Sem5-Fall2021/cos397/f21_iw/data/northeast_opinions_1980-now.txt')

line = curr_file.readline()
counter = 0

while line:
    counter += 1
    line = curr_file.readline()

print(counter)
