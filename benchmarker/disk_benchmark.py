import time
import os

class DiskBenchmark:
    def __init__(self, file_size_mb=100, test_file='test_file.dat'):
        self.file_size = file_size_mb * 1024 * 1024  # Convert MB to Bytes
        self.test_file = test_file

    def write_test(self):
        """Tests write speed by creating a large file."""
        start_time = time.time()
        with open(self.test_file, 'wb') as f:
            f.write(os.urandom(self.file_size))  # Write random data
        elapsed_time = time.time() - start_time
        write_speed = self.file_size / elapsed_time  # Bytes per second
        print(f"Write Speed: {write_speed / (1024 * 1024):.2f} MB/s")  # Convert to MB/s

    def read_test(self):
        """Tests read speed by reading the large file created in the write test."""
        start_time = time.time()
        with open(self.test_file, 'rb') as f:
            f.read()
        elapsed_time = time.time() - start_time
        read_speed = self.file_size / elapsed_time  # Bytes per second
        print(f"Read Speed: {read_speed / (1024 * 1024):.2f} MB/s")  # Convert to MB/s

    def run_benchmark(self):
        self.write_test()
        self.read_test()
        # Clean up the test file
        os.remove(self.test_file)

# Example usage:
if __name__ == '__main__':
    benchmark = DiskBenchmark()
    benchmark.run_benchmark()