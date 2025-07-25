from time import sleep
MAX_NUMBER_OF_BOTTLES: int = 99

def main():
    current_number_of_bottles: int = MAX_NUMBER_OF_BOTTLES

    while current_number_of_bottles > 0:
        if current_number_of_bottles == 2:
            print(f"{current_number_of_bottles} bottles of beer on the wall, {current_number_of_bottles} bottles of beer\nTake one down, pass it around, only 1 bottle of beer on the wall\n")
            current_number_of_bottles -= 1
            sleep(4)
        if current_number_of_bottles == 1:
            print(f"{current_number_of_bottles} bottle of beer on the wall, {current_number_of_bottles} bottle of beer\nTake one down, pass it around, there are no more bottles of beer on the wall!\n")
            current_number_of_bottles = 0
            print("Off to the pub we go!\n")
        else:
            print(f"{current_number_of_bottles} bottles of beer on the wall, {current_number_of_bottles} bottles of beer\nTake one down, pass it around, {current_number_of_bottles - 1} bottles of beer on the wall\n")
            current_number_of_bottles -= 1
            sleep(4)

if __name__ == "__main__":
    main()