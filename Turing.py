import sys

#Global Variables
tape = ['e']
i = 1
state = 'q0'

def main():
    number = input ("* Enter a positive number :\n")
    for d in str(number):
        tape.append(int(d))
    tape.append('#')
    
    print (f"\n* Starting turing machine with initial state {state} on position {i}")
    print (f"* Initial tape is {tape} \n")

    while True:
        Transition()

def Transition():
    global i
    global state
    if state == 'q0':
        if tape[i] == 9:
            i += 1
            return
        if tape[i] == '#':
            tape[i] = '0'
            print (tape)
            state = 'qR9'
            i -= 1
            return
        if tape[i] != 9:
            state = 'q'
            i += 1
            return
    if state == 'q' :
        if tape[i] == '#':
            state = 'qR'
            i -= 1
            return
        if tape[i] != '#':
            i += 1
            return
    if state == 'qR':
        if tape[i] == 9:
            tape[i] = 0
            print (tape)
            i -= 1
            return
        if tape[i] == 0:
            state = 'end'
            tape[i] = 1
            print (tape)
            end()
        if tape[i] == 1:
            state = 'end'
            tape[i] = 2
            print (tape)
            end()
        if tape[i] == 0:
            state = 'end'
            tape[i] = 1
            print (tape)
            end()
        if tape[i] == 2:
            state = 'end'
            tape[i] = 3
            print (tape)
            end()
        if tape[i] == 3:
            state = 'end'
            tape[i] = 4
            print (tape)
            end()
        if tape[i] == 4:
            state = 'end'
            tape[i] = 5
            print (tape)
            end()
        if tape[i] == 5:
            state = 'end'
            tape[i] = 6
            print (tape)
            end()
        if tape[i] == 6:
            state = 'end'
            tape[i] = 7
            print (tape)
            end()
        if tape[i] == 7:
            state = 'end'
            tape[i] = 8
            print (tape)
            end()
        if tape[i] == 8:
            state = 'end'
            tape[i] = 9
            print (tape)
            end()
    if state == 'qR9':
        if tape[i] != 'e':
            tape[i] = 0
            print (tape)
            i -= 1
            return
        if tape[i] == 'e':
            i += 1
            state = 'q1'
            return
    if state == 'q1':
        tape[i] = 1
        print (tape)
        end()


def end():
    sys.exit(f"\n* Machine finished succesfully, final number = {tape}")

if __name__ == "__main__":
    main()
