import graphviz

f = graphviz.Digraph('finite_state_machine', filename='moore_fsm.gv')
f.attr(rankdir='LR', size='8,5')

f.attr('node', shape='doublecircle')
f.node('A')
f.node('I')

f.attr('node', shape='circle')
f.edge('A', 'D', label='0')
f.edge('A', 'B', label='1')
f.edge('B', 'E', label='0')
f.edge('B', 'C', label='1')
f.edge('C', 'F', label='0')
f.edge('C', 'C', label='1')
f.edge('D', 'G', label='0')
f.edge('D', 'E', label='1')
f.edge('E', 'H', label='0')
f.edge('E', 'F', label='1')
f.edge('F', 'I', label='0')
f.edge('F', 'F', label='1')
f.edge('G', 'G', label='0')
f.edge('G', 'H', label='1')
f.edge('I', 'I', label='0')
f.edge('I', 'I', label='1')

f.view()
