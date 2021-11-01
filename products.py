#讀取檔案
products = []
with open('products.csv', 'r') as f: #(, encoding = 'utf-8')加在 'r' 之後
	for line in f:
		if '商品,價格' in line:
			continue #繼續 
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

#讓使用者輸入
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

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w') as f: #建立檔案 #(, encoding = 'utf-8')加在 'r' 之後
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #寫入檔案
