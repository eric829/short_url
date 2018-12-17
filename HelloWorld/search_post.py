# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
from random import Random 
from TestModel.models import Test
# 接收POST请求数据

def post(request):
	

	if 'q' in request.POST:
		Table = Test.objects.filter(typein= request.POST['q'] )

		if len(Table)>0:			
			ran = Table[0].short_name
			ctx = request.POST['q']
			return render(request, "post.html", locals())
		else:
			ctx = request.POST['q']
			ran = random_num()
			testdb(ctx,ran)  
			return render(request, "post.html", locals())    
	
	else:
		return render(request, "post.html", locals())
			
		
		
def random_num():
	str = ''
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	length = len(chars) - 1
	random = Random()
	for i in range(6):
		str += chars[random.randint(0,length)]
	return(str)

def testdb(typein,short):
	test1 = Test(typein= typein ,short_name= short)
	test1.save()