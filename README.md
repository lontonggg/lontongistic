## Nama    : Reyhan Zada Virgiwibowo
## NPM     : 2206081723
## Kelas   : PBP C
## Link Aplikasi : https://lontongistic.adaptable.app/main/

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab : 
- Step pertama adalah membuat virtual environment terlebih dahulu dengan cara menulis perintah `python -m venv env` di cmd
- Aktifkan virtual environment dengan menulis perintah `env\Scripts\activate` di cmd.
- Kemudian buatlah file requirements.txt dan isi dengan dependensi yang diperlukan dan install dengan menjalankan perintah `pip install -r requirements.txt`
- Jalankan project Django dengan menjalankan perintah `django-admin startproject lontongistic`.
- Menambahkan `"*"` pada `ALLOWED_HOSTS` pada `settings.py ` dan membuat file `.gitignore`
- Menjalankan perintah `python manage.py startapp main` untuk membuat aplikasi `main`
- Membuat folder `templates` di dalam `main` dan menambahkan `main.html` didalamnya
- Menambahkan `path('main/', include('main.urls'))` di `urls.py` didalam `lontongistic` 
- Membuat model pada `main` dengan nama `Item` dan menambahkan attributes `name`, `amount`, `description`, `category`, `date_added`
- Membuat function `show_main` dengan context pada `views.py` dengan context `app`, `name`, `class`. Kemudian context tersebut di render pada `main.html` dengan memanggilnya menggunakan `{{app}}`, `{{name}}`, `{{class}}` 
- Membuat `urls.py` pada `main` dan menambahkan ` app_name = `main` `. Add `path('', show_main, name='show_main')` pada list `urlpatterns`
- Deploy aplikasi web pada Adaptable serta melakukan add, commit, dan push ke repository pada GitHub.

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab : 

<img src="/images/bagan.png">

Penjelasan :

Asumsikan ada client yang melakukan suatu aktivitas pada situs berbasis Django, maka browser akan mengirimkan HTTP Request kepada server situs tersebut dan akan dihandle oleh `urls.py` untuk mencari pattern url yang diinginkan client. Kemudian, framework Django akan menggunakan `views.py` untuk melakukan pengolahan dan operasi logika pada data yang terdapat pada `models.py`. Setelah pengolahan data selesai, maka `views.py` akan mengirimkan file `html` yang terdapat pada `templates` kepada client. Setelah itu browser client akan melakukan proses rendering file `html` yang merupakan HTTP Response.
 
### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawab :

Alasan kita perlu menggunakan virtual environment dalam membuat aplikasi web berbasis Django adalah untuk mengisolasi dependensi dari setiap project. Selain itu, dengan menggunakan virtual environment, pengelolaan aplikasi pun menjadi lebih mudah. Meskipun kita tetap dapat membuat aplikasi tanpa menggunakan virtual environment, tetapi tindakan tersebut akan sangat beresiko untuk mengakibatkan terjadinya konflik dependensi yang mungkin terjadi saat mengembangkan beberapa proyek Django di komputer yang sama.

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Jawab : 

### - MVC :
Model View Controller adalah pola arsitektur dalam pembuatan sebuah aplikasi dengan cara memisahkan kode menjadi 3 bagian yaitu :

- Model : Bagian yang bertugas untuk mengatur dan mengorganisasikan data yang ada pada database

- View : Bagian yang bertugas untuk menampilkan informasi kepada user

- Controller : Bagian yang bertugas untuk menghubungkan model dengan view

Alur proses dari MVC dimulai dari View yang akan meminta data untk ditampilkan kepada user, kemudian permintaan tersebut akan diteruskan ke Model melalui Controller, lalu Model akan mencari dan mengolah data yang diminta di dalam database. Setelah data ditemukan dan diolah, Model akan mengirimkan data tersebut kepada Controller untuk diatur dan nantinya akan dikirimkan kembali ke VIew untuk ditampilkan kepada user.

### - MVT :
Model View Template adalah pola arsitektur yang menggunakan 3 komponen utama yaitu Model, View dan Template.

- Model : Bagian yang bertugas untuk mengatur dan mengorganisasikan data yang ada pada database
  
- View : Bagian yang berinteraksi dengan model dan template, mengaplikasikan business logic, dan menghandle request HTTP (web) dan memberikan respons HTTP (web)
  
- Template : Bagian yang bertugas sebagai User Interface dan menhandle komponen statis seperti HTML untuk  merancang tampilan yang akhirnya akan diisi dengan data

Alur proses dari MVT dimulai ketika user mengirim URL request yang kemudian akan diterima oleh view, lalu view akan menjalankan business logic dan berinteraksi dengan Model untuk mengirimkan data dan template untuk mengahasilkan dokumen HTML yang berisikan data. Kemudian dokumen HTML yang telah dibuat akan dikembalikan oleh View sebagai respons kepada user.

### - MVVM :
Model View ViewModel adalah sebuah arsitektur pembuatan aplikasi yang menggunakan 3 komponen utama yaitu Model, View, dan ViewModel.

- Model : Tempat untuk logika bisnis dan data 

- View : Bertanggung jawab untuk mengatur UI yang nantinya akan dilihat oleh pengguna
  
- ViewModel : Berfungsi sebagai pertantara antara Model dan View

Alur proses MVVM dimulai ketika user berinteraksi dengan View, kemudian View akan mengirimkan permintaan ke ViewModel dan ViewModel akan menghubungi Model untuk mengambil atau memproses data. Setelah mendapatkan data dari Model, ViewModel akan mengirimkan data yang diperbarui ke View untuk ditampilkan kembali kepada pengguna.

### Perbedaan antara MVC, MVT dan MVVM
Perbedaan antara MVC, MVT dan MVVM adalah MVC lebih berfokus kepada pengendalian alur kerja aplikasi, sedangkan MVT menggunakan sebuah template untuk menggabungkan data dan tampilan, dan MVVM menggunakan ViewModel untuk mengikat data secara langsung ke tampilan. Pilihan antara ketiga arsitektur tersebut bergantung pada bahasa pemrograman dan framework yang digunakan untuk mengembangkan suatu aplikasi.
  

