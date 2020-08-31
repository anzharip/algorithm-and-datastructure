def hasSingleCycle(array):
    # Write your code here.
    start_idx = 0
    cur_idx = start_idx
    traversed_el = 0
    
    while traversed_el < len(array):
        if traversed_el > 0 and traversed_el < len(array) and cur_idx == start_idx:
            return False
        cur_idx = (cur_idx + array[cur_idx]) % len(array)
        traversed_el += 1
    
    if cur_idx == start_idx:
        return True
    else: 
        return False