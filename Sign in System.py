#make it take them to the stated users account home screen.
#make it so after 5 tries, it takes them to the sign in screen
for number in range(5):
        print ('Please Sign In')
        account = input('Please Enter Account Name: ')
        if account == 'test':
               print ('')
        else:
                print ('This User Does Not Exist. Please Try Again')
                print ('------------------------------------------------------')
                continue
        password = input('Enter Password: ')
        if password == '123':
                print ('')
                break
        else:
                print ('Your Password Is Incorrect, Please Try Again.')
                print ('------------------------------------------------------')
#----------------------------------------------------------------------------------------------------------
        #Below is just while coding please remove when done coding product
        #this is also so we can see the outcome of all of the steps and the results.
for number in range (10):
        print ('hi')
        Dev = input('don\'t answer this question: ')
        if Dev == 'wrong':
                print ('nooblet')
                print ('------------------------------------------------------')
                break
        else:
                print ('noobletx5000')
                print ('------------------------------------------------------')
	

