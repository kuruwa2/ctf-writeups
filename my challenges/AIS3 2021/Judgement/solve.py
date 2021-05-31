from hashlib import sha256
import string
flag = 'AIS3{iT_IS_4_Beaut1FUL_day_0utside_8IrD5_4Re_SiNGin9_F1owERS_Ar3_BlOOmIN6_oN_dAys_1iKe_7h3se_kiDs_1ik3_Y0u_ShOuLD_Be_BUrnin6_1n_h311}'
#It_is_a_beautiful_day_outside_Birds_are_singing_flowers_are_blooming_on_the_days_like_these_kids_like_you_should_be_burning_in_hell
cand = string.ascii_letters + string.digits + '_{}'
charset = string.printable[:93]

enc = ''
for c in flag:
	assert(c in cand)
	enc  += charset[int(sha256(c.encode()).hexdigest(), 16) % len(charset)]

print(enc) 	#)g;Fk@>2g;2V2J?d5G3_8V2<dR2i5GZ@<?2)g\j_2V&?2;@[F@ek2_3"=k&;2)\F2J9LL4g[W2"[2<)RZ23@<?2elFZ?2=@jZ23@=F2Yi52;_L5Vj2J?2J8\e@eW23e2lF330

for i in range(len(flag)):
	can = ""
	for j in cand:
		if charset[int(sha256(j.encode()).hexdigest(), 16) % len(charset)] == enc[i]:
			can += j
	print(can)
