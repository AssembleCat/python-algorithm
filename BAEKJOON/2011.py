cypher = input()
n = len(cypher)
dp = [0] * (n + 1)

if cypher[0] == '0':
    print(0)
else:
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        one_digit = int(cypher[i - 1])
        two_digits = int(cypher[i - 2] + cypher[i - 1])

        if 1 <= one_digit <= 9:
            dp[i] += dp[i - 1]

        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]

    print(dp[n] % 1000000)
