def floor(x) -> int:
    return (
        x if isinstance(x, int) or x - int(x) == 0 else int(x) if x > 0 else int(x - 1)
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
