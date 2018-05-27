"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
import math
from operator import itemgetter

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """

    all_modes = AllModes(hist)

    return all_modes[0][0]


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """

    pairs = [(k, hist[k]) for k in hist.Values()]
    sorted_pairs = sorted(pairs, key=lambda x:x[1], reverse=True)

    return sorted_pairs


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)

    #Weight comparison (exercice 2-4)
    first_mean, firsts_var, nfirsts = firsts.totalwgt_lb.mean(), firsts.totalwgt_lb.var(), len(firsts.totalwgt_lb)
    others_mean, others_var, nothers = others.totalwgt_lb.mean(), others.totalwgt_lb.var(), len(others.totalwgt_lb)
    pooled_var = (nfirsts * firsts_var + nothers * others_var) / (nfirsts + nothers)

    d = (first_mean - others_mean) / (math.sqrt(pooled_var))
    print('Total weight lb d cohen between first and others:', d)
    print('Firsts babies tend to be lighter than others, but the difference is not significant')


if __name__ == '__main__':
    main(*sys.argv)
