# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside the queue functions - move the pointers yourself.

# Exercise 1 - Linear queue
Queue = [] 
HeadPointer = -1
TailPointer = -1
# Write code here to fill Queue with 6 elements, all "" (empty string)
for i in range(6):
    Queue.append("")


def Enqueue(Name):
    # Write your code here
    global Queue, HeadPointer, TailPointer
    if TailPointer == 5:
        return False
    TailPointer = TailPointer + 1
    Queue[TailPointer] = Name
    if HeadPointer == -1:
        HeadPointer = 0
    return True


def Dequeue():
    # Write your code here
    global Queue, HeadPointer, TailPointer
    if HeadPointer == -1 or HeadPointer > TailPointer:
        return ""
    Name = Queue[HeadPointer]
    HeadPointer = HeadPointer + 1
    return Name


# Exercise 2 - Circular queue
CircularQueue = []
CircularHead = -1
CircularTail = -1
NumberItems = 0
# Write code here to fill CircularQueue with 6 elements, all "" (empty string)
for i in range(6):
    CircularQueue.append("")


def CircularEnqueue(Name):
    # Write your code here
    global CircularQueue, CircularHead, CircularTail, NumberItems
    if NumberItems == 6:
        return False
    if NumberItems == 0:
        CircularHead = 0
        CircularTail = 0
    else:
        CircularTail = CircularTail + 1
        if CircularTail == 6:
            CircularTail = 0
    CircularQueue[CircularTail] = Name
    NumberItems = NumberItems + 1
    return True


def CircularDequeue():
    # Write your code here
    global CircularQueue, CircularHead, CircularTail, NumberItems
    if NumberItems == 0:
        return ""
    Name = CircularQueue[CircularHead]
    CircularHead = CircularHead + 1
    if CircularHead == 6:
        CircularHead = 0
    NumberItems = NumberItems - 1
    if NumberItems == 0:
        CircularHead = -1
        CircularTail = -1
    return Name


def ShowQueue():
    # Write your code here
    Text = ""
    Index = CircularHead
    for i in range(NumberItems):
        if i == 0:
            Text = CircularQueue[Index]
        else:
            Text = Text + ", " + CircularQueue[Index]
        Index = Index + 1
        if Index == 6:
            Index = 0
    return Text


# Exercise 3 - Hot potato
def HotPotato(Names, Passes):
    # Write your code here
    global CircularHead, CircularTail, NumberItems
    CircularHead = -1
    CircularTail = -1
    NumberItems = 0
    if len(Names) == 0:
        return ""
    for Name in Names:
        CircularEnqueue(Name)
    while NumberItems > 1:
        for i in range(Passes):
            CircularEnqueue(CircularDequeue())
        CircularDequeue()
    return CircularDequeue()
