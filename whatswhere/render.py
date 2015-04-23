import npyscreen

import itertools


def grid_sort_key(grid_key):
    env, pr_number = grid_key
    return pr_number

def render_grid(grid):
    for key, items in itertools.groupby(sorted(grid, key=grid_sort_key), grid_sort_key):
        right = ' '.join(
        print "PR #{pr_number}: {
