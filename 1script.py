import os
import csv
import commands

#make it into 100 different files

def file_len(fileName): #method to return the number of lines in a file
		with open(fileName) as f:
			for i, l in enumerate(f):
				pass
		return i + 1

NatureData = open("Nature.csv", 'wb')
wr = csv.writer(NatureData, dialect = 'excel')

wr.writerow(['compound','contributorName','contributorInstitution','contributorURL' ,'institutionURL','extractedRef','datatype','measuredProp1', 'measured2d1', 'measuredUnits1', 'measuredProp4', 'measuredValue4', 'measuredUnits4', 'measuredProp5', 'measuredValue5', 'measuredUnits5','measuredProp6', 'measuredValue6', 'measuredUnits6','measuredProp7', 'measuredValue7', 'measuredUnits7','measuredProp8', 'measuredValue8', 'measuredUnits8','measuredProp9', 'measuredValue9', 'measuredUnits9','measuredProp10', 'measuredValue10', 'measuredUnits10', 'conditionProp11', 'condition2d11', 'conditionUnits11' ,'measuredProp11','measured2d11', 'measuredUnits11','conditionProp12', 'condition2d12', 'conditionUnits12','measuredProp12', 'measured2d12', 'measuredUnits12', 'conditionProp13', 'condition2d13', 'conditionUnits13','measuredProp13', 'measured2d13', 'measuredUnits13','conditionProp14', 'condition2d14', 'conditionUnits14','measuredProp14', 'measured2d14', 'measuredUnits14','conditionProp15', 'condition2d15', 'conditionUnits15','measuredProp15', 'measured2d15', 'measuredUnits15'])

compound = ''
contributorName = '' #Raghunathan Ramakrishnan, Pavlo O. Dral, Matthias Rupp & O. Anatole von Lilienfeld'
contributorInstitution = '' #Nature Science Data'
contributorURL = '' #http://www.nature.com/articles/sdata201422'
institutionURL = '' #http://www.nature.com/sdata/'
extractedRef = '10.1038/sdata.2014.22'
datatype = 'experimental'

measuredProp1 = 'Rotational Constant'
rotationalconstantA = 1.00
rotationalconstantB = 1.00
rotationalconstantC = 1.00
measured2d1 = '[' + str(rotationalconstantA) + ',' + str(rotationalconstantB) + ',' + str(rotationalconstantC)+ ']'
measuredUnits1 = 'Hz'
	
#measuredProp2 = 'Rotational Constant B'
#measuredValue2 = 1.00
#measuredUnits2 ='Hz'
	
#measuredProp3 = 'Rotational Constant C'
#measuredValue3 = 1.00
#measuredUnits3 = 'Hz'
	
measuredProp4 = 'Dipole Moment'
measuredValue4 = 1.00
measuredUnits4 = 'D'
	
measuredProp5 = 'Isotropic Polarizability'
measuredValue5 = 1.00
measuredUnits5 = 'Ang3'
	
measuredProp6 = 'HOMO'
measuredValue6 = 1.00
measuredUnits6 = 'eV'
	
measuredProp7 = 'LUMO'
measuredValue7 = 1.00
measuredUnits7 = 'eV'
	
measuredProp8 = 'Band Gap'
measuredValue8 = 1.00
measuredUnits8 =  'eV'
	
measuredProp9 = 'Electronic Spatial '
measuredValue9 = 1.00
measuredUnits9= 'Ang2'
	
measuredProp10 = 'Zero Point Vibrational Energy'
measuredValue10 = 1.00
measuredUnits10 = 'cm-1'
	
conditionProp11 = 'Temperature'
condition2d11 = '[0]'
conditionUnits11 = 'K'
	
measuredProp11= 'Internal Energy'
internalenergy0= 1.00
measured2d11='['+str(internalenergy0)+']'
measuredUnits11 = 'kJ/mol'
	
conditionProp12 = 'Temperature'
condition2d12 = '[298.15]'
conditionUnits12 = 'K'
	
measuredProp12 = 'Internal Energy'
internalenergy298 = 1.00
measured2d12 = '['+str(internalenergy298)+']'
measuredUnits12 = 'kJ/mol'
	
conditionProp13 = 'Temperature'
condition2d13 = '[298.15]'
conditionUnits13 = 'K'
	
measuredProp13 = 'Enthalpy'
enthalpy = 1.00
measured2d13 = '['+ str(enthalpy)+']'
measuredUnits13 = 'kJ/mol'
	
conditionProp14 = 'Temperature'
condition2d14 = '[298.15]'
conditionUnits14 = 'K'
	
measuredProp14 = 'Free Energy'
freeenergy = 1.00
measured2d14 ='['+str(freeenergy)+']'
measuredUnits14 = 'kJ/mol'
	
conditionProp15 = 'Temperature'
condition2d15 = '[298.15]'
conditionUnits15 = 'K'
	
measuredProp15 = 'Heat Capacity'
heatcapacity = 1.00
measured2d15 = '['+ str(heatcapacity) +']'
measuredUnits15 = 'kJ/mol'

fileDir	= 'dsgdb9nsd.xyz'
contents = os.listdir(fileDir) # returns list

for index in enumerate(contents):
	
		

	#fileLength = file_len(fileDir + '/' + fileName)
	#print (fileLength)
	
	#secondLine = ','.join(str.split(commands.getoutput("sed -n 2p " + fileDir + '/' + fileName)))
	#print (secondLine)
	
	
		