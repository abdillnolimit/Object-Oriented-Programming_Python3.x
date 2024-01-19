#Pendahuluan OOP python (TITLE)


'Penulisan Paling Sederhana'

class Hero: # template
    pass


hero1 = Hero() # object / instance (instansiate)
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper"
hero1.health = 100

hero2.name = "sven"
hero2.health = 200

hero3.name = "ucup"
hero3.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.name)
print(Hero.__dict__) 


#Constructure (TITLE)

print(f"\n=====\tConstructure\t=====\n")
class Hero: # template

    def __init__(self, inputName, inputHealth,inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("sniper",100, 10, 4)
hero2 = Hero("mirana",100, 15, 1)
hero3 = Hero("ucup",1000, 100, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)



#Class and Instance Attribute (TITLE)

class Hero: #template
	#class variabel
	jumlah = 0

	def __init__(self,inputName,inputHealth,inputPower,inputArmor):
		# instance variabel
		self.name = inputName #public variable
		self.health = inputHealth#public variable
		self.power = inputPower#public variable
		self.armor = inputArmor#public variable
		Hero.jumlah += 1
		print("membuat Hero dengan nama " + inputName)


hero1 = Hero("sniper",100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("mirana",100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("ucup",1000, 100, 0)
print(Hero.jumlah)




#Method (TITLE)

class Hero:
	# class variabel
	jumlah_hero = 0

	def __init__(self, inputName, inputHealth, inputPower, inputArmor):
		#instance variabel
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor
		Hero.jumlah_hero += 1

	# void function, method tanpa return, tanpa argumen
	def siapa(self):
		print("namaku adalah " + self.name)

	# method dengan argumen, tanpa return
	def healthUp(self,up):
		self.health += up

	# method dengan return
	def getHealth(self):
		return self.health


hero1 = Hero('sniper', 100, 10, 5)
hero2 = Hero('mario bros', 90, 5, 10)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())



# Latihan OOP sederhana (TITLE)
class Hero:

	def __init__(self,name,health,attackPower,armorNumber):
		self.name = name
		self.health = health
		self.attackPower = attackPower
		self.armorNumber = armorNumber

	def serang(self, lawan):
		print(self.name + ' menyerang ' + lawan.name )
		lawan.diserang(self, self.attackPower)

	def diserang(self, lawan, attackPower_lawan):
		print(self.name + ' diserang ' + lawan.name)
		attack_diterima = attackPower_lawan/self.armorNumber
		print('serangan terasa : ' + str(attack_diterima))
		self.health -= attack_diterima
		print('darah ' + self.name + ' tersisa ' + str(self.health))

sniper = Hero('sniper',100,10,5)
rikimaru = Hero('rikimaru',100,20,10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)


print(f"\n========== Review Penulisan Function ==========\n")

class data_mahasiswa:

    def __init__(self,name,npm,major,degree) :
        self.name   = name
        self.npm    = npm 
        self.major  = major
        self.degree = degree

#pengisian atribut/pembuatan spesifikasi dan detail objek dari sebuah class
Abdillah = data_mahasiswa("Mohamad Abdillah", 2206050296, "Phycisc", "Bachelor of Sciences")
Bambang  = data_mahasiswa("Bambang Haryono", 2198774088, "Computer Science", "Bachelor of Computer Sciences")

#memanggil data dictionary dari sebuah objek
print(Abdillah.__dict__)

#pemanggilan data dictionary dari semua objek
# data_mahasiswa.__dict__()
print(f"data seluruh mahasiswa :\n {data_mahasiswa.__dict__}")

#pemanggilan isi data tertentu dari sebuah objek
print(f"\nnama mahasiswa : {Abdillah.name}")

# #pengubahan  isi data variabel publik

Abdillah.name = "Abdillah Mohamad" #bisa seperti ini
print(f"pembaruan nama mahasiswa : {Abdillah.name}")

# Abdillah.name("ucup") #ini cara  yang salah, karena .name() bukan sebuah method ataupun variabel.



# Abdillah.data_mahasiswa() #pemanggilan yang salah, karena data_mahasiswa tidak terhubunng dengan atribut dan variabel.

