from collections import deque

class RecentCounter:
    def __init__(self):
        # Initialize a queue to store the timestamps of the requests
        self.c_requests = deque()

    def ping(self, c_t):
        """
        :type c_t: int
        :rtype: int
        """
        # Add the current request time to the queue
        self.c_requests.append(c_t)

        # Remove all requests that are older than (t - 3000)
        while self.c_requests and self.c_requests[0] < c_t - 3000:
            self.c_requests.popleft()

        # Return the number of requests in the range [t - 3000, t]
        return len(self.c_requests)
