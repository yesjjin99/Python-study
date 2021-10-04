from collections import deque


def change(begin, target, words):
    vocab = {i: set() for i in range(len(begin))}
    for w in words:
        for i in range(len(begin)):
            vocab[i].add(w[i])
    # for idx in vocab:
    #     list(vocab[idx]).sort()
    queue = deque()
    words.append(begin)
    queue.append((begin, 0))
    visited = [False] * len(words)
    while queue:
        word, cnt = queue.popleft()
        cnt += 1  # row 별 더하기
        word_index = words.index(word)

        if word in words and not visited[word_index]:  # 주의
            visited[word_index] = True
            for idx, c in enumerate(word):
                for re in vocab[idx]:
                    new_word = word.replace(c, re)

                    if new_word in words:
                        if new_word == target:

                            return (new_word, cnt)
                        else:
                            queue.append((new_word, cnt))
    return (None, 0)


def solution(begin, target, words):
    if target not in words:
        answer = 0
        return answer

    _, answer = change(begin, target, words)

    return answer