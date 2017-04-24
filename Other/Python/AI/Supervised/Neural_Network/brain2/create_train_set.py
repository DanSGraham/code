import math
import random
#Create training set file to test a NN.


sizeOfDataSet = 1000
functionToTest = math.sin
input_data = []
output_data = []

for j in range(5):
    in_val = [random.random(), random.random()]
    out_val = [0,0]
    input_data.append(in_val)
    output_data.append(out_val)

for i in range(5, sizeOfDataSet):
    in_val = [random.random(), random.random()]
    out_in = input_data[i - 5]
    out_val = [(functionToTest(out_in[0]) - functionToTest(out_in[1])), functionToTest(out_in[0]) + functionToTest(out_in[1])]
    input_data.append(in_val)
    output_data.append(out_val)


write_string = """{{\n"inputSet": {0},\n"outputSet": {1}\n}}""".format(input_data, output_data)

fout = open("train_set1.txt", "w")
fout.write(write_string)
fout.close
