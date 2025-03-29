'''
Project 3: Banker's Algorithim
Group Members: Bronson Garel (ID: 030294431) and Tommy Truong (ID: 027664596) 
Class: CECS326
'''
'''NOTE: Project document did not specify if available, max, and alloc matrices should be prompted'
         for user input, we decided to hard code them instead. n,m, and resource request are still prompted.'''

"Project Document Test Case"
available = [3, 3, 2] 

maximum = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# prompts user to input n processors and m resources types.
n = int(input("How many processors do you have? "))
m = int(input("How many resource types do you have? "))


def need_matrix(max, alloc):
    "Need Matrix (max - alloc.)" 
    need = [[0 for i in range(m)] for _ in range(n)] # initialize empty array to store result
    for i in range(n):
        for j in range(m):
            need[i][j] = maximum[i][j] - allocation[i][j]
    return need

"Returns (true, safe_sequence) if it is safe, or (False, []) when unsafe"
def saftey_algo(available, allocation, need):
    "uncomment if n,m not prefined"
    #n = len(allocation)  # finds number processes
    #m = len(available)   # finds number of resource types

    work = available.copy() # temporary copy of available matrix (we dont want to mess with the actual matrix)
    finish = [False] * n     # starting array with n length and "false" elements. In the while loop, we update these boolean variables to True or False. 
    safe_sequence = []      # empty array to store result

    while len(safe_sequence) < n: 
        found = False      # Flag to check if we found at least one process to finish

        for i in range(n):
            # checks if process i has not finished AND if its needs can be satisfied
            if finish[i] == False and all(need[i][j] <= work[j] for j in range(m)): #available = [3, 3, 2]

                # Simulate process i finishing by releasing its allocated resources
                for j in range(m):
                    work[j] += allocation[i][j]

                finish[i] = True             # Mark process i as finished
                safe_sequence.append(i)     # Add it to the safe sequence
                found = True                # We found a process that can safely finish
                break                       # Break out of the loop to re-check from the beginning
        # If no process can finish in this round, the system is not in a safe state
        if found == False:
            print("System is not in safe state")
            return False, []
    print("System is in a safe state.")
    print("Safe sequence:", safe_sequence)
    return True, safe_sequence

def request_resources(process, request):
    # Check if request exceeds need
    new_need = []
    for i in range(m):
        new_val = need[process][i] + request[i]
        if new_val > maximum[process][i]: 
            print("Error: Not enough resources available.")
            return
        new_need.append(new_val)

    for i in range(m):
        if new_need[i] > available[i]:
            # Do not accept request
            print("Error: Not enough resources available.")
            return

    need[process] = new_need
    saftey_algo(available, allocation, need)
    print("Resources allocated to process", process)
    

# Function calls 
need = need_matrix(maximum, allocation) # Need Matrix
saftey_algo(available, allocation, need) # Call saftey algo

# Handles resource request input
if input("Is there a resource request? (y/n): ").lower() == "y": 
    request = []
    # process number thats requesting resource
    requestingProcess = int(input("Enter process # that is requesting: "))
    for i in range(3): # 3 resources inputs only
        resource_input = int(input(f"Enter Resource {i} (max 3 inputs): "))
        request.append(resource_input)
    request_resources(requestingProcess, request)
else:
    print("no resources requested.")
