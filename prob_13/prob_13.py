k = 100
gamma = 0.8
prev_warm = [0]
prev_cool = [0]

def coolFast(i): # Is in the cool state and has decided to take the fast route
    return ((0.5 * (2 + (gamma**i * prev_cool[-1]))) + (0.5 * (2 + (gamma**i * prev_warm[-1]))))
def coolSlow(i): # Is in the cool state and has decided to take the slow route
    return (1.0 * (1 + (gamma**i * prev_cool[-1])))
def warmSlow(i): # Is in the warm state and has decided to take the slow route
    warm_path = 0.5 * (1.0 + (gamma**i * prev_warm[-1]))
    cool_path = 0.5 * (1.0 + (gamma**i * prev_cool[-1]))
    return warm_path + cool_path
def warmFast(): # This leads to a dead state why would you ever call this?
    return (0)

for i in range(0,k):
    print("Iteration: " + str(i+1))
    # Deciding which cool to use:
    coolFast_val = coolFast(i)
    coolSlow_val = coolSlow(i)
    warmSlow_val = warmSlow(i)
    if(coolFast_val > coolSlow_val):
        prev_cool.append(coolFast_val)
    else:
        prev_cool.append(coolSlow_val)
    # Calculating warm option:
    prev_warm.append(warmSlow_val)
    print("Cool Value: " + str(prev_cool[-1]))
    print("Warm Value: " + str(prev_warm[-1]))
print("Warm List:" + str(prev_warm))
print("Cool List:" + str(prev_cool))
