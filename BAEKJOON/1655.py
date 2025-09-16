import heapq as hq
import sys

n = int(sys.stdin.readline())

lessHeap = [] # 중간값보다 작은 최대 Heap -1 곱해서 넣어줘야함.
moreHeap = [] # 중간값보다 큰 최소 Heap 그대로 넣어주면 됨.
for i in range(n):
    num = int(sys.stdin.readline())

    if len(lessHeap) == len(moreHeap):
        hq.heappush(lessHeap, -num)
    else:
        hq.heappush(moreHeap, num)

    if moreHeap and lessHeap[0] * -1 > moreHeap[0]:
        less = hq.heappop(lessHeap)
        more = hq.heappop(moreHeap)

        hq.heappush(lessHeap, -more)
        hq.heappush(moreHeap, -less)

    print(-lessHeap[0])