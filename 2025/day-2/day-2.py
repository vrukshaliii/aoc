num_range = [
    "199617-254904",
    "7682367-7856444",
    "17408-29412",
    "963327-1033194",
    "938910234-938964425",
    "3207382-3304990",
    "41-84",
    "61624-105999",
    "1767652-1918117",
    "492-749",
    "85-138",
    "140-312",
    "2134671254-2134761843",
    "2-23",
    "3173-5046",
    "16114461-16235585",
    "3333262094-3333392446",
    "779370-814446",
    "26-40",
    "322284296-322362264",
    "6841-12127",
    "290497-323377",
    "33360-53373",
    "823429-900127",
    "17753097-17904108",
    "841813413-841862326",
    "518858-577234",
    "654979-674741",
    "773-1229",
    "2981707238-2981748769",
    "383534-468118",
    "587535-654644",
    "1531-2363"
]

# num_range = [
#     "11-22",
#     "95-115",
#     "998-1012",
#     "1188511880-1188511890",
#     "222220-222224",
#     "1698522-1698528",
#     "446443-446449",
#     "38593856-38593862",
#     "565653-565659",
#     "824824821-824824827",
#     "2121212118-2121212124"
# ]


# Part - 1
def invalid_id(num_range):
    ans = 0
    for n_range in num_range:
        n_range = n_range.split('-')
        for i in range(int(n_range[0]), int(n_range[1])+1):
            if len(str(i))%2 == 0:
                mid = len(str(i)) // 2
                a = str(i)[0:mid]
                b = str(i)[mid:]
                if int(a) == int(b):
                    ans += i
    return ans


# Part - 2
def invalid_id_part2(num_range):
    ans = 0
    for n_range in num_range:
        n_range = n_range.split('-')
        for i in range(int(n_range[0]), int(n_range[1])+1):
            n = len(str(i))
            for m in range(1, n // 2 + 1):
                if n % m == 0:
                    pattern = str(i)[:m]
                    if pattern * (n // m) == str(i):
                        ans += i
                        break
    return ans
    
def main():
    # ans = invalid_id(num_range)
    ans = invalid_id_part2(num_range)
    print(ans)
    
if __name__ == "__main__":
    main()
    