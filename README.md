# Sudoku Solver

<p align="center">
    <img align="center" src="test/image1.png"
</p>

## Latar Belakang
Anda adalah Mr. Khun, saat ini Anda tergabung bersama tim Sweet & Sour untuk mencapai puncak menara. Agar dapat mencapai puncak menara, ada harus melalui serangkaian tes untuk dapat naik ke lantai selanjutnya. Saat ini Anda berada di lantai 18 dan administrator lantai tersebut, yaitu Mr. Le Leo ingin sekali menguji kecerdasan tim Anda dalam membuat strategi. Area permainan pada lantai ini dibagi menjadi 81 area, berbentuk seperti matriks berukuran 9x9. Setiap area ditandai dengan angka, dalam satu kolom maupun satu baris tidak boleh ada angka berulang (seperti pada permainan sudoku). Untuk lolos dari tes ini, tim Anda harus mengumpulkan kristal yang ada pada area bernomor 5. Anda yang bertugas sebagai light bearer (bertugas mengawasi seluruh area permainan dan memberikan petunjuk serta menyusun strategi untuk seluruh anggota tim). Anda bisa berkomunikasi dengan seluruh anggota dan melihat seluruh area permainan melalui lighthouse, tugas Anda adalah mencari tahu nomor untuk semua area permainan dan memberitahukan koordinat (x,y) area-area yang ditandai dengan nomor 5 kepada anggota tim Anda.

### Checklist Program
- [X] Program dibuat dalam bahasa Python
- [X] Program menerima input berupa file eksternal
- [X] Program melengkapi area-area yang nomornya belum diketahui
- [X] Hasil penyelesaian disimpan dalam file eksternal
- [X] Menuliskan koordinat dari area bernomor 5 pada cmd / file eksternal
- [X] Membaca input berupa gambar
- [ ] Program diletakkan di src, file pengujian di test, hasil pengujian berupa screenshot di result
- [X] Program dikerjakan secara Individu dan mencantumkan referensi

### Strategi Pencarian Solusi
Algoritma yang digunakan dalam penyelesaian Sudoku adalah algoritma Backtracking. Alasan penggunaan algoritma Backtracking sendiri adalah karena prinsip dan cara kerja dari algoritma ini menurut saya cukup pintar dan logis seperti cara bermain sudoku yang sebenarnya. Pengisian sudoku memanfaatkan rules dari permainan Sudoku itu sendiri, yaitu memastikan setiap angka yang diisi merupakan angka yang unik pada satu kolom, satu baris, dan satu sub-grid tempat pengisian tersebut. Apabila hasil pengisian mentok pada titik tertentu, pengisian akan dirunut-balik ke pengisian sebelumnya dengan mengganti dengan angka yang lain.

Selain itu, algoritma backtracking juga efisien untuk penyelesaian Sudoku pada kasus rata-rata. Untuk kompleksitas algoritma backtracking pada Sudoku, kompleksitas waktu yang diperlukan adalah O(9^(n*n)). Kompleksitas waktu tersebut diperoleh mengingat banyaknya opsi pemilihan angka dari 1-9 untuk setiap area / cell pada matrix 9x9 (n x n). Sedangkan kompleksitas ruang yang diperlukan adalah O(n^n) untuk menyimpan grid dalam sebuah matrix.

### Library Pengerjaan Bonus
Coming Soon!
Kelebihan = ???
Kekurangan = ???

## Getting Started

## Referensi
1. Sudoku Solver with Backtracking: https://www.geeksforgeeks.org/sudoku-backtracking-7/
2. Implement A Sudoku Solver: https://www.youtube.com/watch?v=JzONv5kaPJM&
3. Algoritma Runut-Balik (Backtracking): https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2017-2018/Algoritma-Runut-balik-(2018).pdf

## Author
**13518056 - Michael Hans** - *Designer, Programmer, and Tester*

## Acknowledgements
* Asisten IRK, Nada Afra Sabrina