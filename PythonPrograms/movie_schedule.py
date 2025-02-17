currentmovies = {'Naal': '6:00 AM',
                 'Sairat': '10:00 AM',
                 'Shwas': '15:00 PM'
                }

print ('We are currently showing:') 
for key in currentmovies:
    print (key)

movie = input('Which movie would you like to watch? \n')

showtime = currentmovies.get (movie)

if showtime == None:
    print ('This movie is not running')
else:
    print ('Movie time is: ', showtime)



