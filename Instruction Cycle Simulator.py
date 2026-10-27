
# Mini Project: Instruction Cycle Simulator
# Subject: Computer Organization and Architecture

def fetch(instruction, pc):
    print("\n--- FETCH PHASE ---")
    print("Program Counter (PC):", pc)
    print("Instruction fetched:", instruction)
    return instruction


def decode(instruction):
    print("\n--- DECODE PHASE ---")
    parts = instruction.split()

    opcode = parts[0]
    operands = parts[1:]

    print("Opcode:", opcode)
    print("Operands:", operands)

    return opcode, operands


def execute(opcode, operands, registers):
    print("\n--- EXECUTE PHASE ---")

    if opcode == "LOAD":
        register = operands[0]
        value = int(operands[1])
        registers[register] = value
        print(register, "loaded with value", value)

    elif opcode == "ADD":
        reg1 = operands[0]
        reg2 = operands[1]
        registers[reg1] += registers[reg2]
        print("Result:", reg1, "=", registers[reg1])

    elif opcode == "SUB":
        reg1 = operands[0]
        reg2 = operands[1]
        registers[reg1] -= registers[reg2]
        print("Result:", reg1, "=", registers[reg1])

    elif opcode == "DISPLAY":
        register = operands[0]
        print("Output:", registers[register])

    else:
        print("Unknown instruction!")


def main():
    print("===== INSTRUCTION CYCLE SIMULATOR =====")

    instructions = [
        "LOAD R1 10",
        "LOAD R2 5",
        "ADD R1 R2",
        "SUB R1 R2",
        "DISPLAY R1"
    ]

    registers = {"R1": 0, "R2": 0}
    pc = 0

    for instruction in instructions:
        fetched = fetch(instruction, pc)
        opcode, operands = decode(fetched)
        execute(opcode, operands, registers)

        pc += 1

    print("\n===== PROGRAM COMPLETED =====")
    print("Final Register Values:", registers)
    print("Total Instructions Executed:", len(instructions))


if __name__ == "__main__":
    main()
