# Part 2 - The Report Builder

import csv

filename = "hubs.csv"

try:
    rows = []
    # Open and read CSV into a list of dictionaries
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
            
    # Calculations
    total_learners = len(rows)
    passed_count = 0
    failed_count = 0
    total_score = 0
    
    for row in rows:
        score = int(row["score"])
        total_score += score
        if row["status"].strip().lower() == "passed":
            passed_count += 1
        else:
            failed_count += 1
            
    average_score = total_score / total_learners if total_learners > 0 else 0
    
    # Write the report to report.txt
    report_content = f"""LEARNER REPORT
Total learners: {total_learners}
Passed: {passed_count}
Failed: {failed_count}
Average score: {average_score:.1f}
"""
    
    with open("report.txt", "w") as report_file:
        report_file.write(report_content)
        
    print("Report written to report.txt")
    print(report_content)

except FileNotFoundError:
    print(f"{filename} not found.")