# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:04:32 2019

@author: Student
"""

def testy():
    
    #Zadanie 1:
    
    p1 = Student("Piotr", "Kiryczuk", 19998, "IIS")
    
    print(p1.imie)
    print(p1.nazwisko)
    print(p1.kierunek)
    print(p1)
    
    print()
    
    
    #Zadanie 2:
    
    p2 = Student("Marek", "Zaliszewki", 22741, "LSG")
    
    print(p1.__lt__(p2))
    print(p1.__eq__(p2))
    
    print()
    
    
    #Zadanie 3:
    
    p3 = Student("Marian","Kaczmarek",14678,"KAP")
    
    print("Licznik: %s"%(p3.getLicznik()))
    
    print()
    
    
    #Zadanie 4:
    
    p4 = StudentInformatyki("Adam", "Inowacki", 56748, "", "Robotyka")
    
    print(p4)
    print(p4.specjalnosc)
    pass
    
    
class Student():
    __licznik = 0
    
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek):
        Student.__licznik += 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.__nr_indeksu = nr_indeksu
        self.kierunek = kierunek
        
    def getLicznik(self):
        return self.__licznik
        
    def __lt__(self,other):
        if self.nazwisko < other.nazwisko:
            return True
        else:
            return False
        
    def __eq__(self,other):
        if self.nazwisko == other.nazwisko:
            return True
        else:
            return False
    
    def __str__(self):
        return "Imie: %s\nnazwisko: %s\nnr ideksu: %s\nkierunek: %s"%(self.imie, self.nazwisko, self.__nr_indeksu, self.kierunek)


class StudentInformatyki(Student):
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek, specjalnosc):
        super(StudentInformatyki,self).__init__(imie, nazwisko, nr_indeksu, kierunek)
        self.kierunek = "IIS"
        self.specjalnosc = specjalnosc


if __name__ == "__main__":
    testy()