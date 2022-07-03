current_users = ['YeetMaster6000', 'JohnnyBadSeed', 'OwO', 'KingBossSlay42069', 'Wooza_Mister']
new_users = ['JohnnyBadSeed', 'discord_kitten_owo', 'YeetMaster6000', 'BigDaddy']

current_users_lower = [x.lower() for x in current_users]
new_users_lower = [y.lower() for y in new_users]

for new_user in new_users_lower:
     if new_user in current_users_lower:
        print('The username '+new_user+' is not available.')
     else:
         print('The username '+new_user+' has been accepted')
