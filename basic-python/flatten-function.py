
def flatten(n): # the function makes the lists flatten. n is a list.
    for i in n:
        if isinstance(i, list): # checks the if element of a list is a list, and if it is a list calls the flatten function again.
            flatten(i)
        else:
            lnew.append(i)
