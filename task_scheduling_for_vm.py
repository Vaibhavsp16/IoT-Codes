import time
from datetime import datetime, timedelta

# Task format: (task_name, start_after_seconds, duration)
tasks = [
    ("Task 1", 0, 3),
    ("Task 2", 5, 2),
    ("Task 3", 8, 4),
    ("Task 4", 13, 3)
]

print("TASK SCHEDULER")
print("-" * 40)

start_time = datetime.now()

# Display the planned timeline
print("\nScheduled Timeline:")
for name, start_after, duration in tasks:
    task_start = start_time + timedelta(seconds=start_after)
    task_end = task_start + timedelta(seconds=duration)

    print(
        f"{name}: "
        f"{task_start.strftime('%H:%M:%S')} -> "
        f"{task_end.strftime('%H:%M:%S')}"
    )

print("\nStarting scheduler...")
print("-" * 40)

# Execute tasks according to their scheduled time
for name, start_after, duration in tasks:

    # Wait until the scheduled start time
    elapsed = time.time() - start_time.timestamp()
    wait_time = start_after - elapsed

    if wait_time > 0:
        time.sleep(wait_time)

    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] "
        f"Starting {name}"
    )

    # Simulate task execution
    time.sleep(duration)

    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] "
        f"Completed {name}"
    )

print("-" * 40)
print("All tasks completed.")