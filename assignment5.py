def lcsequence(X, Y):
    m = len(X)
    n = len(Y)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    length = dp[m][n]

    lcsequence_string = ""

    i = m
    j = n

    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            lcsequence_string = X[i - 1] + lcsequence_string
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return length, lcsequence_string



X = input("Enter first sequence: ")
Y = input("Enter second sequence: ")

length, result = lcsequence(X, Y)

print("Length of Longest Common Subsequence:", length)
print("Longest Common Subsequence:", result)