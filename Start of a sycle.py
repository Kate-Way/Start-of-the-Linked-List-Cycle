class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Floyd's Tortoise and Hare Algorithm
    def floyd_cycle(self):
        # tort (tortoise) - slow moving pointer (1 step at the time)
        tort = self.head
        # hare - fast moving pointer (two steps)
        hare = self.head
        while True:
            # check if the linked list has no values or a single value
            if self.head == None or self.head.next == None:
                return None
            # advance both pointers by 1 step
            hare = hare.next
            tort = tort.next
            # check if there is a value for hare to advance to its desired position (+ 1 step - hare.next)
            if hare == None or hare.next == None:
                return None
            else:
                # advance hare to its final point
                hare = hare.next
            if tort == hare:
                # ones two pointers meet break from the loop
                break

        # to find the start of the loop you need to simultaneously check the next head value and the next hare value
        # till the two meet and return the meeting point (any value, either head or hare, they'll be the same)
        # set another value for the head, so you don't mess up the list while looking for the answer
        h = self.head
        while h != hare:
            h = h.next
            hare = hare.next
        return h