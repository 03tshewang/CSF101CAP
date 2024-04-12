#########################################
#TshewangTashi
#Electronics and communications engineering
#02230115
##########################################
#REFERENCES
#https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
#https://www.w3schools.com/python/
#https://www.geeksforgeeks.org/python-programming-language/
############################################
#SOLUTION
#Solution score:49977
#input_5_cap1.txt
############################################



#function to read input.txt file and the number of rounds
def read_input(file_path):
    #oprn input file to read
    with open(file_path, 'r') as file:
        #iterate and split each line and create tuple containing opponent_choice and your_response
        #stores all tuples in a list and return it
        return [tuple(line.split()) for line in file]

#function to Calculate final score
def calculate_score(no_of_rounds):
    #initialize total score to 0
    total_score = 0
    #iteterate through each round in list of rounds 
    for opponent_choice, your_response in no_of_rounds:
        # Determine the score based on opponent_choice and your_response using conditional operator
        if opponent_choice == "A":
            score = 3 if your_response == "X" else 4 if your_response == "Y" else 8
        elif opponent_choice == "B":
            score = 1 if your_response == "X" else 5 if your_response == "Y" else 9
        elif opponent_choice == "C":
            score = 2 if your_response == "X" else 6 if your_response == "Y" else 7
        #total score increment by score
        total_score += score
    return total_score

#call read_input function to Read the input file
extract_file = read_input('input_5_cap1.txt')

#call calculate_score function to Calculate the final score
final_score = calculate_score(extract_file)

# Print the total score
print("Total score:", final_score)
