# coding: utf-8
# ------ 指定したディレクトリのサイズを計算して出力する。 -------------------------------
# ------ 指定したディレクトリの配下のファイルサイズを計算して出力する。 -----------------
# ------ 引数でサイズを計測するディレクトリを指定する。 ---------------------------------
# ------ 動作はPython 3.6.6で確認 -------------------------------------------------------

# ------ Real Code Start ----------------------------------------------------------------

# ------ Import Libraries ---------------------------------------------------------------
# ------ os はファイル操作とかに使う。 --------------------------------------------------
# ------ mathは数学関数。 ---------------------------------------------------------------
# ------ argparseは引数に使用。 ---------------------------------------------------------
import sys
import os
import math
import argparse
import datetime

# ------ Code Runnable Start ------------------------------------------------------------
# ------ 変数設定 -----------------------------------------------------------------------
# ------ オブジェクトの設定及び引数の取得 -----------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('path')
args = parser.parse_args()

# ------ 出力先設定 ---------------------------------------------------------------------
# ------ 出力する一覧名は（年月）.txt ---------------------------------------------------
date_now = datetime.datetime.now()
outname = '//("出力パス")/{0:%Y%m}.txt'.format(date_now)

# ------ 数値を小数点第2位で四捨五入して文字列に変換する。 ------------------------------
# ------ Python 2.X.Xではroundは四捨五入 ------------------------------------------------
# ------ Python 3.X.Xではroundは五捨六入 ------------------------------------------------
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

# ------ ディレクトリの配下のファイルサイズを合算して出力する。 -------------------------
# ------ ディレクトリの配下のファイル名＋サイズを取得する。 -----------------------------
# ------ サブディレクトリも全部。 -------------------------------------------------------
def get_dir_size(path='.'):
    total = 0
    o2 = open(outname, 'a')
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                # サイズを合計
                total += entry.stat().st_size
                # ファイルサイズを出力
                o2.write(os.path.basename(entry) + '：' + (filesize(entry.stat().st_size)) + '\n' )
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total
    o2.close()

# ------ テスト出力 ---------------------------------------------------------------------
# ------ Test Code Start ----------------------------------------------------------------
# ------ コンソール上に各結果を出力する。 -----------------------------------------------
# print(filesize(get_dir_size(args.param)))
# print(date_now.strftime('%Y%m.txt'))
# ------ コンソール上に結果を出力する。 -------------------------------------------------
#o = open('//("出力パス")/test.txt', 'a')
#o.write(filesize(get_dir_size(args.param)))
#o.close()
# ------ Test Code End ------------------------------------------------------------------

# ------ テキストに結果を出力 -----------------------------------------------------------
outtext = filesize(get_dir_size(args.path))
o1 = open(outname, 'a')
o1.write('合計：' + outtext + '\n')
o1.close()
# ------ Code Runnable End --------------------------------------------------------------
# ------ Real Code End ------------------------------------------------------------------
