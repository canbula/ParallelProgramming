import time,tracemalloc
def performance(func):
    def _performance():
        if not hasattr(_performance,'counter'):
            _performance.counter=1
            _performance.total_time=0
            _performance.totam_mem=0
        time1=time.perf_counter()
        tracemalloc.start()
        func()
        _performance.total_mem+=tracemalloc.get_traced_memory()[1]
        _performance.total_time+=time.perf_counter()-time1
    return _performance()


"""
###################################
        Furkan Soylek
https://leetcode.com/TB09/
https://github.com/TIMEBANDIT11111
###################################
"""
