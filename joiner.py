#!/usr/bin/env python

import sys 
import json 


def writeToFile(returnJson):
    
    with open('result.json', 'w') as outputJsonFile:
        json.dump(returnJson, outputJsonFile, indent=4, sort_keys=True)
        
def innerJoin(left_table, right_table, leftKey, rightKey):

    returnJson = {"result":[]}
    key1,key2, totalOrdersDone= 0,0,0
    
    fulfilled1 = set()
    fulfilled2 = set()
   
    while (key1 < len(left_table) and key2 < len(right_table)):
        
        if(left_table[key1][leftKey] == right_table[key2][rightKey]):
            
            returnJson["result"].append(dict(left_table[key1], **right_table[key2]))
            
            key2 += 1
            totalOrdersDone += 1
            
            fulfilled1.add(key1)
            fulfilled2.add(key2)
            
        elif(left_table[key1][leftKey] < right_table[key2][rightKey]):
            key1 += 1
        elif(left_table[key1][leftKey] > right_table[key2][rightKey]):
            key2 += 1
            
    returnJson.update({"result_count":totalOrdersDone})
    returnJson.update({"skipped_left":len(left_table) - len(fulfilled1)})
    returnJson.update({"skipped_right":len(right_table) - len(fulfilled2)})
    
    writeToFile(returnJson)
    
def init():
    
    joinType = sys.argv[1]
    leftFileName = sys.argv[2] 
    rightFileName = sys.argv[3] 
    leftField = sys.argv[4]
    rightField = sys.argv[5]
  
    left_table = json.load(open(leftFileName))
    right_table = json.load(open(rightFileName))
    
    left_table.sort(key=lambda table:table[leftField])
    right_table.sort(key=lambda table:table[rightField])
    
    if(joinType == "inner"):
        innerJoin(left_table, right_table, leftField, rightField)
    
if __name__ == "__main__":
    
    init()
    
    