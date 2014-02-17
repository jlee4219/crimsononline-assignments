def sortcat(n, *args):

    # sort the arguments by length, highest to lowest
    args = sorted(args, key=len, reverse=True)

    # default for string we'll return
    s = ''

    # if n is -1, concatenate all strings
    if n == -1:
        for i in args:
            s += i

    # else concatenate the first n
    else:
        for i in range(n):
            s += args[i]

    print s