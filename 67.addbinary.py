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