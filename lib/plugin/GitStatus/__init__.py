
from lib.PluginBase import PluginBase

import subprocess, re

class GitStatus(PluginBase):
    '''Useful git status info if cwd is a repo'''
    def __init__(self):
        self.nameslug = 'gitstatus'

    def getItermData(self):
        giticon = ''
        cmdout = subprocess.run(["git", "status", "-s", "-b", "--porcelain"], capture_output=True, text = True)
        if cmdout.returncode != 0:
            return None

        newfile_ct = 0
        indexchange_ct = 0
        workingtree_ct = 0
        unknownfile_ct = 0
        index_str = ''
        working_str = ''
        unknown_str = ''
        branch_str = ''
        ahead_ct = 0
        behind_ct = 0
        ahead_str = ''
        behind_str = ''

        stdoutlines = cmdout.stdout.splitlines(False)
        firstline = stdoutlines.pop(0)

        if '(no branch)' in firstline:
            branch_str = '(no branch)'
        elif 'No commits yet on ' in firstline[3:]:
            branch_str = firstline[21:]
        else:
            # TODO need better regex
            m1 = re.search('^## ([A-Za-z][A-Za-z/]*)', firstline)
            if m1 is not None:
                branch_str = m1.group(1)
            else:
                raise Exception("Assert: Bad regex")

        ahead_match = re.search('ahead ([1-9][0-9]*)', firstline)
        if ahead_match is not None:
            ahead_ct = int(ahead_match.group(1))
        behind_match = re.search('behind ([1-9][0-9]*)', firstline)
        if behind_match is not None:
            behind_ct = int(behind_match.group(1))

        # we did the first line, now the rest
        for line in stdoutlines:
            if line[0:1] == 'A' or line[1:1] == 'A':
                newfile_ct += 1
            elif line[0:1] in 'CDTMRU':
                indexchange_ct += 1
            elif line[1:2] in 'CDTMRU':
                workingtree_ct += 1
            elif line[0:2] == '??':
                unknownfile_ct += 1

        newfile_str = ''
        if newfile_ct > 0:
            newfile_str = f'  {newfile_ct}'
        if indexchange_ct > 0:
            index_str = f'  {indexchange_ct}'
        if workingtree_ct > 0:
            working_str = f'  {workingtree_ct}'
        if unknownfile_ct > 0:
            unknown_str = f' 󱀶 {unknownfile_ct}'
        if ahead_ct > 0:
            ahead_str = f' 󰁞{ahead_ct}'
        if behind_ct > 0:
            behind_str = f' 󰁆{behind_ct}'

        return ''.join([f'{giticon} {branch_str}',
                        f'{index_str}{working_str}',
                        f'{newfile_str}{unknown_str}',
                        f'{ahead_str}{behind_str}'])


def getPlugin():
    return GitStatus()