import re
import fileinput
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

for line in fileinput.input(input_file):

