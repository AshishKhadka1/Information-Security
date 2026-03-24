def rail_fence_decrypt(cipher, rails):
    n = len(cipher)
    pattern = [["" for _ in range(n)] for _ in range(rails)]

    row, direction = 0, 1

    # Mark zigzag positions
    for col in range(n):
        pattern[row][col] = '*'
        row += direction

        if row == 0 or row == rails - 1:
            direction *= -1

    # Fill characters
    index = 0
    for i in range(rails):
        for j in range(n):
            if pattern[i][j] == '*' and index < n:
                pattern[i][j] = cipher[index]
                index += 1

    # Read zigzag
    result = ""
    row, direction = 0, 1
    for col in range(n):
        result += pattern[row][col]
        row += direction

        if row == 0 or row == rails - 1:
            direction *= -1

    return result


# Example
print(rail_fence_decrypt("HOLELWRDLO", 3))