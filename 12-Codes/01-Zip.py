countries = ['India','China','USA','Australia','Jamaica']

gold = [10,50,70,25,15]
silver = [30,100,120,55,32]
bronze = [34,120,134,76,56]

countries_with_gold = list(zip(countries,gold))
#print(countries_with_gold)

for c in countries_with_gold:
    print(str(c).strip('()'))

print("--------------Total Medals----------------")
for x in range(len(countries)):
    c = countries[x]
    g = gold[x]
    s = silver[x]
    b = bronze[x]
    print(c,g+s+b)
