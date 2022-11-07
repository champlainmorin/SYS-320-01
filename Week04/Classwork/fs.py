# File to traverse a given directory and it's subdirs and retrieve all the files
import os, sys, argparse

# parser
parser = argparse.ArgumentParser(

    description="Traverse a directory and builds on forensic body file",
    epilog="Developed by Maxwell Berry, 20220925"

)

# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")

# Parse the arguments
args = parser.parse_args()

rootdir = args.directory

# Get information from the commandline
# print(sys.argv)

# Directory to traverse
#rootdir = sys.argv[1]

# print(rootdir)

# In our Story, we will traverse a directory

# Check if the arguement is a directory
if not os.path.isdir(rootdir):
    print("Invalid directory => {}".format(rootdir))
    exit()

# List to save files
flist = []

# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):

    for f in filenames:

        #print(root + "/" + f)
        filelist = root + "/" + f
        #print(filelist)
        flist.append(filelist)

#print(flist)

def statFile(toStat):

    # i is going to be the variable used for each of the metadata elements
    i = os.stat(toStat,follow_symlinks=False)


    # mode
    mode = i[0]
    # inode
    inode=i[i]
    # uid
    uid = i[4]
    # gid
    gid = i[5]
    # file size 
    fsize = i[6]
    # access time
    atime = i[7]
    # modification time
    mtime = i[8]
    # ctime => windows is the birth of the file, when it was created
    # unix it is when attributes of the file changes.
    ctime = i[9]
    crtime = i[9]

    print("0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(toStat, inode, mode, uid, gid, fsize, atime, mtime, ctime,crtime))

for eachfile in flist:

    statFile(eachfile)