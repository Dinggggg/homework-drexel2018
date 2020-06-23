# -*- coding=utf-8 -*-

# @Author: Ding Junwei
# @Student ID: 320180939671
# @Email: dingjw18@lzu.edu.cn
# @File: kernel2.py
# @Time: 2020/5/22 23:53



import matplotlib.pyplot as plt
from subprocess import Popen,PIPE,DEVNULL


def get_data(versions, repo):
    global time, time_list
    time_stamp_data = []

    for version in versions:
        cmd = 'git tag -l ' + '"' + version + '.*"'
        p = Popen(cmd, cwd=repo, stdout=PIPE, shell=True)
        time, res = p.communicate()
        time_str = time.decode('latin').encode('utf-8').decode('utf-8').split("\n")
        time_list = []
        for i in time_str:
            cmd_get = 'git log -1 --pretty=format:\"%ct\" ' + str(i)
            p = Popen(cmd_get, cwd=repo, stdout=PIPE, shell=True,stderr=DEVNULL)
            time_stamp, res = p.communicate()
            time_stamp = time_stamp.decode('latin').encode('utf8').decode('utf8')
            time_list.append(time_stamp)


        figure_show(time_list,time_str,version)


def figure_show(time_stamp_data,data,version):
    plt.scatter(time_stamp_data,data)
    plt.title("Release Order With Time {}".format(version))
    # plt.xlim(1.42e+09, 1.49e+09)
    plt.xticks(rotation=45, fontsize=5)
    plt.xlabel("Time")
    plt.ylabel("Release_Order")
    plt.savefig("figure_{}.png".format(version))
    plt.show("figure_{}.png".format(version))

path = 'D:\Github\Github_programs\linux-stable'
versions = ['v4.1', 'v4.2', 'v4.3', 'v4.4', 'v4.5', 'v4.6', 'v4.7', 'v4.8', 'v4.9']
get_data(versions, path)
