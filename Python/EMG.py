import sys
def main(n):
    while True:
        print('emg',n)

if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
    except:
        n = 1
    main(n)

