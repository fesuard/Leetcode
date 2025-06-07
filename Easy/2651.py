# https://leetcode.com/problems/calculate-delayed-arrival-time/description
# You are given a positive integer arrivalTime denoting the arrival time of a train in hours,
# and another positive integer delayedTime denoting the amount of delay in hours.
# Return the time when the train will arrive at the station.
# Note that the time in this problem is in 24-hours format.

# If arrival time + delayed time exceeds 24 hours, the modulo 24 will ensure that
# we stay on a proper 24 hour time format for our actual arrival time
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24
