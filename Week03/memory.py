prev_id_ = 0
for i in range(1000):
    s = "\n" if i % 5 == 0 else " "
    id_ = id(i)
    diff = id_ - prev_id_
    print(f"{i}:{id_}", end=s)
    if diff > 32 and i > 1:
        break
    prev_id_ = id_
print()
