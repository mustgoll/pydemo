shop=[('a',100),('b',23),('c',230),('d',765)]
shop_list=[]
hl=input('how money:')
if hl.isdigit():
	hl=int(hl)
	while True:
		for item in shop:
			index=shop.index(item)+1
			print (index,item)
		choice=input('你要什么东西: ')
		if choice.isdigit():
			choice=int(choice)
			if choice<=len(shop) and choice>0:
				p_item = shop[choice-1]
				if p_item[1]>hl:
					print('金额不足')
				else:
					shop_list.append(p_item)
					hl-=p_item[1]
					print ('已将%s加入购物车，剩余￥%s' %(p_item,hl))
		elif choice=='q':
			print('exit')
			break
		else:
			print ('请输入数字')
		