number = {
    'Jen':['2', '1', '3', '235,456,754'],
    'Asswhole':['69', '80,082'],
    'motherfucker':['420', '8,008,132'],
    'Sarah':['23', '7,382,934'],
    'Ligma':['53', '234', '65', '12,345', '7,654'],
}

for name, fav in number.items():
    print(f'{name.title()}\'s favorite number is:')
    for f in fav:
        print(f'\t{f.title()}')     