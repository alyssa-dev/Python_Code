#makes a list of ppls favorite places
fav_places = {
        'SHAWTY':['California', 'Italy', 'France'],
        'Alyssa':['Spain', 'Florida', 'Belize', 'Brazil'],
        'FATHER FIGURE':['Neverland', 'Milk', 'GassStation'],
}

for name, place in fav_places.items():
    print(f'{name.title()}\'s favorite places are:')
    for pla in place:
        print(f'\t{pla.title()}')