#!/usr/bin/python3
#这个python脚本暂时还不能运行在Linux上，原因未知
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import math
import os
import imageio

def createFrame(gifInput,ls):#分割gif为图片列表并把格式转化为jpg
    im = Image.open(gifInput)
    try:
        print("图片分割中... ...")
        im.save('temp{:02d}.png'.format(im.tell()))
        imm = Image.open('temp{:02d}.png'.format(im.tell()))
        bg = Image.new("RGB", imm.size, (255,255,255))
        bg.paste(imm,(0,0))
        bg.save('picframe{:02d}.jpg'.format(im.tell()), quality=95)
        ls.append('picframe{:02}.jpg'.format(im.tell()))
        while True:
            im.seek(im.tell() + 1)
            im.save('temp{:02d}.png'.format(im.tell()))
            imm = Image.open('temp{:02d}.png'.format(im.tell()))
            bg = Image.new("RGB", imm.size, (255,255,255))
            bg.paste(imm,(0,0))
            bg.save('picframe{:02d}.jpg'.format(im.tell()), quality=95)
            ls.append('picframe{:02}.jpg'.format(im.tell()))
    except:
        print("分割完成！")

def bar(queue):#给图片加字幕黑边
    print("生成字幕中...")
    for frame in queue:
        im = Image.open(frame)
        x,y = im.size
        bar = Image.new('RGBA',(x,y - math.trunc(5.0/6.0 *y)),(0,0,0))#制作黑边
        im.paste(bar,(0,math.trunc(5.0/6.0 * y),x,y))#匹配黑边
        im.save(frame)

def recieve_words(amount):#参数就是个变量用来传输要输入几次
    for num in range(amount):
        hello = input("请输入第{}句话：".format(num + 1))
        words.append(hello)
    print("接收成功开始处理，请稍后\n")
    
def for_bar_word(ls,string):#在图片上显示字符
    for frame in ls:
        img = Image.open(frame)
        (img_x, img_y) = img.size
        # 文字字体像素高度为图片高度的 1/10
        ttfont = ImageFont.truetype('simkai.ttf',int(img_y/10))
        draw = ImageDraw.Draw(img)
        draw.text((int(img_x/10), img_y - int((img_y*1.3)/10)), string, (255,255,255), font=ttfont)
        img.save(frame)

def create_gif(lists):#将图片合成为一个gif
    frame = []
    print("正在生成gif...")
    for im in lists:
        frame.append(imageio.imread(im))
    imageio.mimsave('wjz.gif',frame,'GIF',duration = 0.15)
    print("成功！")

def clear_temp():#清理临时文件
    print("清理临时文件")
    os.system('del.bat')
    print("成功！gif生成完成！")

    
        
print("请选择想要制作的表情包：")
print("1)王境泽打脸 你的输入：")
flag = input()

lists = []#临时文件的列表
words = []#说的话的字符串数组
number = [4,4]#各个图片的人的话数

#王境泽的话语帧位置
leftb = [0,12,25,37]
rightb = [8,24,34,47]#王境泽的各个话的左右边界

#gif的文件名
filename1 = 'dalian.gif'
fllename2 = 'weisuo.gif'

if flag == '1':
    recieve_words(number[0])#获取输入的话语
    print("你选择了王境泽表情包")
    createFrame(filename1,lists)#分割成图片，把图片名按顺序存入列表lists中
    bar(lists)#给图片批量加黑边
    print("生成字幕中......")
    for i in range(number[0]):
        for_bar_word(lists[leftb[i]:rightb[i]],words[i])
    create_gif(lists)#生成图片
    clear_temp()

elif flag == '2':
    recieve_words(number[0])#获取输入的话语
    print("你选择了王境泽表情包")
    createFrame(filename1,lists)#分割成图片，把图片名按顺序存入列表lists中
    bar(lists)#给图片批量加黑边
    
    for i in range(number[0]):
        for_bar_word(lists[leftb[i]:rightb[i]],words[i])
    create_gif(lists)#生成图片
