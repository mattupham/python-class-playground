#classes and instances
class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Matt', 'Upham', 10)

print(emp_1)

print('Full Name: ', emp_1.fullname())