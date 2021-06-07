with open('bootstrap.min.css') as f:
    d = f.read()
    l = ''
    for i in d:
        if i in '{;':
            i = i+'\n'
        elif i == '}':
            i = '\n' + i + '\n'
        l+=i
    with open('new.css', 'w') as k:
        k.write(str(l))
