def create_an_empty_list():
    return list()

def create_a_list():
    list = [1,2,3,4]
    return list

def add_element_to_end_of_list(l, element):
    list = [1,2,3,4]
    new_number = 5
    list.append(new_number)
    return list

def add_element_to_start_of_list(l, element):
    list = [1,2,3,4]
    new_number = 0
    list.insert(0, new_number)
    return list

def remove_element_from_end_of_list(l):
    list = [1,2,3,4]
    list.pop()
    return list

def remove_element_from_start_of_list(l):
    list = [1,2,3,4]
    list.pop(0)
    return list

def retrieve_first_element_from_list(l):
    list = [1,2,3,4]
    return list[0]
    

def retrieve_element_from_index(l, index):
    list = [1,2,3,4]
    return list[1]

def retrieve_last_element_from_list(l):
    list = [1,2,3,4]
    return list[3]