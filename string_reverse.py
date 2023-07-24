def reverse_string(string):
  reversed_string = ""
  for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]
  return reversed_string


if __name__ == "__main__":
  string = "hello world"
  reversed_string = reverse_string(string)
  print(reversed_string)
