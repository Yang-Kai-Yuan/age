age = input('請輸入年齡')
age = int(age)
print('原來你', age,'歲阿')
if age > 18:
	if age >= 80:
		print('祝您身體健康長命百歲')
	else :
		print('試著為你自己負責')
elif age <= 18 and age >= 3:
	print('回家找媽媽')
else :
	print('你看懂我打什麼就是神童')