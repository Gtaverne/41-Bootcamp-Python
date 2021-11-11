class Test(object):
	def _decorator(foo):
		def magic( self, *args ) :
			print ("start magic")
			foo( self, *args )
			print ("end magic")
		return magic

	@_decorator
	def bar( self , value) :
		print ("normal call", value)

	@_decorator
	def otherfunc( self) :
		print ("normal call")


	

test = Test()

test.bar(42)
test.otherfunc()