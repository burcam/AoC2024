from dataclasses import dataclass


@dataclass
class PageOrder:
    low: int
    high: int

def get_input():
    pages: list[PageOrder] = []
    updates: list[list[int]] = []
    with open("05") as f:
        while line := f.readline():
            if len(line) == 1:
                break
            low, high = [int(num.strip()) for num in line.split("|")]
            pages.append(PageOrder(low, high))
        while line := f.readline():
            if not line:
                break
            updates.append([int(num) for num in line.split(",")])
    return pages, updates

def flatten_order(key: int, pages: dict[int, tuple[bool, set[int]]]):
    if key not in pages:
        pages[key] = (True, set())
        return
    if pages[key][0] == True:
        return
    for larger_key in pages[key][1]:
        flatten_order(larger_key, pages)
        pages[key][1].update(pages[larger_key][1])
    pages[key][0] = True

def order_pages(pages: list[PageOrder]):
    key_lower_than_value: dict[int, tuple[bool, set[int]]] = {}
    key_higher_than_value: dict[int, tuple[bool, set[int]]] = {}
    for page in pages:
        if page.low not in key_lower_than_value:
            key_lower_than_value[page.low] = [False, set()]
        key_lower_than_value[page.low][1].add(page.high)
        if page.high not in key_higher_than_value:
            key_higher_than_value[page.high] = [False, set()]
        key_higher_than_value[page.high][1].add(page.low)

    start_numbers = [low_num for low_num in key_lower_than_value.keys() if low_num not in key_higher_than_value]
    for num in start_numbers:
        flatten_order(num, key_lower_than_value)
    return {key: value[1] for key, value in key_lower_than_value.items()}

def main1():
    pages, updates = get_input()
    sort_order = order_pages(pages)
    ok_updates: list[int] = []
    for index, update in enumerate(updates):
        ok = True
        for i in reversed(range(len(update) - 1)):
            if update[i+1] not in sort_order[update[i]]:
                ok = False
                break
        if ok:
            ok_updates.append(index)
    middle_nums: list[int] = []
    for idx in ok_updates:
        middle_nums.append(updates[idx][len(updates[idx])//2])
    print(sum(middle_nums))

main1()

def sort_update(update: list[int], sort_order: dict[int, set[int]]):
    if len(update) < 2:
        return update
    left, right = sort_update(update[:len(update)//2], sort_order), sort_update(update[len(update)//2:], sort_order)
    left_idx, right_idx = 0, 0
    sorted: list[int] = []
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] not in sort_order[right[right_idx]]:
            sorted.append(left[left_idx])
            left_idx += 1
        else:
            sorted.append(right[right_idx])
            right_idx += 1
    while left_idx < len(left):
        sorted.append(left[left_idx])
        left_idx += 1
    while right_idx < len(right):
        sorted.append(right[right_idx])
        right_idx += 1
    return sorted

def main2():
    pages, updates = get_input()
    sort_order = order_pages(pages)
    unsorted_updates: list[int] = []
    for index, update in enumerate(updates):
        ok = False
        for i in reversed(range(len(update) - 1)):
            if update[i+1] not in sort_order[update[i]]:
                ok = True
                break
        if ok:
            unsorted_updates.append(index)
    now_sorted_updates: list[list[int]] = []
    for index in unsorted_updates:
        now_sorted_updates.append(sort_update(updates[index], sort_order))
    middle_values: list[int] = []
    for update in now_sorted_updates:
        middle_values.append(update[len(update)//2])
    print(sum(middle_values))
main2()