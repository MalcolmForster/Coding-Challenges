# Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

array1 = [9,11,8,5,7,10]
array2 = [4,2,8,10,3,7,9,4,7,15,8,9,1,4,5,10]
array3 = [7,3,9,7,12,4,6,9,15,2,1,8,2,7,6]

usedArray = array1

maxprofit = 0
maxprofitMin = 0
maxprofitMax = 0
arraylength = len(usedArray)

for x in range(arraylength-1):
    
    min = usedArray[x]
    for num in usedArray[x+1:]:
        if((num - min) > maxprofit):        
            maxprofitMin = min
            maxprofitMax = num
            maxprofit = num - min
        
print("The max profit is "+str(maxprofit) + " by buying at " + str(maxprofitMin) + " and selling at " + str(maxprofitMax))
    
    
    
