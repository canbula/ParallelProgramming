import threading
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

class Fork:
    #CONTEXT KISMI LOCK ACQUIRE VE LOCK RELEASE KISMINDA .
    def __init__(self, index):
        self.index = index
        self.lock = threading.Lock()
    def __enter__(self):
        #KODUN DEVAM ETMESİ İÇİN ÇATALIN ELİMİZE ALANA KADAR BEKLETİYORUZ.
        if self.lock.acquire():
            return self
    def __exit__(self, exc_type, exc_value, traceback):
        #KULLANDIĞI ÇATALI BIRAKTIĞI KISIM.
        self.lock.release()

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork, spaghetti_quantity, eating_sem):
        #GELEN DEĞERLERİ ALDIK VE DEĞİŞKENLERE ATADIK.
        super().__init__()
        #SUPER=BASE CLASS THREADING SINIFINI INITIALIZE EDİYOR.
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.spaghetti_quantity = spaghetti_quantity
        self.eating_sem = eating_sem
        self.eating = False

    def run(self):
        #TABAK BİTENE KADAR YEMEĞE DEVAM ETSİN.
        while self.spaghetti_quantity>0:
            self.think()
            self.eat()

    def think(self):
        #DÜŞÜNME SÜRESİ
        print(f"Philosopher {self.index} is thinking.")
        time.sleep(random.random() * 3)

    def eat(self):
        print(f"Philosopher {self.index} is hungry and trying to pick up forks.")
        #EĞER MAKSİMUM KİŞİ SAYISINA ULAŞILMADIYSA self.eating_sem ÇALIŞIR. ULAŞILDIYSA DA SIRASINI BEKLİYOR.
        #print(self.eating_sem)
        with self.eating_sem:
            # SOL ÇATALI ALANA KADAR BEKLE
            with self.left_fork:
                print(f"Philosopher {self.index} picked up left fork.")
                #DEADLOCK'U SİMULE EDEBİLMEMİZ İÇİN TİME SLEEP EKLEDİK.
                time.sleep(2+ random.random()*5)
                # SAĞ ÇATALI ALANA KADAR BEKLE
                with self.right_fork:
                    print(f"Philosopher {self.index} picked up right fork eating.")
                    self.spaghetti_quantity-=1
                    #ANIMATED TABLE METHODUNDA KIRMIZI VE SİYAH DURUMLARINI KONTROL ETMEMİZ İÇİN SELF EATING DEĞİŞKENİNİ DURUMUNU DEĞİŞTİRİYORUZ. TRUE KIRMIZI, FALSE İSE SİYAHI TEMSİL ETMEKEDİR.
                    self.eating = True
                    time.sleep(random.random() * 5)
                    self.eating = False
                    print(f"Philosopher {self.index} finished eating.")
        

def animated_table(philosophers, forks, n,spaghetti_quantity):
    fig, ax = plt.subplots()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Dining Philosophers")

    philosopher_circles = [plt.Circle((0, 0), 0.2, color="black") for _ in range(n)]
    philosopher_texts = [plt.Text(0, 0, str(philosopher.index), ha="center", va="center") for philosopher in philosophers]

    for philosopher_circle in philosopher_circles:
        ax.add_patch(philosopher_circle)
    for philosopher_text in philosopher_texts:
        ax.add_artist(philosopher_text)

    def update(frame):
        nonlocal philosophers
        for i in range(len(philosophers)):
            angle = 2 * math.pi * i / len(philosophers)
            philosopher_circles[i].center = (0.5 * math.cos(angle), 0.5 * math.sin(angle))
            philosopher_texts[i].set_position((0.5 * math.cos(angle), 0.5 * math.sin(angle)))
           
            if philosophers[i].eating:
                philosopher_circles[i].set_color("red")
            else:
                philosopher_circles[i].set_color("black")
            
            philosopher_circles[i].radius = 0.2* philosophers[i].spaghetti_quantity/spaghetti_quantity
        return philosopher_circles + philosopher_texts

    ani = animation.FuncAnimation(fig, update, frames=range(100000), interval=100, blit=False)
    plt.show()

def dining_philosophers(n, spaghetti_quantity):
    #FİLOZOF SAYISI OLACAK KADAR FORK OBJESİ INITIALIZE EDİLİYOR.
    forks = [Fork(i) for i in range(n)]
    #MANTIKSAL KİLİT = AYNI ANDA MAKSİMUM YEMEK YİYECEK KİŞİ SAYISINI LİMİTLEMEK İÇİN SEMAPHORE KULLANDIK.  
    eating_sem = threading.Semaphore(n - 3)
    #INPUT SAYISI KADAR FİLOZOF OBJESİ ÜRETİYORUZ.
    philosophers = [Philosopher(i, forks[i], forks[(i + 1) % n], spaghetti_quantity, eating_sem) for i in range(n)]
    #THRED'I BAŞLATTIK
    for philosopher in philosophers:
        philosopher.start()
    
    animated_table(philosophers, forks, n,spaghetti_quantity)
    #MAIN THREADN FİLOZOFLAR İŞLEMİN BİTMESİNİ BEKLİYOR.
    for philosopher in philosophers:
        philosopher.join()

if __name__ == "__main__":
    n = int(input("Enter the number of philosophers: "))
    spaghetti_quantity = int(input("Enter quantity of spaghetti:(Each eat reduces 1 spaghetti) "))

    dining_philosophers(n, spaghetti_quantity)