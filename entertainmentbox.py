import heapq
import bisect

def record_shows(k, shows):
    shows.sort(key=lambda x: x[1]) # Sort the shows by end time in ascending order
    pq = [] # Use a priority queue to keep track of the earliest available time slots
    endtimes = []
    recorded = 0
    for i in range(len(shows)):
        start, end = shows[i]
        overlap = bisect.bisect_right(endtimes, start) - 1
        if overlap != -1:
            del pq[overlap] # Remove the earliest available time slot(s) that have already ended
            del endtimes[overlap]
        if len(pq) < k:
            heapq.heappush(pq, (start, end)) # If there are available time slots, record the show
            heapq.heappush(endtimes, (end))
            recorded += 1
    return recorded

if __name__ == '__main__':
    while True:
        try:
            n, k = map(int, input().split())
            shows = [list(map(int, input().split())) for _ in range(n)]
            ans = record_shows(k, shows)
            print(ans)
        except EOFError:
            break