#to write to 100 different csv files

import os
import csv
import commands


def make_new_file(i): #method that creates to new file
	NatureData = open("Nature CSVs/Nature"+ str(i)+".csv", 'wb')
	wr = csv.writer(NatureData, dialect = 'excel')
	wr.writerow(['compound','contributorName','contributorInstitution','contributorURL' ,'institutionURL','extractedRef','datatype', 'conditionProp1', 'condition2d1', 'conditionUnits1' ,'measuredProp1','measured2d1', 'measuredUnits1','conditionProp2', 'condition2d2', 'conditionUnits2','measuredProp2', 'measured2d2', 'measuredUnits2', 'conditionProp3', 'condition2d3', 'conditionUnits3','measuredProp3', 'measured2d3', 'measuredUnits3','conditionProp4', 'condition2d4', 'conditionUnits4','measuredProp4', 'measured2d4', 'measuredUnits4','conditionProp5', 'condition2d5', 'conditionUnits5','measuredProp5', 'measured2d5', 'measuredUnits5', 'measuredProp6', 'measured2d6', 'measuredUnits6', 'measuredProp7', 'measuredValue7', 'measuredUnits7', 'measuredProp8', 'measuredValue8', 'measuredUnits8','measuredProp9', 'measuredValue9', 'measuredUnits9','measuredProp10', 'measuredValue10', 'measuredUnits10','measuredProp11', 'measuredValue11', 'measuredUnits11','measuredProp12', 'measuredValue12', 'measuredUnits12', 'measuredProp13', 'measuredValue13', 'measuredUnits13'])
	return wr

def file_len(fileName): #method to return the number of lines in a file
		with open(fileName) as f:
			for i, l in enumerate(f):
				pass
		return i + 1


def get_compound_name(fileDir, fileName, line):
	fileLength = file_len(fileDir + '/' + fileName)
	line = commands.getoutput("sed -n " + str(fileLength)+"p " + fileDir + '/' + fileName) 
	array = line.split('/')
	return array[1]
	
def write_csv_contents(fileDir, fileName, line):
	secondLine = ','.join(str.split(commands.getoutput("sed -n 2p " + fileDir + '/' + fileName)))
	array = secondLine.split(',')
	
	contributorName = '' #Raghunathan Ramakrishnan, Pavlo O. Dral, Matthias Rupp & O. Anatole von Lilienfeld'
	contributorInstitution = '' #Nature Science Data'
	contributorURL = '' #http://www.nature.com/articles/sdata201422'
	institutionURL = '' #http://www.nature.com/sdata/'
	extractedRef = '10.1038/sdata.2014.22'
	datatype = 'experimental'

	conditionProp1 = 'Temperature'
	condition2d1 = '[0]'
	conditionUnits1 = 'K'
	
	measuredProp1= 'Internal Energy'
	internalenergy0 = float(array[12])*2625.5 #11
	measured2d1='['+str(internalenergy0)+']'
	measuredUnits1 = 'kJ/mol'
	
	conditionProp2 = 'Temperature'
	condition2d2 = '[298.15]'
	conditionUnits2 = 'K'
	
	measuredProp2 = 'Internal Energy'
	internalenergy298 = float(array[13])*2625.5 #12
	measured2d2 = '['+str(internalenergy298)+']'
	measuredUnits2 = 'kJ/mol'
	
	conditionProp3 = 'Temperature'
	condition2d3 = '[298.15]'
	conditionUnits3 = 'K'
	
	measuredProp3 = 'Enthalpy'
	enthalpy = float(array[14])*2625.5 #13
	measured2d3 = '['+ str(enthalpy)+']'
	measuredUnits3 = 'kJ/mol'
	
	conditionProp4 = 'Temperature'
	condition2d4 = '[298.15]'
	conditionUnits4 = 'K'
	
	measuredProp4 = 'Free Energy'
	freeenergy = float(array[15])*2625.5 #14
	measured2d4 ='['+str(freeenergy)+']'
	measuredUnits4 = 'kJ/mol'
	
	conditionProp5 = 'Temperature'
	condition2d5 = '[298.15]'
	conditionUnits5 = 'K'
	
	measuredProp5 = 'Heat Capacity'
	heatcapacity = float(array[16]) #15
	measured2d5 = '['+ str(heatcapacity) +']'
	measuredUnits5 = 'kJ/mol'
	
	
	measuredProp6 = 'Rotational Constant'
	measured2d6 = '[' + str(float(array[2])) + ',' + str(float(array[3])) + ',' + str(float(array[4]))+ ']'
	measuredUnits6 = 'Hz'
	
	measuredProp7 = 'Dipole Moment'
	measuredValue7 = float(array[5]) #4
	measuredUnits7 = 'D'
	
	measuredProp8 = 'Isotropic Polarizability'
	measuredValue8 = float(array[6])*0.148185 #5
	measuredUnits8 = 'Ang3'
	
	measuredProp9 = 'HOMO'
	measuredValue9 = float(array[7])*27.211396 #6
	measuredUnits9 = 'eV'
	
	measuredProp10 = 'LUMO'
	measuredValue10 = float(array[8])*27.211396 #7
	measuredUnits10 = 'eV'
	
	measuredProp11 = 'Band Gap'
	measuredValue11 = float(array[9])*27.211396 #8
	measuredUnits11 =  'eV'
	
	measuredProp12 = 'Electronic Spatial '
	measuredValue12 = float(array[10])*0.280028 #9
	measuredUnits12= 'Ang2'
	
	measuredProp13 = 'Zero Point Vibrational Energy'
	measuredValue13 = float(array[11])*219470 #10
	measuredUnits13 = 'cm-1'
	
	wr.writerow([compound,contributorName,contributorInstitution,contributorURL ,institutionURL,extractedRef,datatype, conditionProp1, condition2d1, conditionUnits1 ,measuredProp1,measured2d1, measuredUnits1,conditionProp2, condition2d2, conditionUnits2,measuredProp2, measured2d2, measuredUnits2, conditionProp3, condition2d3, conditionUnits3,measuredProp3, measured2d3, measuredUnits3,conditionProp4, condition2d4, conditionUnits4,measuredProp4, measured2d4, measuredUnits4,conditionProp5, condition2d5, conditionUnits5,measuredProp5, measured2d5, measuredUnits5, measuredProp6, measured2d6, measuredUnits6, measuredProp7, measuredValue7, measuredUnits7, measuredProp8, measuredValue8, measuredUnits8,measuredProp9, measuredValue9, measuredUnits9,measuredProp10, measuredValue10, measuredUnits10,measuredProp11, measuredValue11, measuredUnits11,measuredProp12, measuredValue12, measuredUnits12, measuredProp13, measuredValue13, measuredUnits13])

compound = ''

fileDir	= 'allXYZfiles'
contents = os.listdir(fileDir) #returns list

fileinc = 0
rowinc = 0
wr = make_new_file(fileinc)

for fileName in contents:
	#print str(fileName)
	#print "fileinc" + str(fileinc)
	if rowinc <= 1338:
		#print inc
		xyzFile = open(str(fileDir + '/' + fileName))
		for line in xyzFile: 
			if line.startswith("InChI"):
					compound = get_compound_name(fileDir, fileName, line)
			if line.startswith("gdb"):
					write_csv_contents(fileDir, fileName, line)
		xyzFile.close()
		rowinc +=1
		#print 'rowinc' + str(rowinc)
	else:
		fileinc += 1
		wr = make_new_file(fileinc)
		rowinc = 0
		
		
		
		
		
		
		