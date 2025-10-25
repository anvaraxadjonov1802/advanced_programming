import unittest
from unittest.mock import Mock
from greeter import Greeter


class TestGreeter(unittest.TestCase):
    def test_greeter_morning(self):
        mock = Mock()
        mock.now_hour.return_value = 8
        greeter = Greeter(mock)
        self.assertEqual(greeter.greet("Anvar"), "Good Morning Jasur!")
    
    def test_greeter_afternoon(self):
        mock = Mock()
        mock.now_hour.return_value = 15
        greeter = Greeter(mock)
        self.assertEqual(greeter.greet("Olim"), "Good Afternoon, Olim!")
        
    def test_greeter_morning(self):
        mock = Mock()
        mock.now_hour.return_value = 21
        greeter = Greeter(mock)
        self.assertEqual(greeter.greet("Bobur"), "Good Evening, Bobur!")

if __name__ == "__main__":
    unittest.main()
        