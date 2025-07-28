# Python Emulated Operating System (PyOS)

This project is an educational exploration into low-level system architecture, created by engineering a lightweight operating system from first principles using Python. It includes an emulated CPU and RAM, along with a custom-designed programming language stack, to provide a hands-on understanding of how computers execute code.

## Core Components

*   **Emulated RAM (`memory.py`)**: A virtual memory module that simulates data storage and retrieval. It uses a dictionary to map hexadecimal addresses to values and features a pointer system for sequential memory access.
*   **Emulated CPU (`processor.py`)**: The brain of the operation. The `Core` class simulates a CPU with a program counter and a primary accumulator (`registerA`). It fetches and executes low-level assembly instructions.
*   **Interpreter (`interpreter.py`)**: The OS "Kernel" that boots the system. It loads a compiled program, initializes the CPU core, and starts the execution cycle.
*   **Compiler (`compiler.py`)**: A powerful tool that translates a high-level, human-readable language into the low-level assembly code that the CPU can understand.

## The Two-Tier Language System

PyOS features a two-tier programming system, separating high-level logic from low-level machine instructions.

### 1. The High-Level Language (`.stm` files)
This is a user-friendly language designed for ease of use. It abstracts away the complexities of memory management and manual jump calculations.

**Features:**
*   **Variables**: Declare variables without worrying about memory addresses (e.g., `set my_var = 10`). The compiler handles memory allocation automatically.
*   **Control Flow**: Built-in support for `if`/`else`, `while` loops, and `repeat` loops.
*   **I/O**: Simple commands for `print`, user `input`, and generating random numbers (`randint`).

**Example `.stm` code:**

### 2. The Assembly Language (`.st` files)
This is the low-level language that the emulated CPU executes directly. It consists of simple, direct instructions that manipulate the CPU registers and RAM. All high-level `.stm` code is compiled down to this language.

**Instruction Set Includes:**
| Opcode | Description |
| :--- | :--- |
| **Memory** | |
| `SET <addr>` | Sets the RAM pointer to a specific address. |
| `STO <val>` | Stores a value into RAM at the current pointer address. |
| `LDA <addr>` | Loads a value from a RAM address into Register A. |
| `RGA` | Stores the value of Register A into RAM at the current pointer address. |
| **Control Flow** | |
| `JMP <line>` | Unconditionally jumps to a specific line number. |
| `JEQ <line>` | Jumps to a line if the value in Register A is `True`. |
| `JPA` | Jumps to the line number stored as a value in Register A. |
| **Logic & Arithmetic**| |
| `CMP <addr>` | Compares the value at `<addr>` with Register A. Sets Register A to `True` if equal. |
| `NCP <addr>` | The inverse of `CMP`. Sets Register A to `True` if not equal. |
| `GRE <addr>` | Sets Register A to `True` if its integer value is greater than the value at `<addr>`. |
| `LES <addr>` | Sets Register A to `True` if its integer value is less than the value at `<addr>`. |
| `ADD <addr>` | Adds the value at `<addr>` to Register A. |
| `INC <addr>` | Increments the integer value at `<addr>` by 1. |
| `NOT` | Inverts the boolean value in Register A. |
| **System** | |
| `DIS` | Displays the current value of Register A. |
| `INP "<prompt>"` | Prompts the user for input and stores it in Register A. |
| `RAN` | Stores a random integer in Register A. |
| `HLT` | Halts program execution. |


## How to Use PyOS

Here is the standard workflow from writing code to execution.

### Step 1: Write Code in the High-Level Language
Create a file with your own name (e.g., `my_program.stm`) and write your logic using the high-level commands like `set`, `if`, `while`, etc.
For convenience, you can use `workspace.st` (though it should conceptually be `workspace.stm`). The compiler is currently hard-coded to read from this file.

### Step 2: Compile Your Code
Run the `compiler.py` to translate your high-level code into low-level `.st` assembly. The compiler will read `workspace.st` and write the compiled output to `template.st`.

```sh
python compiler.py

This process converts your variables into memory addresses and your loops/conditionals into a series of CMP and JEQ instructions.
### Step 3: Run the Compiled Assembly
Execute the program using the interpreter.py, which loads and runs the compiled code from template.st.

# Ensure you are running the interpreter on the *output* file
python interpreter.py template.st

The interpreter will start the CPU, which will execute the assembly instructions one by one until it hits a HLT command.
