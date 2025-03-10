#Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

#Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    return True

def is_leaf(tree):
    return not branches(tree)

#Test Trees
t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
t2 = tree('A', [tree('B'), tree('C', [tree('D'), tree('E')])])
t3 = tree(8,
          [tree(4,
                [tree(2), tree(3)]),
           tree(3,
                [tree(1), tree(1,
                               [tree(1), tree(1)])])])


def print_tree(tree, indent=0):
    print("  " * indent + str(label(tree))) # there are 2 spaces in the quotation marks

    for branch in branches(tree):
        print_tree(branch, indent + 1)


def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and False otherwise.
    >>> scrat = tree('acorn')
    >>> acorn_finder(scrat)
    True
    >>> sproul=tree('roots',[tree('branch1',[tree('leaf'),tree('acorn')]), tree('branch2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """

    if label(t) == 'acorn':
        return True

    for branch in branches(t):
        if acorn_finder(branch):
            return True

    return False

def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label that appears
    in vals removed.  Return None if the entire tree is pruned away.
    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6,[tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    if is_leaf(t):
        if label(t) in vals:
            return None
        return tree(label(t))

    pruned_branches = []

    for branch in branches(t):
        pruned_branch = prune_leaves(branch, vals)
        if pruned_branch is not None:
            pruned_branches.append(pruned_branch)

    if not pruned_branches and label(t) in vals:
        return None

    return tree(label(t), pruned_branches)

def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5
    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
        return tree(label(t), [tree(x) for x in vals])
    else:
        return tree(label(t), [sprout_leaves(branch, vals) for branch in branches(t)])

def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0

    return 1 + max([height(z) for z in branches(t)])

def double_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
                       [tree(2,
                             [tree(3),
                              tree(4)]),
                       tree(5,
                            [tree(6,
                                  [tree(7)]),
                             tree(8)])])
    >>> print_tree(double_tree(numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    """
    if is_leaf(t):
        return tree(label(t) * 2)

    return tree(label(t) * 2, [double_tree(z) for z in branches(t)])

