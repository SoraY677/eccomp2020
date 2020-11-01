import random

MIN_NUM = 1
MAX_NUM = 6


def absRandom(length):
  '''
  完全にランダムで生成する
  '''
  result = [str(random.randint(MIN_NUM, MAX_NUM)) for i in range(length)]
  return ''.join(result)


if __name__ == '__main__':
  print("---------test------------")
  print(absRandom(6))
