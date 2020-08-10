n = int(input())  # Liczba cząstek
speed_of_particles = input().split()
q = int(input())  # Liczba zapytań
inquiry_speed = int(input())

start = 0
end = len(speed_of_particles)

done = False
count = 0
while not done:
    center = int((start + end + 1) / 2)
    place = speed_of_particles[center]
    if place == inquiry_speed:
        count += 1
        start = center
    if start