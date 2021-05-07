from collections import deque


def word_check(word1, word2):
    count = 0
    word_len = len(word1)

    for i in range(word_len):
        if count > word_len - 1:
            return False
        if word1[i] == word2[i]:
            count += 1

    return True if count == word_len - 1 else False


def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [False] * len(words)

    queue = deque([(0, begin)])
    while queue:
        count, word = queue.popleft()

        if word == target:
            return count

        for i, w in enumerate(words):
            if not visited[i] and word_check(w, word):
                queue.append((count + 1, w))
                visited[i] = True

    return 0
