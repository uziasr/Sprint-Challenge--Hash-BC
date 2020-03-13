#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    print(ht)
    if len(weights) < 2:
        return None
    if len(weights) == 2:
        (weights[0] + weights[1]) == limit
        return (1,0)
    for (index,weight) in enumerate(weights):
        hash_table_insert(ht,weight,index) #insert values into the hashtable where value is the key and index is the value
    for weight in weights:
        difference = limit - weight
        print(f"limit: {limit}, weight: {weight}")
        if hash_table_retrieve(ht,difference):
            print("this is the difference ", difference)
            difference_index = (hash_table_retrieve(ht, difference))
            weight_index = hash_table_retrieve(ht, weight)
            if difference_index > weight_index:
                return_tuple =(difference_index, weight_index)
                return  return_tuple
            else:
                return_tuple = (weight_index, difference_index)
                print("it gets this far", return_tuple)
                return return_tuple

        



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
