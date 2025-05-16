import unittest
from src.robot_behaviour_management.robot_state_machines import CheckRobotStateMachine


class TestRobotStateMachine(unittest.TestCase):
    
    def setUp(self):
        print("setUp...")
        self.result1 = CheckRobotStateMachine(10, "A1")
        self.result2 = CheckRobotStateMachine(15, "B1")
        print("setUp: ", self.result1.current_battery_p, self.result1.current_state)
        print("setUp: ", self.result2.current_battery_p, self.result2.current_state)

    def test_increase_battery(self):
        self.result1.increase_battery(5)
        self.result2.increase_battery(6)
        print("test_p_inc: result1: ", self.result1.current_battery_p, " , result2: ", self.result2.current_battery_p)
        self.assertEqual(self.result1.current_battery_p, 15)
        self.assertEqual(self.result2.current_battery_p, 21)

    def test_update_current_state(self):
        self.result1.update_current_state("A2")
        self.result2.update_current_state("B2")
        print("test_p_inc: result1: ", self.result1.current_state, " , result2: ", self.result2.current_state)
        self.assertEqual(self.result1.current_state, "A2")
        self.assertEqual(self.result2.current_state, "B2")


if "__name__" == "__main__":
    unittest.main()
