# coding: utf-8
# ------ 指定したディレクトリのサイズを計算して出力する。 -------------------------------
# ------ 引数でサイズを計測するディレクトリを指定する。 ---------------------------------
# ------ Real Code Start ----------------------------------------------------------------

# ------ Import libraries ---------------------------------------------------------------
# ------ os はファイル操作とかに使う。 --------------------------------------------------
# ------ mathは数学関数。 ---------------------------------------------------------------
# ------ argparseは引数に使用。 ---------------------------------------------------------
import sys
import os
import math
import argparse
import datetime

# ------ Code Runnable Start ------------------------------------------------------------
# ------ オブジェクト及び引数の設定 -----------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('param')
args = parser.parse_args()
parser.add_argument('address')

# ------ 引数が標準入力でなかった場合、私を見て！と主張する。 ---------------------------
def get_args():
    parser = argparse.ArgumentParser()
    if sys.stdin.isatty():
        parser.add_argument('address', help='Please Watch Me!!', type=str)
    args = parser.parse_args()
    return(args)

# ------ ディレクトリの配下のファイルサイズを合算する。サブディレクトリも全部。 ---------
def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total

# ------ 数値を小数点第2位で四捨五入して文字列に変換する。 ------------------------------
# ------ Python3.X.Xではroundは五捨六入 -------------------------------------------------
def roundstr(size):
    return str(round(size, 2))

# ------  ファイルサイズをKB,MB,GB,TB,PB,ZB表記の文字列に変換する。 ---------------------
def filesize(bytesize):
    if bytesize < 1024:
        return str(bytesize) + ' bytes'
    elif bytesize < 1024 ** 2:
        return roundstr(bytesize / 1024.0) + ' KB'
    elif bytesize < 1024 ** 3:
        return roundstr(bytesize / (1024.0 ** 2)) + ' MB'
    elif bytesize < 1024 ** 4:
        return roundstr(bytesize / (1024.0 ** 3)) + ' GB'
    elif bytesize < 1024 ** 5:
        return roundstr(bytesize / (1024.0 ** 4)) + ' TB'
    elif bytesize < 1024 ** 6:
        return roundstr(bytesize / (1024.0 ** 4)) + ' PB'
    elif bytesize < 1024 ** 7:
        return roundstr(bytesize / (1024.0 ** 4)) + ' ZB'
    else:
        return str(bytesize) + ' bytes'

# ------ 出力 ---------------------------------------------------------------------------

date_now = datetime.datetime.now()
outname = '（出力先パス）{0:%Y%m}.txt'.format(date_now)

# ------ テスト出力 ---------------------------------------------------------------------
# ------ Test Code Start ----------------------------------------------------------------
# ------ コンソール上に各結果を出力する。 -----------------------------------------------
# print(filesize(get_dir_size(args.param)))
# print(date_now.strftime('%Y%m.txt'))
# ------ コンソール上に結果を出力する。 -------------------------------------------------
#o = open('//("出力パス")/test.txt', 'w')
#o.write(filesize(get_dir_size(args.param)))
#o.close()
# ------ Test Code End ------------------------------------------------------------------

# ------ テキストに結果を出力 -----------------------------------------------------------
o = open(outname, 'w')
o.write(filesize(get_dir_size(args.param)))
o.close()
# ------ Code Runnable End --------------------------------------------------------------
# ------ Real Code End ------------------------------------------------------------------
