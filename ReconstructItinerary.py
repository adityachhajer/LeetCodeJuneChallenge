tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
di={}
for i in tickets:
    if i[0] not in di.keys():
        di[i[0]]=[i[1]]
    else:
        c=di[i[0]]
        c.append(i[1])
        c=sorted(c)
        di[i[0]]=c
print(di)
itinerary, stack = [], [("JFK")]
while stack:
    curr=stack[-1]
    if curr in di.keys() and len(di[curr])>0:
        stack.append(di[curr].pop(0))
    else:
        itinerary.append(stack.pop(0))
print(itinerary)


