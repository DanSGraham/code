import math
import random
#Create training set file to test a NN.


sizeOfDataSet = 1000
functionToTest = math.sin
input_data = []
output_data = []

for i in range(sizeOfDataSet):
    in_val = [random.random()]
    out_val = [functionToTest(in_val[0])]
    input_data.append(in_val)
    output_data.append(out_val)


write_string = """{{\n"inputSet": {0},\n"outputSet": {1}\n}}""".format(input_data, output_data)

fout = open("train_set1.txt", "w")
fout.write(write_string)
fout.close
