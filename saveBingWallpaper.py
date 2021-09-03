# 仅用于Windows，下载当日Bing图片并设置为桌面
# copyright
# @Time     : 2020/04/14
# @Author   : ZLei
# @Email    : zhibinlei@outlook.com
# @Software : VSCode

import os, re, time
import requests
import win32gui, win32con, win32api

save_dir = "D:\\ZLei\\Documents\\Python\\BingWallpaper\\Bing\\"


# 获取当前日期
def get_today_time():
    t = time.localtime(time.time())
    r_time = t.tm_year * 10000 + t.tm_mon * 100 + t.tm_mday
    return r_time


# 获取当前最新下载日期
def get_newdown_time(file_time):
    fid = open(file_time)
    r_time = int(fid.readline())
    fid.close()
    return r_time


# Windows设置壁纸
def set_desktop_windows(imagepath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                              "Control Panel\\Desktop", 0,
                              win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ,
                           "0")  # 2拉伸适应桌面，0桌面居中，1平铺
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imagepath,
                                  1 + 2)
    print("Set wallpaper successfully.")


# 获取今天的图片的url和copyright信息
def get_bing_info():
    base_url = "http://cn.bing.com/"
    query_url = "HPImageArchive.aspx?format=js&idx=0&n=1"
    print("Searching...")
    r = requests.get(base_url + query_url)
    image_url = base_url + r.json()["images"][0]["url"]
    copyright = r.json()["images"][0]["copyright"]
    copyright = re.sub(r'\(.*\)', '', copyright)
    copyright = copyright.strip().replace('\xa0', ' ')
    copyright = copyright.strip().replace('\xa1', ' ')
    copyright = copyright.strip().replace('\xa2', ' ')
    copyright = copyright.strip().replace('\xa3', ' ')
    copyright = copyright.strip().replace('\xa4', ' ')
    copyright = copyright.strip().replace('\xa5', ' ')
    copyright = copyright.strip().replace('\xa6', ' ')
    copyright = copyright.strip().replace('\xa7', ' ')
    copyright = copyright.strip().replace('\xa8', ' ')
    copyright = copyright.strip().replace('\xa9', ' ')
    copyright = copyright.strip().replace('\xf0', ' ')
    copyright = copyright.strip().replace('\xf1', ' ')
    copyright = copyright.strip().replace('\xf2', ' ')
    copyright = copyright.strip().replace('\xf3', ' ')
    copyright = copyright.strip().replace('\xf4', ' ')
    copyright = copyright.strip().replace('\xf5', ' ')
    copyright = copyright.strip().replace('\xf6', ' ')
    copyright = copyright.strip().replace('\xf7', ' ')
    copyright = copyright.strip().replace('\xf8', ' ')
    copyright = copyright.strip().replace('\xf9', ' ')
    copyright = copyright.strip().replace('?', '_')
    copyright = copyright.strip().replace('"', '\'')
    copyright = copyright.strip().replace(':', '：')
    # copyright = copyright.strip().replace('/', '|')
    print(copyright)
    return (image_url, copyright)


# 下载图片
def down_pic(pic_url, save_dir, t):
    image_name = "BingWallpaper_{}.jpg".format(t)
    # image_name = re.sub(r'.*/', '', pic_url)
    save_path = save_dir + image_name
    # print(save_path)
    r = requests.get(pic_url)
    file = open(save_path, "wb")
    file.write(r.content)
    file.close()
    return save_path


# 向壁纸信息至历史文件添加新行
def save_info(file_hist, time, copyright, pic_url):
    fid = open(file_hist, 'a')
    value = '%s,%s,%s\n' % (str(time), copyright, pic_url)
    # value中含'\xa0'之类字符时，gbk编码无法写入，utf8编码导致乱码，故在copyright中就要更改掉！
    fid.write(value)
    fid.close()


# 更新最新下载日期判别文件内容
def update_date(file_time, t):
    fid = open(file_time, 'w')
    fid.write(str(t))
    fid.close()


def main():
    curPath = os.path.abspath(os.path.dirname(__file__))
    f_newest = '%s\\time' % curPath
    f_hist = '%s\\BingHistory.csv' % curPath
    t_newest = get_newdown_time(f_newest)
    t_today = get_today_time()
    if t_newest != t_today:
        url, copyright = get_bing_info()  # 获取壁纸链接与copyright文字
        path = down_pic(url, save_dir, t_today)  # 下载图片
        save_info(f_hist, t_today, copyright, url)  # 更新存储信息
        update_date(f_newest, t_today)  # 更新判别文件
        # set_desktop_windows(path)  # 设置壁纸，不设置则注释
    else:
        print("Today's picture has been downloaded.")
    print("The program will exit after 5 seconds!")
    time.sleep(5)


main()
