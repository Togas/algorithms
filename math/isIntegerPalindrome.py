def isIntegerPalindrome(number):
    reversedNumber=0
    current=number
    while current>0:
        reversedNumber=reversedNumber*10 + (current%10)
        current//=10
    return reversedNumber==number
