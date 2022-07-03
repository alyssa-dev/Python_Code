cities = {
    'Kokshetau' : {
        'Country':'Kazakhstan',
        'Population':'150,649',
        'Fact':'covers an area of 234 km 2 (90 sq mi).',
    },

    'Crawley' : {
        'Country':'United Kingdom',
        'Population':'106,597',
        'Fact':'The area has been inhabited since the Stone Age, and was a centre of ironworking in Roman times',
    },

    'La Victoria' : {
        'Country':'Venezuela',
        'Population':'2,336',
        'Fact':'The city has an annual flower count dating back to the 1970s. The total blooms counted in 2018 was over 3.4 billion.',
    },

}

for city, info in cities.items():
    print(f'{city}: ')
    for title, sin in info.items():
        print(f'\t{title.title()}: {sin}')