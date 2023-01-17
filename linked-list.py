class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
        self.size += 1

    def insert(self, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size +=1

    def deleteH(self):
        if self.head != None:
            temp = self.head
            self.head = temp.next
            self.size -=1
            print(temp.data)
        else:
            print('Delete Error, No data in Linked List')
    
    def printList(self):
        current = self.head
        temp = []
        while current != None:
            temp.append(current.data)
            current = current.next
        return temp

    def deleteT(self):
        if self.head != None:
            if self.head.next == None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next != None:
                    temp = temp.next
                lastNode = temp.next
                temp.next = None
                print(lastNode.data)
                lastNode = None
                self.size -= 1

    def find(self, data):
        current = self.head
        pos = 1
        while pos <= self.size:
            if current.data == data:
                print(f'Position of {data} is {pos}')
                break
            else:
                current = current.next
                pos += 1
        if pos > self.size:
            print('Data not found')

    def sizes(self):
        return self.size

    def cari(self,data):
        if data > 0 and data <= self.size: 
            cari = False
            current = self.head
            temp = None
            pos = 1
            while not cari:
                if current != None:
                    if data == 1:
                        temp = current.data
                        cari = True
                        return temp
                    elif data > 1 and data < self.size:
                        pos+=1
                        current = current.next
                        
                        if pos == data:
                            cari = True
                            return current.data
                    else:
                        if self.size == 1:
                            return self.head
                        else:
                            temp =self.head
                            while temp.next.next != None:
                                temp = temp.next
                            lastNode = temp.next
                            return lastNode.data


        elif data == 0:
            return 'Data tidak ada, silahkan masukkan angka mulai dari 1.'
        else:
            return 'Data out of range, silahkan masukkan angka mulai dari 1.'

    def delete(self, data):
        if self.head is None:
            return 'Linked list kosong'

        current = self.head
        prev = None
        found = False

        while not found:
            if current.data == data:
                found = True
            else:
                if current.next == None:
                    return "A Node with that value is not present."
                else:
                    prev = current
                    current = current.next

        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next




n = int(input('Banyak data = '))
link = Linked()

for i in range(n):
    temp = int(input(f'Data kata ke {i+1} = '))
    link.append(temp)

listnya = link.printList()

for i in range(len(listnya)):
    if i < len(listnya)-1:
        print(listnya[i],end = '->')
    else:
        print(listnya[i],end='')
print()

CHANCHE = 2
while CHANCHE != 0:
    hapus = input('Apakah anda ingin menghapus data? (y/n) = ').lower()
    if hapus == 'y':
        while hapus == 'y':
            posisi = int(input('Posisi data yang akan dihapus (mulai dari 1) = '))
            if posisi > 0 and posisi <= len(listnya):
                datanya = link.cari(posisi)
                print(f'Data yang dihapus adalah {datanya}')
                link.delete(datanya)
                listnya = link.printList()
                for i in range(len(listnya)):
                    if i < len(listnya)-1:
                        print(listnya[i],end = '->')
                    else:
                        print(listnya[i],end='')
                print()
            
            elif posisi == 0:
                print('Data tidak ada')

            elif posisi > len(listnya):
                print('Posisi out of range')
                listnya = link.printList()
                for i in range(len(listnya)):
                    if i < len(listnya)-1:
                        print(listnya[i],end = '->')
                    else:
                        print(listnya[i],end='')
                print()

            KES = 2
            while KES > 0:
                hapus = input('Apakah anda ingin menghapus data lagi? (y/n) = ').lower()
                if hapus == 'n':
                    if link.size > 0:
                        print('Program selesai dijalankan.')
                    CHANCHE = 0
                    break
                elif hapus == 'y':
                    break
                else:
                    if KES > 1:
                        print('Maaf kode yang anda masukkan salah')
                        KES -= 1
                    else:
                        print('Anda sudah memasukkan kode yang salah berulang kali')
                        print()
                        print('Program selesai dijalankan')
                        CHANCHE = 0
                        break


            if len(listnya) == 0:
                print('Data telah kosong')
                print('Program selsesai dijalankan')
                CHANCHE = 0
                break
    elif hapus == 'n':
        break
    else:
        if CHANCHE > 1:
            print('Maaf kode yang anda masukkan salah')
            CHANCHE -= 1
        else:
            print('Anda sudah memasukkan kode yang salah berulang kali')
            print()
            print('Program selesai dijalankan')
            break
