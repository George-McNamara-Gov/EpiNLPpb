'''
Constants to support package/evaluate/base.py and package/evaluate/evaluate.py

Classes:

    None

Functions:

    None

Misc variables:

    TIME_MAX : int
        Maximum time (s) used to normalise the time value for the radial plot.
    SPACE_MAX : int
        Maximum space (B) used to normalise the space value the for radial plot.
    MEASURE_SIZES1 : list(int)
        A list of sample sizes for approximating complexity.
    MEASURE_SIZES2 : list(int)
        A list of sample sizes for approximating complexity.
    MEASURE_SIZES3 : list(int)
        A list of sample sizes for approximating complexity.
    MEASURE_SIZES4 : list(int)
        A list of sample sizes for approximating complexity.

Exceptions:

    None
'''

TIME_MAX = 200
SPACE_MAX = 10000000000

MEASURE_SIZES1 = [10,20,50,100,200]
MEASURE_SIZES2 = [20,50,100,200,500]
MEASURE_SIZES3 = [100,200,500,1000,2000]
MEASURE_SIZES4 = [200,500,1000,2000,5000]