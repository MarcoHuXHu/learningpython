import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg.fromUserName)
    itchat.send('嗯啊', toUserName=msg['FromUserName'])


itchat.auto_login(hotReload=True)
author = itchat.search_friends(nickName='对方昵称')[0]
author.send('早上好, 这是一条自动发送到消息')
itchat.run()

