
"A host of commands to integrate github with houdini"

import os
import hou

print "loading hougit"

def gitAdd(filepath):

    cmd = "git add {}".format(filepath)
    print cmd
    os.system(cmd)

def gitCommit():

    success, msg = hou.ui.readInput("Commit message", buttons=('OK',))
    print success, msg
    if (success == 0) and (len(msg) > 0):
        print "Commiting"
        cmd = "git commit -m {}".format("\""+ msg + "\"")
        os.system(cmd)

def gitCommitOTL(node):

    gitAdd(node.type().definition().libraryFilePath())
    success, msg = hou.ui.readInput("Commit message", buttons=('OK',))
    print success, msg
    if (success == 0) and (len(msg) > 0):
        print "Commiting"
        cmd = "git commit -m {}".format("\""+ msg + "\"")
        os.system(cmd)

def gitPush():

    cmd = "git push"
    os.system(cmd)

def gitInit():
    pass

def gitLogin():
    pass