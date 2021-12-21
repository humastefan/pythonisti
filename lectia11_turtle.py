import turtle
t = turtle.Turtle()
# #numărul de laturi
# # n = int(input("laturi="))
# n = 7
# #unghiul de rotație
# u = 360 / n
# #contorul pentru while
# laturi = 1
# while laturi <= n:
#     for i in ["red", "green", "yellow", "blue", "black", "magenta", "purple"]:
#         t.color(i)
#         t.fd(50)
#         t.left(u)
#         laturi = laturi + 1


n = int(input("n="))
m = int(input("m="))
laturi = 1
while laturi <= 4:
    if laturi%2==1: #număr impar?
        t.fd(n)
    else:
        t.fd(m)
    t.left(90)
    laturi = laturi + 1
turtle.mainloop()