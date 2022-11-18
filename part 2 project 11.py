#list of state names Abbreviations
abbreviations = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", 
"ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", 
"MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA",
"RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

#list of state names
states =['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 
'CONNECTICUT', 'DELAWARE', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS',
'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS', 
'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA', 
'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 
'OHIO', 'OKLAHOMA', 'OREGON','PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT','VIRGINIA', 'WASHINGTON', 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING']

print('this program will tell you abbreviations and states')
print()

run = True

while run == True:

    print('Enter s or a')
    print()

    whichWay = input('do you choose s or a: ').lower()

    while whichWay != 's' and whichWay != 'a':
        whichWay = input('INPUT ERROR: Please enter an s or a: ').lower()

    if whichWay == 's':
        word = 'states: '
        listToCheck = states
    else:
        word = 'abbreviations: '
        listToCheck = abbreviations

    userInput = input('Enter the ' + word).upper()
    while userInput not in listToCheck:
        userInput = input('Input Error: please enter a valid ' + word)
    print()

    if whichWay == 's':
        for mainIndex in range(len(states)):

            if userInput == states[mainIndex]:
                print('The state is ' + abbreviations[mainIndex] + '.')

    else:
          for mainIndex in range(len(states)):
              if userInput == states[mainIndex]:
                  print('The abbreviat is ' + abbreviations[mainIndex]+ '.')


    print()
    runAgain = input('would you like to run program again? (y/n): ').lower()

    while runAgain != 'y' and runAgain != 'n':
        runAgain = input('INPUT ERROR: Please enter a y or n: ').lower()

    if runAgain == 'n':
        run = False
    print()

    print('Have a nice day.')











        
        





        
