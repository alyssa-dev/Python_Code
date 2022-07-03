glossary = {
    'value':'information associated with a variable',
    'list':'a variable that holds multiple values.',
    'for loop':'''something that loops a list through a set of instructions 
until there are no more values''',
    'Conditions':'Whether something is considered True or False by the code.',
    'tuple':'a sort of list that cannot be amended in any way',
    'Debugger':'''Breaks the code into a step by step showing of what the code is doing.
Used to find flaws and bugs in the code.''',
    'Semantic Errors':'''Bugs that prevent the program from doing what is intended.''',
    'Variable Scopes':'''Variables created inside a function are local scopes and variable 
created outside a function are called global scopes.''',
    'Syntax Errors':'When the error is one of spelling',
    'range()':'''Goes from one number to another. For example: range(4) = 0 to 3
and range(1, 9) = 1 to 8''',
}

print('A glossary of python:')
for word, difine in glossary.items():
    print(f'\n{word.title()}: \n{difine}')