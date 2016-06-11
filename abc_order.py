b = raw_input('')
a = b.split()
minimum = a[0]
result = [ ]
count = len(a)
for x in range(count):
    minimum = a[0]
    for i in a:
        if i > minimum:
            continue
        else:
            minimum = i
    result.append(minimum)
    print minimum
    a.remove(minimum)

