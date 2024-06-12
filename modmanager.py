import os
os.system('cls')
os.system('color 0a')
state = 'main'


def select(args):
    while True:
        x = input()
        if x.isdigit() and int(x) in args:
            return int(x)
        print('Incorrect input')


while state != 'exit':
    os.system('cls')
    if state == 'main':
        f = open('modmanagerdata.txt', 'r')
        current_pack = f.readline().strip()
        f.close()
        print('Factorio Modpack Manager v 1.0')
        print('Installed modpack:', current_pack)
        print()
        print('1.Add new modpack')
        print('2.Change modpack')
        print('3.Exit')
        state = ['add', 'change', 'exit'][select([1, 2, 3]) - 1]
    if state == 'add':
        os.rename('mods', '_mods_' + current_pack)
        os.rename('saves', '_saves_' + current_pack)
        print('Enter new pack name:')
        f = open('modmanagerdata.txt', 'w')
        f.write(input().strip())
        f.close()
        os.mkdir('mods')
        os.mkdir('saves')
        state = 'main'
    if state == 'change':
        content = os.listdir()
        packs = sorted(list(set(i.split('_')[2] for i in content if '_' in i and '.' not in i)))
        print('Enter pack number:')
        x = []
        for i in range(len(packs)):
            x.append(i + 1)
            print(str(i + 1) + '.' + packs[i])
        n = select(x) - 1
        os.rename('mods', '_mods_' + current_pack)
        os.rename('saves', '_saves_' + current_pack)
        os.rename('_mods_' + packs[n], 'mods')
        os.rename('_saves_' + packs[n], 'saves')
        f = open('modmanagerdata.txt', 'w')
        f.write(packs[n])
        f.close()
        state = 'main'
        
