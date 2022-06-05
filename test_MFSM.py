import unittest
from MFSM import state_table, Trans, current_state, event


class MFSMTest(unittest.TestCase):
    def test_FSM(self):
        FSM = Trans("Moore Infinite Machine")
        # state table
        FSM.add("A0", state_table(0, "D", 0))
        FSM.add("A1", state_table(1, "B", 0))
        FSM.add("B0", state_table(0, "E", 0))
        FSM.add("B1", state_table(1, "C", 0))
        FSM.add("C0", state_table(0, "F", 0))
        FSM.add("C1", state_table(1, "C", 0))
        FSM.add("D0", state_table(0, "G", 0))
        FSM.add("D1", state_table(1, "E", 0))
        FSM.add("E0", state_table(0, "H", 0))
        FSM.add("E1", state_table(1, "F", 0))
        FSM.add("F0", state_table(0, "I", 0))
        FSM.add("F1", state_table(1, "F", 0))
        FSM.add("G0", state_table(0, "G", 0))
        FSM.add("G1", state_table(1, "H", 0))
        FSM.add("H0", state_table(0, "H", 0))
        FSM.add("H1", state_table(1, "I", 0))
        FSM.add("I0", state_table(0, "I", 1))
        FSM.add("I1", state_table(1, "I", 1))

        print(FSM.state_history)

        self.assertListEqual(FSM.event_history,[
         event(clock=1, from_state='A', to_state='B', input='10101010', pos=1, output='00'),
         event(clock=2, from_state='B', to_state='E', input='10101010', pos=2, output='000'),
         event(clock=3, from_state='E', to_state='F', input='10101010', pos=3, output='0000'),
         event(clock=4, from_state='F', to_state='I', input='10101010', pos=4, output='00000'),
         event(clock=5, from_state='I', to_state='I', input='10101010', pos=5, output='000001'),
         event(clock=6, from_state='I', to_state='I', input='10101010', pos=6, output='0000011'),
         event(clock=7, from_state='I', to_state='I', input='10101010', pos=7, output='00000111'),
         event(clock=8, from_state='I', to_state='I', input='10101010', pos=8, output='000001111')
         ])

        self.assertListEqual(FSM.state_history,[
         (0, current_state(name='A', all_input='10101010', pos=0, output='0')),
         (1, current_state(name='B', all_input='10101010', pos=1, output='00')),
         (2, current_state(name='E', all_input='10101010', pos=2, output='000')),
         (3, current_state(name='F', all_input='10101010', pos=3, output='0000')),
         (4, current_state(name='I', all_input='10101010', pos=4, output='00000')),
         (5, current_state(name='I', all_input='10101010', pos=5, output='000001')),
         (6, current_state(name='I', all_input='10101010', pos=6, output='0000011')),
         (7, current_state(name='I', all_input='10101010', pos=7, output='00000111')),
         (8, current_state(name='I', all_input='10101010', pos=8, output='000001111'))
        ])




