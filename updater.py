#im gleichen verzeichnis muss die updater.json liegen um
#regelmaesige updates zu ermoeglichen
import os
import git
import sys
import requests
from colorama import init, Fore, Style

path = '/home/pi/roos'

def main():

    print('checking for updates...')
    need_to_update = len(sys.argv) <= 1

    if not need_to_update :
        need_to_update = (sys.argv[1] == '-force' or sys.argv[1] == '-f')
    else:
        need_to_update = check_version()

    if need_to_update == 2:
        print('no network')
    if need_to_update == 1:
        print('update...')
        update()
    else:
        print('up to date')
    #wait 24hours

def check_version():
    path_of_updates = path + '/updates/'
    lastest_version = '0'
    for file in os.listdir(path_of_updates):
        version = file.replace('update', '')
        if version > lastest_version:
            lastest_version = version

    #send https request an license.enwatmon.de fuer version vergleich
    url = 'https://license.enwatmon.de/RPIROversion'
    myobj = {'version': (lastest_version)}
    x = {}
    try:
        x = requests.post(url, data = myobj)
    except Exception as e:
        print(e)

    if not x:
        return 2


    print(x.text)
    return x.text == 'new version available'
def update():
    #git pull muss config auslassen bzw in gitignore schreiben
    print(path)
    g = git.cmd.Git(path + '/')
    g.stash()
    g.pull()

    lastest_version = ''

    for file in os.listdir(path + '/updates'):
        version = file.replace('update', '')
        if version > lastest_version:
            lastest_version = version
            global update_folder
            update_folder = path + '/updates/' + file

    if not update_folder or update_folder == '':
        print('no updates available')
        return
    print(update_folder + '/update.sh')
    f = open(update_folder + '/update.sh')
    orders = f.readlines()

    for order in orders:
        print('\n' + order)
        print(Fore.WHITE + 'Order executing...')
        res = os.popen(order).read()
        print(res)
        print(Fore.GREEN + 'Order done\n')

    print('done')
if __name__ == '__main__':
    main()
