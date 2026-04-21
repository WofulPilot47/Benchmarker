import GPUtil
import time
import numpy as np
import tensorflow as tf

class GPUBenchmark:
    def __init__(self):
        pass

    def benchmark_memory(self, duration=10):
        start_time = time.time()
        end_time = start_time + duration
        memory_usage = []

        while time.time() < end_time:
            gpus = GPUtil.getGPUs()
            for gpu in gpus:
                memory_usage.append(gpu.memoryUsed)
            time.sleep(1)

        avg_memory = np.mean(memory_usage)
        print(f"Average GPU Memory Used: {avg_memory} MiB")

    def benchmark_compute(self, iterations=1000):
        x = tf.random.normal((1000, 1000))
        y = tf.random.normal((1000, 1000))
        start_time = time.time()

        for _ in range(iterations):
            z = tf.matmul(x, y)

        end_time = time.time()
        print(f"Compute time for {iterations} iterations: {end_time - start_time} seconds")

if __name__ == '__main__':
    benchmark = GPUBenchmark()
    benchmark.benchmark_memory(duration=10)
    benchmark.benchmark_compute(iterations=1000)
