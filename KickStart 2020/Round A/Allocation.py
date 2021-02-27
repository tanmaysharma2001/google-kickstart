t = int(input())

for t_itr in range(1, t + 1):

    integers = input().split()

    n = int(integers[0])

    b = int(integers[1])

    prices = list(map(int, input().split()))

    prices = sorted(prices)

    sum = 0

    count = 0

    for i in prices[0:n]:
        if ((sum + i) <= b):
            sum = sum + i
            count = count + 1
        else:
            break

    print("Case #" + str(t_itr) + ": " + str(count))