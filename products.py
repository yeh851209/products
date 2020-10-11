import os
def read_file(filename):
	products = []
	with open(filename, 'r', encoding= 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price  = line.strip().split(',')
			products.append([name,price])
			return products	

def user_input(products):
	while True:
		name = input('請輸入商品名稱，輸入完畢請輸入q： ',)
		if name == 'q':
			break
		price = input('請輸入商品價格： ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

def print_products(products):
	for p in products:
		print(p[0], '價格是', p[1])

def wright_file(filename, products):
	with open(filename, 'w', encoding= 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main(filename):
	if os.path.isfile(filename):
		products = read_file(filename)
		print(products)
	else:
		print('第一次輸入')

	products = user_input(products)
	print_products(products)
	wright_file('products.csv', products)

main('products.csv')