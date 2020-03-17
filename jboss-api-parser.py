import requests
import time
import csv


def jboss_parser(user_limit):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'developer.jboss.org',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }
    limit = 700
    data = requests.get(
        f'https://developer.jboss.org/__services/v2/rest/users/-1/browse?filterGroupID=people&token=MTU4NDAwMjc3NTg0NHwyMHxbQkA1YTVkNjI1NA%3D%3D&itemViewID=detail&start={limit}&numResults=20&filterID=all&itemView=detail&userID=-1', headers=headers)
    lst.extend([i["username"] for i in data.json()['items']])
    print(data.json())

    while limit < user_limit:
        limit = limit + 20
        data = requests.get(
            f'https://developer.jboss.org/__services/v2/rest/users/-1/browse?filterGroupID=people&token=MTU4NDAwMjc3NTg0NHwyMHxbQkA1YTVkNjI1NA%3D%3D&itemViewID=detail&start={limit}&numResults=20&filterID=all&itemView=detail&userID=-1', headers=headers)
        lst.extend([i["username"] for i in data.json()['items']])


def writer(lst):
    with open("{}.txt".format(str(input("Enter file name: "))), "w", encoding="utf-8") as filename:
        writer = None
        for i in lst:
            output = {'Link': "https://developer.jboss.org/" + i}
            if not writer:
                writer = csv.DictWriter(filename, delimiter=";", fieldnames=output.keys())
                writer.writeheader()
            writer.writerow(output)


lst = []
user_limit = int(input('Set the limit: ').lower().strip(' '))
jboss_parser(user_limit)
print('Collected:', len(lst))
writer(lst)
