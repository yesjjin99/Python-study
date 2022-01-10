n, m = map(int, input().split()) 
count = 0
answer = ''
dna = []
for i in range(n):
    dna.append(input())

for i in range(m):
    c = [0, 0, 0, 0] # a, c, g, t
    for j in range(n):
        if dna[j][i] == 'A':
            c[0] += 1
        elif dna[j][i] == 'C':
            c[1] += 1
        elif dna[j][i] == 'G':
            c[2] += 1
        elif dna[j][i] == 'T':
            c[3] += 1
    s = c.index(max(c))
    if s == 0:
        answer += 'A'
    elif s == 1:
        answer += 'C'
    elif s == 2:
        answer += 'G'
    elif s == 3:
        answer += 'T'  
    count += n - max(c)

print(answer)
print(count)
