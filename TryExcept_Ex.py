


def getInfo():
    var1 = input('Please provide the first numeric value:\n>>>')
    var2 = input('Please provide the second numeric value:\n>>>')
    return var1, var2

def multiply():
    go = True 
    while go:
        num1, num2 = getInfo()
        try:
            sum = int(num1) * int(num2)
            print('{} * {} = {}'.format(num1, num2, sum))
            go = False 
        
        except ValueError as error:
            print('{}: You did not provide a numeric value!'.format(error))
        finally:
            print("Welp, it's over squirt")



def compute():
    go = True
    while go:
        # you can return multiple values, but must set them respectively to whats being returned
        var1, var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            print('\n{} + {} = {}'.format(var1, var2, var3))
            go = False
        except ValueError as e :
            print('\n{}: You did not provide a numeric value!!!'.format(e))
        except: 
            print('\nOpps, you provided an invalid input, program will close now!')
        # finally:
            # print('Moving on...')




if __name__ == '__main__':
    # compute()
    multiply() 