import time
import lib

print(" ")
print("Witaj w Pythonowym stoperze!")
print(" ")
print("Do ilu chcesz odliczać? (w sekundach)")
sec = input()

if not lib.is_int(sec):
    print("Niepoprawny argument!")
    exit(1)

sec = int(sec)

print("Ile razy program ma zadzwonić? (max 15, min 1)")
ring = input()

if not lib.is_int(ring):
    print("Niepoprawny argument!")
    exit(1)

ring = int(ring)

if ring > 15 or ring < 1:
    print("Niepoprawny numer!")
    exit(1)

print(" ")
print("Zaczynamy!!!")
print(" ")
time.sleep(1)
print(sec)

timer = time.time()
while sec != 0:
    if time.time() - timer > 1:
        sec = sec - 1
        print(sec)
        timer = time.time()
    time.sleep(0.05)

if sec == 0:
    for i in range(ring):
        print(" ")
        print("BING BANG BONG!!!")
        time.sleep(1)
