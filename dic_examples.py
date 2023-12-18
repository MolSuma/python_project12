d = {"john":40, "peter":45}
print(d)
#True(equal)
d1 = {"john":40, "peter":45}
d2 = {"john":40, "peter":45}
print(d1 == d2)
#False(not equal)
d1 = {"john":40, "peter":45}
d2 = {"john":401, "peter":45}
print(d1 == d2)
# > we can't use arithmetic operators. it will show error
'''d1 = {"john":40, "peter":45}
d2 = {"john":407, "peter":45}
print(d1 > d2)'''
# print the value of particular key
d = {"john":40, "peter":45}
print(d["john"])
#To delete
d={"john":40, "peter":45}
d.__delitem__(["john"])