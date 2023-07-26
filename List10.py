def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    x = list_num[0]
    if list_num[-1]>list_num[0]:
        
        x = list_num[-1]
    return x
print(main([8,5,4,9,6]))