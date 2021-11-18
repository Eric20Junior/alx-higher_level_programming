#!/usr/bin/python3
if __name__ == "__main__":
    import sys import agrv
    from calculator_1 import add, sub, mul, div
    count = len(argv)

    if count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>".format(argv[0])
                exit(1)

                num1 = int(argv[1])
                num2 = int(argv[3])
                op = argv[2]

                def not_found():
                    print("Unknown operator. Available operators: +, -, * and /")
                    exit(1)

                    def my_add():
                    toatl = add(num1, num2)
                    print("{:d} + {:d}".format(num1, num2, total)))
                    return total

                def my_sub():
                    toatl = sub(num1, num2)
                    print("{:d} - {:d}".format(num1, num2, total)))
                    return total

                def my_mul():
                    toatl = mul(num1, num2)
                    print("{:d} * {:d}".format(num1, num2, total)))
                    return total

                def my_div():
                    toatl = div(num1, num2)
                    print("{:d} / {:d}".format(num1, num2, total)))
                    return total

                options = {
                        "+": my_add,
                        "-": my_sub,
                        "*": my_mul,
                        "/": my_div,
                        }
                options.get(op, not_found)()
