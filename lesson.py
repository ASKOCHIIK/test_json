import json

"""load           -                 loads,  
   read           -              json > str

   dump           -                  dumps
   write          -               str > json
   """


def writer(data, filename):
    data = json.dumps(data)
    # data = json.loads(data)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

adam = {
    'имя': 'Айыма',
    'Aage': 17,
    'podruga': 'Malika',
    'Mage': 16
}

writer(adam, 'podruga.json')

with open('podruga.json') as file:
    print(json.load(file))

def hi(info):
    with open('info.json', 'w') as ayimochka:
        json.dump(info, ayimochka, indent=4)

an = {
    'Aiyma': 'Aiymochka',
    'email': 'aiyma_senior_pomidor@gmail.com'
}
hi(an)













