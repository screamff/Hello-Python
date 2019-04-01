#! python3
# coding:utf-8
import os

# 备份游戏存档
# 1.读取原文件内容
# 2.创建备份文件夹，copy原文件
# 3.rollback功能


def quickbackup(file):
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
        foldername = os.path.dirname(file)
        backup_file = foldername + '\\backup\\' + filename
        if os.path.exists(foldername+'\\backup'):
            pass
        else:
            os.mkdir(foldername+'\\backup')
        with open(backup_file, 'wb+') as a:
            a.write(save)
        print('-----*-----')
        print("快速备份完成！")
        print('-----*-----')


def quickrollback(file):
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
        print('-----*-----')
        print("快速载入完成!")
        print('-----*-----')


def rollback(save, rawfile):
    """save为要载入的存档路径，rawfile为原存档路径"""
    try:
        with open(save, 'rb') as f:
            save = f.read()
    except FileNotFoundError:
        print("文件不存在")
    except Exception as e:
        print(e)
    else:
        with open(rawfile, 'wb+') as a:
            a.write(save)
        print('-----*-----')
        print("载入成功!")
        print('-----*-----')


def loadsave(file):
    """载入所有存档文件夹,file为原存档文件"""
    savefilename = os.path.basename(file)
    foldername = os.path.dirname(file)
    folders = os.listdir(foldername)
    folders = list(map(lambda x: os.path.join(foldername, x), folders))
    # print('folders:', folders)
    savefolders = []
    for i in folders:
        if os.path.isdir(i):
            # print("isdir:", i)
            savefolders.append(os.path.join(i, savefilename))
    savefolders = sorted(savefolders,  key=lambda x: os.path.getctime(x))
    for i in range(len(savefolders)):
        print("%d--%s" % (i, os.path.basename(
                                             os.path.dirname(savefolders[i]))))
    choice = input("输入要载入的存档编号:")
    rollback(savefolders[int(choice)], file)


def main():
    file = input("输入文件路径:")
    while True:
        print('-----选择功能-----')
        print('1--快速备份')
        print('2--快速读取')
        print('3--新建备份')
        print('4--载入存档')
        print('------------------')
        choice = input('输入功能编号:')
        if choice == '1':
            quickbackup(file)
        if choice == '2':
            quickrollback(file)
        if choice == '4':
            loadsave(file)


if __name__ == '__main__':
    main()
