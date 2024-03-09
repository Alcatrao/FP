import math

def floatInput(prompt, min=-math.inf, max=math.inf):
    while True:
        assert min<max
        try:
            res = float(input(prompt))
            #return res
        except:
            print("ERROR: Not a float!")
        else:
            validez = checkValue(res, min, max)
            if validez == None or validez == False:
                print("ERROR: Value should be in [{}, {}]!".format(min, max))
                #raise Exception(f"res = {res} is not in the range [{min}, {max}]!")
            else:
                return res

def checkValue(n, min, max):
    try:
        if n>=min and n<=max:
            return True
        else:
            return False
    except:
        print("ERROR: Invalid values!")
        return None


def main():
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    v = floatInput("Value? ")
    print("v:", v)

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    h = floatInput("Humidity (%)? ", 0, 100)
    print("h:", h)

    print("c) Try entering invalid values such as 23C or -274.")
    t = floatInput("Temperature (Celsius)? ", min=-273.15)
    print("t:", t)

    # d) What happens if you uncomment this?
    impossible = floatInput("Value in [3, 0]? ", min=3, max=0)

    return

if __name__ == "__main__":
    main()
