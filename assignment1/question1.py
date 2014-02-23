"""
Question 1

objectives
    - get more comfortable with Python
    - learn how to handle exceptions
    - work with the file system
"""

def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    from collections import Counter
    import re
    text = re.findall(r'\w+', open(filename).read())
    counts = Counter(text).most_common()
    return [k for (k,v) in counts]

    pass

def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    return [word for word in common_words(filename) if len(word) > min_chars]
    pass

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    from collections import Counter
    import re
    text = re.findall(r'\w+', open(filename).read())
    return [(k, v) for (k, v) in Counter(text).most_common() if len(k) > min_chars]
    pass

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try:
        common_words_tuple(filename, min_chars)
    except IOError:
        print "An IOError has occurred."
    pass