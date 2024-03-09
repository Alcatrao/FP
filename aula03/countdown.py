import time


def countdown(n):
    if n<=0:
        #print(0)
        exit()
    print(n)
    time.sleep(0.1)
    countdown(n-1)

def main():

    N=29
    countdown(N)

main()