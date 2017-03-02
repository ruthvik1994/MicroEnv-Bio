__author__ = 'ruthvik1994'
import CrdHandler
import PdbHandler

def main():

    inp = input("Enter crd or pdb : ")
    if inp == 'crd':
        try:
            chk = open("radiuscrd.dat","r")
            chk.close()
            CrdHandler.crdHandler()
        except:
            print("File name radiuscrd.dat is not found")
            return
    elif inp == 'pdb':
        try:
            chk = open("radiuspdb.dat","r")
            chk.close()
            PdbHandler.pdbHandler()
        except:
            print("File name radiuspdb.dat is not found")
            return
    else :
        print("Unknown file format")
        main()
main()