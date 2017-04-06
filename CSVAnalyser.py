#
# Python CSV Analyser
#
# @created 2017-03-24
# @version 0.01 (beta)
# @author 
# @email 
#
# CSV Analyser
# This python script which was originally developed to calculate 
# the extent of missing-ness in a given CSV file. 
# The script will output information on any given CSV file.
# The information calculated for each column is:
# Stats
#	- total number of values (numValues)
#	- number of unique values (uniqueValuesList)
#	- number of unique values (uniqueValuesList)
#	- number of duplicates (numDuplicates)
# Missing (defined as 'NaN' values)
#	- number of missing values (numMissingValues)
#	- number of non-missing values (numNonMissingValues)
# List of Unique Values
#	outputs each of the unique values, 
#	followed by the total number.
#
#
# How to run:
#
# > python CSVAnalyser.py testFile.csv
# 
# To print the unique values, the use the command line switch 
# -printUniqueValues 
# after the file name
#
# > python CSVAnalyser.py testFile.csv -printUniqueValues
#

import time

def fileAnalysisColumns(fileHeaders,dataset):
	print(" file analysis of columns ")
	
	missingValuesList = ['NaN']
	
	colIndex=0
	
	numValues=0
	numUniqueValues=0
	numMissingValues=0
	
	numMissingValues=0	
	numNonMissingValues=0	
	
	for i in fileHeaders:
		print('  For Column ('+str(colIndex)+'): '+i)
	
		numValues=0
		numUniqueValues=0
		numMissingValues=0
		numDuplicates=0
	
		numMissingValues=0
		numNonMissingValues=0
	
		uniqueValuesList=[]
	
		for j in dataset:
			currentValue = j[colIndex]
			#print(currentValue)

			numValues=numValues+1
			
			if currentValue in uniqueValuesList:
				#print("Contained")
				#print(" Value= "+currentValue)				
				#print(uniqueValuesList)
				numDuplicates=numDuplicates+1
			else:
				#print("Not contained")
				uniqueValuesList.append(currentValue)

			#Checks for missing ness
			if currentValue in missingValuesList:
				#print("Value missing")
				numMissingValues=numMissingValues+1
			else:
				#print("Value not missing")
				numNonMissingValues=numNonMissingValues+1
				
			
				
		print('   numValues='+str(numValues))			
		print('   uniqueValuesList='+str(len(uniqueValuesList)))
		print('   numDuplicates='+str(numDuplicates))
		print('  Missing ')
		print('   numMissingValues='+str(numMissingValues))		
		print('   numNonMissingValues='+str(numNonMissingValues))					
		print('  Missing Cals')
		totalMissing=numMissingValues/numValues
		print('   Total missing percentage '+str(round(totalMissing,2))+' %. (numMissing) '+str(numMissingValues)+' / (TotalValue) '+str(numValues)+' = '+str(totalMissing))
		

		# list of unique values
		if printUniqueValue:
			print('  List of Unique Values')
			kcounter=0
			for k in uniqueValuesList:		
				print('   ['+str(kcounter)+'] '+k)
				kcounter=kcounter+1
			print('  Unique values count='+str(kcounter))


		# end
		print('')			
		colIndex=colIndex+1			

# /fileAnalysisColumns()
	
	


	
	
#
# Main
#	
	
import csv
import io
import sys

	
print("Starting")
start_time = time.time()	

sourceFile=''
printUniqueValue=False

if len(sys.argv)>1:	
	sourceFile=sys.argv[1]
	#print sourceFile
else:
	print("-")
	print("- Error: No command line argument for input file")
	print("-")


if len(sys.argv)>2:
	if sys.argv[2]=='-printUniqueValues':
		printUniqueValue=True

else:
	print("-")
	print("- Error: No command line argument for input file")
	print("-")


#with open(baseDir+file_dataset, 'rb') as f:
#with io.open(baseDir+file_dataset, 'rt', encoding='utf8') as f:
with io.open(sourceFile, 'rt', encoding='utf8') as f:
    reader = csv.reader(f)
    fileHeaders = next(reader)#skip header
    dataset = list(reader)


#print(fileHeaders)
print(" dataset name = "+sourceFile)	
print(" number rows   = "+str(len(dataset)))	

fileAnalysisColumns(fileHeaders,dataset)

#
print("Runtime: %s seconds" % (time.time() - start_time))
print("End")


