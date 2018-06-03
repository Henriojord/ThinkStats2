import thinkstats2

def mean(pmf):
    m = 0

    for x, p in pmf.Items():
        m += p * x

    return m

def var(pmf):
    m = mean(pmf)
    s = 0

    for x, p in pmf.Items():
        s += p * (x - m)**2

    return s


d = { 7: 8, 12: 8, 17: 14, 22: 4,
     27: 6, 32: 12, 37: 8, 42: 3, 47: 2 }

pmf = thinkstats2.Pmf(d, label='PMF')

assert pmf.Mean() == mean(pmf), 'Mean function uncorrect'

assert pmf.Var() == var(pmf), 'Var function uncorrect'

print('All tests passed.')
