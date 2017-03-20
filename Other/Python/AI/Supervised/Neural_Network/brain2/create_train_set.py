import math
import random
#Create training set file to test a NN.


sizeOfDataSet = 1000
functionToTest = math.sin
input_data = []
output_data = []

in_val = [random.random(), random.random()]
out_val = [(functionToTest(in_val[0]) - functionToTest(in_val[1])), functionToTest(in_val[0]) + functionToTest(in_val[1])]
input_data.append(in_val)
output_data.append(out_val)
for i in range(1, sizeOfDataSet):
    in_val = [random.random(), random.random()]
    out_val = [(functionToTest(in_val[0]) - functionToTest(input_data[i -1][1])), functionToTest(input_data[i-1][0]) + functionToTest(in_val[1])]
    input_data.append(in_val)
    output_data.append(out_val)


write_string = """{{\n"inputSet": {0},\n"outputSet": {1}\n}}""".format(input_data, output_data)

fout = open("train_set1.txt", "w")
fout.write(write_string)
fout.close
