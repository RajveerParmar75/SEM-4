list = []
l = [1, 2, 3, 4, 5, 6, 7]
print(len(l))
print(l[0::len(l)//2])
l1 = ["rajveer", 18, 5.9, "pending", "address"]
it_compnies = ['Facebook', 'Google', 'Microsoft',
               'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_compnies)
print(len(it_compnies))
print(it_compnies[0::len(it_compnies)//2])
it_compnies[0] = "mata"
print(it_compnies)
it_compnies.append("boat")
it_compnies.insert(len(it_compnies)//2, "demo")
it_compnies[3] = it_compnies[3].upper()
print("#".join(it_compnies))
print("certain" in it_compnies)
it_compnies.sort()
it_compnies.reverse()
print(it_compnies[:3])
print(it_compnies[-3:])
print(it_compnies[len(it_compnies)//2])
print(it_compnies.pop(0))
print(it_compnies.pop(len(it_compnies)//2))
print(it_compnies.pop())
it_compnies.clear()
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
demo = front_end+back_end
fullstack = demo.copy()
fullstack.append("redux")
fullstack.append("python")
fullstack.append("sql")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(max(ages), min(ages))
ages.append(max(ages))
ages.append(min(ages))
median = ages[len(ages)//2]
avg = sum(ages)/len(ages)
print(abs(min(ages)-avg), abs(max(ages)-avg))
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]
print(countries[len(countries)//2])
if len(countries) % 2 == 0:
    first = countries[:len(countries)/2]
    second = countries[len(countries)/2:]
else:
    countries.insert(0, 'India')
    first = countries[:len(countries)//2]
    second = countries[len(countries)//2:]
c1, c2, c3, *scandic = ['China', 'Russia', 'USA',
                        'Finland', 'Sweden', 'Norway', 'Denmark']
