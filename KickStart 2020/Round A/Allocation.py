t = int(input())
# Number of test cases!

for t_itr in range(1, t + 1):

    integers = input().split()

    n = int(integers[0])      # Value of N

    b = int(integers[1])      # Value of B

    prices = list(map(int, input().split()))
    # All the prices which need to be sorted
    # so that we can easily retrieve the required
    # elements.

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