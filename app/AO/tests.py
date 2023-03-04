from django.test import TestCase,TransactionTestCase
from .models import Appoinment,Organization,filter_by_date
import random
import time

class AppoinmentTestCase(TransactionTestCase):
    def setUp(self):
        org=Organization.objects.create(name="test",email="test@email.com")
        for _ in range(10000):
            d=Appoinment(
                first_name="name tests",
                last_name="last name Test",
                date=f"{random.randint(1000,2023)}-{random.randint(10,12)}-{random.randint(10,28)}",
                time=f"{random.randint(10,23)}:{random.randint(10,59)}:{random.randint(10,59)}",
                organization=org
            )
            d.save()
        print('end creationg')
        
    def test_bin_search(self):
        data = Appoinment.objects.order_by('date')
        last = data[len(data)-1].date
        t=time.time()
        for i in range(10000):        
            d = filter_by_date(data,last)
        
        print('found:'+d.first_name)
        d = filter_by_date(data,'2024-01-01')
        print('not found:'+str(d))
        print('binary-search:'+str(time.time()-t))

    # def test_order_tree(self):
    #     t=time.time()
    #     data = Appoinment.objects.as_tree()
    #     print('as_tree-alg:'+str(time.time()-t))
        
    #     #self.assertEqual(data.head.value[0].first_name,'name tests')
        
    #     t=time.time()
    #     for i in range(1000):
    #         data.find(int(str('2000-12-28').replace('-','')))
    #     print('appo-tree-t:'+str(time.time()-t))
        
    #     t=time.time()
    #     for i in range(1000):
    #         Appoinment.objects.filter(date='2000-12-28')
    #     print('django-time:'+str(time.time()-t))
        