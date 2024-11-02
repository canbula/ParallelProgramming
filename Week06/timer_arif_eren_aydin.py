import asyncio
import time
class Timer:
    def __init__(self) -> None:
        self.start_time = None  
        self.end_time = None    
        print(f"initing:{__class__.__name__}")
    async def __aenter__(self)-> "Timer":
        self.start_time= time.time()
        await asyncio.sleep(1) 
        print(f"entering:{self.__class__.__name__}")
        return self
    async def __aexit__(self,exc_type,exc_vol,exc_tb)->bool:
        self.end_time= time.time() 
        self.time=self.end_time-self.start_time
        print(f"Elapsed time: {self.time:.5f} seconds")
        await asyncio.sleep(0)
        print(f"e:{exc_type},v:{exc_vol},tb:{exc_tb}")
        return True
    async def __call__(self,task:str) -> None:
        print("Called")
        return None
