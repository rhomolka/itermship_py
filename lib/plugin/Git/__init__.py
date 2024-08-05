
import subprocess

giticon = ''
def getItermData():
    cmdout = subprocess.run(["git", "status", "-s", "-b", "--porcelain"], capture_output=True, text = True)
    if cmdout.returncode != 0:
        return ['git', '']
    
    newfile = 0
    indexchange = 0
    workingtree = 0
    indexstring = ''
    workingstring = ''
    branch = ''
    aheadstring = ''
    behindstring = ''
    for line in cmdout.stdout.splitlines(False):
        if line[0:2] == '##':
            if '(no branch)' in line:
                branch = '(no branch)'
            elif 'No commits yet on ' in line[3:]:
                branch = line[21:]
            else:
                restofline = line[3:]
                aheadblock = ''
                
                try:
                    aheadindex = restofline.index('[')
                except:
                    pass
                else:
                    aheadblock = restofline[aheadindex:]
                    restofline = restofline[0:aheadindex - 1]
                
                try:
                    index = restofline.index('.')
                except:
                    pass
                else:
                    # we don't care about remote branch, yet
                    restofline = restofline[0:index]
                branch = restofline
        elif line[0:1] in 'ACDTMRU':
            indexchange += 1
        elif line[1:2] in 'ACDTMRU':
            workingtree += 1
        elif line[0:2] == '??':
            newfile += 1
        

    newfilestring = ''
    if newfile > 0:
        newfilestring = f' 󰝒 {newfile}'
    if indexchange > 0:
        indexstring = f'  {indexchange}'
    if workingtree > 0:
        workingstring = f'  {workingtree}'
            
    return ["git",f"{giticon} {branch}{indexstring}{workingstring}{newfilestring}{aheadstring}{behindstring}"]