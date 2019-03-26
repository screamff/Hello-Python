#! python3
# coding:utf-8
import os

# 备份游戏存档
# 1.读取原文件内容
# 2.创建备份文件夹，copy原文件
# 3.rollback功能

def backup(file):
    """file为存档文件路径"""
    try:
        with open(file, 'rb') as f:
            save = f.read()
    except FileNotFoundError:
        print("文件不存在")
    except Exception as e:
        print(e)
    else:
        filename = os.path.basename(file)
        p_filepath = os.path.dirname(file)
        backup_file = p_filepath + '\\backup\\' + filename
        if os.path.exists(p_filepath+'\\backup'):
            pass
        else:
            os.mkdir(p_filepath+'\\backup')
        with open(backup_file, 'wb+') as a:
            a.write(save)

def rollback(file):
    filename = os.path.basename(file)
    p_filepath = os.path.dirname(file)
    backup_file = p_filepath + '\\backup\\' + filename
    try:
        with open(backup_file, 'rb') as f:
            save = f.read()
    except FileNotFoundError:
        print("文件不存在")
    except Exception as e:
        print(e)
    else:
        with open(file, 'wb+') as a:
            a.write(save)

if __name__ == '__main__':
    file = input("输入文件路径:")
    print('-----选择功能-----')
    print('1--备份文件')
    print('2--还原文件')
    print('------------------')
    choice = input('输入功能编号:')
    if choice == '1':
        backup(file)
    if choice == '2':
        rollback(file)
