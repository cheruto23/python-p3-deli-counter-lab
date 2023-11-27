def line(list):
    if len(list) > 0:
        result = ['The line is currently:']
        counter = 1
        for element in list:
          result.append(f"{counter}. {element}")
          counter+=1
        result = ' '.join(result)
        print(result)
    else:
        print('The line is currently empty.')

def take_a_number(queue, name):
    number_in_line = len(queue) + 1
    queue.append(name)
    print(f"Welcome, {name}. You are number {number_in_line} in line.")
    return queue
    

def now_serving(queue):
    if len(queue) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {queue[0]}.")
        queue.pop(0)
        return queue