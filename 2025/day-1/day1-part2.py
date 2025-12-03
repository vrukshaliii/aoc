from AdventOfCodeInputReader import AdventOfCodeInputReader

reader = AdventOfCodeInputReader("_ga=GA1.2.178448345.1764661135; _gid=GA1.2.1051773786.1764661135; session=53616c7465645f5fd35d78868655c98c2f52df19a9d38f16a69a48e69c1a1f903c2ba3c821e09b70125334a38ed803a1aa2c761b53428b1e15da7d74dcd58c03; _gat=1; _ga_MHSNPJKWC7=GS2.2.s1764769204$o4$g1$t1764769229$j35$l0$h0", 2025, 1)
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