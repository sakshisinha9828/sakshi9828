s=set()
states = {'New Hampshire': ['Concord', 'Hanover'],'Massachusetts': ['Boston', 'Concord', 'Springfield'],'Illinois': ['Chicago', 'Springfield', 'Peoria'] }
d=dict()
for value in states:
   
    for value1 in states[value]:
        s.add(value1)

for value in s:
    for value1 in states:
        if value in states[value1]:
            x=d.get(value,None)
            if x is not None:
                d[value].append(value1)
            else:
                d[value]=[value1]
print(d)
