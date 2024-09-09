def main():
    # Input for total memory available
    ms = int(input("Enter the total memory available (in Bytes) -- "))
    
    temp = ms
    mp = []
    n = 0
    ch = 'y'
    
    while ch == 'y':
        # Input for memory required by the process
        mem_req = int(input(f"Enter memory required for process {n + 1} (in Bytes) -- "))
        
        if mem_req <= temp:
            print(f"Memory is allocated for Process {n + 1}")
            mp.append(mem_req)
            temp -= mem_req
        else:
            print("Memory is Full")
            break
        
        # Ask if the user wants to continue
        ch = input("Do you want to continue (y/n) -- ").strip().lower()
        n += 1
    
    # Display results
    print(f"\nTotal Memory Available -- {ms}")
    print("\n\tPROCESS\t\tMEMORY ALLOCATED")
    
    for i in range(n):
        print(f"\t{i + 1}\t\t{mp[i]}")
    
    total_allocated = ms - temp
    print(f"\nTotal Memory Allocated is {total_allocated}")
    print(f"Total External Fragmentation is {temp}")

if __name__ == "__main__":
    main()
