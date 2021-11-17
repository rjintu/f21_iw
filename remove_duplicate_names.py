white_1 = ('Adam, Chip, Harry, Josh, Roger, Alan, Frank, Ian, Justin, Ryan, '
'Andrew, Fred, Jack, Matthew, Stephen, Brad, Greg, Jed, Paul, Todd, Brandon, '
'Hank, Jonathan, Peter, Wilbur, Amanda, Courtney, Heather, Melanie, Sara, '
'Amber, Crystal, Katie, Meredith, Shannon, Betsy, Donna, Kristin, Nancy, Stephanie, '
'Ellen, Lauren, Peggy, Colleen, Emily, Megan, Rachel, Wendy')

black_1 = ('Alonzo, Jamal, Percell, Theo, Alphonse, Jerome, '
'Leroy, Torrance, Darnell, Lamar, Lionel, Rashaun, Tyree, Deion, Lamont, Malik, Terrence, Tyrone, Lavon, Marcellus, Terryl, Wardell, Aiesha, '
'Shereen, Ebony, Latisha, Shaniqua, Teretha, Jasmine, Latonya, Tanisha, Tia, '
'Lakisha, Latoya, Sharise, Yolanda, Malika, Tawanda, Yvette')

white_2 =  ('Abigail, Allison, Amy, Anne, Bradley, Brett, Caitlin, Carly, Carrie, Claire, Cody, Cole, Colin, Connor, Dustin, Dylan, Emily, Emma, Garrett, '
'Geoffrey, Greg, Hannah, Heather, Holly, Hunter, Jack, Jake, Jay, Jenna, Jill, '
'Katelyn, Katherine, Kathryn, Katie, Kristen, Logan, Luke, Madeline, Matthew, '
'Maxwell, Molly, Sarah, Scott, Tanner, Todd, Wyatt')

black_2 = ('Aaliyah, Alexus, Darius, Darnell, DeAndre, DeShawn, Deja, Dominique, Ebony, Jada, Jamal, Jasmin, Jasmine, Jazmine, Jermaine, Keisha, Kiara, LaShawn, Latonya, Latoya, Precious, Rasheed, Raven, '
'Terrance, Tremayne, Tyrone, Xavier')

white_3 = ('Molly, Amy, Claire, Emily, Katie, Madeline, Katelyn, Emma, '
'Abigail, Carly, Jenna, Heather, Katherine, Caitlin, Kaitlin, Holly, Allison, Kaitlyn, Hannah, Kathryn, Jake, Connor, Tanner, Wyatt, Cody, Dustin, Luke, Jack, '
'Scott, Logan, Cole, Lucas, Bradley, Jacob, Garrett, Dylan, Maxwell, Hunter, '
'Brett, Colin')

black_3 = ('Imani, Ebony, Aaliyah, Precious, Nia, Deja, Diamond, Asia, Jada, Tierra, Tiara, Kiara, Jazmine, Jasmin, Jazmin, Jasmine, Alexus, '
'Raven, DeShawn, DeAndre, Marquis, Darnell, Terrell, Malik, Trevon, Tyrone, '
'Willie, Dominique, Demetrius, Reginald, Jamal, Maurice, Jalen, Darius, Xavier, '
'Terrance, Andre, Darryl')

all_names = [white_1, black_1, white_2, black_2, white_3, black_3]
names_list = []

for name_set in all_names:
    curr = name_set.split(',')
    for i in range(len(curr)):
        curr[i] = curr[i].strip()
    names_list.append(curr)

all_white = set(names_list[0] + names_list[2] + names_list[4])
all_black = set(names_list[1] + names_list[3] + names_list[5])

print('Set of White names')
print(all_white)
print()
print('Set of Black names')
print(all_black)