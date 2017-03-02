__author__ ="Ruthvik Mandava"

import math
import constants2


lastAtom = 0
pdb_entries = {}
residues = {}
SGatoms = []
CysRes = {}
resABType = []
curResCount = 0
chain_res = {}
curResMap = {}
terminal_res = []
chain_start_res = []
XCor = [0 for i in range(1,10000)]
YCor = [0 for i in range(1,10000)]
ZCor = [0 for i in range(1,10000)]
rf_dictionary = {}
radius_dictionary = {}

global distance_matrix

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def readPdb(inputPdb):
    pdbfile = open(inputPdb,"r")
    global pdb_entries,XCor,YCor,ZCor,lastAtom, chain_res, curResCount, chain_start_res, SGatoms, CysRes, terminal_res
    for line in pdbfile:
        if(line[0:5].strip(' ') == 'ATOM'):
            res_no = (line[22:27].strip(' '))
            resName = line[17:20].strip(' ')
            resFlag = line[16:17]
            #print("%s %s"%(res_no,RepresentsInt(res_no)))
            if RepresentsInt(res_no) is False:
                continue
            res_no = int(res_no)
            chain = (line[21:22])

            if chain in chain_res:
                if res_no not in chain_res[chain].keys():
                    curResCount+=1
                chain_res[chain][res_no] = curResCount
            else:
                chain_res[chain] = {}
                curResCount+=1
                chain_res[chain][res_no] = curResCount
                chain_start_res.append(curResCount)
            if resFlag is not ' ':
                if curResCount not in resABType: resABType.append(curResCount)
            if curResCount not in curResMap:
                curResMap[curResCount] = {}
                curResMap[curResCount]['Chain'] = chain
                curResMap[curResCount]['Map'] = res_no

            atomNo = int(line[6:11].strip(' '))
            atomName = line[12:16].strip(' ')

            if atomName == 'OXT':
                    if curResCount not in terminal_res:
                        terminal_res.append(curResCount)

            SGFlag = 0
            if atomName == 'SG':
                SGatoms.append(atomNo)
                SGFlag = 1
            Xco = float(line[30:38].strip(' '))
            Yco = float(line[38:46].strip(' '))
            Zco = float(line[46:54].strip(' '))
            occupancy = float(line[54:60].strip(' '))
            pdb_entries[atomNo] = [res_no,resName,atomNo,atomName,Xco,Yco,Zco,occupancy]
            XCor[atomNo] = Xco
            YCor[atomNo] = Yco
            ZCor[atomNo] = Zco
            #print(pdbEntries[atomNo])
            if curResCount in residues:
                residues[curResCount]['atoms'].append(atomNo)
                lastAtom = atomNo
                if SGFlag:
                    CysRes[atomNo] = curResCount
            else:
                residues[curResCount] = {}
                residues[curResCount]['mapRes'] = curResCount
                residues[curResCount]['RESNo'] = res_no
                residues[curResCount]['atoms'] = []
                residues[curResCount]['RES'] = resName
                residues[curResCount]['atoms'].append(atomNo)
                if SGFlag:
                    CysRes[atomNo] = curResCount


    pdbfile.close()
    detectThioLinkage()


def detectThioLinkage():
    for one in SGatoms:
        for two in SGatoms:
            if one is not two:
                dist = getDistance(XCor[one],YCor[one],ZCor[one],XCor[two],YCor[two],ZCor[two])
                if dist < 2.5 :
                    SGatoms.remove(one)
                    SGatoms.remove(two)
                    residues[CysRes[one]]['RES'] = 'CY2'
                    residues[CysRes[two]]['RES'] = 'CY2'
                    pdb_entries[one][1] = 'CY2'
                    pdb_entries[two][1] = 'CY2'
                    break

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


def getDistance(x1,y1,z1,x2,y2,z2):
    x = (x1-x2)*(x1-x2)
    y = (y1-y2)*(y1-y2)
    z = (z1-z2)*(z1-z2)
    dist = x+y+z
    dist = math.sqrt(dist)
    return dist


def find_distances():
    global distance_matrix
    distance_matrix = [[0 for i in range(1,lastAtom+2)]for j in range(1,lastAtom+2)]
    for i in range(1,lastAtom+1):

        if XCor[i] == 0 and YCor[i]==0 and ZCor[i]==0:
            continue
        for j in range(i+1,lastAtom+1):
            if XCor[j] == 0:continue
            d = getDistance(XCor[i],YCor[i],ZCor[i],XCor[j],YCor[j],ZCor[j])
            distance_matrix[i][j] = d
            distance_matrix[j][i] = d

def getHpy(resno):
    atomsNeg = []
    resName = residues[resno]['RES']
    groups = constants2.GROUPS[resName]['G']
    resHpy = {}
    for group in groups:
        atomsList = []
        groupAtoms = constants2.GROUPS[resName][group]
        if resno in chain_start_res:
            groupAtoms.append('H1')
            groupAtoms.append('H2')
            groupAtoms.append('H3')
        elif resno in terminal_res:
            groupAtoms.append('OXT')
        for atmno in residues[resno]['atoms']:
            if pdb_entries[atmno][3] in groupAtoms:
                atomsList.append(atmno)
                atomsNeg.append(atmno)
        resHpy[group] = getGroupHpy(resno, resName, atomsList, group, residues[resno]['atoms'])
    '''
    exitFl = 0
    for atom in residues[resno]['atoms']:
        if atom not in atomsNeg:
            print("%d is neglected"%atom)
            exitFl = 1
    '''
    return resHpy

def getGroupHpy(resno, resname, atmList, group, resAtoms):
    hpy = 0
    for restAtom in pdb_entries:
        maxDB = 0
        atmNo = pdb_entries[restAtom][2]
        atmName = pdb_entries[restAtom][3]
        atmResName = pdb_entries[restAtom][1]
        if atmNo in resAtoms:
            continue
        try:
            rf = rf_dictionary[atmResName][atmName]
        except:
            if atmName in ['H1','H2','H3']:
                rf = 0
            elif atmName == 'OXT':
                rf = -0.65
            else : print("rf values not available for %s %s" %(atmResName,atmName))
        #print("%d  %s  %s %f"%(atmNo,atmName,atmResName,rf))
        for each in atmList:
            try:
                if pdb_entries[each][3] in ['H1','H2','H3']:
                    radius = 0.2245
                elif pdb_entries[each][3] == 'OXT':
                    radius = 1.7
                else: radius = radius_dictionary[resname][pdb_entries[each][3]]
                nR = radius+2.275
                eR = nR+0.2
                try:
                    distance = float(distance_matrix[atmNo][each])
                    if(distance <= nR):curDB = 1
                    elif distance >= eR: curDB = 0
                    else:
                        curDB = (((eR - distance)*(eR - distance))*(eR + (2*distance) - (3*nR)))/((eR-nR)*(eR-nR)*(eR-nR))
                    if(curDB > maxDB):
                        maxDB = curDB
                except:
                    print("Distance value not available atom %d and atom %d"%(each,atmNo))
            except:
                print("radius values not available for %s %s"%(resname,pdb_entries[each][3]))


        if maxDB:
            hpy = hpy + (maxDB*rf)
    return round(hpy,3)
    
def calculateHpy(inputPdb):
    inp = input('Enter Residue Number or Enter 0 to get Hpy for all Residues : ')
    inp = int(inp)
    if inp>curResCount:
        print("Input Protein doesn't have %d residue"%inp)
        calculateHpy(inputPdb)
    else:
         if(inp == 0):
             outFileName = input("Enter the output File name : ")
             fileOut = open(outFileName,"w")
             totalResC = len(residues)
             for i in range(1,totalResC+1):
                 resHpy = getHpy(i)
                 for group in constants2.GROUPS[residues[i]['RES']]['G']:
                    try:
                        hpy = resHpy[group]
                        #print("%d %s %s %.3f"%(inp,residues[i]['RES'],group,hpy))
                        fileOut.writelines("%s  %s  %d  %s  %.3f"%(residues[i]['RES'],curResMap[i]['Chain'],curResMap[i]['Map'],group,hpy))
                        fileOut.writelines("\n")
                    except:
                        print("Exception occurred calculating Hpy for %d %s %s"%(i,residues[i]['RES'],group))
             return
         else:
            print("Given Residue Number : %d"%inp)
            for each in chain_res:
                if inp in chain_res[each]:
                    resNo = chain_res[each][inp]
                    print("Chain : %s "%(each))
                    print("Residue name : %s"%residues[resNo]['RES'])
                    resHpy = getHpy(resNo)
                    for group in constants2.GROUPS[residues[resNo]['RES']]['G']:
                       try:
                           hpy = resHpy[group]
                           print("%d %s %s %.3f"%(inp,residues[resNo]['RES'],group,hpy))
                       except:
                           print("Exception occurred calculating Hpy for %d %s %s"%(inp,residues[inp]['RES'],group))
    inp = input("Enter -1 to exit or 0 to continue : ")
    inp = int(inp)
    if(inp < 0) : return
    else: calculateHpy(inputPdb)
    return

def removeRedundantAtoms():
    removedAtoms = []
    for each in resABType:
        atmList = residues[each]['atoms']
        for atom in atmList:
            for tempAtom in atmList:
                if tempAtom is not atom:
                    if pdb_entries[atom][3] == pdb_entries[tempAtom][3]:
                        oc1 = pdb_entries[atom][7]
                        oc2 = pdb_entries[tempAtom][7]
                        if oc1 >= oc2:
                            residues[each]['atoms'].remove(tempAtom)
                            removedAtoms.append(tempAtom)
                        else:
                            residues[each]['atoms'].remove(atom)
                            removedAtoms.append(atom)
    for each in removedAtoms:
        del pdb_entries[each]

def pdbHandler():

    inputPdb = input("Enter the name of pdb file : ")
    try:
        chkFile = open(inputPdb,"r")
        chkFile.close()
    except:
        print("Given Pdb file doesn't exist in the same directory")
        pdbHandler()
    try:
        readRFnRadius('radiuspdb.dat')
    except:
        print("Radius.dat file is not in this directory")
    try:
        readPdb(inputPdb)
        print("Total Number of residues : %d"%len(residues))
    except:
        print("Exception occurred reading the pdb file")
    try:
        removeRedundantAtoms()
    except:
        print("Exception occurred during removing reduntant atoms for A or B chain of same residue")
    try:
        find_distances()
    except:
        print("Exception occurred finding the distance between every pair of atoms")
    try:
        calculateHpy(inputPdb)
    except:
        print("Exception occurred calculating Hpy")

