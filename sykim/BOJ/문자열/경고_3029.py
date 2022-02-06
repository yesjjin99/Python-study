import sys
input = sys.stdin.readline

timesDict = {}
index = ['s','t']
for i in range(2):
    # sec, min, hour
    times = list(map(int,input().rstrip().split(':')))
    times.reverse()
    timesDict[index[i]] = times
newTimes=[0,0,0]

for idx in range(len(newTimes)):
    if timesDict['s'][idx] > timesDict['t'][idx]:
        if idx == (len(newTimes) - 1):
            newTimes[idx] = timesDict['t'][idx] + 24 - timesDict['s'][idx]
        else:
            timesDict['t'][idx + 1] -= 1
            newTimes[idx] = timesDict['t'][idx]+60-timesDict['s'][idx]
    else:
        newTimes[idx] = timesDict['t'][idx] - timesDict['s'][idx]

for idx in range(len(newTimes)):
    if newTimes[idx] < 10:
        newTimes[idx] ='0'+str(newTimes[idx])
    else:
        newTimes[idx] = str(newTimes[idx])
newTimes.reverse()
out = ':'.join(newTimes)
if out =='00:00:00':
    out = '24:00:00'
print(out)

#key: 시간 처리
#todo: module로 해보기
