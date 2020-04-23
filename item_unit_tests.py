import unittest

import item

class TestItemClassInit(unittest.TestCase):
    
    def test_init_x(self):
        i = item.Item(0, 0, 20, 20, 50, 50)
        result = item.getX()
        self.assertEqual(0, result)
    
    def test_init_y(self):
        i = item.Item(0, 0, 20, 20, 50, 50)
        result = item.getY()
        self.assertEqual(0, result)
    
    def test_init_width(self):
        i = item.Item(0, 0, 20, 20, 50, 50)
        result = item.getWidth()
        self.assertEqual(20, result)
    
    def test_init_height(self):
        i = item.Item(0, 0, 20, 20, 50, 50)
        result = item.getHeight()
        self.assertEqual(20, result)
    
    def test_init_world_width(self):
        i = item.Item(0, 0, 20, 20, 50, 50)
        result = item.getWorldWidth()
        self.assertEqual(50, result)
    
    def test_init_world_height(self):
        i = item.Item(0, 0, 20, 20, 50, 50)
        result = item.getWorldHeight()
        self.assertEqual(50, result)
    
    def test_init_alive(self):
        i = item.Item(0, 0, 20, 20, 50, 50)
        result = item.isAlive
        self.assertEqual(True, result)

class TestItemClassMethods(self):
    
    def test_kill_method(self):
        i = item.Item(0, 0, 20, 20, 50, 50)
        i.kill()
        result = item.isAlive()
        self.assertEqual(False, result)

    def test_revive_method(self):
        i = item.Item(0, 0, 20, 20, 50, 50)
        i.kill()
        i.revive()
        result = item.isAlive()
        self.assertEqual(False, result)
    
    def test_hits_method(self):
        i = item.Item(0, 0, 20, 20, 50, 50)
        other = item.Item(10, 10, 20, 20, 50, 50)
        result = item.hits(other)
        assertEqual(True, result)

if __name__ == '__main__':
    unittest.main()