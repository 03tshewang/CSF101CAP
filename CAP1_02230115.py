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
#Solution score:49995
#input_5_cap1.txt
############################################




#function to read the input.txt file and extract the number of rounds
def read_input(file_path):
    #initialize empty list to store number of rounds
    no_of_rounds= []
    #open input file to read
    with open(file_path,'r') as file:
        #iterate through each line in file
        for line in file:
            #split each line and extract opponent_choice and your_response
            opponent_choice, your_response = line.split()
            #append opponent_choice and your_response to the list of no_of_rounds
            no_of_rounds.append((opponent_choice,your_response))
        return no_of_rounds

#function to calculate total score
def calculate_score(no_of_rounds):
    score = 0
    #create dictionaries to assign score to opponent_choice and your_response
    opponent_choice_score = {'A':1, 'B':2, 'C':3}
    your_response_score = {'X':0, 'Y':3, 'Z':6}
    
    #iterate through list of no_of_rounds
    for opponent_choice, your_response in no_of_rounds:
        #score increment by sum of opponent_choice_score and your_response_score
        score += opponent_choice_score.get(opponent_choice, 0) + your_response_score.get(your_response, 0)
    return score

#call read_input function to read file and extract number of rounds assigning to new variable
extract_file = read_input('input_5_cap1.txt')
#call total_score function to calculate total score assigning to new variable
total_score = calculate_score(extract_file)
#print total score
print("Total score:", total_score)