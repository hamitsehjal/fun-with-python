aliens=[{'color':'pink','points':5},{'color':'red','points':10}]
print(aliens)
for alien in aliens[:3]:
    if alien['color'] == 'pink':
        alien['points']=50
        alien['color']='yellow'

print(aliens)
