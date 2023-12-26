import threading
import random
import time
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

PHILOSOPHERS_COUNT = 5
MAX_PHILOSOPHERS_EATING = 3
SPAGHETTI_PER_PHILOSOPHER = 7


SEAT = threading.Semaphore(MAX_PHILOSOPHERS_EATING)

'''
Burada SEAT adında bir semafor oluşturduk.
ve maksimum sayısı MAX_PHILOSOPHERS_EATING olarak belirledik.
Semaforlar, paylaşılan bir kaynağa erişimi kontrol etmek için kullanılır
ve bu durumda belirli bir anda aynı anda kaç filozofun yemek yemesine
izin verileceğini kontrol ediyor.

'''



def use_seat(fn, *args, **kwargs):
    def wrapper(self):
        with SEAT:
            return fn(self, *args, **kwargs)
    return wrapper

'''
Bu fonksiyon, başka bir fonksiyonu (fn) alır
ve yeni bir fonksiyonu (wrapper) döndürür.
Decorator'lar, dekore ettikleri fonksiyonun davranışını
değiştirmek için kullanılır.

fn: Bu, dekore edilen orijinal fonksiyonu temsil eder.
*args ve **kwargs: Bu, dekoratörün orijinal fonksiyona geçirilebilecek
herhangi bir sayıda pozisyonel ve
anahtar kelime argümanı kabul etmesini sağlar.

wrapper, dekoratör tarafından döndürülen yeni fonksiyondur.
with SEAT ifadesi içerisinde, semafor SEAT'i alıyoruz
Blok içinden çıkıldığında ise semaforu serbest bırakıyoruz.
with SEAT bloğu içerisinde, orijinal fonksiyon fn çağrılır
ve argümanları (*args ve **kwargs) iletilir.

Dekoratör, şimdi orijinal fonksiyonun etrafında semafor kontrolünü içeren
wrapper fonksiyonunu döndürüyor.

Özetle, use_seat dekoratörü, dekore ettiği herhangi bir fonksiyonun
yemek yeme koltuğuna kontrol edilmiş erişim sağlamasını sağlar.
Bu, semafor SEAT temel alınarak aynı anda yemek
yiyebilecek filozof sayısını sınırlar. Semafor, yarış koşullarını önlemeye
yardımcı olur ve yemek yeme sürecinde bir dereceye kadar senkronizasyonu
sağlar.
'''



class Fork:
    def __init__(self, index: int):
        '''
        __init__ fonksiyonu, sınıfın bir örneği (nesnesi)
        oluşturulduğunda çağrılır.
        '''
        self.index: int = index
        '''
        index parametresi, çatalın bir benzersiz kimliğini temsil eder ve
        çatalın dizindeki yerini belirler.
        '''
        self.lock: threading.Lock = threading.Lock()
        '''
        lock adında bir threading.Lock nesnesi oluşturulur.
        Bu, çatala aynı anda sadece bir filozofun erişebilmesini sağlayan
        bir kilit mekanizmasıdır.
        '''
        self.picked_up: bool = False
        '''
        picked_up, çatalın bir filozof tarafından alınıp alınmadığını
        gösteren bir bayraktır. Başlangıçta False olarak ayarlanır,
        çünkü başlangıçta çatal kimse tarafından alınmamıştır
        '''
        self.owner: int = -1
        '''
        owner, çatalı alan filozofun indisini tutar. 
        Başlangıçta -1 olarak ayarlanır, çünkü çatal henüz hiçbir
        filozof tarafından alınmamıştır.
        '''

    def __enter__(self):
        return self
    '''
    __enter__ metodu, bir nesnenin bir with ifadesi içinde 
    kullanıldığında çağrılır.u metod, çatalın kendisini döndürür.
    with bloğu içinde, çatal nesnesi üzerinde işlemler gerçekleştirilebilir. 
    '''

    def __call__(self, owner: int):
        '''
        __call__ metodu, bir nesne fonksiyon olarak çağrıldığında
        bu metot çağırılır.Çatalı almak için kullanılır.
        owner parametresi, çatalı alan filozofun indisini temsil eder.
        '''
        if self.lock.acquire():
            '''
            self.lock.acquire() ifadesi, çatalın kilidini almayı dener.
            Başarılı olursa, çatal alınır (picked_up ve owner özellikleri
            güncellenir) ve çatal nesnesi döndürülür.
            '''
            self.owner = owner
            self.picked_up = True
            return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.lock.release()
        self.picked_up = False
        self.owner = -1
    '''
    __exit__ metodu, with bloğundan çıkıldığında çağrılır.
    Çatalın kilidi serbest bırakılır (self.lock.release()).
    picked_up ve owner özellikleri sıfırlanır,
    çünkü çatal artık kimse tarafından alınmamıştır.
    '''

    def __str__(self):
        return f"F{self.index:2d} ({self.owner:2d})"
    
    '''
    __str__ metodu, print(my_fork) gibi bir nesnenin dizgisini oluşturmak
    için kullanılır.
    Bu durumda, çatalın dizgi temsilini oluşturur. Çatalın indeksi ve 
    sahibinin indisini içerir. :2d ifadesi, indisleri iki haneli sayı
    olarak görüntülemek için kullanılır.

    Bu sınıf, filozofların çatal alıp bırakma işlemlerini düzenli bir
    şekilde yönetmek için kullanılır. Her çatal, bir kilit (lock) ile
    birlikte tutularak, yemek yiyen filozofların bu çatala güvenli bir
    şekilde erişmeleri sağlanır.

    '''


class Philosopher(threading.Thread):
    def __init__(self, index: int, left_fork: Fork, right_fork: Fork, spaghetti: int):
        super().__init__()
        self.index: int = index
        #index, filozofun benzersiz bir kimliğini temsil eder.
        self.left_fork: Fork = left_fork
        #filozofun sol ve sağ çatalını temsil eder ve Fork sınıfından örneklerdir.
        self.right_fork: Fork = right_fork
        self.spaghetti: int = spaghetti
        #spaghetti, filozofun sahip olduğu makarna sayısını belirtir.
        self.eating: bool = False
        #eating, filozofun şu anda yemek yiyip yemediğini belirtir.

    def use_forks(fn, *args, **kwargs):
        #use_forks bir decorator fonksiyonudur ve bir filozofun çatal alıp yemesini
        #sağlamak için kullanılır.fn burada orijinal fonksiyonu temsil eder.
        def wrapper(self):
            with self.left_fork(self.index):
    #wrapper fonksiyonu, çatal almak için self.left_fork'u ve self.right_fork'u kullanır.
                time.sleep(2 + random.random() * 5)
                with self.right_fork(self.index):
                    fn(self, *args, **kwargs)

        return wrapper

    def run(self):
        #run metodu, filozofun bir thread olarak çalışmasını sağlar.
        while self.spaghetti > 0:
            self.think()
            self.eat()

    def think(self):
        time.sleep(random.random() * 3)




    '''
    @use_seat ve @use_forks decorator'ları, filozofun yemek yemesi için
    güvenli bir şekilde çatal almasını ve semafor ile kontrol etmesini
    sağlar.
    '''

    @use_seat
    @use_forks
    def eat(self):
        self.spaghetti -= 1
        self.eating = True
        time.sleep(random.random() * 5)
        self.eating = False

    def __str__(self):
        return f"P{self.index:2d} ({self.spaghetti:2d})"
    
    '''
    __str__ metodu, filozof nesnesinin bir dizgisini temsil eder.
    Filozofun indisini ve sahip olduğu makarna sayısını içerir.
    '''


def animated_table(philosophers: list[Philosopher], forks: list[Fork], m: int):
    """
    Creates an animated table with the philosophers and forks.

    :param philosophers: The list of philosophers.
    :param forks: The list of forks.(Çatallarin listesi)
    :param m: The amount of spaghetti each philosopher has.
    """
    fig, ax = plt.subplots()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Dining Philosophers")
    philosopher_circles: list[plt.Circle] = [
        plt.Circle((0, 0), 0.2, color="black") for _ in range(len(philosophers))
    ]
    philosopher_texts: list[plt.Text] = [
        plt.Text(
            0,
            0,
            str(philosopher.index),
            horizontalalignment="center",
            verticalalignment="center",
        )
        for philosopher in philosophers
    ]
    fork_lines: list[plt.Line2D] = [
        plt.Line2D((0, 0), (0, 0), color="black") for _ in range(len(forks))
    ]
    fork_texts: list[plt.Text] = [
        plt.Text(
            0,
            0,
            str(fork.index),
            horizontalalignment="center",
            verticalalignment="center",
        )
        for fork in forks
    ]
    for philosopher_circle in philosopher_circles:
        ax.add_patch(philosopher_circle)
    for fork_line in fork_lines:
        ax.add_line(fork_line)
    for philosopher_text in philosopher_texts:
        ax.add_artist(philosopher_text)
    for fork_text in fork_texts:
        ax.add_artist(fork_text)

    def update(frame):
        """
        Updates the table.
        """
        # get the philosophers and forks from the global scope
        nonlocal philosophers, forks
        for i in range(len(philosophers)):
            philosopher_circles[i].center = (
                0.5 * math.cos(2 * math.pi * i / len(philosophers)),
                0.5 * math.sin(2 * math.pi * i / len(philosophers)),
            )
            # update the labels as text on the plot
            philosopher_texts[i].set_position(
                (
                    0.9 * math.cos(2 * math.pi * i / len(philosophers)),
                    0.9 * math.sin(2 * math.pi * i / len(philosophers)),
                )
            )
            philosopher_texts[i].set_text(
                str(philosophers[i]) if philosophers[i].spaghetti > 0 else "X"
            )
            if philosophers[i].eating:
                philosopher_circles[i].set_color("red")
            else:
                philosopher_circles[i].set_color("black")
            philosopher_circles[i].radius = 0.2 * philosophers[i].spaghetti / m
            fork_lines[i].set_data(
                (
                    0.5 * math.cos(2 * math.pi * i / len(philosophers)),
                    0.5 * math.cos(2 * math.pi * (i + 1) / len(philosophers)),
                ),
                (
                    0.5 * math.sin(2 * math.pi * i / len(philosophers)),
                    0.5 * math.sin(2 * math.pi * (i + 1) / len(philosophers)),
                ),
            )
            # add the labels of the forks as text on the plot
            fork_texts[i].set_position(
                (
                    0.5 * math.cos(2 * math.pi * i / len(philosophers))
                    + 0.5 * math.cos(2 * math.pi * (i + 1) /
                                     len(philosophers)),
                    0.5 * math.sin(2 * math.pi * i / len(philosophers))
                    + 0.5 * math.sin(2 * math.pi * (i + 1) /
                                     len(philosophers)),
                )
            )
            fork_texts[i].set_text(str(forks[i]))
            if forks[i].picked_up:
                fork_lines[i].set_color("red")
            else:
                fork_lines[i].set_color("black")
        return philosopher_circles + fork_lines + philosopher_texts + fork_texts

    ani = animation.FuncAnimation(
        fig, update, frames=range(100000), interval=10, blit=False
    )
    plt.show()

    '''
    animation.FuncAnimation ile bir animasyon oluşturulur.
    update fonksiyonu her bir çerçeve için çağrılacaktır.

    frames=range(100000) ile çerçeve sayısı belirlenir 

    interval=10 ile çerçeve arasındaki süre belirlenir (ms cinsinden).

    Bu fonksiyonu ile filozofların ve çataların
    durumlarını animasyonlu bir şekilde görselleştirmek için kullandık.
    '''


def table(philosophers: list[Philosopher], forks: list[Fork], m: int):
    """
    Prints the table with the philosophers and forks.

    :param philosophers: The list of philosophers.
    :param forks: The list of forks.
    :param m: The amount of spaghetti each philosopher has.

    table fonksiyonu, filozofların ve çataların durumlarını
    basit bir metin tablosu şeklinde ekrana yazdıran bir fonksiyondur.

    """
    while sum(philosopher.spaghetti for philosopher in philosophers) > 0:
        eating_philosophers: int = sum(
            philosopher.eating for philosopher in philosophers
        )
        # clear the screen
        print("\033[H\033[J")
        print("=" * (len(philosophers) * 16))
        # print a line for each philosopher if they are eating, thinking, or done
        print(
            "         ",
            "             ".join(
                ["E" if philosopher.eating else "T" for philosopher in philosophers]
            ),
        )
        print("       ".join(map(str, forks)), "     ", forks[0])
        print(
            "      ",
            "       ".join(map(str, philosophers)),
            "      : ",
            str(eating_philosophers),
        )
        print("Sum ", sum(philosopher.spaghetti for philosopher in philosophers))
        time.sleep(0.1)


def main() -> None:
    n: int = PHILOSOPHERS_COUNT
    m: int = SPAGHETTI_PER_PHILOSOPHER

    forks: list[Fork] = [Fork(i) for i in range(n)]
    philosophers: list[Philosopher] = [
        Philosopher(i, forks[i], forks[(i + 1) % n], m) for i in range(n)
    ]
    #Her filozofun sol çatalı forks[i], sağ çatalı ise forks[(i + 1) % n] olarak atanır.
    #Bu, filozofları bir daire şeklinde oturttuğumuzdan dolayı
    #sağ taraftaki çatalın sol taraftaki çatala bağlı olması için yapılır.
    for philosoper in philosophers:
        philosoper.start()
    threading.Thread(target=table, args=(
        philosophers, forks, m), daemon=True).start()
    animated_table(philosophers, forks, m)
    for philosoper in philosophers:
        philosoper.join()
        #Her filozofun çalışmasının bitmesi beklenir (join methodu).


if __name__ == "__main__":
    main()
