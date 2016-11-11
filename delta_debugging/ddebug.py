
from covenant import pre, post
from sudoku import draw_sudoku
from test_sudoku import test_sudoku, create_random_constraints
from stringsearch import no_rats

    
@pre(lambda data, granularity: len(data) > 1)
@post(lambda subsets, data, granularity: min(map(len, subsets)) > 0)
def get_partitions(data, granularity):
    """Produces #granularity subsets with left out slices from data"""
    subsets = []
    size = max(1, len(data) / granularity)
    start = 0
    while start < len(data):
        end = start + size
        subset = data[:int(start)] + data[int(end):]
        subsets.append(subset)
        start = end
    return subsets
    # yield incompatible with @post

@pre(lambda data, test, granularity: test(data)=='FAIL')
@post(lambda result, data, test, granularity: test(result)=='FAIL')
def delta_debug(data, test, granularity=2):
    print('\nexamining "{1}" (granularity={0})'.format(granularity, data))
    for subset in get_partitions(data, granularity):
        result = test(subset)
        print('{} -> {}'.format(subset, result))
        if result == 'FAIL':
            if len(subset) > 1:
                return delta_debug(subset, test, granularity)
            else:
                return subset # minimal failing subset
    if granularity < len(data):
        return delta_debug(data, test, granularity + 1)
    return data



if __name__ == '__main__':
    constraints = [(1,1,9), (1,2,3), (8,8,7), (4,2,9), (2,2,9)]
    constraints = [(1,1,9), (1,2,3), (8,8,7), (2,2,9)]
    constraints = [(1,1,1), (2,1,2), (3,1,3), (4,2,1), (5,2,2), (6,2,3), (7,3,7), (8,3,8), (9,3,9)]
    #constraints = [(1,1,1), (2,1,2), (3,1,3)]
    minimal = delta_debug(constraints, test_sudoku)
    print(draw_sudoku(constraints))
    print('minimal failing subset:')
    print(draw_sudoku(minimal))

    """
    # Example 3
    for i in range(10):
        constraints = create_random_constraints()
        if test_sudoku(constraints) == 'FAIL':
            print("run #", i)
            print(i, "#constraints:", len(constraints))
            minimal = delta_debug(constraints, test_sudoku)
            print(draw_sudoku(constraints))
            print(draw_sudoku(minimal))
            print(minimal)
    """
