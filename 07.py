#Day 07

with open('./07.txt') as myinput:
    inputlines = myinput.readlines()

wire_list = [line.replace('AND', '&')
                 .replace('OR', '|')
                 .replace('NOT', '~')
                 .replace('LSHIFT', '<<')
                 .replace('RSHIFT', '>>')
                 .strip().split(' -> ') for line in inputlines]

for (signal, wire) in wire_list:
    if '~' in signal:
        wire_list[wire_list.index([signal, wire])][0] += ' & 65535'

def get_signal(wire_list, resulting_signals, wire_a_signal):
    wires = [signal_wire[:] for signal_wire in wire_list]
    if wire_a_signal:
        for (signal, wire) in wires:
            if wire == 'b':
                wires[wires.index([signal, wire])][0] = wire_a_signal
                break
    for (signal, wire) in wires:
        if signal.isdigit():
            resulting_signals.add((signal, wire))
    while True:
        for idx in range(len(wires)):
            if not wires[idx][0].isdigit():
                for (resulting_signal, resulting_wire) in resulting_signals:
                    if resulting_wire in wires[idx][0].split():
                        wires[idx][0] = wires[idx][0].replace(resulting_wire, resulting_signal)
                try:
                    wires[idx][0] = str(eval(wires[idx][0]))
                    resulting_signals.add((wires[idx][0], wires[idx][1]))
                    if wires[idx][1] == 'a':
                        return wires[idx][0]
                except:
                    continue

#Part 1

wire_a_signal = get_signal(wire_list, set(), 0)
print(wire_a_signal)

#Part 2

wire_a_signal = get_signal(wire_list, set(), wire_a_signal)
print(wire_a_signal)