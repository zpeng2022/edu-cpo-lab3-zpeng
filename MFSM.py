from collections import namedtuple
import copy

event = namedtuple("event", "clock, from_state, to_state, input, pos, output")
current_state = namedtuple("current_state", "name, all_input, pos, output")
state_table = namedtuple("state_table", "input next_state output")


def name_helper(name, index):
    return name + str(index)


class Trans(object):
    def __init__(self, name):
        self.name = name
        self.states = []
        self.state_dict = {}
        self.state_history = []
        self.event_history = []

    # pos --> input[pos - 1]
    def set_initial_state(self, name, input, pos, output):
        state = current_state(name, input, pos, output)
        return state

    def _trans_event(self, clock, state):
        name = state[0]
        all_input = state[1]
        pos = state[2]
        output = state[3]
        pos += 1
        # print("all input string: " + all_input)
        # print("pos: " + str(pos - 1))
        index = all_input[pos - 1]
        state_name = name_helper(name, index)
        table = self.state_dict[state_name]
        next_state = table[1]
        next_output = table[2]
        output += str(next_output)
        result_event = event(clock, name, next_state, all_input, pos, output)
        return result_event

    def _trans_state(self, event):
        input = event[3]
        name = event[2]
        pos = event[4]
        output = event[5]
        state = current_state(name, input, pos, output)
        return state

    def add(self, name, table):
        self.state_dict[name] = table

    def add_stats_from_table(self, filename):
        table_file = open(filename, "r")
        # FSM.add_state(tem)
        result = table_file.readline()
        states = result.split(' ')
        for elem in states:
            self.add_state(elem)

        # FSM.add(d, state_table(a, b, c))
        trans_state = table_file.readline()
        while trans_state != "":
            chunks = trans_state.split(' ')
            self.add(chunks[0],
                     state_table(int(chunks[1]),
                                 chunks[2],
                                 int(chunks[3])))
            trans_state = table_file.readline()

        table_file.close()

    def add_state(self, name):
        self.states.append(name)

    def visualize(self):
        res = ["digraph finite_state_machine {",
               " rankdir=LR;", " node [shape = circle];"]

        for state_name, state in self.state_dict.items():
            name = state_name[0]
            input = state[0]
            next_state = state[1]
            res.append(" {} -> {} [label = '{}'];".format(
                name, next_state, input))

        res.append("}")
        return "\n".join(res)

    def run(self, initial_state, initial_output, series, limit=100):
        clock = 0
        index = len(series)
        # print("index: " + str(index))
        result = initial_output
        state = self.set_initial_state(initial_state,
                                       series, 0, initial_output)
        events = []
        self.state_history = [(clock, copy.copy(state))]

        while limit > 0 and clock < index:
            limit -= 1
            clock += 1
            # print("clock: " + str(clock))
            new_events = self._trans_event(clock, state)
            new_state = self._trans_state(new_events)
            events = new_events
            state = new_state
            self.state_history.append((clock, copy.copy(state)))
            self.event_history.append(events)
            result = events[5]

        if limit == 0:
            print("limit reached!")
        return result
