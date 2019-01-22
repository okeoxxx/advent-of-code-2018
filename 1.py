
frequency = 0
results = [0]
counter = 0
file = open('1.txt','r')

def find_twice(frequency,counter):
    file.seek(0)
    while True:
        try:
            change = int(file.readline())
        except:
            break
        frequency += change
        result = frequency
        if result in results:
#            print(result,results)
            return result,results
        elif counter == 0:
            results.append(result)
    counter += 1
    print(frequency, counter)
    return find_twice(frequency,counter)

print(find_twice(frequency,counter))
