# menus = [
#     ['eggs', 'cereal', 'waffel'],
#     ['Chicken soup', 'Thai Curry', 'Noodles'],
#     ['Rice' ,'Bread' ,'Steak']
# ]

# print ('Breakfast menu is:\t', menus [0])
# print('Lunch menu is:\t', menus[1])
# print ('Dinner menu is:\t', menus[2])

# print (menus [1][0])

menus = { 'Breakfast':  ['eggs', 'cereal', 'waffel'],
          'Lunch': ['Chicken soup', 'Thai Curry', 'Noodles'],
          'Dinner': ['Rice' ,'Bread' ,'Steak']

}

# print('Menu for Breakfast is:\t', menus ['Breakfast'])
# print('Menu for Lunch is:\t', menus ['Lunch'])
# print('Menu for Dinner is:\t', menus ['Dinner'])

for name,menu in menus.items():
    print (name ,':', menu)
