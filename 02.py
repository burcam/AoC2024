def get_input():
    with open("02") as f:
        for row in f.readlines():
            if not row:
                continue
            yield [int(item) for item in row.split()], row

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

def main1():
    reports = get_input()
    safe_list: list[int] = []
    for report, row in reports:
        report_result = check_report(report)
        if report_result:
            safe_list.append(1)
        else:
            safe_list.append(0)
    return sum(safe_list)


print(main1())
