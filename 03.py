import re
def get_input():
    with open("03") as f:
        return "A".join(f.readlines())

def find_muls(input: str):
    mul_regex = "mul\\(\\d{1,3}\\,\\d{1,3}\\)"
    muls: list[str] = re.findall(mul_regex, input)
    prods: list[int] = []
    for mul in muls:
        first, second = mul.split("(")[-1].split(",")
        first = int(first)
        second = int(second[0:-1])
        prod = first * second
        prods.append(prod)
    return prods

def main1():
    input = get_input()
    mul_regex = "mul\\(\\d{1,3}\\,\\d{1,3}\\)"
    muls: list[str] = re.findall(mul_regex, input)
    prods: list[int] = []
    for mul in muls:
        first, second = mul.split("(")[-1].split(",")
        first = int(first)
        second = int(second[0:-1])
        prod = first * second
        prods.append(prod)
    print(sum(prods))

main1()

def main2():
    input = get_input()
    dont_wraps = input.split("don't()")
    prod_groups: list[int] = []
    prod_groups.append(sum(find_muls(dont_wraps[0])))
    dont_wraps.pop(0)
    for wrap in dont_wraps:
        dos = wrap.split("do()")[1:]
        for active in dos:
            prod_groups.append(sum(find_muls(active)))
    print(sum(prod_groups))
main2()