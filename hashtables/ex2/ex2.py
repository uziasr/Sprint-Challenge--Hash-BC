#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    for ticket in tickets:
        hash_table_insert(hashtable,ticket.source,ticket.destination)
    x = "NONE"
    # print(hash_table_retrieve(hashtable, x))
    count = 0
    while True:
        x = hash_table_retrieve(hashtable, x)
        print(x)
        route[count] = x 
        count += 1
        if hash_table_retrieve(hashtable, x) == "NONE":
            print("this is the route!!", route)
            break
    return route
    """
    YOUR CODE HERE
    """
# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]
# reconstruct_trip(tickets, len(tickets))