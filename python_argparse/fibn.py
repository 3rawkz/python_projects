# uses the argparse module to handle command line options and arguments
# generates help and provides usage cases for enduser
# great for input validation of tooling and utilities
import argparse


def fib(n):
    a, b = 0, 1
    for element in range(n):
        a, b = b, a+b
    return a

def Main():
    parser = argparse.ArgumentParser()
	# determines args that can't be called at the same time
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-v, "--verbose", action="store_true")
	group.add_argument("-q, "--quiet", action="store_true")
	# testing argparse with fibonacci number
    parser.add_argument("num", help="The number of ele in fib series to calculate", type=int)
    parser.add_argument('-o', '--output', help="Output result to .txt file",
                        action="store_true")
    # parse parses args according to above parameters
    args = parser.parse_args()

    # after the parse num is now an attribute of the 'args' object
    result = fib(args.num)
    print("The "+str(args.num)+'th fib number is: '+str(result))

    if args.output:
        file = open("fibonacci.txt", "a")
        file.write(str(result)+'\n')
    Main()
	
    parser.add_argument("num", help="The number of ele in fib series to calculate", type=int)
    parser.add_argument('-o', '--output', help="Output result to .txt file",
                        action="store_true")
    # parse parses args according to above parameters
    args = parser.parse_args()

    # after the parse num is now an attribute of the 'args' object
    result = fib(args.num)
    print("The "+str(args.num)+'th fib number is: '+str(result))

    if args.output:
		# if file doesn't exist it will be created, if does overwritten
        file = open("fibonacci.txt", "a")
        file.write(str(result)+'\n')
	elif args.quiet:
		print(result)
	else:
		print("Fib("+str(args.num)+") = " str(result)) =

# if the file_name is called via cmd line then main is run
if __name__ == '__main__':
	Main()
