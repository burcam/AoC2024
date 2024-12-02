def get_subsections(row_items: list[int]):
    yield row_items
    for item in row_items:
        subsection = list(row_items)
        subsection.remove(item)
        yield subsection

def get_input():
    with open("02") as f:
        for row in f.readlines():
            if not row:
                continue
            row_items = [int(item) for item in row.split()]
            yield row_items

def check_report(levels: list[int]):
    if len(levels) < 2:
        return True
    if levels[0] == levels[1]:
        return False
    asc = levels[0] < levels[1]
    def comp(i1, i2):
        if asc:
            return 0 < i2 - i1 < 4
        else:
            return 0 < i1 - i2 < 4
    for i in range(len(levels) - 1):
        if not comp(levels[i], levels[i+1]):
            return False
    return True

def main2():
    safe_list: list[int] = []
    for section_list in get_input():
        if any(check_report(sub_report) for sub_report in get_subsections(section_list)):
            safe_list.append(1)
        else:
            safe_list.append(0)
    return sum(safe_list)
print(main2())
