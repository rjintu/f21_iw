WHITE_1 = ('Adam, Chip, Harry, Josh, Roger, Alan, Frank, Ian, Justin, Ryan, '
'Andrew, Fred, Jack, Matthew, Stephen, Brad, Greg, Jed, Paul, Todd, Brandon, '
'Hank, Jonathan, Peter, Wilbur, Amanda, Courtney, Heather, Melanie, Sara, '
'Amber, Crystal, Katie, Meredith, Shannon, Betsy, Donna, Kristin, Nancy, Stephanie, '
'Ellen, Lauren, Peggy, Colleen, Emily, Megan, Rachel, Wendy')

BLACK_1 = ('Alonzo, Jamal, Percell, Theo, Alphonse, Jerome, '
'Leroy, Torrance, Darnell, Lamar, Lionel, Rashaun, Tyree, Deion, Lamont, Malik, Terrence, Tyrone, Lavon, Marcellus, Terryl, Wardell, Aiesha, '
'Shereen, Ebony, Latisha, Shaniqua, Teretha, Jasmine, Latonya, Tanisha, Tia, '
'Lakisha, Latoya, Sharise, Yolanda, Malika, Tawanda, Yvette')

WHITE_2 =  ('Abigail, Allison, Amy, Anne, Bradley, Brett, Caitlin, Carly, Carrie, Claire, Cody, Cole, Colin, Connor, Dustin, Dylan, Emily, Emma, Garrett, '
'Geoffrey, Greg, Hannah, Heather, Holly, Hunter, Jack, Jake, Jay, Jenna, Jill, '
'Katelyn, Katherine, Kathryn, Katie, Kristen, Logan, Luke, Madeline, Matthew, '
'Maxwell, Molly, Sarah, Scott, Tanner, Todd, Wyatt')

BLACK_2 = ('Aaliyah, Alexus, Darius, Darnell, DeAndre, DeShawn, Deja, Dominique, Ebony, Jada, Jamal, Jasmin, Jasmine, Jazmine, Jermaine, Keisha, Kiara, LaShawn, Latonya, Latoya, Precious, Rasheed, Raven, '
'Terrance, Tremayne, Tyrone, Xavier')

WHITE_3 = ('Molly, Amy, Claire, Emily, Katie, Madeline, Katelyn, Emma, '
'Abigail, Carly, Jenna, Heather, Katherine, Caitlin, Kaitlin, Holly, Allison, Kaitlyn, Hannah, Kathryn, Jake, Connor, Tanner, Wyatt, Cody, Dustin, Luke, Jack, '
'Scott, Logan, Cole, Lucas, Bradley, Jacob, Garrett, Dylan, Maxwell, Hunter, '
'Brett, Colin')

BLACK_3 = ('Imani, Ebony, Aaliyah, Precious, Nia, Deja, Diamond, Asia, Jada, Tierra, Tiara, Kiara, Jazmine, Jasmin, Jazmin, Jasmine, Alexus, '
'Raven, DeShawn, DeAndre, Marquis, Darnell, Terrell, Malik, Trevon, Tyrone, '
'Willie, Dominique, Demetrius, Reginald, Jamal, Maurice, Jalen, Darius, Xavier, '
'Terrance, Andre, Darryl')

# Extra sets, for testing
BLACK_4 = ('Aisha, Ebony, Keisha, Kenya, Lakisha, Latonya, Latoya, Tamika, Tanisha, Darnell, Hakim, Jamal, Jermaine, Kareem, Leroy, Rasheed, Tremayne, Tyrone')

BLACK_5 = ('Jalen DeAndre Malia Tanisha Jabari Taniya Darius Janae Hakim Kenya '
           'Lamar Reginald Monique Latoya Keyshawn Divine Maurice Heaven Tremayne Lakisha '
           'DaQuan Marques Shania Aisha Dwayne Keyana Jayvon Erykah Delroy Precious '
           'Nia Cedric Jada Rasheed Marquise Bria Latrell Octavia Jerome Kiara '
           'Ebony Aaliyah DeShawn Darnell Tamia Savion Tionna Denzel Keisha Kareem '
           'Shanice Denisha Malcom Tyrone Kimani D’Andre Lyric Terrell Latonya Leroy '
           'Tyra Jasmine Quincy Jamal Aniya Jaleel Kaylah Wendell Tamika Terell '
           'Unique Chanel Andre Jermaine Amari Kevon Sade Tevin Ashanti Deshawn')

all_names = [WHITE_1, BLACK_1, WHITE_2, BLACK_2, WHITE_3, BLACK_3, BLACK_4, BLACK_5]
names_list = []

for name_set in all_names[:-1]:
    curr = name_set.split(',')
    for i in range(len(curr)):
        curr[i] = curr[i].strip()
    names_list.append(curr)

curr = all_names[-1].split(' ')
for i in range(len(curr)):
    curr[i] = curr[i].strip()
names_list.append(curr)

all_white = set(names_list[0] + names_list[2] + names_list[4])
all_black = set(names_list[1] + names_list[3] + names_list[5] + names_list[6] + names_list[7])

print('Set of white names')
print(all_white)
print()
print('Set of black names')
print(all_black)

# pipe names to output file
# with open('white_names.txt', 'w') as white_output:
#     for name in all_white:
#         white_output.write(name + '\n')

with open('black_names2.txt', 'w') as black_output:
    for name in all_black:
        black_output.write(name + '\n')
