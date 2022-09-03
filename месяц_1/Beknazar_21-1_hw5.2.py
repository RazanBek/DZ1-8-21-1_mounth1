data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []
for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)
operations = {}
b = 0
while len(operations) != len(designations):
    operations[designations[b]] = codes[b]
    b += 1
del operations['Katel'], operations['Fonex']
operations['O!'] = [operations['O!']]
operations['Megacom'] = [operations['Megacom']]
operations['Beeline'] = [operations['Beeline']]
operations['O!'].extend({'0723', '0756' })
operations['O!'] = set(operations['O!'])
operations['Megacom'].extend({'0500', '0800'})
operations['Megacom'] = set(operations['Megacom'])
operations['Beeline'].extend({'0500', '0800'})
operations['Beeline'] = set(operations['Beeline'])
for k, v in operations.items():
    print(f'{k} - {v}')