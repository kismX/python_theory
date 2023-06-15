import timeit

def time_it(N):
    setup_queue = f"from collections import deque; dq=deque(range({N}, 0, -1))"
    fifo_queue = "dq.appendleft(None); dq.pop()"

    queue_time = timeit.repeat(setup=setup_queue,
                            stmt= fifo_queue,
                            repeat=10,
                            number= 1000)

    queue_mean = sum(queue_time) / len(queue_time)

    setup_list = f"num = list(range({N}, 0, -1))" 
    fifo_list = "num.append(None); num.pop(0)"

    list_time = timeit.repeat(setup=setup_list,
                            stmt= fifo_list,
                            repeat = 3,
                            number = 1000)

    list_mean = sum(list_time) / len(list_time)                        

    return queue_mean, list_mean


X = [10, 100, 1000, 10000, 100000]
Y_queue = [time_it(num)[0] for num in X]
Y_list = [time_it(num)[1] for num in X]


# plot Y_queue vs X
# plot Y_list vs X
# what is the time complexity of deques and list when we apply fifo-behaviour?


import matplotlib.pyplot as plt
plt.plot(X, Y_queue, label="Y_queue(deque)")
plt.plot(X, Y_list, label="Y_list")
plt.legend()
plt.show()

