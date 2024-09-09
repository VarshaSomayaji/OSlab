def main():
    # Input for total memory and block size
    ms = int(input("Enter the total memory available (in Bytes) -- "))
    bs = int(input("Enter the block size (in Bytes) -- "))
    
    # Calculations for number of blocks and external fragmentation
    nob = ms // bs
    ef = ms % bs
    
    # Input for number of processes
    n = int(input("\nEnter the number of processes -- "))
    
    # Input for memory required by each process
    mp = []
    for i in range(n):
        mem_req = int(input(f"Enter memory required for process {i + 1} (in Bytes)-- "))
        mp.append(mem_req)
    
    # Display results
    print(f"\nNo. of Blocks available in memory -- {nob}")
    print("\nPROCESS\tMEMORY REQUIRED\tALLOCATED\tINTERNAL FRAGMENTATION")
    
    tif = 0  # Total Internal Fragmentation
    p = 0  # Number of allocated blocks

    for i in range(n):
        if p >= nob:
            break
        mem_req = mp[i]
        print(f"\n{i + 1}\t\t{mem_req}", end='')
        
        if mem_req > bs:
            print("\t\tNO\t\t---", end='')
        else:
            internal_frag = bs - mem_req
            print(f"\t\tYES\t{internal_frag}", end='')
            tif += internal_frag
            p += 1
    
    if p < n:
        print("\nMemory is Full, Remaining Processes cannot be accommodated")

    # Display total fragmentation results
    print(f"\n\nTotal Internal Fragmentation is {tif}")
    print(f"Total External Fragmentation is {ef}")

if __name__ == "__main__":
    main()
