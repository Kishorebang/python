applicationname=['C','java','python']
author=['gowtham', 'kishore', 'ram']
version=[1,2,3]
year=[2015,2010,2000]
cost=[ 2340, 456, 789]
j=1
while(1):
    choice=int(input("Enter your choice\t:\t"))
    if(choice==1):
        find_author=input("Enter author\t:\t")
        n=len(author)
        exist=0
        for i in range(0,n):
            if(find_author==author[i]):
                print('application name\t:\t',applicationname[i])
                print('Author name\t:\t',author[i])
                print('version\t\t:\t',version[i])
                print('year\t\t:\t',year[i])
                print('cost\t\t:\t',cost[i])
                exist=1
        if(not exist):
            print('the author name does not exist in the list')
    if(choice==2):
        find_year=int(input("Enter Year\t:\t"))
        n=len(year)
        exist=0
        for i in range(0,n):
            if(find_year==year[i]):
                print('application name\t:\t',applicationname[i])
                print('Author name\t:\t',author[i])
                print('version\t\t:\t',version[i])
                print('year\t\t:\t',year[i])
                print('cost\t\t:\t',cost[i])
                exist=1  
        if(not exist):    
            print('the year does not exist in the list')
    if(choice==3):
            test_list=[['gowtham','C',1,2015,2340],['kishore','java',2,2010,456],['ram','python',3,2000,789]]
            test_list.sort(key=lambda test_list:test_list[4])
            print(" "+str(test_list))
    if(choice==4):
        n=len(applicationname)
        for i in range(0,n):
                print('application name\t:\t',applicationname[i])
                print('Author name\t:\t',author[i])
                print('version\t\t:\t',version[i])
                print('year\t\t:\t',year[i])
                print('cost\t\t:\t',cost[i])
    if(choice==5):
        find_year=int(input("Enter Year\t:\t"))
        find_author=input("Enter author name\t:\t")
        n=len(year)
        exist=0
        for i in range(0,n):
            if((find_year==year[i])and(find_author==author[i])):
                    print('application name\t:\t',applicationname[i])
                    print('Author name\t:\t',author[i])
                    print('version\t\t:\t',version[i])
                    print('year\t\t:\t',year[i])
                    print('cost\t\t:\t',cost[i])
                    exist=1
        if(not exist):
            print('the authorname and year does not found in the list')
    if(choice==6):
        exit()
