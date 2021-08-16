d = 256

#alphabet range
def rabinkarp(pat, text, q):

    M = len(pat)
    N = len(test)

    i, j = 0, 0

    patHash, textHash = 0, 0

    h = 1

    for i in range(M-1):
        h = (h * d ) % q

    for i in range(M):
        patHash = (d * patHash + ord(pat[i])) % q
        textHash = (d * textHash + ord(text[i])) % q

    for i in range(N-M + 1):

        if patHash == textHash:

            for j in range(M):
                if txt[i+j] != pat[j]:
                    break

            j += 1

            if j == M:
                #pattern found

        if i < N-M:
            textHash = (d*(textHash - ord(text[i])) * h) + ord(text[i+M]) % q

            if textHash < 0:
                textHash = textHash + q
