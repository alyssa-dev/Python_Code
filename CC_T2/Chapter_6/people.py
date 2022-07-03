#this is using an dictonary to store info on my loved ones

ppl = {
    'Chad' : {
        'age': '21',
        'city': 'Austin, Tx',
        'last_name': 'Smith',
        'first_name': 'Chad',
    },
    
    'Dad' : {
        'age' : '42',
        'city' : 'Austin, Tx',
        'last_name' : 'Smith',
        'first_name' : 'Joshua' ,
    },

    'Jonathan' : {
        'age' : '16',
        'city' : 'Austin, Tx',
        'last_name' : 'Smith',
        'first_name' : 'Jonathan',
    }

}

for people, info_ppl in ppl.items():
    print(f'Information on: {people.title()}')
    
    #assigning functions to make things easier
    full_name = f"{info_ppl['first_name']} " + f"{info_ppl['last_name']}"
    age = f"{info_ppl['age']}"
    location = f"{info_ppl['city']}"

    print(f'\tFull Name: {full_name}')
    print(f'\tCity and State: {location}')
    print(f'\tAge: {age}')