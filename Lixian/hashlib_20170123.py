
# '''
# __author__ = 'zhengbin'
# '''
# import hashlib 
# md5
# md5 = hashlib.md5()
# md5.update('love you'.encode('utf-8'))
# print(md5.hexdigest())

# sha1
# sha1 = hashlib.sha1()
# sha1.update('love you'.encode('utf-8'))
# print(sha1.digest())

# password = input('please input your password:')
# def calc_md5(password_str):
    # md5 = hashlib.md5()
    # md5.update(password_str.encode('utf-8'))
    # password_md5 = md5.hexdigest()
    # return md5.hexdigest()
# print(calc_md5(password))

import hashlib 
SALT = 'mywebsite'
db={}

def getMd5(password_str):
    md5 = hashlib.md5()
    md5.update(password_str.encode('utf-8'))
    return md5.hexdigest()

def register(username,password):
    print(password+username+SALT)
    db[username] = getMd5(password+username+SALT)
    print(username,password,':',db[username])
    return db

if __name__ == '__main__':
    register('abc','zhengbin')
    register('def','zhengbin')
    register('tom','zhengbin')
    # print(db)
    
    user_input = input('please input your name:')
    password_input=input('please input your password:')
    if user_input in db.keys():
        if getMd5(password_input+user_input+SALT) == db[user_input]:
            print('check ok , login success...')
        else:
            print('password is incorrect...')
    else:
        print('No such user ,please register first ...')
    

