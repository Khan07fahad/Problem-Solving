
#Program to show all the combinations Rs 3 can be made from 2p, 5p, 10p, 20p, 50p coins

import sys

def total_combination(coins1, total1, incr1):
    for a in range(len(coins)-1, len(coins)):			#initially 50p coin
        for b in range(len(coins)-2, len(coins)):			#initially 20p coin
            for c in range(len(coins)-3, len(coins)):				#initially 10p coin
                for d in range(len(coins)-4, len(coins)):				#initially 5p coin
                    for e in range(len(coins)-5, len(coins)):					#initially 2p coin
                        set1 = 0
                        while set1 <= total1/coins[len(coins)-1]:
                            set2 = 0
                            while set2 <= total1/coins[len(coins)-2]:
                                set3 = 0
                                while set3 <= total1/coins[len(coins)-3]:
                                    set4 = 0
                                    while set4 <= total1/coins[len(coins)-4]:
                                        set5=0
                                        while set5 <= total1/coins[len(coins)-5]:
                                            newtotal = (coins1[e]*set5)+(coins1[d]*set4)+(coins1[c]*set3)+(coins1[b]*set2)+(coins1[a]*set1)
                                            if(newtotal == total1):	#if the combination is equal to 300
                                                #print("%d*%d    %d*%d   %d*%d   %d*%d   %d*%d" % (coins1[e], set5, coins1[d], set4, coins1[c], set3, coins1[b],set2, coins1[a], set1))
                                                incr1 = incr1+1
                                            set5 = set5+1
                                        set4 = set4+1
                                    set3 = set3+1
                                set2 = set2+1
                            set1 = set1+1
    return incr1


def total_3s_combination(coins1, total1, incr1):
    for a in range(len(coins)-3, len(coins)):			#initially 10p coin			
        for b in range(len(coins)-4, len(coins)):			#initially 5p coin
            for c in range(len(coins)-5, len(coins)):				#initially 2p coin
                set1 = 0
                while set1 <= total1/coins[len(coins)-5]:
                    set2 = 0
                    while set2 <= total1/coins[len(coins)-5]:
                        set3 = 0
                        while set3 <= total1/coins[len(coins)-5]:
                            newtotal = (coins1[c]*set3)+(coins1[b]*set2)+(coins1[a]*set1)
                            if(newtotal == total1):	#if the combination is equal to 300
                                #print("%d*%d    %d*%d   %d*%d" % (coins1[c], set3, coins1[b],set2, coins1[a], set1))
                                incr1 = incr1+1
                            set3 = set3+1
                        set2 = set2+1
                    set1 = set1+1
    return incr1






coins = [2, 5, 10, 20, 50]	# 2p, 5p, 10p, 20p, 50p Coins
total = 300   
incr = 0
#combination = total_combination(coins, total, incr)
combination_3s = total_3s_combination(coins, total, incr)
#print("Total Number of Combinations are %d"%(combination))
print("Total Number of 3's Combinations are %d"%(combination_3s))
