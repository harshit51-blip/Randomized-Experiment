import math
import random
import msvcrt
import statistics

# function to print out a refined output
def lst_refine(a: list) -> str:
    new_str = ""
    for i in a:
        new_str += f"{i} "
    return f"{new_str}\n"

def central_tendency(l):
    arith_mean = statistics.mean(l)
    
    return round(arith_mean,4)

# Main function
def main():
    # Initialization
    c = 1
    counter = 1
    num_list = []
    precision = 4
    ifactor = 0

    iterations = int(input("Enter number of iterations:  "))
    elements = int(input("Enter number of elements:  "))
    starting_val = float(input("Enter starting value:  "))

    for idx, _ in enumerate(range(elements)):
        some_val = math.sin(starting_val + idx)
        num_list.append(round(some_val, precision))
   
    print("iteration: ", counter)
    print("central tendency: ",central_tendency(num_list))
    print(lst_refine(num_list))

    while counter < iterations:

        some_list = [1,2,3,4]
        random_num = random.randint(1,101)
        if random_num in some_list:
            ifactor += random.randint(-50,51)
            print("ifactor: ", ifactor)

        for idx, i in enumerate(range(len(num_list))):
            num_list[i] = round(math.sin(starting_val + idx + c), precision)

        if ifactor > 0:
            num_list = [_ + round(ifactor/elements, precision) for _ in num_list]
        elif ifactor < 0:
            num_list = [_ - round(abs(ifactor/elements), precision) for _ in num_list]
        
        c += 1
        counter += 1
        print("iteration: ", counter)
        print("central tendency: ",central_tendency(num_list))
        print(lst_refine(num_list))


if __name__ == '__main__':
    main()
    char = msvcrt.getch()
