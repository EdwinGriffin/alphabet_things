import random
import csv
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = list(alpha)
alpha_list_for_random = list(alpha)
alpha_pho_dict = {'a': 'ay', 'b': 'bee', 'c': 'see', 'd': 'dee', 'e': 'ee', 'f': 'ef', 'g':'jee', 'h':'aitch', 'i':'eye',
             'j': 'jay', 'k':'kay', 'l':'el', 'm':'em', 'n':'en', 'o':'oh', 'p':'pee', 'q':'cue', 'r':'ar', 's':'ess',
             't': 'tee', 'u': 'you', 'v': 'vee', 'w':'doubleu', 'x':'ex', 'y':'why', 'z': 'zed'}
inv_alpha_pho_dict = {v: k for k, v in alpha_pho_dict.items()}
random.shuffle(alpha_list_for_random)
rand_alpha = ''.join(alpha_list_for_random)

def generate_random():
    random.shuffle(alpha_list_for_random)
    rand_alpha = ''.join(alpha_list_for_random)
    return rand_alpha

alpha_pho_list = []
for key in alpha_pho_dict:
    alpha_pho_list.append(alpha_pho_dict[key])

def reorder(alphabet_as_string, input_as_list, start, iteration=0, old_input=None, iterations=1, file=None):
    
    if iteration == iterations:
        #print("Finished iterations")
        return alphabet_as_string
    #print(f"Cycle: {iteration + 1}")
    #print(f"Alphabet used this cycle: {alphabet_as_string}")
    #print(f"Input phonemes: {input_as_list}")
    staged = sorted(input_as_list, key=lambda word: [alphabet_as_string.index(c) for c in word])
    #print(f"New Phonemes: {staged}")
    new_alpha = ''
    for e in staged:
        new_alpha += inv_alpha_pho_dict[e]
    #print(f"New Alphabet: {new_alpha}")
    if staged == old_input:
        # print("Steady State Achieved")
        # print(f"Cycles to achieve Steady State: {iteration}")
        # print(f"Final Alpha: {new_alpha}")
        writer.writerow([iteration, start, new_alpha])
        return iteration
    return reorder(new_alpha, staged, start = start, iteration = iteration + 1, old_input = input_as_list, iterations = iterations, file=file)

# print(reorder(alpha, alpha_pho_list, iterations=100))
# quit()
f = open('alphabet_fun_output.csv', 'w', newline='')
writer = csv.writer(f)
average_cycles = []
for i in range(10000):
    rando = generate_random()
    average_cycles.append(reorder(rando, alpha_pho_list, start = rando, iterations=100, file=writer))
f.close()
print(sum(average_cycles) / len(average_cycles))

f = open('alphabet_fun_output.csv')
reader = csv.reader(f, delimiter=',')
alphas = []
finals = []
for row in reader:
    cycle, alpha, final = row
    alphas.append(alpha)
    finals.append(final)
count = 0
for i, test in enumerate(finals):
    for idx, other in enumerate(finals[i+1:]):
        if test == other:
            print(alphas[i], test)
            count+= 1
print(f"Count: {count}")