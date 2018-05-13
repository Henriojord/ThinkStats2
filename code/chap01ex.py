"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def CleanFemPreg(df):
    """Recodes variables from the pregnancy frame.

    df: DataFrame
    """

    pass

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemPreg(df)

    return df

def check_pregnum(resp):
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)

    for index, pregnum in resp.pregnum.items():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        if len(indices) != pregnum:
            print('Respondent {} has a pregnum of {} but {} pregnancies recorded'.format(caseid, pregnum, len(indices)))

            return False

    return True

def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    resp = ReadFemResp()
    #Compare Respondent's pregnum and NSFG codebook
    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    #Compare Respondent's pregnum and number of records in file
    assert(check_pregnum(resp))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
