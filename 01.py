def get_input():
    first_list: list[int] = []
    second_list: list[int] = []
    with open("01") as f:
        for row in f.readlines():
            if not row:
                continue
            row = row.strip()
            grps = row.split()
            first_list.append(int(grps[0]))
            second_list.append(int(grps[-1]))
    first_list.sort()
    second_list.sort()
    return first_list, second_list
def main1():
    first, second = get_input()
    distances: list[int] = []
    for i in range(len(first)):
        distances.append(abs(first[i] - second[i]))
    return sum(distances)

def main2():
    first, second = get_input()
    j = 0
    list_len = len(first)
    sim_scores: list[int] = []
    for i in range(list_len):
        sim_scores.append(0)
        while j < list_len and second[j] < first[i]:
            j += 1
        while j < list_len and second[j] == first[i]:
            sim_scores[-1] += first[i]
            j += 1
        if j == list_len:
            break
    return sum(sim_scores)

print(main2())
