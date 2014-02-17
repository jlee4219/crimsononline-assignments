from collections import Counter

def swapchars (s):
    # make the string lowercase.  Use the counter module to count letters
    x = Counter(s.lower())
    counts = x.most_common()

    # defaults for high frequency and low frequency letters
    hifreq = ''
    lofreq = ''

    # loop through the counts, find the highest and lowest frequency
    # characters that are alphabetical
    for i in counts:
        if (i[0][0].isalpha()):
            hifreq = i[0][0]
            print hifreq
            break

    for i in (reversed(counts)):
        if (i[0][0].isalpha()):
            lofreq = i[0][0]
            print lofreq
            break

    # replace lower and uppercase versions of that letter
    s = s.replace(hifreq, lofreq)
    s = s.replace(hifreq.upper(), lofreq.upper())

    print s