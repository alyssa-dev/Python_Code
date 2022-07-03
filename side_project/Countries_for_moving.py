import random
from tkinter import HORIZONTAL, VERTICAL

all_countries = [
    'Afghanistan', 'Albania', 'Algeria', ' America Samoa', 'Andorra', 'Angola', 'Aruba', 
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
    'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia' , 'Bosnia & Herzegovina',
    'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 
    'Cape Verde Islands', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Islands',
    'Colombia', 'Comoros Islands', 'Congo', 'Congo DR/', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 
    'Czechia', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Dutch Antilles', 'East Timor', 'Easter Island',
    'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 
    'Faroe Islands', 'Fiji Islands', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia', 
    'Georgia', 'Germany', 'Ghana', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guinea', 
    'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 
    'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya',
    'Kiribati Islands', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 
    'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldive Islands', 
    'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova',
    'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal',
    'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Northern Mariana', 'Norway', 
    'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 
    'Pitcairn Island', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Samoa', 
    'Sao Tome', 'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 
    'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Helena',
    'St. Kitts & Nevis', 'St. Lucia', 'St. Vincent & Gren.', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 
    'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tokelau Islands', 'Tonga', 'Trinidad', 'Tunisia', 
    'Turkey', 'Turkmenistan', 'Turks & Caicos', 'Tuvalu', 'UAE', 'Uganda', 'Ukraine', 'United Kingdom', 'Uruguay', 
    'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam',' Virgin Islands US','Virgin Islands UK', 'Wallis & Futuna', 
    'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe'
]


selected_countries, bad_countries, num_chosen = [], [], []
all_countries_length = len(all_countries)
for country in range(0, all_countries_length):
    rando = random.randrange(0, all_countries_length)
    while rando in num_chosen:
        rando = random.randrange(0, all_countries_length)
    num_chosen.append(rando)
    check_me = all_countries[rando]
    q = input(f'How does this country sound? --> {check_me}: ')
    if q == '':
        q = 'y'
    if q.lower() == 'y':
        selected_countries.append(check_me)
    else:
        bad_countries.append(check_me)

selected_val = len(selected_countries)
print(f'Out of the {all_countries_length} countries, only {selected_val} were chosen:')

for value in selected_countries:
    print(value, end = ', ')