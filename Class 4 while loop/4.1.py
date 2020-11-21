politicleParties=['AAP', 'Elephant', 'Hand', 'Rest']
electionYear = ['2014', '2009', '2005', '2001']
countryStatus = ['wrost', 'developing', 'developed']
corruptionStatus = ['Max', 'Normal', 'Min']

while politicleParties:
    year = input('Enter a year:: ')

    if year in electionYear:
        if year == '2014' or year == quit:
            print('AAP Wins!')
            print('Country Status: ' + countryStatus[2])
            print("Corruption Status: " + corruptionStatus[2])
            #break
        elif year == '2009':
            print('Hand Won: ')
            print('Country status: ' + countryStatus[0])
            print("Corruption Status: " + corruptionStatus[0])
            #break

        elif year == '2005':
            print('Hand won!')
            print('Country status: “' + countryStatus[0])
            print('Corruption Status: ' + corruptionStatus[0])
            #break

        elif year == '2001':
            print('Rest Won!')
            #break

        else:
            print('Wrong year of election!')
    else:
        print('You wanted to quit program!')
        break

