# Use this script to pull the most frequently occurring terms from each corpus
# Find intersections as well
# Note: perhaps remove punctuation from consideration here

# perhaps create three charts: one showing similarities across ALL corpora, one showing similarities
# across all regions in each time period, and one showing similarities across all time periods in each
# region?

# import seaborn as sns
# import matplotlib.pyplot as plt

# regions = ['northeast', 'south', 'midwest', 'west', 'federal']
# times = ['1860-1889', '1890-1919', '1920-1949', '1950-1979', '1980-now']

# vocab_info = {}

# for time in times:
#     for region in regions:
#         filename = f'vocab_{region}_opinions_{time}_formatted.txt'
#         curr = open(filename, 'r')

#         entry_name = f'{region}_{time}'
#         for i in range(42):
#             line = curr.readline().split(' ')
#             if entry_name in vocab_info:
#                 vocab_info[entry_name].add((line[0]))
#             else:
#                 vocab_info[entry_name] = set()
#                 vocab_info[entry_name].add((line[0]))

# # now, find intersections
# all_corpora = []
# for entry_name in vocab_info:
#     all_corpora.append(vocab_info[entry_name])

# print(all_corpora)

# print(all_corpora[0].intersection(*all_corpora))

# # all_corpora = set(all_corpora)
# # for elem in all_corpora:
# #     print(elem)

# # most frequent terms across time period? 
# corpora_time = []
# for time in times:
#      #print(time)
#     for entry_name in vocab_info:
#         if time in entry_name:
#             corpora_time.append(vocab_info[entry_name])
#     # print(corpora_time[0].intersection(*corpora_time))
#     corpora_time = []


# # most frequent terms across region?
# corpora_region = []
# for region in regions:
#     print(region)
#     for entry_name in vocab_info:
#         if region in entry_name:
#             corpora_time.append(vocab_info[entry_name])
#     print(corpora_time[0].intersection(*corpora_time))
#     corpora_region = []

# histogram of term frequencies (excluding words < 10 times)

# region = 'northeast'
# time = '1860-1889'
# frequencies = []
# filename = f'vocab_{region}_opinions_{time}_formatted.txt'
# curr = open(filename, 'r')

# entry_name = f'{region}_{time}'
# line = curr.readline()

# while line:
#     frequencies.append(line.split(' ')[1][:-1])
#     line = curr.readline()

# print(frequencies)

# sns.histplot(data=frequencies, color = 'navy', bins = 20)
# plt.show()


