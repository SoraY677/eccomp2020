import csv
import subprocess

filename = "result.csv"

with open(filename, 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(["created_num", "result", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"])

if __name__ == "__main__":
  with open(filename, 'a', newline='') as f:
    writer = csv.writer(f)
    for i in range(10000):
      print(i)
      count = 0
      proc = subprocess.Popen(["exec"], shell=True, stdout=subprocess.PIPE)
      for line in proc.stdout:
        count += 1
        if count == 3:
          output = str(line).split(',')
          output[0] = str(output[0]).split("'")[1]
          output[len(output) - 1] = str(output[len(output) - 1]).split("\\")[0]
          writer.writerow(output)
