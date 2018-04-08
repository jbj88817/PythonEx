def city_temp(**param):
    # print(param) # {'bj': '12c', 'sh': '42c'}
    # print(type(param))  # <class 'dict'>

    for key, value in param.items():  # 遍历字典，同时获得key value
        print(key, value)


city_temp(bj='32c', xm='12c', sh='31c')

a = {'bj': '12c', 'sh': '42c'}
city_temp(**a)

city_temp()  # 可变参数可以什么都不传
