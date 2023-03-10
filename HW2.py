import itertools
#This program implements a bottom up synthesis approach that builds on HW1
#The key differences in this program's performance are how the operands are iterated. 
#It is still a brute force approach but synthesizes the functions by enumerating all of the combinations of operands.

def check(program, examples):
    for input, output in examples:
        if eval(program,{'x': input}) != output:
            return False
    return True

def synthesis(examples):
    for i in range(1, 5):
        operations = ['+', '-', '*', '/'] #grammar
        op_combo = itertools.product(operations, repeat=i)
        nums = itertools.product(range(1, 11), repeat=i+1)
        #find the cartesian product of the operands - all possible combinations
        for ops in ob_combo:
            for num in nums:
                num_ops = zip(num[:-1], ops)
                program = []
                for x,op in num_ops:
                    program.append(str(x) + op)
                #zip pairs the first item in each iterator together (num and operation)
                program = ' '.join(program) + str(num[-1])
                if check(program, examples):
                    return program
    
if __name__ == '__main__':
    examples = input("Please enter your input-output examples separated by commas: ")
    examples = examples.split(',')
    examples = [tuple(map(int, example.strip().split())) for example in examples]

    print("\nExamples:", examples)
    solution = synthesis(examples)
    if solution:
        print("Solution:", solution)
    else:
        print("Sorry, no solution was found.")
