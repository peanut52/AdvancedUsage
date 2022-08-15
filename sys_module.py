import sys
import os
import argparse


def do_sth(title_name):
    print(title_name)


def cmd_do_sth(title_name):
    # sys.executable获取解释器路径
    cmd = "\"%s\" %s --title_name=%s" % (sys.executable, __file__, title_name)
    os.system(cmd)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="I am doing ...")
    parser.add_argument('--title_name', type=str, required=True)
    args = parser.parse_args()
    do_sth(args.title_name)