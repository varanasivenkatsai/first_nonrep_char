# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:02:04 2020

@author: varan
"""


import argparse

def Main(string):
    
    if not string:
        print("No non-repeating charecter")
        return string
    
    count_dict={} # {charecter:[no.of occurances,[indexes]]} example:{z,[3,[2,5,6]]}
    
    
    for i,char in enumerate(string): 
        if char.lower() in count_dict:
            count_dict[char.lower()][0]+=1
            count_dict[char.lower()][1].append(i)
            
        else:
            count_dict[char.lower()]=[1,[i]]
            
            
    
    sd=sorted(count_dict.items(),key= lambda x:x[1][0]) # sort the dictionary based on number of occurances
    
    if sd[0][1][0]==1:
        print("first non-repeating char is :",sd[0][0])
    else:
        print("No non-repeating charecter")
    
    
    result = []  # reorderingthe string based on number of occurances
    for element in sd:
        for i in element[1][1]:
            result.append(string[i])
    string=("".join(result))
    return string



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-i", "--input", required=True, help="give input string ")
    
    args = parser.parse_args()
    string=Main(args.input)
    print("Reordered string:",string)