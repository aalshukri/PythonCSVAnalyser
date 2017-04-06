# PythonCSVAnalyser

Python CSV Analyser

Version 0.01 (beta)


This python script was (originally) developed to calculate 
the extent of missing-ness in a given CSV file. 
This script will also output information for each column as detailed below:

Stats
	- total number of values (numValues)
	- number of unique values (uniqueValuesList)
	- number of unique values (uniqueValuesList)
	- number of duplicates (numDuplicates)
Missing (defined as 'NaN' values)
	- number of missing values (numMissingValues)
	- number of non-missing values (numNonMissingValues)
List of Unique Values
	outputs each of the unique values, 
	followed by the total number.


# Running Instructions

To perform a test run with the given test file, run the command below:

> python CSVAnalyser.py testFile.csv
 
To print the unique values from each column in the CSV file,
the use the command line switch -printUniqueValues.

> python CSVAnalyser.py testFile.csv -printUniqueValues




