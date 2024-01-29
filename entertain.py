import heapq

def record_shows(k, shows):
    shows.sort(key=lambda x: x[1]) # Sort the shows by end time in ascending order
    pq = [] # Use a priority queue to keep track of the earliest available time slots
    recorded = 0
    for i in range(len(shows)):
        start, end = shows[i]
        if pq and pq[0][1] <= start:
            del pq[0] # Remove the earliest available time slot that have already ended
        if len(pq) < k: 
            heapq.heappush(pq, (start, end)) # If there are available time slots, record the show
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