def rail_fence_encrypt(text, rails):
    text = text.replace(" ", "")
    fence = [[] for _ in range(rails)]

    row = 0
    direction = 1  # 1 = down, -1 = up

    for char in text:
        fence[row].append(char)
        row += direction

        if row == 0 or row == rails - 1:
            direction *= -1

    cipher = ""
    for rail in fence:
        cipher += "".join(rail)

    return cipher


# Example
print(rail_fence_encrypt("HELLO WORLD", 3))


