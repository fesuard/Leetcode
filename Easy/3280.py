# https://leetcode.com/problems/convert-date-to-binary/description
# You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd
# format. date can be written in its binary representation obtained by converting year,
# month, and day to their binaryrepresentations without any leading zeroes and writing
# them down in year-month-day format. Return the binary representation of date.


# We get a list of the date numbers with the help of the split function. For each number
# we convert it to an integer, then to a binery, and add it into our res list.
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        res = []
        date_nums = date.split('-')

        for num in date_nums:
            res.append(bin(int(num))[2:])

        return '-'.join(res)
