""" Assigment 2
"""
import argparse
import numpy as np


class VoltageData:
    """Class for handling a set of measurements of the voltage at different
    times.""" 
    
    def __init__(self, times, voltages):
        t = np.array(times, dtype=np.float64)
        v = np.array(voltages, dtype=np.float64)
        self._data = np.column_stack((t, v))

    @property
    def voltages(self):
        return self._data[:, 1]

    @property
    def timestamps(self):
        return self._data[:, 0]

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):  #index qualsiasi cosa, posso fare anche lo slice
        return self._data[index]

    def __str__(self):
        output_string = list()
        for i, element in enumerate(self._data):
            output_string.append(f'{i:d}) t={element[0]} v={element[1]}')
        return '\n'.join(output_string)

if __name__ == '__main__':
    """ Here we test the functionalities of our class. These are not proper
    UnitTest - which you will se in a future lesson."""
    parser = argparse.ArgumentParser(description='Read and converte a time-voltage file text')
    parser.add_argument('path', type=str, help='File path to read')
    args = parser.parse_args()

    print(args.path)

    # Load some data
    t, v = np.loadtxt(args.path, unpack=True)
    # Thest the constructor
    v_data = VoltageData(t, v)
    # Test len()
    assert len(v_data) == len(t)
    # Test the timestamps attribute
    assert np.all(v_data.voltages == v)
    # Test the voltages attribute
    assert np.all(v_data.timestamps == t)
    # Test square parenthesis
    assert v_data[3, 1] == v[3]
    assert v_data[-1, 0] == t[-1]
    # Test slicing
    assert np.all(v_data[1:5, 1] == v[1:5])
    # Test iteration
    for i, entry in enumerate(v_data):
        assert entry[0] == t[i]
        assert entry[1] == v[i]
    # Test printing
    print(v_data)
    