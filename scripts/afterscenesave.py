import subprocess
import os

print "Attempting add {}".format(kwargs['file'])


# Only run the command if the save succeeded and it's
# not an autosave
if kwargs["success"] and not kwargs["autosave"]:
    # Pass the scene file path to the git command
    print "Adding file to git"
    cmd = "git add {}".format(kwargs['file'])
    os.system(cmd)