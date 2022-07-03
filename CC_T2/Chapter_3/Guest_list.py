ppl = ['Mom','Dad','Chad','Sarah','Jonathan']

invite_1 = f"Hey {ppl[0]} come on over for dinner at my place!"
invite_2 = f"Hey {ppl[1]} come on over for dinner at my place!"
invite_3 = f"Hey {ppl[2]} come on over for dinner at my place!"
invite_4 = f"Hey {ppl[3]} come on over for dinner at my place!"
invite_5 = f"Hey {ppl[4]} come on over for dinner at my place!"

print(invite_1)
print(invite_2)
print(invite_3)
print(invite_4)
print(invite_5)

popped = ppl.pop(3)
print(f"\n {popped} could not make it.")

invite_1 = f"Hey {ppl[0]} come on over for dinner at my place!"
invite_2 = f"Hey {ppl[1]} come on over for dinner at my place!"
invite_3 = f"Hey {ppl[2]} come on over for dinner at my place!"
invite_4 = f"Hey {ppl[3]} come on over for dinner at my place!"

print(f"\n{invite_1}")
print(invite_2)
print(invite_3)
print(invite_4)


ppl.insert(0, 'Mother Theresa')
ppl.insert(3, 'Hitler')
ppl.append('George the Monkey')

invite_1 = f"Hey {ppl[0]} come on over for dinner at my place!"
invite_2 = f"Hey {ppl[1]} come on over for dinner at my place!"
invite_3 = f"Hey {ppl[2]} come on over for dinner at my place!"
invite_4 = f"Hey {ppl[3]} come on over for dinner at my place!"
invite_5 = f"Hey {ppl[4]} come on over for dinner at my place!"
invite_6 = f"Hey {ppl[5]} come on over for dinner at my place!"
invite_7 = f"Hey {ppl[6]} come on over for dinner at my place!"

print("\nK, now I have room for three more peeps, so I am inviting them")

print(f"\n{invite_1}")
print(invite_2)
print(invite_3)
print(invite_4)
print(invite_5)
print(invite_6)
print(invite_7)

Nope = ppl.pop(4)
Noooo = ppl.pop(3)
n = ppl.pop(2)
Na = ppl.pop(1)
Nah = ppl.pop(0)

print("\nregretfully, we have learned there is no longer any room for more than two guests")

print(f"\nSadly, I can no longer invite you over {Nope}")
print(f"Really sorry mah dude, but you, {Noooo}, can no longer be invited")
print(f"Yeah, sorry, {n}, you are no longer invited")
print(f"It is with great regret that we must inform {Na} that they may no longer come over")
print(f"{Nah} you cant come over")

print(f"\n{ppl[0]} your cool, you can come over")
print(f"{ppl[1]} you can come over tho")

print("\nThe number of ppl left on the list is:")
print(len(ppl))

del ppl[0]
del ppl[0]

print("\nThe number of ppl left on the list is:")
print(len(ppl))


