import unittest
from server import Tally, User

class TestTally(unittest.TestCase):

	def setUp(self):
		self.tally = Tally([User('foo'), User('bar')])

	def test_all_voted(self):
		self.tally.set_voted('foo', True)
		self.tally.set_voted('bar', True)

		self.assertTrue(self.tally.all_voted())

	def test_all_voted_false(self):
		self.tally.set_voted('foo', True)
		self.tally.set_voted('bar', False)

		self.assertFalse(self.tally.all_voted())

	def test_get_brews(self):
		self.tally.add_to('foo')
		self.tally.add_to('foo')

		self.assertEquals(2, self.tally.get_brews('foo'))

if __name__ == '__main__':
	unittest.main()