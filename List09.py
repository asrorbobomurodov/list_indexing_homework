def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    l = len(list1)
    i = 0
    while l>0:
        l = l-1
        if list1[0] == list1[i]:
            x = True
        else:
            x = False
        i = i+1
    return x
print(main(["x","x","x","u"]))

# n=2
# print(n%2==0)