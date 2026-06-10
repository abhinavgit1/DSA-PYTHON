arr = [2, 7, 11, 15]
target = 9
seen = set()
for el in arr:
    req = target-el
    if req in seen:
        print(el,req)
    else:
        seen.add(el)



