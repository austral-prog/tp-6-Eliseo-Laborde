# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements)>5:
        del list_to_remove_elements[0]
        del list_to_remove_elements[3]
        del list_to_remove_elements[3]
    elif len(list_to_remove_elements)==5:
        del list_to_remove_elements[0]
        del list_to_remove_elements[2]
    elif len(list_to_remove_elements)==4:
        del list_to_remove_elements[0]
    elif len(list_to_remove_elements)==1:
        del list_to_remove_elements[0]
    else:
        list_to_remove_elements=list_to_remove_elements
    return(list_to_remove_elements)


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,"Pink")
    list_to_add_elements.append("Yellow")
    return(list_to_add_elements)

def is_empty(list_to_check):
    if list_to_check==[]:
        return(True)
    else:
        return(False)

def check_lists(list_to_compare1, list_to_compare2):
    if list_to_compare1[2]==list_to_compare2[2]:
        return(True)
    else:
        return(False)

def list_of_lists(list_of_lists_to_modify):
    list1 = list_of_lists_to_modify[0]
    list2 = list_of_lists_to_modify[1]
    list3 = list_of_lists_to_modify[2]

    if len(list1)>2:
        new_list1=[list1[0], list1[1]]
    else:
        new_list1=list1

    if len(list2)>=4:
        new_list2=list2[1:4]
    elif len(list2)==3:
        new_list2=list2[-2:]
    elif len(list2)==2:
        new_list2=[list2[-1]]
    else:
        new_list2=[]
    if len(list3)>=3:
        new_list3=list3[-2:]
    elif len(list3)==2:
        new_list3=[list3[-1]]
    else:
        new_list3=[]
    list_of_lists_to_modify=[new_list1, new_list2, new_list3]
    return(list_of_lists_to_modify)
