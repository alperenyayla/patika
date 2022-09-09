### Proje:

[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

Örnek: root x'dir. root'un sağından y bulunur. Solunda z bulunur vb.

### Cevap:
1. Root=6 olarak seçilmiştir.
2. 7 root'un sağına alınır.
3. 5 root'un soluna alınır.
4. 1 root'tan ve 5'ten küçük olduğu için 5'in soluna alınır.
5. 8 root'tan ve 7'den büyük olduğu için 7'nin sağına alınır.
6. 3 root'tan ve 5'ten küçük 1'den büyük olduğu için 1'in sağına alınır.
7. 0 root'tan, 5'ten ve 1'den küçük olduğu için 1'in soluna alınır.
8. 9 root'tan, 7'den ve 8'den büyük olduğu için 8'in sağına alınır.
9. 4 root'tan ve 5'ten küçük 1'den ve 3'ten büyük olduğu için 3'ün sağına alınır.
10. 2 root'tan ve 5'ten küçük, 1'den büyük ve 3'ten küçük olduğu için 3'ün soluna alınır.

### Final:
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|--|--|- |- |- |- |- |- |- |- |- |- |- |
|  |  |  |  |  |  | 6|  |  |  |  |  |  | 
|  |  |  |  |  | /|  |\ |  |  |  |  |  | 
|  |  |  |  | 5|  |  |  |7 |  |  |  |  | 
|  |  |  | /|  |  |  |  |  |\ |  |  |  |
|  |  | 1|  |  |  |  |  |  |  | 8|  |  |
|  | /|  |\ |  |  |  |  |  |  |  |\ |  |
| 0|  |  |  | 3|  |  |  |  |  |  |  | 9|
|  |  |  | /|  |\ |  |  |  |  |  |  |  |
|  |  | 2|  |  |  | 4|  |  |  |  |  |  |
