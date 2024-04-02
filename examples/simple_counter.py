import pyverilator

sim = pyverilator.PyVerilator.build("counter.v")

trace_en = False
logs = True
if trace_en:
    # start gtkwave to view the waveforms as they are made
    sim.start_gtkwave()


if trace_en:
    # add all the io and internal signals to gtkwave
    sim.send_to_gtkwave(sim.io)
    sim.send_to_gtkwave(sim.internals)
# tick the automatically detected clock
sim.clock.tick()

# set rst back to 0
sim.io.rst = 0

# check out when en = 0
sim.io.en = 0
curr_out = sim.io.out
# sim.io is a pyverilator.Collection, accessing signals by attribute or
# dictionary syntax returns a SignalValue object which inherits from int.
# sim.io.out can be used just like an int in most cases, and it has extra
# features like being able to add it to gtkwave with
# sim.io.out.send_to_gtkwave(). To just get the int value, you can call
# sim.io.out.value
if logs:
    print("sim.io.out = " + str(curr_out))

# check out when en = 1
sim.io.en = 1
curr_out = sim.io.out
if logs:
    print("sim.io.out = " + str(curr_out))

sim.clock.tick()

# check out after ticking clock
curr_out = sim.io.out
if logs:
    print("sim.io.out = " + str(curr_out))

sim.clock.tick()

# check out after ticking clock
curr_out = sim.io.out
if logs:
    print("sim.io.out = " + str(curr_out))

sim.io.rst = 1
curr_out = sim.io.out
if logs:
    print("sim.io.out = " + str(curr_out))

sim.clock.tick()

# check out after ticking clock
curr_out = sim.io.out
if logs:
    print("sim.io.out = " + str(curr_out))

sim.clock.tick()

# check out after ticking clock
sim.io.rst = 0
curr_out = sim.io.out
if logs:
    print("sim.io.out = " + str(curr_out))

for count in range(0, 260):
    sim.clock.tick()

    if logs:
        # check out after ticking clock
        curr_out = sim.io.out
        print("sim.io.out = " + str(curr_out))

# sim.stop_gtkwave()
