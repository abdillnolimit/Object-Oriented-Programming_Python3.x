#Pendahuluan Abstraction (TITLE)
"""
Abstraksi dalam Pemrograman Berorientasi Objek (OOP) dengan Python mengacu pada 
konsep mengisolasi atau menyembunyikan detail-detail kompleks dari suatu objek 
dan hanya menampilkan informasi yang penting. Dengan kata lain, abstraksi 
memungkinkan Anda untuk fokus pada aspek-aspek yang relevan dari suatu objek 
tanpa perlu tahu semua detail implementasinya. Ini membantu meningkatkan 
keterbacaan, pemeliharaan, dan fleksibilitas kode.


alur program ordinary class :
class -> instance -> object

alur program abstracted class :
abstract class -> inheritance -> class(wajib inherit abstractmethod dan method abstracted class nya) -> Object

"""

#contoh sederhana abstraction
"""membuat class abstract
abc = abstract base class"""
print(f"=====Contoh Sederhana=====")

from abc import ABC,abstractmethod

class Button(ABC):

	@abstractmethod
	def click(self): #ini abstracted instance yang tidak bisa diakses/dijadikan objek
		pass #abstracted class hanya memberikan kerangka untuk subclass nya

class PushButton(Button): #jika ingin inheritate abstracted class,  wajib inheritate abstractmethod nya.
	
	def click(self):
		print("push button click")

class RadioButton(Button):

	def click(self):
		print("radio button click")
	

tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()

#contoh penerapan
"""
Misalnya kita ingin membuat kelas "Mobil" dengan konsep abstraksi. Kita dapat 
mengisolasi detail-detail kompleks tentang bagaimana mesin bekerja atau bagaimana 
transmisi beroperasi, dan hanya memperhatikan informasi penting tentang mobil, 
seperti merk, model, dan kecepatan saat ini. Berikut contoh implementasi sederhana:
"""
print(f"\n=====Contoh penerapan=====\n")

from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, merk, model):
        self.merk = merk
        self.model = model
    
    @abstractmethod
    def info(self):
        pass

class Mobil(Kendaraan):
    def __init__(self, merk, model, kecepatan):
        super().__init__(merk, model)
        self.kecepatan = kecepatan
    
    def info(self):
        return f"Mobil {self.merk} {self.model}, Kecepatan: {self.kecepatan} km/jam"

class Sepeda(Kendaraan):
    def __init__(self, merk, model, jenis):
        super().__init__(merk, model)
        self.jenis = jenis
    
    def info(self):
        return f"Sepeda {self.merk} {self.model}, Jenis: {self.jenis}"

mobil = Mobil("Toyota", "Camry", 100)
sepeda = Sepeda("Polygon", "Xtrada", "Gunung")

print(mobil.info())   # Output: Mobil Toyota Camry, Kecepatan: 100 km/jam
print(sepeda.info())  # Output: Sepeda Polygon Xtrada, Jenis: Gunung

"""
Dalam contoh ini, kita menggunakan kelas abstrak Kendaraan dengan metode abstrak 
info() yang harus diimplementasikan oleh kelas turunannya. Ini memungkinkan 
kita untuk mengisolasi detail-detail internal dan hanya fokus pada informasi 
yang penting untuk setiap jenis kendaraan.
"""

#Abstract Base Class dan Decorator (TITLE)
"Problem ini mungkin saja terjadi dan tidak salahnya untuk dipelajari."

print(f"\n\n=====Abstract Class dengan Decorator=====\n")

from abc import ABC,abstractmethod

class Button(ABC):

	def __init__(self,set_link):
		self.link = set_link #variabel link disini hanya penamaan, berbeda dengan fungsi link di bawah.

	@abstractmethod #decorator ini untuk membuat atribut button, karena pada python tidak bisa langsung di subclass
	def click(self):
		pass

	@property #decorator ini untuk membuat atribut link yang juga pada python tidak bisa langsung pada subclassnya!
	@abstractmethod
	def link(self):
		pass


class PushButton(Button):
	
	def click(self):
		print("Go To: {}".format(self.link))

	@Button.link.setter #jangan lupa untuk namespace connections nya!
	def link(self,input):
		self.__link = input

	@link.getter #diakses supaya bisa akses fungsi link di abstract class nya
	def link(self):
		return self.__link	



tombol1 = PushButton("www.kelasterbuka.id")
tombol1.click()	