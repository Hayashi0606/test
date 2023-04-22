import os
for i in range(200):
    is_file =  os.path.isfile("../hoge{}.png".format(i))
    if is_file:
        os.remove("../hoge{}.png".format(i))
    else:
        break
    

for i in range(200):
    is_file =  os.path.isfile("./date/pokemon{}".format(i))
    if is_file:
        os.remove("./date/pokemon{}".format(i))
    else:
        break
