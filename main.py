from math import ceil
import random

VERBOSE = False
LOOP_LENGTH = 100


def log(message):
    if VERBOSE:
        print(message)


def createBoxes(length):
    boxes = {}
    numberLists = list(range(1, length + 1))
    random.shuffle(numberLists)
    for index, item in enumerate(numberLists):
        boxes[index + 1] = item

    return boxes


def play(box_length, prisoner):
    boxes = createBoxes(box_length)
    allowed_box_open = ceil(box_length / 2)
    chances = allowed_box_open
    next_box_to_open = prisoner
    while chances >= 0:
        opened_box = boxes[next_box_to_open]
        if opened_box == prisoner:
            log('Prisoner {} found its number on {} tries'.format(
                prisoner, allowed_box_open - chances))
            return True
        else:
            next_box_to_open = opened_box
            chances -= 1
    log('Prisoner {} failed'.format(prisoner))
    return False


def loop_play(people_length):
    people = list(range(1, people_length + 1))
    result = [play(people_length, person) for person in people]
    if result.count(False) == 0:
        log("All prisoners are safe")
        return True
    else:
        log("Everybody got executed")
        return False


def main():
    people_length = int(input("How many prisoners are playing? "))
    result = [loop_play(people_length) for i in range(LOOP_LENGTH)]
    print("Success Rate {}%".format(result.count(True) / LOOP_LENGTH * 100))
    print("Failure Rate {}%".format(result.count(False) / LOOP_LENGTH * 100))


if __name__ == "__main__":
    main()
