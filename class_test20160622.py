
class aa:
	w = 10
	def __init__(self):
		self.x = 11
		self.y = 12
	def add(self):
		return self.x + self.y
		
a = aa()
b = aa()
print(a.w)
print(b.w)
a.w = 122
aa.w = 100
print(a.w)
print(b.w)


print(a.add())

aa.w = 20
a.w = 13
print(aa.w,a.w)

a.t = 14
a.q = 15
print(a.t,a.q)

aa.m = 30
aa.n = 40
print(aa.m,aa.n)

b = aa()
print(b.x,b.y)
print(b.t,b.q)
print(b.m,b.n)