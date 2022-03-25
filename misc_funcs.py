import datetime

def get_todays_datetime(country):

    return 127

def get_2alpha_list(countries):
    with open("countries_iso_alpha.txt", "r") as txt:
        countries = txt.read().split("\n")
        countries_json = {}
    
        for n in range(0, len(countries), 2):
            countries_json.update({countries[n]: countries[n+1]})

        with open("list_countries.json", "w") as jsonfile:
            jsonfile.dumps(countries_json, indent=1)
    
        return countries_json