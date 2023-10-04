#写run函数来完成各项功能调用
from interface import user

user_data = {
    'name':None,
    'is_auth':False
}
#登录
def login():
    if user_data['is_auth']:
        print('你已登录')
        return
    print('请先登录喔')

    count = 0
    while True:
        name = input("请输入用户名：").strip()
        user_dic = user.get_userinfo_by_name(name)
        if user_dic:
            print(user_dic['locked'])
            if user_dic['locked']:
                user.unlock_name(name)
                count = 0
                continue
            pwd = input("请输入密码：").strip()
            if user_dic['password'] == pwd and not user_dic['locked']==user_dic:
                user_data['name'] = name
                user_data['is_auth'] = True
                print('登录成功')
                break
            else:
                print('密码错误')
                count += 1
            if count >= 3:
                # 十三。锁定接口
                # 需要的是锁定 写入 user_dic  locked 变 True  写入 json数据修改
                user.lock_user(name)
        else:
            print('用户名不存在')

#注册
def register():
    if user_data['is_auth']:
        print('你已登录')
        return
    print('注册loading....')
    while True:
        name = input('请输入用户名：').strip()
        #调用接口查看用户是否已经注册
        user_dic = user.get_userinfo_by_name(name)
        #print(user_dic)
        if not user_dic:
            pwd = input('请输入密码：').strip()
            pwd1 = input('请确认密码：').strip()
            if pwd==pwd1:
                user.register_user(name,pwd)
            else:
                print('2次密码不一，请重新输入')
        else:
            print('用户名已经存在')
#查看余额
def check_balance():
    pass
#转账
def transfer():
    pass
#还款
def repay():
    pass
#取款
def withdraw():
    pass
#查看流水
def check_record():
    pass
#购物
def shopping():
    pass
#查看购物车
def look_shoppingcart():
    pass
#注销
def loginout():
    pass

fun_dic={'1':login,
         '2':register,
         '3':check_balance,
         '4':transfer,
         '5':repay,
         '6':withdraw,
         '7':check_record,
         '8':shopping,
         '9':look_shoppingcart,
         '10':loginout,
         }


def run():
    while True:
        print("""
    "1":登录
    "2":注册
    "3":查看余额
    "4":转账
    "5":还款
    "6":取款
    "7":查看流水
    "8":购物
    "9":查看购买商品
    "10":注销

        """)
        choice = input("请输入选择功能编号：").strip()

        
        if choice not in fun_dic:continue
        # fun_dic[choice]拿到函数内存地址，加括号调用
        fun_dic[choice]()



