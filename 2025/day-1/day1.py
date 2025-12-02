from AdventOfCodeInputReader import AdventOfCodeInputReader

reader = AdventOfCodeInputReader("_session", 2025, 1)
step = reader.get_input() 

# print(step)

# step = ['L10', 'L20']
# step = [
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

# part - 1 solution
def rotate(step):
    start = 50
    ans = 0
    for i in step:
        direction = i[0]
        number = int(i[1:])
        if direction == 'L':
            start = (start-number)%100
        else:
            start = (start+number)%100
        
        if start == 0:
            ans+=1
    return ans

def main():
    ans = rotate(step)
    print(ans)

if __name__ == "__main__":
    main()
    
    
    # dial = [i for i in range(0, 100)]
    # ans = 0
    # extract direction and number from step
        # direction = step[0]
        # number = step[1:]
    # for i in range(step):
        # if direction = 'L':
            # diff = abs((start+number)-0)
            # if diff == 0:
                # start = start - number
        
        # else:
            # diff = abs((start+number)-99)
            # if diff == 0:
                #  start = start + number
            
        # if start == 0:
            #  ans+=1
