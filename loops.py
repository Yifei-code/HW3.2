def sum_of_odds(a):
    counter = 0
    sum = int(0)
    while True:
        if counter % 2 == 1:
            print(counter)
            sum = sum + counter
            counter = counter + 1
            continue
        elif counter > 2:
            break
        print("sum:",sum)





def count_up(a):
    counter = 0
    sum = int(0)
    while counter <= a:
        print(counter)
        sum = sum+counter
        counter = counter+1
    print("sum:",sum)
    
    
def count_down(a):
    sum = int(0)
    while a >= 0:
        print(a)
        sum = sum + a
        a = a - 1
    print("sum:",sum)
    
    
def main():
        # count_down(5)
        # count_up(4)
        # sum_of_odds(10)
        print_range_for(range(1,10,3))
        print_range_for("Goffy plays basketball all day long!!!")
        
if __name__ == '__main__':
    main()