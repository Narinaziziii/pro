

nam_qaza=str(input("nam qaza ra vared konid:"))
tedad=int(input("tedad sefares ra vared konid:"))


if nam_qaza=='pitza':
    print(tedad*250000)
elif nam_qaza=='burger':
    print(tedad*180000)
elif nam_qaza=='sandevich':
    print(tedad*120000)
elif nam_qaza!='pitza' or nam_qaza!='burger' or nam_qaza!='sandevich':
    print("nam qaza eshtebah")