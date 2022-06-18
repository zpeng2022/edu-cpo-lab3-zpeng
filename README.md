# slay_the_dragon - lab #3 - variant 4

This is an example project which demonstrates Moore finite state structure and necessary

## Project structure

- `MFSM.py` -- implementation of `Moore finite state` class
- `test_MFSM.py` -- tests for Moore finite state machine
- `localcheck.bash` -- check codestyle and typical python error
- on a local machine

## Features

- add test_FSM
- add test_elevator_example
- add test_visual

## Contribution

- Zhan,Peng (zpeng@hdu.edu.cn) -- write the main class part.
- Zhong,ZhuZhou(212320020@hdu.edu.cn) -- write the test part.

## Changelog

- 06.05.2022 - 3
  - add visualize for moore finite machine
- 06.05.2022 - 2
  - add test_MFSM.py
  - add local checker
- 06.05.2022 - 1
  - add MFSM.py
  - update README.md


## Show Graphviz
```graphviz
digraph finite_state_machine {
    fontname="Helvetica,Arial,sans-serif"
    node [fontname="Helvetica,Arial,sans-serif"]
    edge [fontname="Helvetica,Arial,sans-serif"]
    rankdir=LR;
    node [shape = doublecircle]; A I;
    node [shape = circle];
    A -> D [label = "0"];
    A -> B [label = "1"];
    B -> E [label = "1"];
    B -> C [label = "1"];
    C -> F [label = "0"];
    C -> C [label = "1"];
    D -> G [label = "0"];
    D -> E [label = "1"];
    E -> H [label = "0"];
    E -> F [label = "1"];
    F -> I [label = "0"];
    F -> F [label = "1"];
    G -> G [label = "0"];
    G -> H [label = "1"];
    H -> H [label = "0"];
    H -> I [label = "1"];
    I -> I [label = "0"];
    I -> I [label = "1"];
}
```

## Design notes

- Advantages of unit testing:
  - it help us write better code
  - it help us catch bugs earlier
  - it makes us more efficient at writing code
  - it make us detect regression bugs
- Disadvantage of unit testing:
  - it takes time to write cases
  - tests require a lot of time for maintenance
  - it can be challenging to test GUI code
  - unit testing can't catch all errors
- Advantages of PBT testing:
  - the PBT provides a reasonable estimate of the
  - evidential test result within the relevant forensic range
- Disadvantages of PBT testing:
  - it also be challenging to test GUI code
