##Robert Fernandez
##Complete
##Read numbers 50 to 100 and use a for loop.


# Open file in read mode
with open('number_list.txt', 'r') as infile:
    
    # Read each line in the file
    for line in infile:
        
        # Print the line after stripping 
        print(line.strip())
