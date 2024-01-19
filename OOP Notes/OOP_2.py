#tkinter (TITLE)
"membuktikan bahwa tkinter python menggunakan paradigma OOP"

import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = "label1")
label2 = tkinter.Label(main_window, text = "label2")

tombol1 = tkinter.Button(main_window, text = "tombol1")
tombol2 = tkinter.Button(main_window, text = "tombol2")

# method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method menampilkan GUI
main_window.mainloop()


#private and protected variable (TITLE)
"""
-Variabel private
Variabel pribadi (private variables) dalam OOP Python merujuk pada variabel 
yang dimaksudkan untuk hanya dapat diakses dan dimodifikasi dari dalam kelas 
tempat variabel tersebut didefinisikan. 
Private variable dituliskan dengan awalan dounder(double underscore)
e.g : self.__name = data 

Meskipun Python tidak menerapkan akses yang benar-benar pribadi secara ketat 
seperti bahasa pemrograman lain, konvensi penggunaan underscore menunjukkan 
kepada pengembang bahwa variabel tersebut sebaiknya tidak diakses 
secara langsung dari luar kelas.




"""


#contoh private dan protected variable dengan cara akses yang salah

class Hero:

	# class variabel
	jumlah = 0
	__privateJumlah = 0

	def __init__(self,name,health):
		self.name = name
		self.health = health

		# variabel instance private
		self.__private = "privat"
		# variabel instance protected
		self._protected = "dilindungi"
"seharusnya menggunakan method untuk mengakses private variabel"


lina = Hero("lina",100)

print(lina.__dict__)
# print(Hero.__dict__)
print(lina.__privateJumlah())



#Pendahuluan Encapsulation (TITLE)
class Hero:

	def __init__(self,name,health,attackPower):
		self.__name = name#private variable
		self.__health = health#private variable
		self.__attPower = attackPower#private variable

	# getter (jika menaruh self pada argumen getter, artinya mengakses objeknya saja)
	def getName(self):
		return self.__name

	def getHealth(self):
		return self.__health

	# setter (jika menaruh self pada argumen setter, artinya mengubah objeknya saja)

	def diserang(self,serangPower):
		self.__health -= serangPower

	def setAttPower(self,nilaibaru):
		self.__attPower = nilaibaru

# awal dari game
earthshaker = Hero("earthshaker",50, 5)

# game berjalan

print(f"nama hero : {earthshaker.getName()}")
print(f"health hero sekarang : {earthshaker.getHealth()}")
earthshaker.diserang(5)
print(f"health hero sekarang : {earthshaker.getHealth()}")





#Staticmethod dan Classmethod (TITLE)

"""Decorator Method

staticmethod dan classmethod adalah dua jenis metode khusus dalam bahasa 
pemrograman Python yang dapat digunakan dalam konteks pemrograman 
berorientasi objek (OOP).

-Staticmethod
staticmethod adalah metode yang terkait dengan kelas, tetapi tidak memiliki 
akses ke atribut atau metode kelas. Metode ini bertindak sebagai fungsi 
biasa yang terkait dengan kelas tersebut. Dalam sebuah staticmethod, Anda 
tidak perlu mengakses atribut atau metode instan atau kelas. 
Anda hanya perlu mendeklarasikan metode tersebut menggunakan dekorator 
@staticmethod.


-Classmethod
classmethod adalah metode yang didekorasi dengan dekorator @classmethod. 
Metode ini menerima argumen cls yang mengacu pada kelas itu sendiri, 
bukan instance objek. classmethod sering digunakan untuk mengakses atau 
mengubah atribut kelas yang bersifat bersama (shared) di antara semua 
instance objek.

Kedua jenis metode ini memungkinkan Anda untuk melakukan tugas-tugas tertentu 
yang terkait dengan kelas tanpa harus membuat instance objek terlebih dahulu 
atau akses atribut instan.
"""


class Hero:

	#private class variabel
	__jumlah = 0;

	def __init__(self,name):
		self.__name = name
		Hero.__jumlah += 1

	# method ini hanya berlaku untuk objek
	def getJumlah(self):
		return Hero.__jumlah

	# method ini tidak berlaku untuk objek tapi berlaku untuk class
	def getJumlah1():
		return Hero.__jumlah

	# method static (decorator) nempel ke objek dan class
	@staticmethod
	def getJumlah2():
		return Hero.__jumlah

    #memnempel ke class nya saja.
	@classmethod
	def getJumlah3(cls): 
		return cls.__jumlah
"""penggunaan argumen  cls atau lainnya sebenarnya bebas,yang ingin ditekankan adalah
kita ingin decorator method ini menempel ke class saja. Jadi, ketika kita
mengubah nama class yang semula hero menjadi ucup, tentu merepotkan kita
untuk mengubah penulisan penamaan pada variabel yang ada di dalam class.
Cara ini lebih elegan dan simple.
"""

sniper = Hero('sniper')
print(Hero.getJumlah2())
rikimaru = Hero('rikimaru')
print(sniper.getJumlah2())
drowranger = Hero('drowranger')
print(Hero.getJumlah3())



# @property untuk getter dan setter pada encapsulation (TITLE)
"""INGAT KEMBALI
enkapsulasi dikatakan berhasil jika:

-aksesibilitas atribut dan metode
Menggunakan aksesibilitas private pada atribut dan 
metode kelas yang ingin dienkapsulasi.

-Getter dan setter
Menerapkan metode getter dan setter jika diperlukan untuk mengakses dan 
mengubah nilai atribut pribadi. Metode ini memungkinkan Anda untuk 
memproses validasi atau logika tambahan saat mengakses atau mengubah 
data.


-Keterbatasan Akses
Memastikan bahwa hanya metode publik yang dapat diakses dari luar kelas. 
Atribut dan metode pribadi hanya dapat diakses oleh metode lain dalam kelas.

-Konvensi Penamaan
Mengikuti konvensi penamaan yang umum digunakan oleh komunitas Python untuk 
menunjukkan atribut atau metode sebagai pribadi, seperti menggunakan awalan 
garis bawah ganda (__) pada nama atribut.

-Penggunaan Dekorator Property (opsional)
Menggunakan decorator property jika Anda ingin memberikan akses yang terkendali 
ke atribut, memungkinkan Anda untuk menjaga logika tambahan saat mengakses 
atau mengubah data.

-Pemahaman Tentang Encapsulation
Memiliki pemahaman yang jelas tentang prinsip-prinsip enkapsulasi, yaitu 
membatasi akses langsung ke data kelas dan mendorong penggunaan metode publik 
untuk berinteraksi dengan data.

Dengan mematuhi syarat-syarat ini, Anda dapat mencapai enkapsulasi dalam 
OOP Python, yang membantu dalam memisahkan antara implementasi internal 
kelas dan cara penggunaan eksternalnya, serta mempromosikan isolasi data 
dan fungsionalitas yang lebih baik

"""




class Hero:

	def __init__(self, name, health, armor):
		self.name = name
		self.__health = health
		self.__armor = armor
		#self.info = "name {} : \n\thealth: {}".format(self.name,self.__health)
        #jangan menggunakan variabel ini lagi untuk enkapsulasi, karena dinamis.

	@property #method menjadi variabel yang dapat diakses
	def info(self): #asli ini simple banget
		return "name {} : \n\thealth: {}\narmor : {}".format(self.name,self.__health,self.armor)
        #jangan lupa kasih format penamaan variabel nya untuk mengakses info objek
	@property 
	def armor(self): #armor fungsi ini bukan armor pada class dan objek yaa!
		pass #pass yang mengartikan bahwa fungsi ini akan dibuat lebih lanjut ke bawahnya

	@armor.getter #untuk mengakses variabel private instan pada atribut
	def armor(self):
		return self.__armor #direturn supaya bisa langsung diprint

	@armor.setter #untuk mengubah variabel private instan pada atribut
	def armor(self, input):
		self.__armor = input #tidak direturn, jadi butuh assignment print

	@armor.deleter #untuk menghapus variabel private instan pada atribut
	def armor(self):
		print('armor di-delete')
		self.__armor = None

sniper = Hero('sniper',100,10)

print('\n===== mengubah info objek ===== \n')
print(sniper.info) #mengakses informasi objek melalui dekorator @property di atas yang semula info berbentuk method menjadi variabel.
sniper.name = 'dadang' #mengubah nama sniper melalui variabel publik pada atribut, cara standar
print(sniper.info) #mengakses informasi sniper menggunakan format sniper.info yang ditetapkan melalui dekorator property 

print('\n=====getter dan setter untuk __armor =====\n')
print(f"armor sniper : {sniper.armor}")
sniper.armor = 50 #setter 
"""cara standard jika kita mennggunakan setter aja(tanpa property)
sniper.armor(valueUpdate)
"""
print(f"armor sekarang setelah mengalami update : {sniper.armor}")

print('\n=====delete armor=====\n')
del sniper.armor #ingat syntax ini dan juga syntax method nya di atas.
print(sniper.__dict__)

# print(sniper.info)

"""Kalau bingung
encapsulation itu konsepnya adalah
kita harus menjaga data internal kita agar tidak mudah diakses oleh publik/user secara langsung.
Python memiliki konvensi untuk mengakses dan juga mengubah isi class internal kita.
Jadi, untuk itu kita membuat variabel private ataupun protected pada atribut class,
setelah itu kita membuat method yang dapat mengakses serta mengubah variabel-
variabel tersebut.
"""


#Latihan Encapsulation (TITLE)
"menggunakan getter dan setter tanpa dekorator property dan menggunakan dekorator property."
"Konsep nya masih serang dan diserang, hanya menambahkan experience."

class Hero:

	#private class variabel
	__jumlah = 0

	def __init__(self,name,health,attPower,armor):
		self.__name = name
		self.__healthStandar = health
		self.__attPowerStandar = attPower
		self.__armorStandar = armor
		self.__level = 1
		self.__exp = 0

		self.__healthMax = self.__healthStandar * self.__level
		self.__attPower = self.__attPowerStandar * self.__level
		self.__armor = self.__armorStandar * self.__level

		self.__health = self.__healthMax

		Hero.__jumlah += 1

	@property
	def info(self):
		return "{} level {}: \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPower,self.__armor)

	@property
	def gainExp(self):
		pass

	@gainExp.setter
	def gainExp(self,addExp):
		self.__exp += addExp
		if (self.__exp >= 100):
			print(self.__name, 'level up')
			self.__level += 1
			self.__exp -= 100

			self.__healthMax = self.__healthStandar * self.__level
			self.__attPower = self.__attPowerStandar * self.__level
			self.__armor = self.__armorStandar * self.__level

	def attack(self,musuh):
		self.gainExp = 50

slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)
print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)

print(slardar.info)



class Hero:

	#private class variabel
	__jumlah = 0

	def __init__(self,name,health,attPower,armor):
		self.__name = name
		self.__healthStandar = health
		self.__attPowerStandar = attPower
		self.__armorStandar = armor
		self.__level = 1
		self.__exp = 0

		self.__healthMax = self.__healthStandar * self.__level
		self.__attPower = self.__attPowerStandar * self.__level
		self.__armor = self.__armorStandar * self.__level

		self.__health = self.__healthMax

		Hero.__jumlah += 1

	@property
	def info(self):
		return "{} level {}: \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPower,self.__armor)

	@property
	def gainExp(self):
		pass

	@gainExp.setter
	def gainExp(self,addExp):
		self.__exp += addExp
		if (self.__exp >= 100):
			print(self.__name, 'level up')
			self.__level += 1
			self.__exp -= 100

			self.__healthMax = self.__healthStandar * self.__level
			self.__attPower = self.__attPowerStandar * self.__level
			self.__armor = self.__armorStandar * self.__level

	def attack(self,musuh):
		self.gainExp = 50

slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)
print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)

print(slardar.info)

