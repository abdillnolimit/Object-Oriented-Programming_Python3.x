#Pendahuluan inheritance (TITLE)

"""Apa itu konsep inheritance pada OOP?
Inheritance (warisan) adalah salah satu konsep utama dalam pemrograman berorientasi 
objek (OOP) yang memungkinkan Anda membuat hierarki kelas di mana kelas baru 
dapat mewarisi sifat dan perilaku dari kelas yang sudah ada. Dalam OOP Python, 
konsep ini memungkinkan Anda untuk membuat kelas baru yang memiliki semua atribut 
dan metode dari kelas yang sudah ada, serta memiliki kemampuan untuk menambahkan 
atribut dan metode tambahan atau mengubah perilaku yang diwarisi dari kelas induk.


Dalam konteks inheritance, ada dua jenis kelas yang relevan:

-Kelas Induk (Parent Class atau Superclass): 
Kelas yang menyediakan sifat dasar dan perilaku umum yang dapat diwarisi oleh 
kelas lain. Kelas ini mungkin memiliki metode dan atribut yang menjadi dasar 
bagi kelas anak.

-Kelas Anak (Child Class atau Subclass): 
Kelas yang mewarisi sifat dan perilaku dari kelas induk. Kelas anak juga dapat 
menambahkan atribut dan metode tambahan, serta mengubah atau meng-overide metode 
yang diwarisi dari kelas induk.


"""

#ingat konvensi python, penulisan nama class diawali dengan huruf kapital!
class Hero: #ini disebut superclass/parent class jika argumen class berikutnya menyisipkan argumen nama class ini.

	def __init__(self,name,health):
		self.name = name
		self.health = health

class Hero_intelligent(Hero): #ini subclass/child class
	pass

class Hero_strength(Hero): #ini subclass/child class
	pass

lina = Hero('lina',100)
techies = Hero_intelligent('techies',50)
axe = Hero_strength('axe',200)

print(lina.name)
print(techies.name)
print(axe.name)


#super (TITLE)

"""
Super merupakan metode yang digunakan untuk mewarisi atribut dan method dari
superclass ke subclass.
syntax super yang sederhana membuat method ini banyak digunakan oleh banyak
developper.
"""
class Hero:
	def __init__(self,name,health):
		self.name = name
		self.health = health

	def showInfo(self):
		print ("\n{} dengan health: {}".format(self.name,self.health))

class Hero_intelligent(Hero):
	def __init__(self,name):
		#Hero.__init__(self, name, 100)
		super().__init__(name, 100)
		super().showInfo()

class Hero_strength(Hero):
	def __init__(self,name):
		super().__init__(name, 200)
		super().showInfo()

lina = Hero_intelligent('lina')
axe = Hero_strength('axe')



#override (TITLE)
"""override
Override adalah konsep dalam pemrograman berorientasi objek (OOP) di mana Anda 
dapat mengganti atau mengubah implementasi metode yang diwarisi dari kelas induk 
(superclass) dalam kelas anak (subclass). Dengan override, Anda dapat memodifikasi 
perilaku atau fungsi dari metode yang diwarisi sehingga sesuai dengan kebutuhan 
spesifik kelas anak.

Dalam Python, ketika Anda mendefinisikan metode dengan nama yang sama di dalam 
kelas anak seperti yang ada di kelas induk, metode kelas anak akan "mengoverride" 
metode kelas induk. Ini berarti bahwa ketika Anda memanggil metode pada objek 
kelas anak, implementasi metode dari kelas anak akan dijalankan, bukan implementasi 
dari kelas induk.

Dengan inheritance, Anda dapat membuat hierarki kelas yang lebih kompleks dan 
mengatur kode secara lebih terstruktur, menghindari duplikasi, dan mempermudah 
pengembangan aplikasi yang lebih besar.

"""


class Hero:
	def __init__(self,name,health):
		self.name = name
		self.health = health

	def showInfo(self):
		print("\n=====showInfo di class Hero=====\n")
		print("{} health: {}".format(
			self.name,
			self.health
			)
		)


class Hero_intelligent(Hero):
	def __init__(self,name):
		super().__init__(name,100)

	# override
	def showInfo(self):
		print("\n=====showInfo di subclass Hero_intelligent=====\n")
		print("{} \n\tTipe: intelligent, \n\thealth: {}".format(
			self.name,
			self.health
			)
		)


class Hero_strength(Hero):
	def __init__(self,name):
		super().__init__(name,200)


lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

lina.showInfo() #ini akan mengikuti override, karena sifat dari superclass tertimpa
axe.showInfo() #ini masih mengikuti sifat yang diwariskan superclass


#Latihan Inheritance (TITLE)

from hero import HeroIntelligent,HeroStrength


lina = HeroIntelligent('lina')
slardar = HeroStrength('slardar')

lina.show_info()
slardar.show_info()

lina.gainExp = 200
slardar.gainExp = 250

lina.show_info()
slardar.show_info()


#Multiple Inheritance(TITLE)
"""
Multiple inheritance adalah keadaan di mana subclass memiliki inheritance
dari 2 atau lebih superclass.
Multiple inheritance sendiri juga bisa tidak sepenuhnya mewariskan, melainkan
dapat dioverride.
Pada Multiple inheritance, berlaku urutan akses class yang dapat kita lihat urutannya
menggunakan Method Resolution Order(MRO) dengan memanggil objek menggunakan
method help, contoh variabel objek ucup, maka untuk melihat urutan inheritance
superclass : help(ucup)

"""
#contoh sederhana
class A:

	def method_A(self):
		print("ini adalah method A")

class B:

	def method_B(self):
		print("ini adalah method B")


class C(A,B): #C mendapatkan inherit dari A lalu ke B
	pass


objek = C()

objek.method_A()
objek.method_B()


#contoh penerapan

class Team:
	def setTeam(self,team):
		self.team = team

	def showTeam(self):
		print(self.team)


class Tipe_Hero:
	def setTipe(self,tipe):
		self.tipe = tipe

	def showTipe(self):
		print(self.tipe)


class Hero(Team,Tipe_Hero):
	
	def __init__(self,name,health):
		self.name = name
		self.health = health

Ucup = Hero('Ucup',100)
Ucup.setTeam("merah")
Ucup.setTipe("cundang")

Ucup.showTeam()
Ucup.showTipe()



#Method Resolution Order/MRO (TITLE)
"Method MRO membantu user mencari tau diagram alur inheritance dari multiple inheritance."

class A:
	
	def show(self):
		print("ini adalah show A")

class B:

	def show(self):
		print("ini adalah show B")

class C(B,A):
	pass
	


objek = C()
objek.show()
#help(objek)


#Diamond Problem (TITLE)
"""Diamond Problem
adalah kondisi masalah yang mungkin saja terjadi jika subclass mendapatkan
inherit dari dua atau lebih superclass dan masing-masing superclass nya tersebut
mendapatkan inherit dari sebuah superclass yang sehingga jika digambarkan
diagram inheritance nya membentuk diamond.
"""

class A:
	
	def show(self):
		print("ini adalah show A")

class B(A):
	
	def show(self):
		print("ini adalah show B")

class C(A):
	
	def show(self):
		print("ini adalah show C")

class D(B,C):
	pass

objek = D()
objek.show()

"sederhananya, diamond akan melaju dari arah kiri lalu ke kanan(jika terkena pass) dan ke atas."


#Magic Method (TITLE)
"""
Magic method memiliki ciri khas penulisan yang sama seperti init dengan menggunakan
dounder(double underscore).
Magic method memudahkan developper untuk membuat syntax code menjadi lebih
elegan/sederhana.

ada banyak jenis magic method yang bisa diakses di library python.
berikut beberapa contoh sederhana dari magic method.

Beberapa magic method memerlukan dekorator @property untuk dapat digunakan.
"""

class Mangga:

	#magic method
	def __init__(self,nama,jumlah):
		self.nama = nama
		self.jumlah = jumlah

	def __repr__(self):
		return "Debug - Mangga: {} dengan jumlah: {}".format(self.nama,self.jumlah)

	def __str__(self):
		return "Mangga: {} dengan jumlah: {}".format(self.nama,self.jumlah)

	def __add__(self,objek):
		return self.jumlah + objek.jumlah

	@property
	def __dict__(self):
		return "objek ini mempunyai nama dan jumlah"


belanja1 = Mangga("arumanis",10)
belanja2 = Mangga("mana lagi",30)
print(belanja1) #pemanggilan setelah menggunakan magic method
print(belanja2) #jika tidak menggunakan magic method, yang terakses hanyalah alamat address memori objeknya saja.
print(belanja1 + belanja2)
print(belanja1.__dict__)


"""
__repr__(self) adalah magic method yang membuat fungsi sederhana yang nantinya
memudahkan developper untuk mengakses, tanpa harus mencantumkan namespace pada
variabel objeknya.

__str__(self) sama seperti __repr__(self) . Perbedaannya adalah __str__(self)
digunakan ketika program sudah siap dipublikasikan (sudah menjadi produk),
sedangkan __repr__(self) digunakan pada fase debugging.

__dict__ yang sering kita pakai pada namespace variabel juga merupakan magic method
, magic method ini memerlukan dekorator @property agar dapat digunakan.


"""





