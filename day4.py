lgs = []
lg = []
attrs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
stuff = (open('input4.txt', 'r')).read().split('\n')
for i, line in zip(range(len(stuff)), stuff):
    if i == len(stuff) - 1 or (not len(line)):
        lgs.append(lg)
        lg = []
    elif len(line):
        lg.append(line)
for i, group in zip(range(len(lgs)), lgs):
    lgs[i] = [attr.split(':') for attr in ' '.join(group).split(' ')]

truthyA = [all([attr in [attrg[0] for attrg in group] for attr in attrs]) for group in lgs]
truthyB = []
for group in lgs:
    if(all([a in [attr[0] for attr in group] for a in attrs])):
        it = []
        for attrg in group:
            switcher = {'byr': lambda x: (lambda a, b: (lambda x: int(x) >= a and int(x) <= b))(1920, 2002)(x), 'iyr': lambda x: (lambda a, b: (lambda x: int(x) >= a and int(x) <= b))(2010, 2020)(x), 'eyr': lambda x: (lambda a, b: (lambda x: int(x) >= a and int(x) <= b))(2020, 2031)(x), 'hgt': lambda x: (lambda a, b: (lambda x: int(x) >= a and int(x) <= b))(150, 193)(x[:-2]) if x[-2:] == 'cm' else (lambda a, b: (lambda x: int(x) >= a and int(x) <= b))(59, 76)(x[:-2]) if x[-2:] == 'in' else False, 'hcl': lambda x: x[0] == '#' and len(x[1:]) == 6 and all([y in [*list(map(str, range(10))), 'a', 'b', 'c', 'd', 'e', 'f'] for y in x[1:]]), 'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 'pid': lambda x: len(x) == 9, 'cid': lambda x: True}
            truthy = switcher[attrg[0]](attrg[1])
            it.append(truthy)
        truthyB.append(all(it))
    else:
        truthyB.append(False)

# one line attempt so far
# print(a := [all([{'byr': lambda x: (lambda a, b: (lambda x: int(x) >= a and int(x) <= b))(1920, 2002)(x), 'iyr': lambda x: (lambda a, b: (lambda x: int(x) >= a and int(x) <= b))(2010, 2020)(x), 'eyr': lambda x: (lambda a, b: (lambda x: int(x) >= a and int(x) <= b))(2020, 2031)(x), 'hgt': lambda x: (lambda a, b: (lambda x: int(x) >= a and int(x) <= b))(150, 193)(x[:-2]) if x[-2:] == 'cm' else (lambda a, b: (lambda x: int(x) >= a and int(x) <= b))(59, 76)(x[:-2]) if x[-2:] == 'in' else False, 'hcl': lambda x: x[0] == '#' and len(x[1:]) == 6 and all([y in [*list(map(str, range(10))), 'a', 'b', 'c', 'd', 'e', 'f'] for y in x[1:]]), 'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 'pid': lambda x: len(x) == 9, 'cid': lambda x: True}[attr.split(':')[0]](attr.split(':')[1]) for attr in attrs.replace(';', ' ').split(' ')[:-1]]) if all([a in [attr.split(':')[0] for attr in attrs.replace(';', ' ').split(' ')[:-1]] for a in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']]) else False for attrs in ';'.join(m.split('\n')).split(';;')])
print(truthyA.count(True), truthyB.count(True))

