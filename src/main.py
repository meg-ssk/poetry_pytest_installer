from lib.operator import BasicArithmeticOperator
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('val1')
    parser.add_argument('val2')

    args = parser.parse_args()

    val1, val2 = float(args.val1), float(args.val2)
    operator = BasicArithmeticOperator(val1, val2)

    print("add: " + str(operator.add()))
    print("sub: " + str(operator.sub()))
    print("mul: " + str(operator.mul()))
    print("dev: " + str(operator.dev()))

if __name__ == '__main__':
    main()