import time

def part1():
    total = 0

    illegal = {')': 3, ']': 57, '}': 1197, '>': 25137}

    for o in open("input.txt"):
        l = o.strip()
        while l.count('{}') > 0 or l.count('[]') > 0 or l.count("<>") > 0 or l.count("()") > 0:
            l = l.replace("{}", "").replace("<>", "").replace("[]", "").replace("()", "")

        p = [l.index(i) for i in illegal if i in l]

        if len(p) > 0:
            total += illegal[l[min(p)]]

    print(total)



def part2():
    prize = {')': 1, ']': 2, '}': 3, '>': 4}
    comp = {'{': '}', '(': ')', '[': ']', '<': '>'}

    scores = []
    for o in open("input.txt"):
        l = o.strip()
        while l.count('{}') > 0 or l.count('[]') > 0 or l.count("<>") > 0 or l.count("()") > 0:
            l = l.replace("{}", "").replace("<>", "").replace("[]", "").replace("()", "")

        p = [l.index(i) for i in prize if i in l]

        if len(p) == 0:
            local_tmp = 0
            for i in l[::-1]:
                local_tmp *= 5
                local_tmp += prize[comp[i]]
            print(o.strip(), l, local_tmp)
            scores.append(local_tmp)

    scores.sort()
    print(scores)
    print(scores[len(scores) // 2])


if __name__ == "__main__":
    part1()
    part2()