def solution(text, sticky):
  text = text.replace('e', '', 1).replace('h', '', 1)
  return text


def main():
  text = "hheello world"
  sticky = ["e", "h"]
  print("The original text is:", text)
  print("The sticky keys are:", sticky)
  print("The corrected text is: ", solution(text, sticky))


if __name__ == "__main__":
  main()
