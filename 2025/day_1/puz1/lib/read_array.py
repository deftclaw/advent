def read_lines(leaf):
    lines = []

    with open(leaf, 'r') as handle:
        lines = handle.read().split('\n')

    return [ x for x in lines if x.strip() ]  # Remove empty lines from the array
