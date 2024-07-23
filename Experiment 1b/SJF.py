def sjf_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    completed = [False] * n
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    completed_processes = 0
    print("Process ID | Arrival Time | Burst Time | Waiting Time | Turnaround Time")
    while completed_processes < n:
        # Get the list of processes that have arrived and are not completed
        eligible_processes = [p for p in processes if p[1] <= current_time and not completed[processes.index(p)]]
        if eligible_processes:
            # Select the process with the shortest burst time
            eligible_processes.sort(key=lambda x: x[2])
            process = eligible_processes[0]
            process_id, arrival_time, burst_time = process

            waiting_time = current_time - arrival_time
            total_waiting_time += waiting_time
            turnaround_time = waiting_time + burst_time
            total_turnaround_time += turnaround_time

            # Update current time and mark the process as completed
            current_time += burst_time
            completed[processes.index(process)] = True
            completed_processes += 1

            print(f"{process_id:^10} | {arrival_time:^12} | {burst_time:^10} | {waiting_time:^12} | {turnaround_time:^15}")
        else:
            # If no process is ready, increment the current time
            current_time += 1
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    print(f"\nSJF Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"SJF Average Turnaround Time: {avg_turnaround_time:.2f}")

# Example process list: [(process_id, arrival_time, burst_time)]
processes = [
    (5, 3, 4),
    (4, 2, 7),
    (6, 1, 9),
    (7, 0, 11),
]
print("SJF Scheduling:")
sjf_scheduling(processes)
