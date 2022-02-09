q = []


def display():
    print(q)
    size = int(input("Please enter the size of the Queue: "))
    while True:
        print("Select the operations: 1.Add 2.Delete 3.Display 4.Quit")
        choice = int(input())
        if choice == 1:
            enqueue(size)
        elif choice == 2:
            dequeue()
        elif choice == 3:
            display()
        elif choice == 4:
            break
        else:
            print('Invalid Option!!')

def enqueue(size):
    if len(q) == size:
        print("Queue is full")
    else:
        element = input("Enter the element:")
        q.append(element)
        print(f"{element} is added to the Queue.")

def dequeue():
    if len(q) != 0:
        e = q.pop(0)
        print(f"{e} has been removed.")



display()