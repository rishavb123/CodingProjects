__author__ = 'Bhagat'
def input_data():
    name = raw_input("Disease Name: ")
    print 'Enter the year as -1 to stop'
    xs=[]
    ys=[]
    while True:
        try_again=True
        year=0
        while try_again:
            try_again=False
            year = raw_input("Year: ")
            try:
                if int(year)>2017 or (int(year)<=0 and int(year)!=-1):
                    raise ValueError
            except ValueError:
                print 'Please enter a valid year'
                try_again=True
        if int(year)!=-1:
            xs.append(int(year))
        else:
            break
        try_again=True
        num_of_people=0
        while try_again:
            try_again=False
            num_of_people = raw_input("People who got "+name+": ")
            try:
                if int(num_of_people)>8*10**9 or int(num_of_people)<=0:
                    raise ValueError
            except ValueError:
                print 'Please enter a valid number of people'
                try_again=True
        ys.append(int(num_of_people))
    file = open('text.txt','w')
    file.write(name)
    file.close()
    file = open(name+'xs.txt','w')
    file.write(str(xs))
    file.close()
    file = open(name+'ys.txt','w')
    file.write(str(ys))
    file.close()
input_data()