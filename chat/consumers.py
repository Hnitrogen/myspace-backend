# from channels.generic.websocket import WebsocketConsumer
# from channels.exceptions import StopConsumer 
# from asgiref.sync import async_to_sync
 
# class ChatConsumer(WebsocketConsumer):
#     def websocket_connect(self,message):
#         print("有人进入聊天室！")
#         self.accept() 
#         async_to_sync(self.channel_layer.group_add)("2712",self.channel_name)

#         # 服务端主动向客户端发送消息        
#         # self.send("来了啊，猪头！")
    
#     def websocket_receive(self,message): 
        
#         # print("收到消息--> " + message['text'])
#         # text = message['text']
#         # res = "欢迎：{} 大神！".format(text) 
        
#         async_to_sync(self.channel_layer.group_send)("2712",{"type":"xx.oo","message":message})
#         self.send(res) 

#     # . -> _ 
#     def xx_oo(self,event): 
#         text = event['message']['text'] 
#         self.send(text) 

#     # 连接断开就会触发 , 无论是客户端/服务端谁发起连接 
#     # 如果想让服务端断开连接之后不触发  websocket_disconnect
#     # self.close() 
#     # raise StopConsumer()
#     def websocket_disconnect(self,message):
#         # print("断开连接") ;
#         # raise StopConsumer()        
#         async_to_sync(self.channel_layer.group_discard)("2712",self.channel_name)
#         raise StopConsumer()


from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import asyncio

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)('x1', self.channel_name)
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("接受到消息！")
        async_to_sync(self.channel_layer.group_send)('x1', {
            'type': 'xxx.ooo',
            'message': text_data
        })

    def xxx_ooo(self, event):
        message = event['message']
        self.send(message)

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)('x1', self.channel_name)