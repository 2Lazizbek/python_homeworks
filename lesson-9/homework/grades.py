import csv
from collections import defaultdict

# Step 1: Create grades.csv file
def create_initial_csv():
    data = [
        ['Name', 'Subject', 'Grade'],
        ['Alice', 'Math', '85'],
        ['Bob', 'Science', '78'],
        ['Carol', 'Math', '92'],
        ['Dave', 'History', '74']
    ]
    
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Step 2: Read and process the data
def process_grades():
    # Read data from grades.csv into a list of dictionaries
    grades_data = []
    with open('grades.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert Grade to float for calculations
            row['Grade'] = float(row['Grade'])
            grades_data.append(row)
    
    # Calculate average grade per subject
    subject_totals = defaultdict(float)  # Total grades per subject
    subject_counts = defaultdict(int)    # Number of grades per subject
    
    for entry in grades_data:
        subject = entry['Subject']
        grade = entry['Grade']
        subject_totals[subject] += grade
        subject_counts[subject] += 1
    
    # Calculate averages
    subject_averages = {}
    for subject in subject_totals:
        subject_averages[subject] = subject_totals[subject] / subject_counts[subject]
    
    return subject_averages

# Step 3: Write average_grades.csv
def write_averages_csv(averages):
    with open('average_grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        
        # Write each subject's average
        for subject, avg in averages.items():
            writer.writerow([subject, avg])

# Main execution
def main():
    try:
        # Create initial grades.csv
        create_initial_csv()
        print("Created grades.csv")
        
        # Process grades and calculate averages
        averages = process_grades()
        print("\nSubject Averages:")
        for subject, avg in averages.items():
            print(f"{subject}: {avg}")
        
        # Write averages to new CSV
        write_averages_csv(averages)
        print("\nCreated average_grades.csv")
        
    except FileNotFoundError:
        print("Error: Could not find the input file")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()