PASS_MARK = 40

def average(marks):
    return round(sum(marks) / len(marks), 1)

def grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= PASS_MARK:
        return "C"
    else:
        return "F"


if __name__ == "__main__":
    print("Testing scoretools directly")
    print(average([70, 80, 90]), grade(82))