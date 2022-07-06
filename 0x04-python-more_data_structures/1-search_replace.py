#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces occurence of search element with replace elements in my_list"""
    copy_list = my_list[:]
    for i in range(len(copy_list)):
        if copy_list[i] == search:
            copy_list[i] = replace
    return (copy_list)
