"""
@author: zlh
@file: notification.py
@time: 2022/8/18 15:09
@desc: notification in macos
"""

from plyer.platforms.macosx import notification

if __name__ == '__main__':

    notification.instance().notify(
        title = "Alert",
        message = "Take a break!",
        timeout = 10
    )
