import requests
dates = [
    '2020',
    '2021',
    '2022'
]
def get_deaths(date):
    response = requests.get('https://covid-api.com/api/reports/total?date=' + date)
    year = date.split('-', 1)
    if response.status_code == 200:
        if (year[0] not in dates):
            return ("No results for that year")
        else:
            data = response.json()
            return (data['data']['deaths'])
    else:
        return ("No results for that year")
input_year = input("Year for deaths: ")
print(get_deaths(input_year + '-12-31'))