products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	p = [name, price]
	#p = []
	#p.append(name)
	#p.append(price)
	products.append(p)
	#products.append([name, price])最簡潔寫法
print(products)

for p in products:
	print(p[0], '的價格是', p[1])


with open('products.csv', 'w',  encoding = 'utf-8') as f: #建立檔案
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #寫入檔案
