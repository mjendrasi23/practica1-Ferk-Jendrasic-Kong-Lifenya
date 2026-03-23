def check_triangle(a, b, c):
    if (c < a + b) and (b < a + c) and (a < c + b):
        if a == b and a == c:
            return "Equilateral triangle"
        elif a == b or b == c:
            return "Isosceles triangle"
        else:
            return "Scalene triangle"
    else:
        return "It is not a triangle."

def main():
    n_input = input("Number of test cases: \n")
    n = int(n_input)
    print(n)
    
    for i in range(1, n + 1):
        print("Mark the length values of the sides of the triangle (one per line):")
        a = int(input())
        b = int(input())
        c = int(input())
        print(f"{a},{b},{c}:")
        print(check_triangle(a, b, c))
    

if __name__ == "__main__":
    main()