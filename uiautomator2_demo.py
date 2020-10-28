import uiautomator2

devices = uiautomator2.connect("D3H7N17B11010237")


devices.app_start("guoyuan.szkingdom.android.phone", "kds.szkingdom.modemain.android.phone.UserMainActivity")
# devices.xpath(
#     '//*[@resource-id="guoyuan.szkingdom.android.phone:id/main_page_bottomBar_view"]/android.widget.LinearLayout[5]').click()
#
# devices(resourceId="guoyuan.szkingdom.android.phone:id/zjQieHuan").click_exists(10)
#
# devices(resourceId="khbz").send_keys("15240029081")
# devices(text="请输入您的交易密码").send_keys("123456")
# devices.xpath('//*[@resource-id="loginForm"]/android.view.View[10]').click()

devices(text="点击登录 >").click()
devices(text="请输入您的手机号码").send_keys("15240029081")
devices(text="获取验证码").click()
devices(text="请输入验证码").send_keys("11111")
devices(resourceId="guoyuan.szkingdom.android.phone:id/btn_register").click_exists(10)

