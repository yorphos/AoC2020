print((lambda x, y : 'Results:')(parsed := [(tuple(map(int, r.split('-'))), l[0], p) for r, l, p in [ff.split(' ') for ff in open('input2.txt', 'r').read().split('\n')][:-1]], part := 0),
    '-Part-' + str(part := part + 1) + '-> ' + str([pp.count(ll) in range(r0, r1 + 1) for (r0, r1), ll, pp in parsed].count(True)),
    '-Part-' + str(part := part + 1) + '-> ' + str([(pp[r0 - 1], pp[r1 - 1]).count(ll) == 1 if len(pp) >= r1 else pp[r0 - 1].count(ll) == 1 for (r0, r1), ll, pp in parsed].count(True)),
    sep='\n')
