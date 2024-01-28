import sys

def main():
    # Initialize variables to track cat visit statistics
    count_their_cat = 0
    count_our_cat = 0
    total_time_stayed = 0
    longest_visit_time = 0
    shortest_visit_time = float('inf')

    try:
        # Get the log file name from the command line arguments
        log_file_name = sys.argv[1]
        
        # Open the log file in read mode
        with open(log_file_name, "r") as log_file:
            # Read all lines from the log file
            data = log_file.readlines()

            # Iterate through each line in the log file
            for line in data:
                # Split each line into words using comma as the delimiter
                words = line.strip().split(',')
                
                # Check if the cat belongs to 'THEIRS' or 'OURS'
                if words[0] == 'THEIRS':
                    count_their_cat += 1
                elif words[0] == 'OURS':
                    count_our_cat += 1

                    # Calculate the time the cat stayed in the house
                    time_stayed = int(words[2]) - int(words[1])
                    total_time_stayed += time_stayed

                    # Update longest and shortest visit times
                    if time_stayed > longest_visit_time:
                        longest_visit_time = time_stayed
                    if time_stayed < shortest_visit_time:
                        shortest_visit_time = time_stayed

        # Print cat visit statistics
        print(f"Cat Visits: {count_our_cat}")
        print(f"Other Cats: {count_their_cat}")
        print(f"Total Time in House: {total_time_stayed//60} Hours, {total_time_stayed%60} Minutes")
        
        # Calculate and print the average visit length
        if count_our_cat != 0:
            average_visit_time = total_time_stayed // count_our_cat
            print(f"Average Visit Length: {average_visit_time} Minutes")
        
        # Print the longest and shortest visit times
        print(f"Longest Visit: {longest_visit_time} Minutes")
        print(f"Shortest Visit: {shortest_visit_time} Minutes")

    except IndexError:
        # Handle the case where the command line argument is missing
        print("Missing command line argument")
    except FileNotFoundError:
        # Handle the case where the specified log file is not found
        print(f"Cannot open '{log_file_name}'!")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # Call the main function when the script is executed
    main()
