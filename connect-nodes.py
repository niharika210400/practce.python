# Ques: https://practice.geeksforgeeks.org/problems/connect-nodes-at-same-level/1
# Soln:

class newnode: 
    def __init__(self,data): 
        self.data = data  
        self.left = None
        self.right = None
        self.nextRight = None
          
# This function returns the leftmost child of   
# nodes at the same level as p. This function  
# is used to getNExt right of p's right child  
# If right child of is None then this can also 
# be used for the left child  
def getNextRight(p): 
    temp = p.nextRight  
  
    # Traverse nodes at p's level and find  
    # and return the first node's first child  
    while (temp != None): 
        if (temp.left != None): 
            return temp.left  
        if (temp.right != None):  
            return temp.right  
        temp = temp.nextRight 
  
    # If all the nodes at p's level are  
    # leaf nodes then return None  
    return None
  
# Sets nextRight of all nodes of a tree  
# with root as p  
def connect(p): 
    temp = None
  
    if (not p):  
        return
  
    # Set nextRight for root  
    p.nextRight = None
  
    # set nextRight of all levels one by one  
    while (p != None): 
        q = p  
  
        # Connect all childrem nodes of p and  
        # children nodes of all other nodes  
        # at same level as p  
        while (q != None): 
              
            # Set the nextRight pointer for  
            # p's left child  
            if (q.left): 
                  
                # If q has right child, then right  
                # child is nextRight of p and we  
                # also need to set nextRight of  
                # right child  
                if (q.right):  
                    q.left.nextRight = q.right  
                else: 
                    q.left.nextRight = getNextRight(q) 
  
            if (q.right): 
                q.right.nextRight = getNextRight(q)  
  
            # Set nextRight for other nodes in 
            # pre order fashion  
            q = q.nextRight 
  
        # start from the first node  
        # of next level  
        if (p.left): 
            p = p.left  
        elif (p.right): 
            p = p.right  
        else: 
            p = getNextRight(p) 



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    


def InOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated in order Traversal of the given tree.
    '''
    if root is None: # check if the root is none
        return
    InOrder(root.left) # do in order of left child
    print(root.data, end=" ")  # print root of the given tree
    InOrder(root.right) # do in order of right child

def printSpecial(root):
    leftmost_node = root

    while leftmost_node :
        curr_node = leftmost_node
        leftmost_node = None
        if curr_node.left :
            leftmost_node = curr_node.left
        elif curr_node.right :
            leftmost_node = curr_node.right

        print(curr_node.data,end=" ")
        while curr_node.nextRight :
            print(curr_node.nextRight.data,end=" ")
            curr_node = curr_node.nextRight
    print()


    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        connect(root)
        printSpecial(root)
        InOrder(root)
        print()
        
        

# } Driver Code Ends
