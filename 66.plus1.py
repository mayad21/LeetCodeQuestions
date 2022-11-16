#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

#Constraints
# 1 <= digits.length <= 100
#0 <= digits[i] <= 9
#digits does not contain any leading 0's.

#things to look out for: 
# if len(array) = 1 and array[0] = 9
# if array[len(array)] = 9 and array[len(array)-1] = 9, then have to keep track of how many digits to update. ex 199 -> 200
#check if 9 is the leading digit meaning that we have to add 0 at the end for another place ex 9 -> 10 


class Solution(object):
    def plusOne(self, digits):
        #did we see a 9?
        nineflag = False
        #index of the leading 9, init = 0
        nineIndex = 0
        # if digits = [9]
        if len(digits) == 1 and digits[0] == 9:
            digits[0] = 1
            digits.append(0)
            return digits
        #start from the back of the array, ones place up to most significant bit
        for x in reversed(range(len(digits))):
            #check if we have a 9
            if digits[x] == 9:
                #if we don't have a 9 in the previous place, then we can update the current place = 0, and the previous place += 1, and then break out of the loop 
                if digits[x-1] != 9:
                    digits[x] = 0
                    digits[x-1] += 1
                    break
                #if we're not on the leading digit, then the nineIndex will be the previous place
                elif x!=0:
                    nineIndex = x-1 
                    nineflag = True 
            #if we didn't encounter a 9, we can just update in place normally      
            else: 
                digits[x] += 1
                break
        #if we did encounter a 9, then we have to change the digits after the leading 9 to the last nine to be 0
        if nineflag:
            for x in range(nineIndex+1, len(digits)):
                digits[x] = 0
            #if 9 is the leading digit, we have to add a 0 to create a new place and change the first 9 to 1
            if nineIndex == 0:
                digits[nineIndex] = 1
                digits.append(0)

        return digits
        """
        :type digits: List[int]
        :rtype: List[int]
        """
