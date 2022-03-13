import argparse
import random

parser = argparse.ArgumentParser(description='指定された抽選対象リストが空になるまで抽選し続けます。')
parser.add_argument('-l', nargs="*", type=str, default='0',
                    help='抽選対象の文字列を半角スペース区切りで入力してください。') 
args = parser.parse_args()

lotteryList = args.l

try:
    if not lotteryList:
        error = 1 / 0
except ZeroDivisionError:
    print('-lオプション指定を確認しましたが、抽選するリストが入力されていません。')
    print('抽選するリストを入力して再度実行してください。')
    exit()

try:
    if lotteryList[0] == '0':
        error = 1 / 0
except ZeroDivisionError:
    print('-lオプション指定、および抽選するリストが入力されていません。')
    print('-lオプションを使用し、抽選するリストを入力して再度実行してください。')
    exit()

print('抽選対象 => {}'.format(lotteryList))
print('{} 項目の抽選対象リストから、1つずつ抽選していきます。'.format(len(lotteryList)))

for i in range(0,len(lotteryList)):
    r = random.choice(lotteryList)
    print('{}番目 {}'.format(i+1,r))
    lotteryList.pop(lotteryList.index(r))