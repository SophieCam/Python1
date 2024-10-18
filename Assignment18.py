from lib2to3.fixes.fix_tuple_params import tuple_name


def concat_tuples(tuple1, tuple2):
    #check if inputs are tuples
    if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
        raise ValueError("Both inputs must be tuples.")

    results = tuple1 + tuple2
    return results

try:
    tupleA = ( 1, 2, 3,4 )
    tupleB = ( 5, 6, 7, 8)

    result = concat_tuples(tupleA, tupleB)
    print(result)
except ValueError as e:
    print(e)