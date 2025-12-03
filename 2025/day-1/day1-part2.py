from AdventOfCodeInputReader import AdventOfCodeInputReader

reader = AdventOfCodeInputReader("_session", 2025, 1)
step = reader.get_input() 

# print(step)

# step = ['L10', 'L20']
# step = [
#     "R1000",
#     "L68",
#     "L30",
#     "R48",
#     "L5",
#     "R60",
#     "L55",
#     "L1",
#     "L99",
#     "R14",
#     "L82"
# ]

def rotate(step):
    start = 50
    ans = 0

    for i in step:
        direction = i[0]
        number = int(i[1:])
        for i in range(number):
            if direction == "R":
                start = (start + 1) % 100
            elif direction == "L":
                start = (start - 1) % 100
            if start == 0:
                ans += 1
        
    return ans

def main():
    ans = rotate(step)
    print(ans)
    
if __name__ == "__main__":
    main()