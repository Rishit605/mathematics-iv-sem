def u_cal(u, n):
    temp = u;
    for i in range(1, n):
        temp = temp * (u - i);
    return temp;


# calculating factorial of given number n
def fact(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;


# Driver Code

# Number of values given
n = 3;
x = [1, 3, 5];

# y[][] is used for difference table
# with y[][0] used for input
y = [[0 for i in range(n)]
     for j in range(n)];
y[0][0] = 40;
y[1][0] = 45;
y[2][0] = 54;

# Calculating the forward difference
# table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];

# Displaying the forward difference table
for i in range(n):
    print(x[i], end="\t");
    for j in range(n - i):
        print(y[i][j], end="\t");
    print("");

# Value to interpolate at
value = 4;

# initializing u and sum
sum = y[0][0];
u = (value - x[0]) / (x[1] - x[0]);
for i in range(1, n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i);

print("\nValue at", value,
      "is", round(sum, 6));

# This code is contributed by mits