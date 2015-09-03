#Jason Hill
#CSCI 3202 AI
#Assignment 1

import Queue
#a function that takes a list and feeds them into a queue and prints 
#as it dequeues
def queueDemo(numArr):
	q = Queue.Queue()
	for element in numArr:
		q.put(element)
	while not q.empty():
		print q.get()
		
#simple demo of the queueDemo function		
numList = [5,6,22,6,7,2,7,95,1,5]
queueDemo(numList)


#a stack class based on built-in functionality of python lists
class stackDemo:
	
	def __init__(self, ):
		self.stack = []
		
	def push(integer):
		self.stack.append(integer)
		
	def pop():
		return self.stack.pop()
		
	def checkSize():
		return len(self.stack)
		
#demo of our stack class
s = stackDemo()
quitter = 'n'
while quitter != 'quit':
	n = raw_input("Print 'q' to quit, or any number to add to stack:")
	if n == 'q':
		quitter = 'quit'
	else:
		s.push(n)
print "The size of your stack is: " 
print s.checkSize()
for element in s.stack:
	print s.pop()
	
class node:
	def __init__(self, key):
		self.key = key
		self.lc = None
		self.rc = None
		self.p = None
		
class binaryTree:
	def __init__(self):
		self.root = None
		
	def searchTree(self, value):
		#use a recursive BFS to search the tree because it is unsorted
		
	def addNode(self, key, parentValue):
		newNode = node(key)
		parent = searchTree(parentValue)
		if parent != None:
			if parent.left == None:
				parent.left = newNode
				newNode.p = parent
			else if parent.right == None:
				parent.right = newNode
				newNode.p = parent
			else:
				print "Parent has two children, node not added"
		else:
			print "Parent not found"
			
	def deleteNode(self, value):
		deleter = searchTree(value)
		if deleter == None:
			print "Node not found."
		elif deleter.l != None or deleter.r != None:
			print "Node not deleted, has children"
		else:
			if deleter.p.r == deleter:
				deleter.p.r == None
			else:
				deleter.p.l == None
	def traversePrint():
		#pre-order traversal
		
		
		
		
class Graph:
	
	def __init__(self):
		
	def addVertex(value):
		#check if value is already in the graph
		#if its not, add it
	def addEdge(value1, value2):
		#search list of vertices for the two values
		print "One or more vertices not found"
		#else: add the other vertext to its other's adj list
		
	def findVertex(value):
		#search for the key value and print adj vertices if its found
	
		
		
		
	
	
	
	
	

		
