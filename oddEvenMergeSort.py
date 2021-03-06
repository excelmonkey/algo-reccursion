# Batcher Even-Odd Sort
# Source: Wiki Article
#http://en.wikipedia.org/wiki/Batcher_odd%E2%80%93even_mergesort


def oddeven_merge(lo, hi, r):
    step = r * 2
    if step < hi - lo:
        yield from oddeven_merge(lo, hi, step)
        yield from oddeven_merge(lo + r, hi, step)
        yield from [(i, i + r) for i in range(lo + r, hi - r, step)]
    else:
        yield (lo, lo + r)
 
def oddeven_merge_sort_range(lo, hi):
    """ sort the part of x with indices between lo and hi.
 
    Note: endpoints (lo and hi) are included.
    """
    if (hi - lo) >= 1:
        # if there is more than one element, split the input
        # down the middle and first sort the first and second
        # half, followed by merging them.
        mid = lo + ((hi - lo) // 2)
        yield from oddeven_merge_sort_range(lo, mid)
        yield from oddeven_merge_sort_range(mid + 1, hi)
        yield from oddeven_merge(lo, hi, 1)
 
def oddeven_merge_sort(length):
    """ "length" is the length of the list to be sorted.
    Returns a list of pairs of indices starting with 0 """
    yield from oddeven_merge_sort_range(0, length - 1)
 
def compare_and_swap(x, a, b):
    if x[a] > x[b]:
        x[a], x[b] = x[b], x[a]


##########################
####Inputs

# >>> data = [2, 4, 3, 5, 6, 1, 7, 8]
# >>> pairs_to_compare = list(oddeven_merge_sort(len(data)))
# >>> pairs_to_compare
# [(0, 1), (2, 3), (0, 2), (1, 3), (1, 2), (4, 5), (6, 7), (4, 6), (5, 7), (5, 6), (0, 4), (2, 6), (2, 4), (1, 5), (3, 7), (3, 5), (1, 2), (3, 4), (5, 6)]
# >>> for i in pairs_to_compare: compare_and_swap(data, *i)
# >>> data
# [1, 2, 3, 4, 5, 6, 7, 8]

