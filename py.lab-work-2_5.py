'''Write the code to do following:
* create dict with 5 items, where keys will be country name and value
- domain name, i.e. {Ukraine:UA}
* create another dict with 5 items, where values of countries will be keys,
and values will be the capitals i.e. {'UA': 'Kiev'}
* add one more element to each dict above
* print sentence "Domain for COUNTRY is DOMAIN."
for each record in countries with the replace from dicts
* print sentence "The capital of COUNTRY is CAPITAL"
for each record in capitals with the replace from dicts
* Merge sentences above together with one cycle
* Add to each value of first dict another two domains: COM and GOV'''

# Mapping of coutry to their domain code
countries = {
	'Ukraine': 'UA',
	'Belgium': 'BE',
	'England': 'UK',
	'Italy': 'IT',
	'Germany': 'DE'
	}

capitals = {
	'UA': 'Kyiv',
	'BE': 'Brussels',
	'UK': 'Londan',
	'IT': 'Rome',
	'DE': 'Berlin'
	}
# add one more element to each dict above
countries['Netherlands'] = 'NL'
capitals['NL'] = 'Amsterdam'

for key, value in countries.items():
	print ("Domain for {} is {}.".format(key, value))

for key, value in capitals.items():
	print ("The capital of {} is {}".format(key, value))	

for key, value in countries.items():
	print ("Domain for {} is {}.The capital is {}".format(key, value, capitals[value]))
		
for key, value in countries.items():
	countries[key] = [value, 'COM', 'GOV']
	
for key, value in countries.items():
	print ("Domain for {} is {}.The capital is {}".format(key, value, capitals[value[0]]))