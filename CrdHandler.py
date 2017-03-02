__author__ = "Ruthvik Mandava"

import math
import constants

############################ GLOBAL VARIABLES ####################
totalNATMS = 0
atomsNeg = []
crd_entries = []
residues = {}
SGatoms = []
XCor = []
YCor = []
ZCor = []
rf_dictionary = {}
radius_dictionary = {}
global distance_matrix
#########################################################

####################### READS COORDINATES AND RESIDUES INFORMATION OF GIVEN CRD FILE #################
def readCrd(CrdFile):
    global totalNATMS, XCor, YCor, ZCor, crd_entries, residues, SGatoms
    crd_file = open(CrdFile,"r")
    crd_entries.append([0,'null',0,'null',0,0,0,0])
    XCor.append(0)
    YCor.append(0)
    ZCor.append(0)

    for line in crd_file:
        line = line.split()
        if(line[0] == '*'):
            flag = 0
            continue
        if flag is 0:
            flag = 1
            continue
        if(line[7] == 'MAIN'):
            atm_no = int(line[0].strip(' '))
            res_no = int(line[1].strip(' '))
            res_name = line[2].strip(' ')
            atm_name = line[3].strip(' ')
            if atm_name == 'SG':
                SGatoms.append(atm_no)
            X = float(line[4].strip(' '))
            Y = float(line[5].strip(' '))
            Z = float(line[6].strip(' '))
            asa = float(line[9].strip(' '))
            crd_entries.append([res_no,res_name,atm_no,atm_name,X,Y,Z,asa])
            if res_no in residues:
                residues[res_no]['atoms'].append(atm_no)
            else:
                residues[res_no] = {}
                residues[res_no]['RESNo'] = res_no
                residues[res_no]['atoms'] = []
                residues[res_no]['RES'] = res_name
                residues[res_no]['atoms'].append(atm_no)
            XCor.append(X)
            YCor.append(Y)
            ZCor.append(Z)
            totalNATMS = totalNATMS+1
    crd_file.close()
    detectThioLinkage()
################################################################################

##################### Disulphide Detection #####################################

def detectThioLinkage():
    for i in SGatoms:
        for j in SGatoms:
            if i != j:
                dist = getDistance(XCor[i],YCor[i],ZCor[i],XCor[j],YCor[j],ZCor[j])
                if dist < 2.5 :
                    crd_entries[i][1] = 'CY2'
                    crd_entries[j][1] = 'CY2'
                    residues[crd_entries[i][0]]['RES'] = 'CY2'
                    residues[crd_entries[j][0]]['RES'] = 'CY2'
                    SGatoms.remove(i)
                    SGatoms.remove(j)
                    break
################################################################################

######################### READS RADIUS AND REKKER FRAGMENTAL COEFFICIENTS ############################
def readRFnRadius(inp_file):
    global radius_dictionary
    global rf_dictionary
    radius_file = open(inp_file,"r")
    for line in radius_file:
        if(line[0:4] == 'RESI'):
            current_residue = line[5:9].strip(' ')
            radius_dictionary[current_residue] = dict()
            rf_dictionary[current_residue] = dict()
            continue
        elif(line[0:4] == 'ATOM'):
            atom = line[5:9].strip(' ')
            r = line[39:45].strip(' ')
            rf = line[32:38].strip(' ')

            radius_dictionary[current_residue][atom] = float(r)
            rf_dictionary[current_residue][atom] = float(rf)
            continue
        else: continue
    radius_file.close()
######################################################################################

################## UTILITY MATH FUNCTION : DISTANCE BETWEEN TWO VERTICES IN 3D COORDINATE SYSTEM ###############
def getDistance(x1,y1,z1,x2,y2,z2):
    x = (x1-x2)*(x1-x2)
    y = (y1-y2)*(y1-y2)
    z = (z1-z2)*(z1-z2)
    dist = x+y+z
    return dist
########################################################################################

####################### CALCULATES DISTANCE BETWEEN EVERY PAIR OF ATOMS ###############
def find_distances():
    global distance_matrix
    distance_matrix = [[0 for i in range(1,totalNATMS+2)]for j in range(1,totalNATMS+2)]
    for i in range(1,totalNATMS+1):
        for j in range(i+1,totalNATMS+1):
            d = getDistance(XCor[i],YCor[i],ZCor[i],XCor[j],YCor[j],ZCor[j])
            distance_matrix[i][j] = d
            distance_matrix[j][i] = d
####################################################################################################

################################# CALCULATES HPY FOR A GIVEN RESIDUE NUMBER #######################
def getHpy(resno):
    resName = residues[resno]['RES']
    groups = constants.GROUPS[resName]['G']
    resHpy = {}
    for group in groups:
        atomsList = []
        if resno == 1 and group in ['AM','AP']:
            groupAtoms = constants.GROUPS['NTER']
        elif resno == len(residues) and group is 'CM':
            groupAtoms = constants.GROUPS['CTER']
        else: groupAtoms = constants.GROUPS[resName][group]

        for atmno in residues[resno]['atoms']:
            if crd_entries[atmno][3] in groupAtoms:
                atomsList.append(atmno)
        groupHpy = getGroupHpy(resno, resName, atomsList)
        resHpy[group] = groupHpy

    return resHpy
##################################################################################################3

########################## CALCULATES HPY OF A SINGLE GROUP ####################################3
def getGroupHpy(resno, resname, atmList):
    hpy = 0
    for restAtom in crd_entries:
        if restAtom[0] == 0:continue
        maxDB = 0
        if restAtom[0] is resno:
            continue
        if restAtom[3] in ['OT1','OT2']:
            rf = -0.65
        elif restAtom[3] in ['HT1','HT2','HT3']:
            rf = 0
        else:
            try :
                rf = rf_dictionary[restAtom[1]][restAtom[3]]
            except:
                print("rf values not available for %s %d" %resname %restAtom[3])

        for each in atmList:
            if crd_entries[each][3] in ['OT1', 'OT2']:
                radius = 1.7
            elif crd_entries[each][3] in ['HT1','HT2','HT3']:
                radius = 0.2245
            else:
                radius = radius_dictionary[resname][crd_entries[each][3]]
            nearRadius = radius+2.275
            extendedRadius = nearRadius+0.2
            distance = distance_matrix[restAtom[2]][each]
            if(distance <= (nearRadius*nearRadius)):curDB = 1
            elif distance >= (extendedRadius*extendedRadius): curDB = 0
            else:
                distance = math.sqrt(distance)
                curDB = ((((extendedRadius - distance)*(extendedRadius - distance))*
                                (extendedRadius + (2*distance) - (3*nearRadius)))/
                               ((extendedRadius-nearRadius)*(extendedRadius-nearRadius)*(extendedRadius-nearRadius)))

            if(curDB > maxDB):
                maxDB = curDB
        if maxDB:
            hpy = hpy + (maxDB*rf)
    return round(hpy,3)
#######################################################################################################

################## UTILITY FUNCTION TO GET HPY FOR COMPLETE PROTEIN OR FOR SINGLE RESIDUE ##############
def calculateHpy(inputCrd):
    print('Enter Residue Number or Enter 0 to get Hpy for all Residues ')
    inp = input("Enter Here : ")
    inp = int(inp)
    if inp > len(residues):
        print("Input Protein doesn't have %d residue"%inp)
        calculateHpy(inputCrd)
    else:
        if inp == 0:
            outputFile = open(inputCrd[0:5]+".menv","w")
            for i in range(1,len(residues)+1):
                resHpy = getHpy(i)
                for group in constants.GROUPS[residues[i]['RES']]['G']:
                    try:
                        hpy = resHpy[group]
                    except:
                        print("Error calculating Hpy for %d %s %s"%(i,residues[i]['RES'],group))
                    try:
                        resName = residues[i]['RES']
                        solventHpy = constants.SOLVENTHPY[resName][group]
                        for each in residues[i]['atoms']:
                            if crd_entries[each][3] in constants.GROUPS[resName][group]:
                                asa = crd_entries[each][7]
                                break
                        totalHpy = (1-asa)*hpy
                        totalHpy = totalHpy+asa*solventHpy
                        rHpy = totalHpy/solventHpy
                        outputFile.write("%d %s %s %.3f %.3f %.3f %.3f"%(i,residues[i]['RES'],group,1-asa,hpy,totalHpy,rHpy))
                        outputFile.write("\n")
                    except:
                        print("solvent values not found for %d %s %s"%(inp,residues[i]['RES'],group))

            outputFile.close()
            print("Check the output file with the name : %s"%(inputCrd[0:5]+".menv"))

        else :
            resHpy = getHpy(inp)
            for group in constants.GROUPS[residues[inp]['RES']]['G']:
                try:
                    hpy = resHpy[group]
                except:
                    print("Error calculating Hpy for %d %s %s"%(inp,residues[inp]['RES'],group))
                try:
                    resName = residues[inp]['RES']
                    solventHpy = constants.SOLVENTHPY[resName][group]
                    for each in residues[inp]['atoms']:
                        if crd_entries[each][3] in constants.GROUPS[resName][group]:
                            asa = crd_entries[each][7]
                            break
                    totalHpy = (1-asa)*hpy
                    totalHpy = totalHpy+asa*solventHpy
                    rHpy = totalHpy/solventHpy
                    print("%d %s %s %.3f %.3f %.3f %.3f"%(inp,residues[inp]['RES'],group,1-asa,hpy,totalHpy,rHpy))
                except:
                    print("Solvent contribution is not available for residue %d %s %s"%(inp,resName,group))


    inp = input("Enter -1 to exit or 0 to continue : ")
    inp = int(inp)
    if(inp < 0) : return
    else: calculateHpy(inputCrd)

###################################################################################

####################### MAIN Function ############################################
def crdHandler():
    inputCrd = input("Enter the name of crd file : ")
    try:
        chkFile = open(inputCrd,"r")
    except:
        print("Given Crd file doesn't exist in the same directory")
        crdHandler()
    readCrd(inputCrd)
    print("Total Number of Residues : %d"%len(residues))
    readRFnRadius('radiuscrd.dat')
    find_distances()
    calculateHpy(inputCrd)


for i in range(1,10):
    crdHandler()