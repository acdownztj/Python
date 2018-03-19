#!/usr/bin/python
# -*- coding:utf-8 -*-
# Date: 2018-03-19

# 此文件用于显示目录下文件数和目录数，对比两目录下文件数和目录数 

import os, sys

def countFiles(path):
    '''此方法用于计算目录文件数，并以字典方式返回结果'''
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
    '''打印单一目录下的计算结果'''
    if os.path.isdir(path):
        path_ret = countFiles(path)
	print '**Path: ' + os.path.abspath(path)
	print '**Files: ' + path_ret['files']
	print '**Dirs: ' + path_ret['dirs']
	print '**Total: ' + path_ret['total']
    else:
        print path + ' is not a direcotry!'
	return False
    return True

def countDirs(path1,path2):
    '''打印连个目录对比的计算结果'''
    if os.path.isdir(path1):
        path1_ret = countFiles(path1)
    else:
        print path1 + ' is not a direcotry! Please input a direcotry.'
	return False
			
    if os.path.isdir(path2):
        path2_ret = countFiles(path2)
	print '**Path: ' + os.path.abspath(path_name1) + '\t|\t' + os.path.abspath(path_name2)
        print '**Files: ' + path1_ret['files'] + '\t|\t' + path2_ret['files']
        print '**Dirs: ' + path1_ret['dirs'] + '\t|\t' + path2_ret['dirs']
        print '**Total: ' + path1_ret['total'] + '\t|\t' + path2_ret['total']
   
        if int(path1_ret['total']) == int(path2_ret['total']):
            print '**  Same!'   # 如果文件和目录总数一致，返回 Same！
        else:
            print '**  Different!'   # 如果文件和目录总数不一致，返回 Different！
    else:
        print path2 + u' is not a direcotry! Please input a direcotry.'
	return False
    return True
	
def printErr:
    print 'Useage: python2.6 /file/path/count_files.py path1 [path2]\n'
    print 'Example: \n1)python2.6 count_files.py /tmp/\n2)python2.6 count_files.py /tmp/vmware-root/ /tmp/vmware-root-bak/\n'

if __name__ == '__main__':
    try:
	num_of_args = len(sys.argv)
	if num_of_args == 2:    # 接受一个路径参数
            path_name1 = sys.argv[1]
            countSingleDir(path_name1)
        elif num_of_args == 3:  # 接受两个路径参数
        path_name1 = sys.argv[1]
            path_name2 = sys.argv[2]
            countDirs(path_name1,path_name2)
	else:
            printErr()
            
    except IndexError, e:
        print e
        printErr()
