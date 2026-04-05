def edit_distance(s1, s2):
    """
    Compute the minimum edit distance between two strings.
    """

    if s1 == "" and s2 == "":
        return 0
    if s1 == "":
        return len(s2)
    if s2 == "":
        return len(s1)
        
    dp = [[0] * len(s2) for _ in range(len(s1))]

    if s1[0] != s2[0]:
        dp[0][0] = 1

    for j in range(1, len(s2)):
        dp[0][j] = dp[0][j - 1] + 1
    
    for i in range(1, len(s1)):
        dp[i][0] = dp[i - 1][0] + 1
    
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[-1][-1]
