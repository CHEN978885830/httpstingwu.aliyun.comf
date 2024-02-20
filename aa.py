'https://opensea.io/collection/dragondeeznft'
from sysconfig import get_path

'c'
import os

import pandas as pd
import asyncio
import getpass
import hashlib
import json
import random
import time

from playwright.async_api import async_playwright



class BSigns:
    def __init__(self):
        self.topic_list = []




    async def start_browser(self):
        __USER_DATE_DIR_PATH__ = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Google\\Chrome\\User Data"
        __EXECUTABLE_PATH__ = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # 请根据您的实际路径进行修改
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch_persistent_context(
            user_data_dir=__USER_DATE_DIR_PATH__,
            executable_path=__EXECUTABLE_PATH__,
            accept_downloads=True,
            headless=False,
            bypass_csp=True,
            slow_mo=10,
            args=['--disable-blink-features=AutomationControlled']
        )
        self.page = await self.browser.new_page()

        await self.page.add_init_script(path='stealth.min.js')

    import os
    import time

    async def shang_chuan_batch(self, directory):
        await self.page.click('.sc-doOioq.sc-futREh.NHItI.iqFouc.ButtonList')
        await self.page.click('.sc-cvBxsj.hYssPy')

        upload_element = await self.page.wait_for_selector('.ant-upload-btn')

        files = os.listdir(directory)
        num = 0
        while files:
            print(files)

            print('剩余未转文件个数：', len(files))
            if num >0:
                await self.page.click('.sc-doOioq.sc-futREh.NHItI.iqFouc.ButtonList')
                await self.page.click('.sc-cvBxsj.hYssPy')

                upload_element = await self.page.wait_for_selector('.ant-upload-btn')
            # 选择列表中的前50个文件
            files_batch = files[:30]
            # 移除已选择的文件
            files = files[30:]

            # 构建新的文件路径列表
            new_files = [os.path.join(directory, filename) for filename in files_batch]

            # 点击上传元素，打开文件选择对话框
            await upload_element.click()

            # 等待文件选择器弹窗出现
            async with self.page.expect_file_chooser() as fc_info:
                await self.page.get_by_text("本地音视频文件到这里").click()

            file_chooser = await fc_info.value

            # 设置文件选择器的文件列表
            await file_chooser.set_files(new_files)

            # 等待上传完成
            await self.page.get_by_text("开始转写").click()
            time.sleep(20)  # 这里可以根据需要调整等待时间
            num+=1

    async def close_browser(self):
        await self.browser.close()
        await self.playwright.stop()

    async def create_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    async def go_to_url(self, ):
        await self.page.goto('https://tingwu.aliyun.com/home')
        username = 'chuan5949'
        password = 'Dg220616'

        # 等待立即登录按钮出现并点击
        login_button = await self.page.wait_for_selector('.ant-btn-primary')
        await login_button.click()

        # 等待 "账号密码登录" 标签出现并点击
        # account_password_tab =  await self.page.wait_for_selector('.tabs-nav-item-text:has-text("账号密码登录")')
        # await account_password_tab.click()
        #
        # 等待表单加载完成
        # login_form = await self.page.wait_for_selector('#login-form')

        # 输入用户名
        # username_input = await login_form.query_selector('#fm-login-id')
        # await username_input.fill(username)
        #
        # 输入密码
        # password_input = await login_form.query_selector('#fm-login-password')
        # await password_input.fill(password)

        # 提交表单
        # login_button =await login_form.query_selector('.fm-submit')
        # await login_button.click()
        # 点击具有特定类名的元素
        while True:
            directory = input('是否继续转写，如果是输入路径，否则按q结束：')
            if directory.lower() == 'q':

                break

            await self.shang_chuan_batch(directory)
            time.sleep(2)

            # time.sleep(100)




        # 等待对话框出现
        # file_input = await self.page.wait_for_selector('input[type=file]')
        # await file_input.set_input_files('G:\学生项目\playwright\上传音频\批量音频\\ceshi.mp3')


        #
        # # 遍历文件夹中的文件
        # for file_name in os.listdir(folder_path):
        #     # 构建文件的完整路径
        #     file_path = os.path.join(folder_path, file_name)
        #
        #     # 如果是文件（非文件夹），则上传
        #     if os.path.isfile(file_path):
        #         print(f'上传文件：{file_path}')
        #         # 选择文件输入框并上传文件
        #         await self.page.click("input[type=file]")
        #         await self.page.set_input_files("input#upload", file_path)
        #
        #         # 这里可以添加等待页面响应的逻辑
        #
        #         # 上传完一个文件后，等待一段时间以便服务器处理
        #         # await self.page.wait_for_timeout(2000)  # 例如等待2秒


async def main():
    bot = BSigns()
    await bot.start_browser()

    await bot.go_to_url()


if __name__ == "__main__":
    asyncio.run(main())

