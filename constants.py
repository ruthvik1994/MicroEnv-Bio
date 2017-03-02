GROUPS = {}

GROUPS['ARG'] = {}
GROUPS['ARG']['G'] = ['AM', 'HP', 'GS', 'CM']
GROUPS['ARG']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['ARG']['HP'] = ['CB', 'HB1', 'HB2', 'CG', 'HG1', 'HG2']
GROUPS['ARG']['GS'] = ['CD', 'HD1', 'HD2', 'NE', 'HE', 'CZ', 'NH1', 'HH11', 'HH12', 'NH2', 'HH21', 'HH22']
GROUPS['ARG']['CM'] = ['C', 'O']

GROUPS['CYS'] = {}
GROUPS['CYS']['G'] = ['AM', 'TO', 'CM']
GROUPS['CYS']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['CYS']['TO'] = ['CB', 'HB1', 'HB2', 'SG', 'HG1']
GROUPS['CYS']['CM'] = ['C', 'O']

GROUPS['CY2'] = {}
GROUPS['CY2']['G'] = ['AM', 'TD', 'CM']
GROUPS['CY2']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['CY2']['TD'] = ['CB', 'HB1', 'HB2', 'SG', 'HG1']
GROUPS['CY2']['CM'] = ['C', 'O']

GROUPS['GLN'] = {}
GROUPS['GLN']['G'] = ['AM', 'HP', 'AD', 'CM']
GROUPS['GLN']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['GLN']['HP'] = ['CB', 'HB1', 'HB2']
GROUPS['GLN']['AD'] = ['CG', 'HG1', 'HG2', 'CD', 'OE1', 'NE2', 'HE21', 'HE22']
GROUPS['GLN']['CM'] = ['C', 'O']

GROUPS['MET'] = {}
GROUPS['MET']['G'] = ['AM', 'HP', 'TE', 'CM']
GROUPS['MET']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['MET']['HP'] = ['CB', 'HB1', 'HB2']
GROUPS['MET']['TE'] = ['CG', 'HG1', 'HG2', 'SD', 'CE', 'HE1', 'HE2', 'HE3']
GROUPS['MET']['CM'] = ['C', 'O']

GROUPS['TRP'] = {}
GROUPS['TRP']['G'] = ['AM', 'HP', 'RS', 'RS1', 'CM']
GROUPS['TRP']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['TRP']['HP'] = ['CB', 'HB1', 'HB2']
GROUPS['TRP']['RS'] = ['CG', 'CD2', 'CD1', 'HD1', 'NE1', 'HE1', 'CE2']
GROUPS['TRP']['RS1'] = ['CE3', 'HE3', 'CZ2', 'HZ2', 'CZ3', 'HZ3', 'CH2', 'HH2']
GROUPS['TRP']['CM'] = ['C', 'O']

GROUPS['ALY'] = {}
GROUPS['ALY']['G'] = ['AM', 'HP', 'AS', 'CM', 'HP']
GROUPS['ALY']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['ALY']['HP'] = ['CB', 'HB1', 'HB2', 'CG', 'HG1', 'HG2', 'CD', 'HD1', 'HD2']
GROUPS['ALY']['AS'] = ['CE', 'HE1', 'HE2', 'NZ', 'HZ', 'CL', 'OL']
GROUPS['ALY']['HP1'] = ['CLY', 'HL1', 'HL2', 'HL3']
GROUPS['ALY']['CM'] = ['C', 'O']

GROUPS['PRO'] = {}
GROUPS['PRO']['G'] = ['AP', 'HP', 'CM']
GROUPS['PRO']['AP'] = ['N', 'CA', 'HA', 'CD', 'HD1', 'HD2']
GROUPS['PRO']['HP'] = ['CB', 'HB1', 'HB2', 'CG', 'HG1', 'HG2']
GROUPS['PRO']['CM'] = ['C', 'O']

GROUPS['ILE'] = {}
GROUPS['ILE']['G'] = ['AM', 'HP', 'CM']
GROUPS['ILE']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['ILE']['HP'] = ['CB', 'HB', 'CG2', 'HG21', 'HG22', 'HG23', 'CG1', 'HG11', 'HG12', 'CD', 'CD1', 'HD1', 'HD2',
                       'HD3']
GROUPS['ILE']['CM'] = ['C', 'O']

GROUPS['TYR'] = {}
GROUPS['TYR']['G'] = ['AM', 'HP', 'RS', 'PH', 'CM']
GROUPS['TYR']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['TYR']['HP'] = ['CB', 'HB1', 'HB2']
GROUPS['TYR']['RS'] = ['CG', 'CD1', 'HD1', 'CD2', 'HD2', 'CE1', 'HE1', 'CE2', 'HE2']
GROUPS['TYR']['PH'] = ['CZ', 'OH', 'HH']
GROUPS['TYR']['CM'] = ['C', 'O']

GROUPS['GLY'] = {}
GROUPS['GLY']['G'] = ['AM', 'CM']
GROUPS['GLY']['AM'] = ['N', 'HN', 'CA', 'HA1', 'HA2']
GROUPS['GLY']['CM'] = ['C', 'O']

GROUPS['VAL'] = {}
GROUPS['VAL']['G'] = ['AM', 'HP', 'CM']
GROUPS['VAL']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['VAL']['HP'] = ['CB', 'HB', 'CG1', 'HG11', 'HG12', 'HG13', 'CG2', 'HG21', 'HG22', 'HG23']
GROUPS['VAL']['CM'] = ['C', 'O']

GROUPS['LYS'] = {}
GROUPS['LYS']['G'] = ['AM', 'HP', 'AS', 'CM']
GROUPS['LYS']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['LYS']['HP'] = ['CB', 'HB1', 'HB2', 'CG', 'HG1', 'HG2', 'CD', 'HD1', 'HD2']
GROUPS['LYS']['AS'] = ['CE', 'HE1', 'HE2', 'NZ', 'HZ1', 'HZ2', 'HZ3']
GROUPS['LYS']['CM'] = ['C', 'O']

GROUPS['HIS'] = {}
GROUPS['HIS']['G'] = ['AM', 'HS', 'CM']
GROUPS['HIS']['AM'] = ['N', 'HA', 'CA']
GROUPS['HIS']['HS'] = ['CB', 'CG', 'CD2', 'ND1', 'CE1', 'NE2']
GROUPS['HIS']['CM'] = ['C', 'O']

GROUPS['HSE'] = {}
GROUPS['HSE']['G'] = ['AM', 'HS', 'CM']
GROUPS['HSE']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['HSE']['HS'] = ['NE2', 'HE2', 'CD2', 'HD2', 'ND1', 'CG', 'CE1', 'HE1', 'CB', 'HB1', 'HB2']
GROUPS['HSE']['CM'] = ['C', 'O']

GROUPS['HSD'] = {}
GROUPS['HSD']['G'] = ['AM', 'HS', 'CM']
GROUPS['HSD']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['HSD']['HS'] = ['ND1', 'HD1', 'CG', 'CB', 'HB1', 'HB2', 'NE2', 'CD2', 'HD2', 'CE1', 'HE1']
GROUPS['HSD']['CM'] = ['C', 'O']

GROUPS['GLU'] = {}
GROUPS['GLU']['G'] = ['AM', 'HP', 'CO', 'CM']
GROUPS['GLU']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['GLU']['HP'] = ['CB', 'HB1', 'HB2']
GROUPS['GLU']['CO'] = ['CG', 'HG1', 'HG2', 'CD', 'OE1', 'OE2']
GROUPS['GLU']['CM'] = ['C', 'O']

GROUPS['ASP'] = {}
GROUPS['ASP']['G'] = ['AM', 'CO', 'CM']
GROUPS['ASP']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['ASP']['CO'] = ['CB', 'HB1', 'HB2', 'CG', 'OD1', 'OD2']
GROUPS['ASP']['CM'] = ['C', 'O']

GROUPS['SER'] = {}
GROUPS['SER']['G'] = ['AM', 'OL', 'CM']
GROUPS['SER']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['SER']['OL'] = ['CB', 'HB1', 'HB2', 'OG', 'HG1']
GROUPS['SER']['CM'] = ['C', 'O']

GROUPS['THR'] = {}
GROUPS['THR']['G'] = ['AM', 'OL', 'HP', 'CM']
GROUPS['THR']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['THR']['OL'] = ['CB', 'HB', 'OG1', 'HG1']
GROUPS['THR']['HP'] = ['CG2', 'HG21', 'HG22', 'HG23']
GROUPS['THR']['CM'] = ['C', 'O']

GROUPS['ALA'] = {}
GROUPS['ALA']['G'] = ['AM', 'HP', 'CM']
GROUPS['ALA']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['ALA']['HP'] = ['CB', 'HB1', 'HB2', 'HB3']
GROUPS['ALA']['CM'] = ['C', 'O']

GROUPS['LEU'] = {}
GROUPS['LEU']['G'] = ['AM', 'HP', 'CM']
GROUPS['LEU']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['LEU']['HP'] = ['CB', 'HB1', 'HB2', 'CG', 'HG', 'CD1', 'HD11', 'HD12', 'HD13', 'CD2', 'HD21', 'HD22', 'HD23']
GROUPS['LEU']['CM'] = ['C', 'O']

GROUPS['ASN'] = {}
GROUPS['ASN']['G'] = ['AM', 'AD', 'CM']
GROUPS['ASN']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['ASN']['AD'] = ['CB', 'HB1', 'HB2', 'CG', 'OD1', 'ND2', 'HD21', 'HD22']
GROUPS['ASN']['CM'] = ['C', 'O']

GROUPS['PHE'] = {}
GROUPS['PHE']['G'] = ['AM', 'HP', 'RS', 'CM']
GROUPS['PHE']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['PHE']['HP'] = ['CB', 'HB1', 'HB2']
GROUPS['PHE']['RS'] = ['CG', 'CD1', 'HD1', 'CD2', 'HD2', 'CE1', 'HE1', 'CE2', 'HE2', 'CZ', 'HZ']
GROUPS['PHE']['CM'] = ['C', 'O']

GROUPS['HSP'] = {}
GROUPS['HSP']['G'] = ['AM', 'HS', 'CM']
GROUPS['HSP']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['HSP']['HS'] = ['ND1', 'HD1', 'NE2', 'HE2', 'CE1', 'HE1', 'CD2', 'HD2', 'CG', 'CB', 'HB1', 'HB2']
GROUPS['HSP']['CM'] = ['C', 'O']

GROUPS['HSC'] = {}
GROUPS['HSC']['G'] = ['AM', 'HS', 'CM']
GROUPS['HSC']['AM'] = ['N', 'HN', 'CA', 'HA']
GROUPS['HSC']['HS'] = ['ND1', 'HD1', 'NE2', 'HE2', 'CE1', 'HE1', 'CD2', 'HD2', 'CG', 'CB', 'HB1', 'HB2']
GROUPS['HSC']['CM'] = ['C', 'O']



GROUPS['NTER'] = ['HT1', 'N', 'HT2', 'HT3', 'CA', 'HA']
GROUPS['CTER'] = ['C', 'OT1', 'OT2']


SOLVENTHPY = {}

SOLVENTHPY['HIS'] = {}
SOLVENTHPY['HIS']['AM'] = -10.923
SOLVENTHPY['HIS']['CM'] = -6.765
SOLVENTHPY['HIS']['HS'] = -27.219

SOLVENTHPY['GLU'] = {}
SOLVENTHPY['GLU']['AM'] = -10.391
SOLVENTHPY['GLU']['CM'] = -7.749
SOLVENTHPY['GLU']['HP'] = -8.807
SOLVENTHPY['GLU']['CO'] = -16.590

SOLVENTHPY['ASP'] = {}
SOLVENTHPY['ASP']['AM'] = -9.474
SOLVENTHPY['ASP']['CM'] = -6.230
SOLVENTHPY['ASP']['CO'] = -16.590

SOLVENTHPY['TYR'] = {}
SOLVENTHPY['TYR']['AM'] = -9.241
SOLVENTHPY['TYR']['CM'] = -7.216
SOLVENTHPY['TYR']['HP'] = -8.682
SOLVENTHPY['TYR']['RS'] = -21.232
SOLVENTHPY['TYR']['PH'] = -8.127

SOLVENTHPY['LYS'] = {}
SOLVENTHPY['LYS']['AM'] = -9.7
SOLVENTHPY['LYS']['CM'] = -7.046
SOLVENTHPY['LYS']['HP'] = -19.929
SOLVENTHPY['LYS']['AS'] = -19.400

SOLVENTHPY['ARG'] = {}
SOLVENTHPY['ARG']['AM'] = -10.682
SOLVENTHPY['ARG']['CM'] = -7.179
SOLVENTHPY['ARG']['HP'] = -15.418
SOLVENTHPY['ARG']['GS'] = -28.486

SOLVENTHPY['SER'] = {}
SOLVENTHPY['SER']['AM'] = -11.245
SOLVENTHPY['SER']['CM'] = -7.704
SOLVENTHPY['SER']['OL'] = -15.061

SOLVENTHPY['THR'] = {}
SOLVENTHPY['THR']['AM'] = -8.858
SOLVENTHPY['THR']['CM'] = -8.350
SOLVENTHPY['THR']['OL'] = -13.125
SOLVENTHPY['THR']['HP'] = -12.781

SOLVENTHPY['CYS'] = {}
SOLVENTHPY['CYS']['AM'] = -9.188
SOLVENTHPY['CYS']['CM'] = -7.969
SOLVENTHPY['CYS']['TO'] = -17.109

SOLVENTHPY['CY2'] = {}
SOLVENTHPY['CY2']['AM'] = -9.188
SOLVENTHPY['CY2']['CM'] = -7.969
SOLVENTHPY['CY2']['TD'] = -17.109

SOLVENTHPY['GLY'] = {}
SOLVENTHPY['GLY']['AM'] = -14.249
SOLVENTHPY['GLY']['CM'] = -9.317

SOLVENTHPY['ALA'] = {}
SOLVENTHPY['ALA']['AM'] = -10.514
SOLVENTHPY['ALA']['CM'] = -7.706
SOLVENTHPY['ALA']['HP'] = -13.516

SOLVENTHPY['LEU'] = {}
SOLVENTHPY['LEU']['AM'] = -9.238
SOLVENTHPY['LEU']['CM'] = -6.639
SOLVENTHPY['LEU']['HP'] = -24.912

SOLVENTHPY['ILE'] = {}
SOLVENTHPY['ILE']['AM'] = -8.051
SOLVENTHPY['ILE']['CM'] = -6.111
SOLVENTHPY['ILE']['HP'] = -26.398

SOLVENTHPY['VAL'] = {}
SOLVENTHPY['VAL']['AM'] = -10.181
SOLVENTHPY['VAL']['CM'] = -7.60
SOLVENTHPY['VAL']['HP'] = -22.463

SOLVENTHPY['TRP'] = {}
SOLVENTHPY['TRP']['AM'] = -8.314
SOLVENTHPY['TRP']['CM'] = -6.228
SOLVENTHPY['TRP']['HP'] = -8.689
SOLVENTHPY['TRP']['RS'] = -14.066
SOLVENTHPY['TRP']['RS1'] = -20.066

SOLVENTHPY['GLN'] = {}
SOLVENTHPY['GLN']['AM'] = -9.076
SOLVENTHPY['GLN']['CM'] = -7.739
SOLVENTHPY['GLN']['HP'] = -9.026
SOLVENTHPY['GLN']['AD'] = -19.416

SOLVENTHPY['ASN'] = {}
SOLVENTHPY['ASN']['AM'] = -9.971
SOLVENTHPY['ASN']['CM'] = -7.450
SOLVENTHPY['ASN']['AD'] = -20.634

SOLVENTHPY['PHE'] = {}
SOLVENTHPY['PHE']['AM'] = -9.931
SOLVENTHPY['PHE']['CM'] = -7.305
SOLVENTHPY['PHE']['HP'] = -8.342
SOLVENTHPY['PHE']['RS'] = -24.399

SOLVENTHPY['PRO'] = {}
SOLVENTHPY['PRO']['AP'] = -15.178
SOLVENTHPY['PRO']['CM'] = -7.725
SOLVENTHPY['PRO']['HP'] = -16.136

SOLVENTHPY['MET'] = {}
SOLVENTHPY['MET']['AM'] = -10.942
SOLVENTHPY['MET']['CM'] = -8.552
SOLVENTHPY['MET']['HP'] = -8.769
SOLVENTHPY['MET']['TE'] = -20.739

SOLVENTHPY['ALY'] = {}
SOLVENTHPY['ALY']['AM'] = -9.700
SOLVENTHPY['ALY']['CM'] = -7.046
SOLVENTHPY['ALY']['HP'] = -19.929
SOLVENTHPY['ALY']['AS'] = -19.400
SOLVENTHPY['ALY']['HP1'] = -13.516

SOLVENTHPY['HSP'] = {}
SOLVENTHPY['HSP']['AM'] = -10.923
SOLVENTHPY['HSP']['CM'] = -6.765
SOLVENTHPY['HSP']['HS'] = -27.219