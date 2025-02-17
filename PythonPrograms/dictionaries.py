acronym = {'LOL': 'Laugh Out Loud', 'IDK': 'I dont Know','TBD': 'To Be Discussed', 'BTW':'By The Way'}

#print (acronym['LOL'])

#del (acronym['IDK'])
# definition = acronym.get ('BTW')
# if definition: print (definition)
# else:
#     print ('Key is not available')

#print (acronym)

sentence = 'IDK' + ' what happened but ' + 'LOL'
translation = acronym.get('IDK') + ' what happened but ' + acronym.get('LOL')

print ('sentence:', sentence)
print ('translation:', translation)