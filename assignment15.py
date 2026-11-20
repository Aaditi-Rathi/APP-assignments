import gc
import tracemalloc

def create_objects():
    for i in range(100):
        obj = []
        obj.append(obj)

def show_memory(message):
    current, peak = tracemalloc.get_traced_memory()

    print(message)
    print("Current Memory:", current / 1024, "KB")
    print("Peak Memory:", peak / 1024, "KB")
    print()

tracemalloc.start()

gc.collect()
show_memory("Initial Memory Usage:")

gc.disable()

create_objects()

show_memory("Memory After Creating Objects:")

gc.set_debug(gc.DEBUG_STATS)

collected = gc.collect()

print("Garbage Collector Collected:", collected, "objects")

show_memory("Memory After Garbage Collection:")

gc.set_debug(0)

gc.enable()

tracemalloc.stop()

print("Garbage Collection Completed!")