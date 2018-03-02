#!/usr/bin/python -tt
import sys
def add(n1, n2):
  print float(n1) + float(n2)

def main():
  if (len(sys.argv) >= 3) :
    add(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
  main()
