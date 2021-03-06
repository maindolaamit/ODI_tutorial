# !bin/python
import os, sys, random, string, datetime
from shutil import rmtree

purge_dir_name = 'purge_testing'
purge_dir = os.path.join(os.getcwd(), purge_dir_name)
table_name = 'HR.XX_PURGE_DIRS'


def create_dirs_files():
    """This Function will create a Directory purge_testing and inside that 
    5 SubDirectories will be created with some files of various Timestamps
    the SubDirectories will have names like 'archive_[n]'

    """
    # create a main Directory, if not exists
    if not os.path.exists(purge_dir):
        os.mkdir(purge_dir)
    else:
        print 'Directory already exists : %s' % (purge_dir)

    # Loop to create SubDirectories
    for i in range(5):
        new_dir = os.path.join(purge_dir, 'archive_%d' % (i))
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
            # print 'Created Directory %s'%(new_dir)

        days_to_keep = random.randint(10, 20)  # Days to keep files from
        chars = string.ascii_lowercase  # all alphabets

        # print 'Sub Directory : %s' % (new_dir)
        # Create some random number files in the directory
        files_count = random.randint(10, 50)
        for j in range(files_count):
            new_file_name = ''.join(random.choice(chars) for i in range(10)) + '.dat'
            new_file_path = os.path.join(new_dir, new_file_name)
            if not os.path.exists(new_file_path):
                # Write in the File, random lines, random words
                fp = open(new_file_path, 'w')
                for k in range(random.randint(20, 100)):
                    fp.write(''.join(random.choice(chars) for x in range(100)) + '\n')
                fp.close()
                # Get the Random back Date
                epoch_date = datetime.datetime(1970, 1, 1)
                crdate = datetime.datetime.today() - datetime.timedelta(days=random.randint(5, 30))
                td = crdate - epoch_date
                os.utime(new_file_path, (td.total_seconds(), td.total_seconds()))

        # print 'Number of Files Created : %d' % (files_count)
        # print the Insert Statements
        print "INSERT INTO %s VALUES ('%s',%d,'Y',SYSDATE)\n" % (table_name, new_dir, days_to_keep)


def count_files():
    """ This function will show the count of files in each SubDirectories
    """
    if os.path.exists(purge_dir):
        for root, dirs, files in os.walk(purge_dir):
            if not root.endswith(purge_dir_name):
                print "%s : %d" % (root, len(files))
    else:
        print 'No such Directory : %s' % (purge_dir)


def files_stats():
    """This method will print the SubDirectories and files with their size, creation_date
    :returns: None

    """
    if os.path.exists(purge_dir):
        for root, dirs, files in os.walk(purge_dir):
            if not root.endswith(purge_dir_name):
                print '%s' % (root)
                print '%s %s %s' % ('File'.center(20), 'Size(KB)'.center(10), 'Creation Time'.center(15))
                print '-' * 50
                for k in files:
                    statinfo = os.stat(os.path.join(root, k))
                    size_kb = round(float(statinfo.st_size) / 1024, 2)
                    crdate = datetime.datetime.fromtimestamp(statinfo.st_mtime).strftime('%Y-%m-%d')
                    print '%s %s %s' % (k.rjust(20), str(size_kb).center(10), crdate.center(15))
                print ''
    else:
        print 'No such Directory : %s' % (purge_dir)


def delete_dirs():
    """This method will delete the purge_testing folder and all its SubDirectories
    :returns: TODO

    """
    # Delete tree if exists
    if os.path.exists(purge_dir):
        rmtree(purge_dir)
        print 'Directory deleted : %s' % (purge_dir)
    else:
        print 'No such Directory exists : %s' % (purge_dir)


valid_parameters = "CREATE, COUNT, DELETE, STATS"
if len(sys.argv) == 1 is None:
    print "Please pass either parameters  -" + valid_parameters
    exit(1)

mode = str(sys.argv[1]).upper()

if mode == 'CREATE':
    create_dirs_files()
elif mode == 'COUNT':
    count_files()
elif mode == 'DELETE':
    delete_dirs()
elif mode == 'STATS':
    files_stats()
else:
    print "Invalid parameter passed. Valid values are - " + valid_parameters
