nama = str(input("Masukkan nama : "))
nim = str(input("Masukkan NIM : "))
uts = int(input("Masukkan nilai UTS : "))
uas = int(input("Masukkan nilai UAS : "))
tugas = int(input("Masukkan nilai Tugas : "))

Uts = uts*40/100;
Uas = uas*40/100;
Tugas = tugas*20/100;
nilai_akhir = Uts+Uas+Tugas;

print ("\nnama : %s"%nama)
print("nim : %s"%nim)
print("nilai uts : %i"%uts)
print("nilai uas : %i"%uas)
print("nilai tugas : %d"%tugas)
print("nilai akhir : ",float(nilai_akhir))

if nilai_akhir >= 80:
	print("\nnilai huruf : A")
elif nilai_akhir >= 70:
	print("\nnilaihuruf : B")
elif nilai_akhir >= 55:
	print("\nnilai huruf : C")
elif nilai_akhir >= 40:
	print("\nnilai huruf : D")
elif nilai_akhir <= 39:
	print("\nnilai huruf : E")
	
if nilai_akhir >=60:
	print ("Keterangan : Lulus")
else:
	print("Keterangan : Tidak Lulus")
	
	








