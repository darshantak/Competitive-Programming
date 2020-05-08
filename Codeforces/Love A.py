# input_string=input()
# input_list=list(input_string)
# count=0
# sol=[]
# fin=[]
# for i in input_list:
#     if i=="a":
#         count+=1
# if count>len(input_list)/2:
#     print(len(input_list))
# elif count==0:
#     print(0)
# elif len(input_list)==1 and input_list[0]=="a":
#     print(1)
# else:
#     for i in range(len(input_list)):
#         if input_list[i] =="a":
#             sol.append(i)
#     if len(sol)==1:
#         x=max(sol)-0
#         y=len(input_list)-max(sol)-1
#         if x>y:
#             print(y+1)
#             exit()
#         else:
#             print(x+1)
#             exit()
#     for i in range(1,len(sol)):
#         temp=sol[i]-sol[i-1]
#         fin.append(temp)
#     print(len(input_list)-max(fin)+1)
