politicleParties=["AAP", "Elephent", "Hand", "Rest"]
electionYear=['2014', '2009', '2005', '2001', "quit"]
countryStatus=["worst", "developing", "developed"]
corruptionStatus=["Max", "Normal", "Min"]

while politicleParties:
    year = input("Enter Year:: ")
    if year in electionYear:
        if year == "2014":
            print("AAp Wins!")
            print("Country status: "+ countryStatus[2])
            print("Corruption Status: "+ corruptionStatus[2])
            #break

        elif year == "2009":
            print("Hand Won:")
            print("Country status: " + countryStatus[0])
            print("Corruption Status: " + corruptionStatus[0])
            #break

        elif year == "2005":
            print("Hand won!")
            print("Country status: " + countryStatus[0])
            print("Corruption Status: " + corruptionStatus[0])
            #break

        elif year == "2001":
            print("Rest Won!")
            #break

        elif year == "quit":
            print("You wanted to exit")
            break
    else:
        print("Wrong year of election, Do you want to continue? y/n")
        a = input("Enter Decesion: ")
        if a == 'y' or a == 'Y':
            #print("Input Year: ")
            continue
        else:
            print("Exit")
            break

else:
    print("The above loop was just for demonstration purpose!")