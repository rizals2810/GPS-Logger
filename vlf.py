import numpy as np
from struct import *
import os

f=open('/Users/rizal/Downloads/PTK2012010100.spc', 'rb')

header_raw = f.read(10*2)
header = np.array(unpack('h'*10, header_raw))
print("Year = ", header[0])
print("Month = ", header[1]/100)
print("Day = ", header[1] % 100)
print("Hour = ", header[2])
print("sampling freq = ", header[3])
print("data lenght for FFT = ", header[4])
print("Average time = ", header[5])
print("Number of average point in freq = ", header[6])
print("Number of freq CH = ", header[7])
print("Freq resolution (Hz) = ", header[8])
print("Block size (byte) = ", header[9])
file_size = int(os.path.getsize('/Users/rizal/Downloads/PTK2012010100.spc'))
n_block = int(header[9])-1
##m_arr = file_size/n_block
#ft=open('/Users/rizal/Downloads/PKT-DATA-3.txt', 'w')

xinput = f.read()
data = np.array(unpack('h'*484474,xinput))
print(data)
"""
for i in range(0,n_block):
    xinput = f.read(194)
    data = np.array(unpack('h'*97, xinput))
    text_data = str(data)+'\r\n'
    ft.write(text_data)
    if data[0] == 32767:
        print("start = ", data[0])
        print("time = ", data[1])
        print("Amplitude = ", data[2])
        print("Phasa = ", data[3])
ft.close()
"""
f.close()
    
