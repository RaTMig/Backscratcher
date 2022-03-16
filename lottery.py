import argparse
import random


class ArgError(Exception):
    pass


parser = argparse.ArgumentParser(
    description='指定された抽選対象リストが空になるまで抽選し続けます。'
)
parser.add_argument(
    '-l',
    nargs="*",
    type=str,
    default='0',
    help='抽選対象の文字列を半角スペース区切りで入力してください。'
)


args = parser.parse_args()


try:
    if not args.l:
        raise ArgError('ArgError')
except ArgError as e:
    exit(
        'Exception Handler : {} \n'.format(e) +
        '-lオプションのリストが未入力です。処理を中断します。'
    )


try:
    if args.l[0] == '0':
        raise ArgError('ArgError')
except ArgError as e:
    exit(
        'Exception Handler : {} \n'.format(e) +
        '-lオプション指定、およびリストが未入力です。処理を中断します。'
    )


print(
    '抽選対象 => {}\n'.format(args.l) +
    '{} 項目の抽選対象リストから、1つずつ抽選していきます。'
    .format(len(args.l))
)


for i in range(0, len(args.l)):
    r = random.choice(args.l)
    print(
        '{}番目 {}'
        .format(i + 1, r)
    )
    args.l.pop(
        args.l.index(r)
    )
