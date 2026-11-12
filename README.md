# PLP Python Week 7 Assignment - File Handling (My Notes & The Report Builder)

This repository contains solutions for Week 7, focusing on file input/output operations, reading CSV datasets into dictionaries, handling missing files defensively, and generating text reports.

## File Descriptions
- ** notes.txtmy_n **: A text file generated and updated dynamically by my_notes.py.
- ** my_notes.py **: Demonstrates file creation, writing (w), appending (a), and reading line-by-line (r).
- ** hubs.csv **: Contains learner records used as input data for the report generator.
- ** report_builder.py **: Processes CSV data, computes summary metrics (total, passed, failed, and average), handles missing file exceptions, and outputs a formatted report.txt.
- ** report.txt **: The generated final summary report output.

## Technical Question
**What would happen if you changed (a) to (w) in Question 1?**
If you change the file open mode from 'a' (append) to 'w' (write) when adding new notes, Python will overwrite the entire file from the beginning instead of adding content to the end. This would erase all previously written notes in 'my_notes.txt'.# PLP Python Week 7 Assignment - File Handling (My Notes & The Report Builder)

This repository contains solutions for Week 7, focusing on file input/output operations, reading CSV datasets into dictionaries, handling missing files defensively, and generating text reports.

## File Descriptions
- ** my_notes.txt **: A text file generated and updated dynamically by 'my_notes.txt'.
- ** my_notes.txt **: Demonstrates file creation, writing (w), appending ('a'), and reading line-by-line (r).
- ** hubs.csv**: Contains learner records used as input data for the report generator.
- ** report_builder.py **: Processes CSV data, computes summary metrics (total, passed, failed, and average), handles missing file exceptions, and outputs a formatted 'report.txt'.
- ** report.txt **: The generated final summary report output.

## Technical Question
**What would happen if you changed 'a' to 'w'in Question 1?**
If you change the file open mode from 'a' (append) to 'w' (write) when adding new notes, Python will overwrite the entire file from the beginning instead of adding content to the end. This would erase all previously written notes in 'my_notes.txt'.