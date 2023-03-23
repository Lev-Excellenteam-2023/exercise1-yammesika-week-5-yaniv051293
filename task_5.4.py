def interleave(*args):
    """
    A function that accepts one or more iterable parameters,
    and returns a list of the interwoven members
    :param args: lists, tuples or strings
    :return: a list of the interwoven members
    """
    for i in range(0, len(args[0])):
        for lst in args:
            yield lst[i]
    return


def main():
    lst=[]
    for word in interleave('abc', [1, 2, 3], ('!', '@', '#')):
        lst.append(word)
    print(lst)


if __name__ == '__main__':
    main()
