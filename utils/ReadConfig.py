import os

import yaml

# ==========================================================
# 读取配置文件
# ==========================================================


# 配置文件位置
config_path = 'D:\seafile\hydee\dev\py-demos\config'

def read_config(parameter):
    # config_path2 = os.path.abspath(os.path.join(os.getcwd(), "../config"))
    with open(config_path, 'r', encoding='utf8') as f:
        data = yaml.load(f.read(),Loader=yaml.FullLoader)
    return data[parameter]


if __name__ == '__main__':
    pos_address = read_config("pro_login")["address"]
    print(pos_address)
