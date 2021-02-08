#1导入库
import PySimpleGUI as sg 
import qrcode

#2确定行数
layout = [
				[sg.Text("制作二维码")],
				[sg.Text("姓名：")],
				[sg.Input()],
				[sg.Text("电话：")],
				[sg.Input()],
				[sg.Button("确定")]
						]

#3创建窗口
window = sg.Window("二维码制作", layout)

#4事件循环
while True:

	event, values = window.read()   #窗口的读取，有两个返回值（1.事件 2.值）
	print(event,values)

	if event == None:    #窗口关闭事件
		break

	txt = "姓名:"+values[0]+"\n"+"电话:"+values[1]
	img = qrcode.make(txt)
	name = "qrcode.png"
	img.save(name)

	sg.Popup("二维码已制作完成\n名称为"+name)



#5关闭窗口
window.close()