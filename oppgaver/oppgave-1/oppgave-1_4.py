fruits = ["eple", "banan", "appelsin", "drue", "kiwi"]

while True: # Wrapped in an infinite while-loop so it will prompt you to try again if failed
    try:
        first_index = int(input("Please enter the first index to replace: "))
        second_index = int(input("Please enter the second index to replace: "))

        fruits[first_index], fruits[second_index] = fruits[second_index], fruits[first_index]

    except IndexError:
        print("ERROR: One of the indices are invalid. Please try again.")
        continue

    except Exception:
        print("ERROR: Unknown error. Please check your input and try again.")
        continue

    else:
        print("Success!\nIndices successfully swapped. New list:\n")
        print(fruits)
        break
#%% md
## Oppgave 1.5