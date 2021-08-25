# coding : utf-8
import time

def compare_list(df_list, key):
    if key in df_list:
        return True
    else:
        return False

def compare_dict(df_dict, key):
    if key in df_dict:
        return True
    else:
        return False

def compare_dict_get(df_dict, key):
    if df_dict.get(key) == None:
        return True
    else:
        return False

def compare_dict_value(df_dict, key):
    if key in df_dict.values():
        return True
    else:
        return False


def main():
    N = int(input())
    S = {}
    for i in range(N):
        name = input()
        if name in S:
            continue
        else:
            print(i+1)
            S[name] = True
    return

main()


