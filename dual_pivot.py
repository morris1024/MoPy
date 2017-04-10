'''
a dual-pivot-quick-sort test module
'''
def dual_pivot_sort(data, key=None, reverse=False):
    '''
    data: list | data to be sorted
    key: function | get value to compare
    reverse: boolean | reverse
    '''
    dual_pivot_sort_core(data, 0, len(data)-1, key)
    if reverse:
        data.reverse()

def dual_pivot_sort_core(data, start_index, end_index, key):
    '''
    core function for dual_pivot_sort
    '''
    if start_index > end_index:
        return
    if key is None:
        value_wrap = lambda v: v
    else:
        value_wrap = key
    pivot1 = data[start_index]
    pivot2 = data[end_index]
    if value_wrap(pivot2) < value_wrap(pivot1):
        exchange(data, start_index, end_index)
    if value_wrap(pivot1) == value_wrap(pivot2):
        while value_wrap(pivot1) == value_wrap(pivot2) and start_index < end_index:
            start_index += 1
            pivot1 = data[start_index]
    i = start_index + 1
    lt = start_index + 1
    gt = end_index - 1

    while i <= gt:
        if value_wrap(data[i]) < value_wrap(pivot1):
            exchange(data, i, lt)
            i += 1
            lt += 1
        elif value_wrap(data[i]) > value_wrap(pivot2):
            exchange(data, i, gt)
            gt -= 1
        else:
            i += 1
    lt -= 1
    gt += 1
    exchange(data, start_index, lt)
    exchange(data, end_index, gt)

    dual_pivot_sort_core(data, start_index, lt-1, key)
    dual_pivot_sort_core(data, lt+1, gt-1, key)
    dual_pivot_sort_core(data, gt+1, end_index, key)

def exchange(data, index1, index2):
    '''
    exchange function
    '''
    tmp = data[index1]
    data[index1] = data[index2]
    data[index2] = tmp

if __name__ == '__main__':
    d = [4, 3, 1, 5, 2, 5]
    print(d)
    dual_pivot_sort(d)
    print(d)
