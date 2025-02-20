def get_remarks(score):
    if 4.50 <= score <= 5.00:
        return "Outstanding"
    elif 4.00 <= score <= 4.49:
        return "Very Satisfactory"
    elif 3.50 <= score <= 3.99:
        return "Satisfactory"
    elif 3.00 <= score <= 3.49:
        return "Needs Improvement"
    elif score < 2.99:
        return "Poor"
    else:
        return "Invalid score"

def main():
    while True:
        name = input("Enter Faculty name: ")
        try:
            score = float(input("Enter the evaluation score (0.00 - 5.00): "))
            if 0.00 <= score <= 5.00:
                remarks = get_remarks(score)
                print(f"\nFaculty Name: {name}")
                print(f"Evaluation Score: {score}")
                print(f"Faculty Remarks: {remarks}\n")
            else:
                print("Invalid score. Score must be between 0.00 and 5.00.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the score.")

        another = input("Evaluate another faculty? (yes/no): ").lower()
        if another != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()