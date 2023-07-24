def count_tiny_pairs(a, b, k):
  """
  Counts the number of tiny pairs in two arrays a and b.

  Args:
    a: An array of integers.
    b: An array of integers.
    k: An integer.

  Returns:
    The number of tiny pairs in a and b.
  """

  count = 0
  i = 0
  j = len(b) - 1
  while i < len(a) and j >= 0:
    x = a[i]
    y = b[j]
    if x * 10 + y < k:
      count += 1
    i += 1
    j -= 1
  return count


if __name__ == "__main__":
  a = [1, 2, 3, 4, 5]
  b = [5, 4, 3, 2, 1]
  k = 15
  print(count_tiny_pairs(a, b, k))
