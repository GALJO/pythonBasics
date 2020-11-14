n = int(input())  # Liczba cząstek
speed_of_particles = input().split()
q = int(input())  # Liczba zapytań
inquiry_speeds = []
results = []


def amount_of_occurrences(_speed_of_particles, _place, _center):
    _count = 0
    for i in range(_center, len(_speed_of_particles)):
        if int(_speed_of_particles[i]) == _place:
            _count += 1
        else:
            break
    for i in range(_center - 1, 0, -1):
        if int(_speed_of_particles[i]) == _place:
            _count += 1
        else:
            break
    return _count


def find_speed(_x, _speed_of_particles):
    count = 0
    done = False
    start = 0
    end = len(_speed_of_particles) - 1

    while not done:
        center = int((start + end) / 2)
        place = int(_speed_of_particles[center])

        if place == _x:
            count = amount_of_occurrences(_speed_of_particles, place, center)
            done = True
        elif start >= end:
            done = True
        elif place > _x:
            end = center - 1
        elif place < _x:
            start = center + 1
    return count


for i in range(q):
    inquiry_speeds.append(int(input()))

for i in range(q):
    results.append(find_speed(inquiry_speeds[i], speed_of_particles))

for result in results:
    print(result)
