import pyopencl as cl
import numpy as np
import time

def run_gpu_computation():
    # 初始化 OpenCL
    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)

    n = 1 << 20  # 1,048,576 个元素
    a = np.ones(n, dtype=np.float32)
    b = np.full(n, 2.0, dtype=np.float32)
    c = np.empty_like(a)

    # 创建缓冲区
    d_a = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=a)
    d_b = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=b)
    d_c = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, c.nbytes)

    # 编译内核
    prg = cl.Program(ctx, """
    __kernel void constant_computation(__global const float *a, __global const float *b, __global float *c) {
        int idx = get_global_id(0);
        c[idx] = a[idx] * b[idx];  // 简单计算：元素乘法
    }
    """).build()

    try:
        while True:
            prg.constant_computation(queue, (n,), None, d_a, d_b, d_c)
            cl.enqueue_copy(queue, c, d_c)
            print(f"Computation performed at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(1)  # 每秒执行一次
    except KeyboardInterrupt:
        print("Computation stopped by user.")

if __name__ == "__main__":
    run_gpu_computation()