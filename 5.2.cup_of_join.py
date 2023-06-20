def join(*lists, separate='-'):
    """Concatenates an arbitrary number of lists."""
    if lists is None:
        return None
    result = []
    for lst in lists:
        result = result + lst + [separate]
    return result[:-1]


def main():
    assert (join([1, 2], [8], [9, 5, 6], separate='@') == [1, 2, '@', 8, '@', 9, 5, 6])
    print("All work good")


if __name__ == '__main__':
    main()
