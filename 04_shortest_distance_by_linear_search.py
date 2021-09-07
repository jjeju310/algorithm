"""N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오."""
class CLList:
	class Node:
		def __init__(self, val, link):
			self.val = val
			self.link = link
			
	def __init__(self):
		self.tail = None
		self.size = 0
		
	def getSize(self):
		return self.size
		
	def isEmpty(self):
		return self.size == 0
	
	def insert(self, val):
		node = self.Node(val, None)
		if self.isEmpty():
			node.link = node
			self.tail = node
		else:
			node.link = self.tail.link
			self.tail.link = node
		self.size += 1
		
	def getFirst(self):
		if self.isEmpty():
			print("nothing")
		f = self.tail.link
		return f.val

	def getTail(self):
		if self.isEmpty():
			print("nothing")
		f = self.tail
		return f.val

	def printList(self):
		if self.isEmpty():
			print('List is empty.')
		else:
			f = self.tail.link
			p = f
			while p.link != f:	
				print(p.val, ' -> ', end='')
				p = p.link
			print(p.val)

	def moveTail(self,n):
		p = self.tail
		while(n>0):
			p = p.link
			n-=1
		self.tail = p

	def delete(self):  # 연결 리스트의 첫 노드를 삭제
		if self.isEmpty():
			print("nothing")
		x = self.tail.link
		if self.size == 1:	# 연결 리스트에 노드가 1개인 경우
			self.tail = None  # empty 리스트가 됨
		else:  # 노드가 2개 이상인 경우
			self.tail.link = x.link	 # last가 참조하는 노드가 두번째 노드를 연결
		self.size -= 1
		return x.val

cllist = CLList()
n, k= input().split()
n = int(n)
k = int(k)
for i in reversed(range(1,n+1)):
	cllist.insert(i)

result = []
while(n>0):
	cllist.moveTail(k-1)
	result.append(cllist.getFirst())
	cllist.delete()
	n -= 1

r_text = "<"
for idx, n in enumerate(result):
	if(idx==len(result)-1):
		r_text = r_text+str(n)+">"
	else:
		r_text = r_text+str(n)+", "

print(r_text)