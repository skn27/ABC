if __name__ == "__main__":
    total = int(input())
    num_500 = total // 500
    num_5 = (total%500) // 5
    print(num_500*1000 + num_5*5)
