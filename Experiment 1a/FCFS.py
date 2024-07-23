def fcfs_scheduling(processes):
    # Sort processes by their arrival time
    processes.sort(key=lambda x: x[1])
    n = len(processes)
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    print("Process ID | Arrival Time | Burst Time | Waiting Time | Turnaround Time")

    for process in processes:
        process_id, arrival_time, burst_time = process
        # Calculate the waiting time
        if current_time < arrival_time:
            current_time = arrival_time
        waiting_time = current_time - arrival_time
        total_waiting_time += waiting_time
        # Calculate the turnaround time
        turnaround_time = waiting_time + burst_time
        total_turnaround_time += turnaround_time
        # Move the current time forward by the burst time
        current_time += burst_time

        print(f"{process_id:^10} | {arrival_time:^12} | {burst_time:^10} | {waiting_time:^12} | {turnaround_time:^15}")

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    print(f"\nFCFS Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"FCFS Average Turnaround Time: {avg_turnaround_time:.2f}")


# Example process list: [(process_id, arrival_time, burst_time)]
processes = [
    (9, 0, 8),
    (3, 1, 4),
    (4, 9, 2),
   (2, 5, 6),
]

print("FCFS Scheduling:")
fcfs_scheduling(processes)
