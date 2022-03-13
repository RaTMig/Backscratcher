import argparse
import random
from dbc2sbc import dbc2sbc

# ランダムな文字列を生成する。

parser = argparse.ArgumentParser(description='ランダムな文字列を生成します。')
parser.add_argument('-c', type=str, default='8',
                    help='文字数を整数(半角)で入力してください。初期値は8です。')
parser.add_argument('-jh', action='store_true', default=bool(0),
                    help='日本語(ひらがな)を含めます。')
parser.add_argument('-jk', action='store_true', default=bool(0),
                    help='日本語(カタカナ)を含めます。')
parser.add_argument('-a', action='store_true', default=bool(0),
                    help='アルファベット(半角大文字小文字)を含めます。')                    
parser.add_argument('-n', action='store_true', default=bool(0),
                    help='数字を含めます。')
parser.add_argument('-s', action='store_true', default=bool(0),
                    help='記号(+-*/.,_!?^~:;)を含めます。')
args = parser.parse_args()

# デフォルトリストは空。
randomList = []
outputStr = ''

# 使わなさそう。
if args.jh:
    randomList.extend(['あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と','な','に','ぬ','ね','の','は','ひ','ふ','へ','ほ','ま','み','む','め','も','や','ゆ','よ','ら','り','る','れ','ろ','わ','を','ん','ぁ','ぃ','ぅ','ぇ','ぉ','が','ぎ','ぐ','げ','ご','ざ','じ','ず','ぜ','ぞ','だ','ぢ','づ','で','ど','ば','び','ぶ','べ','ぼ','ぱ','ぴ','ぽ','ぺ','ぽ','っ','ゃ','ゅ','ょ','ゎ'])

# 使わなさそう。
if args.jk:
    randomList.extend(['ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','サ','シ','ス','セ','ソ','タ','チ','ツ','テ','ト','ナ','ニ','ヌ','ネ','ノ','ハ','ヒ','フ','ヘ','ホ','マ','ミ','ム','メ','モ','ヤ','ユ','ヨ','ラ','リ','ル','レ','ロ','ワ','ヲ','ン','ガ','ギ','グ','ゲ','ゴ','ザ','ジ','ズ','ゼ','ゾ','ダ','ヂ','ヅ','デ','ド','バ','ビ','ブ','ベ','ボ','パ','ピ','プ','ペ','ポ','ァ','ィ','ゥ','ェ','ォ','ッ','ャ','ュ','ョ','ヮ'])

if args.a:
    randomList.extend(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])

if args.n:
    randomList.extend(['0','1','2','3','4','5','6','7','8','9'])

if args.s:
    randomList.extend(['+','-','*','/','.',',','_','!','?','^','~',':',';'])

try:
    if not randomList:
        error = 1 / 0
except ZeroDivisionError:
    print('ランダム文字列の素が選択されていません。')
    print('ヘルプを参照し、オプションを選択して再度実行してください。')
    exit()

# 全角で数字が入力された時に備える。
count = dbc2sbc(args.c)

for i in range(0,int(count)):
    outputStr += random.choice(randomList)

print(outputStr)
