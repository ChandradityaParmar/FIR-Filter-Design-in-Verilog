import numpy as np
import matplotlib.pyplot as plt

# Function to convert signed binary to signed decimal representation

def todecimal(x, bits):
    assert len(x) <= bits
    n = int(x, 2)
    s = 1 << (bits - 1)
    return (n & s - 1) - (n & s)

# Form a binary representation of the filter coefficients
# Number of coefficients
tap = 8
# Filter coefficients are represented as 8 bit numbers
N1 = 8
# Filter input to 16-bit signed values
N2 = 16
# Output size
N3 = 32

real_coeff = (1 / tap);
print(real_coeff)

# Binary 8-bit representation of the real coefficients
coeff_bit = np.binary_repr(int(real_coeff*(2 ** (N1 - 1))), N1)

# Generation of Test Sequence
timeVector = np.linspace(0, 2*np.pi, 100)

output = np.sin(2 * timeVector) + np.cos(3 * timeVector) + 0.3 * np.random.randn(len(timeVector))
#plt.plot(output)
#plt.show()

# Convert to integers
# List having 16 - bit signed representation of the sin sequence
list1 = []
for number in output:
    list1.append(np.binary_repr(int(number * (2 ** (N1 - 1))), N2))

# Save sequence into a data file
with open('input.data', 'w') as file:
    for number in list1:
        file.write(number + '\n')

# Plotting the filtered output obtained from Vivado
read_b = []
# Read data
with open("save.data") as file:
    for line in file:
        read_b.append(line.rstrip('\n'))

# List having the converted values
n_l = []
for by in read_b:
    n_l.append(todecimal(by, N3)/(2 ** (2 * (N1 - 1))))

plt.plot(output, color = 'blue', linewidth = 3, label = 'Original Signal')
plt.plot(n_l, color = 'red', linewidth = 3, label = 'Filtered Signal')
plt.legend()
plt.savefig('results.png', dpi = 600)
plt.show()