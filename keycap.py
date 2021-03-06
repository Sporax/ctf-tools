#!/usr/bin/python

import sys,pandas

if len(sys.argv) < 2:
    print('Usage: python keycap.py [file]')
    exit(0)

input_file=sys.argv[1]
f = open(input_file).read().split('\n')[:-1]

keymap = {'04':'a','05':'b','06':'c','07':'d','08':'e','09':'f','0A':'g','0B':'h','0C':'i','0D':'j','0E':'k','0F':'l','10':'m','11':'n','12':'o','13':'p','14':'q','15':'r','16':'s','17':'t','18':'u','19':'v','1A':'w','1B':'x','1C':'y','1D':'z','1E':'1','1F':'2','20':'3','21':'4','22':'5','23':'6','24':'7','25':'8','26':'9','27':'0','28':'\n\r','29':'[esc]','2A':'[del]','2B':'\t','2C':' ','2D':'-', '2E':'=','2F':'[','30':']','31':'\\','32':'#','33':';','34':'\'','35':'`','36':',','37':'.','38':'/','39':'[caps]','3A':'[f1]','3B':'[f2]','3C':'[f3]','3D':'[f4]','3E':'[f5]','3F':'[f6]','40':'[f7]','41':'[f8]','42':'[f9]','43':'[f10]','44':'[f11]','45':'[f12]','46':'[prntscrn]','47':'[scrllck]','48':'[pause]','49':'[ins]','4A':'[home]','4B':'[pgup]','4C':'[del]','4D':'[end]','4E':'[pgdn]','4F':'[right]','50':'[left]','51':'[down]','52':'[up]'}
keymap_shift = {'04':'A','05':'B','06':'C','07':'D','08':'E','09':'F','0A':'G','0B':'H','0C':'I','0D':'J','0E':'K','0F':'L','10':'M','11':'N','12':'O','13':'P','14':'Q','15':'R','16':'S','17':'T','18':'U','19':'V','1A':'W','1B':'X','1C':'Y','1D':'Z','1E':'!','1F':'@','20':'#','21':'$','22':'%','23':'^','24':'&','25':'*','26':'(','27':')','28':'\n\r','29':'[esc]','2A':'[del]','2B':'\t','2C':' ','2D':'_', '2E':'+','2F':'{','30':'}','31':'|','32':'~','33':':','34':'"','35':'~','36':'<','37':'>','38':'?','39':'[caps]','3A':'[f1]','3B':'[f2]','3C':'[f3]','3D':'[f4]','3E':'[f5]','3F':'[f6]','40':'[f7]','41':'[f8]','42':'[f9]','43':'[f10]','44':'[f11]','45':'[f12]','46':'[prntscrn]','47':'[scrllck]','48':'[pause]','49':'[ins]','4A':'[home]','4B':'[pgup]','4C':'[del]','4D':'[end]','4E':'[pgdn]','4F':'[right]','50':'[left]','51':'[down]','52':'[up]'}
 
result = ['']
row = 0
#print(f)
for e in f:
    m = e[4:6].upper()
    i = e[:2]
    if m in keymap:
        if m == '28':
            result.append('')
            row += 1
        elif m == '51':
            row += 1
        elif m == '52':
            row -= 1
        elif i == '02':
            result[row] += keymap_shift[m]
        else:
            result[row] += keymap[m]

print(result)
