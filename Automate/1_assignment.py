def duplicate_list(list1: list, list2: list):
    res = []
    # convert list to set and use intersection to find duplicate number.
    intersec_set = set(list1).intersection(set(list2))
    # convert intersection set back to list.
    res = list(intersec_set)
    return res

def main():
    listA = [1,2,3,5,6,8,9]
    listB = [3,2,1,5,6,0]
    result_list = duplicate_list(listA, listB)
    print(result_list)

if __name__=="__main__":
    main()
