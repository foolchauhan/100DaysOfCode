if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        word = str(input())
        odd_str=''
        even_str=''
        for i in range(len(word)):
            if(i%2==0):
                odd_str = odd_str+word[i]
            else:
                even_str = even_str+word[i]
        print(odd_str + " " + even_str)