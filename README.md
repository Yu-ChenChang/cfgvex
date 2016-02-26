# cfgvex
CFG-VEX is a sub-project based on [MC-Semantics](https://github.com/trailofbits/mcsema) and [PyVEX](https://github.com/angr/pyvex) for adding VEX\_IR into original CFG file. The CFG protocol is extended with additional option entry \(vex\_ir\) for each instruction.

### Building
The project needs to install [MC-Semantics](https://github.com/trailofbits/mcsema), [PyVEX](https://github.com/angr/pyvex) and [Protocol Buffer](https://github.com/google/protobuf). Change directory into cfgvex and `make` will setup extended CFG protocol.

### Usage
`tools` contains useful tools such as converting original CFG files into extended CFG files with VEX IR for each instruction. `cfg_examples` are examples from [MC-Semantics](https://github.com/trailofbits/mcsema) with extended CFG protocol.
