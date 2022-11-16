#Given two binary strings a and b, return their sum as a binary string.

#constraints: 
#1 <= a.length, b.length <= 104
#a and b consist only of '0' or '1' characters.
#Each string does not contain leading zeros except for the zero itself.

class Solution(object):
    def addBinary(self, a, b):
        #convert the strings into integers
        a = int(a,2)
        b = int(b,2)
        #do integer addition
        sum = a+b
        #convert integer sum to binary using bin(), .replace gets rid of "0b"
        sum = bin(sum).replace("0b","")
        return sum
        """
        :type a: str
        :type b: str
        :rtype: str
        """