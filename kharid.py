
money=float(input("mablaq kharid ra vared konid:"))
ersal=str(input("noe ersal ra vared konid (addi_sari):"))

if ersal=='addi' and money<2000000 :
    print("majmu kharid shoma:",money+50000)
elif ersal=='sari':
    print("majmu kharid shoma:",money+100000)
if money>=2000000 and ersal=='addi':
    print("majmu kharid shpma:",money)

