def maxproduct(number, digits):
    """Calculate the maximum product of the n-adjacent digits of number."""
    zeros = 0
    product = 1
    result = 0

    # Calculate the first, initial product.
    for x in number[:digits]:
        x = int(x)
        if x:
            product *= int(x)
        else:
            # This digit is 0. This will make our product zero
            # too (losing information about other digits) and will
            # also cause trouble with division later. Instead of
            # storing the zero in the product, we increment a counter.
            zeros += 1

    if not zeros:
        # This product is the highest we have seen so far.
        result = product

    # Calculate the other products with the remaining digits.
    for i in range(digits, len(number)):
        # Digit to remove.
        x = int(number[i - digits])
        # Digit to add.
        y = int(number[i])

        if x:
            product //= x
        else:
            # The digit to remove is 0.
            zeros -= 1

        if y:
            product *= y
        else:
            zeros += 1

        if not zeros and product > result:
            result = product

    return result

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(maxproduct(str(num), k))