import unittest
from azurecrcAPI import updatecount
 
class TestCounter(unittest.TestCase):

    def test_updatecount(self):
        result = updatecount({'PartitionKey': '0', 'RowKey': '0', 'Counter': 0})
        self.assertEqual(result, {'PartitionKey': '0', 'RowKey': '0', 'Counter': 1})

if __name__ == '__main__':
    unittest.main()