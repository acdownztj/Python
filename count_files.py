#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, sys


def countFiles(path):
    '''This shell is used to count files and directories under "path" '''
    a = os.walk(path)
    file_list = []
    dir_list = []
    for root, dirs, files in a:
        for each in files:
            file_list.append(each)
        for each in dirs:
            dir_list.append(each)
    file_counts = len(file_list)
    dir_counts = len(dir_list)
    result = {'files':str(file_counts),'dirs':str(dir_counts),'total':str(file_counts + dir_counts)}
    return result

def countSingleDir(path):
    if os.path.isdir(path):
        path_ret = countFiles(path)
	print '**Path: ' + os.path.abspath(path)
	print '**Files: ' + path_ret['files']
	print '**Dirs: ' + path_ret['dirs']
	print '**Total: ' + path_ret['total']
    else:
        print path + ' is not a direcotry!'
	
	return True

def countDirs(path1,path2):
    if os.path.isdir(path1):
        path1_ret = countFiles(path1)
    else:
        print path1 + ' is not a direcotry!'
			
    if os.path.isdir(path2):
        path2_ret = countFiles(path2)
	    print 'Path: ' + os.path.abspath(path_name1) + '\t|\t' + os.path.abspath(path_name2)
        print '**Files: ' + path1_ret['files'] + '\t|\t' + path2_ret['files']
        print '**Dirs: ' + path1_ret['dirs'] + '\t\t|\t' + path2_ret['dirs']
        print '**Total: ' + path1_ret['total'] + '\t|\t' + path2_ret['total']
		if int(path1_ret['total']) == int(path2_ret['total']):
		    print '** Same！'
		else: print '** Different!'
    else:
        print path2 + ' is not a direcotry!'
	
	return True
	
	
if __name__ == '__main__':
    try:
	dir_count = len(sys.argv)
	if dir_count == 2:
            path_name1 = sys.argv[1]
            countSingleDir(path_name1)
        elif dir_count == 3:
            path_name1 = sys.argv[1]
            path_name2 = sys.argv[2]
            countDirs(path_name1,path_name2)
	else:
            print 'Example: \n1)python2.6 count_files.py /tmp/\n2)python2.6 count_files.py /tmp/vmware-root/ /tmp/vmware-root-bak/'
            
    except IndexError, e:
        print e
        print 'please input a direcotry after shell as a argument!'
        print 'Example: \n1)python2.6 count_files.py /tmp/\n2)python2.6 count_files.py /tmp/vmware-root/ /tmp/vmware-root-bak/'
