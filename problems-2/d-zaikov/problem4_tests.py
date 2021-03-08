import unittest
import tempfile
from problem4 import find_seq

class TestStringMethods(unittest.TestCase):

  def test_123(self):
    cnt, posl = find_seq('123', 'pi.txt')
    self.assertEqual(cnt, 4185)
    self.assertEqual(posl, [1923, 2937, 2975, 3891, 6547])
    
  def test_1415(self):
    cnt, posl = find_seq('1415', 'pi.txt')
    self.assertEqual(cnt, 424)
    self.assertEqual(posl, [0, 6954, 29135, 45233, 79686])
    
  def test_file_not_found(self):
    self.assertRaises(FileNotFoundError, find_seq, '1111', '')
    
  def test_is_a_dir(self):
    with tempfile.TemporaryDirectory() as tmpdir:
        self.assertRaises(IsADirectoryError, find_seq, '1111', str(tmpdir))
  #WINDOWS TEST
  #def test_permission(self):
  #  self.assertRaises(PermissionError, find_seq, '1111', 'pi_admin.txt')

if __name__ == '__main__':
    unittest.main()