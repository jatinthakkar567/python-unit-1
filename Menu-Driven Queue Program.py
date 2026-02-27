queue = []

while True:
    print("\n--- Queue Menu ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter element to enqueue: ")
        queue.append(item)
        print("Element added to queue.")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty.")
        else:
            removed = queue.pop(0)
            print("Removed element:", removed)

    elif choice == 3:
        print("Queue elements:", queue)

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")