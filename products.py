products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = [name, price]
	#p = []
	#p.append(name)
	#p.append(price)
	products.append(p)
	#products.append([name, price])最簡潔寫法
print(products)

