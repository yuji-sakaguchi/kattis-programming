import math
import heapq

def min_sprinklers(n, l, w, sprinklers):
    pq = [] # new sprinklers that cover entire area
    k = 0 # check through sprinklers to get optimal ones
    covered = 0 # the length covered by sprinklers
    sprinklers = [s for s in sprinklers if s[1] > w/2]
    for i in range(len(sprinklers)):
        newradius = math.sqrt((sprinklers[i][1])**2 - (w/2)**2)
        sprinklers[i] = (sprinklers[i][0] - newradius, sprinklers[i][0] + newradius)
    sprinklers.sort(key=lambda x: x[0])  # sort by position

    for i in range(len(sprinklers)):
        leftside, rightside = sprinklers[i]
        while k in range(len(pq)):
            if k == 0:
                if leftside <= 0 and rightside >= pq[k][1]:
                    del pq[k]
                else:
                    k += 1
            else:
                if leftside <= pq[k-1][1] and rightside >= pq[k][1]:
                    del pq[k] # Remove sprinklers that are not needed anymore
                else:
                    k += 1
        k = 0
        if leftside <= covered and (not pq or rightside > pq[-1][1]):
            heapq.heappush(pq, (leftside, rightside)) # Add sprinkler to queue if it covers the strip
            covered = rightside
        if covered >= l:
            return len(pq)
    if covered < l:
        return -1
    
if __name__ == '__main__':
    while True:
        try:
            #input_str = input()
            n, l, w = map(int, input().split())
            sprinklers = [list(map(int, input().split())) for i in range(n)]
            ans = min_sprinklers(n, l, w, sprinklers)
            print(ans)
        except EOFError:
            break