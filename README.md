# 下载Bing壁纸并设置为桌面

1. saveBingWallpaper.py为主程序，在其中修改图片保存路径和图片文件名规则；
2. 主程序中可通过注释行设置是否需要设置为桌面；
3. BingWallpaper.bat为Windows批处理程序，可创建快捷方式放入启动文件夹中，随系统启动（需修改bat文件中的Python路径及py文件路径）；或设置定时启动事件，参考[CSDN文章](https://blog.csdn.net/circle_do/article/details/84861028)；
4. time为记录当前最新一次下载时间的文件，若当日图片已下载，当日再次调用程序时即跳过；
5. BingHistory.csv为记录下载历史的表格，含每次下载的日期，copyright信息，以及图片链接，每次下载时更新。

**自制小程序，欢迎自由修改使用！如有更好的意见欢迎交流沟通！**