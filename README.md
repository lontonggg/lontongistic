## Nama    : Reyhan Zada Virgiwibowo
## NPM     : 2206081723
## Kelas   : PBP C
## Link Aplikasi : http://reyhan-zada-tugas.pbp.cs.ui.ac.id/

<details>
<summary><b>Tugas 2</b></summary>

## Tugas 2
### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab : 
- Step pertama adalah membuat virtual environment terlebih dahulu dengan cara menulis perintah `python -m venv env` di cmd
- Aktifkan virtual environment dengan menulis perintah `env\Script\activate` di cmd.
- Kemudian buatlah file requirements.txt dan isi dengan dependensi yang diperlukan dan install dengan menjalankan perintah `pip install -r requirements.txt`
- Jalankan project Django dengan menjalankan perintah `django-admin startproject lontongistic`.
- Menambahkan `"*"` pada `ALLOWED_HOSTS` pada `settings.py ` dan membuat file `.gitignore`
- Menjalankan perintah `python manage.py startapp main` untuk membuat aplikasi `main`
- Membuat folder `templates` di dalam `main` dan menambahkan `main.html` didalamnya
- Menambahkan `path('main/', include('main.urls'))` di `urls.py` didalam `lontongistic` 
- Membuat model pada `main` dengan nama `Item` dan menambahkan attributes `name`, `amount`, `description`, `category`, `date_added`
- Membuat function `show_main` dengan context pada `views.py` dengan context `app`, `name`, `class`. Kemudian context tersebut di render pada `main.html` dengan memanggilnya menggunakan `{{app}}`, `{{name}}`, `{{class}}` 
- Membuat `urls.py` pada `main` dan menambahkan ` app_name = 'main' `. Add `path('', show_main, name='show_main')` pada list `urlpatterns`
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
</details>

<details>
<summary><b>Tugas 3</h1></b></summary>

## Tugas 3

### 1. Apa perbedaan antara form POST dan form GET dalam Django?

Jawab:

### POST :

POST adalah method request HTTP dimana data yang dikirimkan tidak terlihat pada URL. Method ini tidak memiliki limitasi untuk ukuran data yang akan dikirim. Method POST biasa digunakan untuk mengirimkan informasi yang kredensial atau sensitif seperti password.

### GET :

GET adalah method request HTTP dimana data yang dikirimkan akan terlihat pada URL. Method ini dibatasi untuk mengirimkan maksimal 2048 karakter. Method GET lebih baik digunakan untuk mengirimkan informasi yang tidak sensitif.

### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

Jawab :

### XML :

XML (Extensible Markup Language) adalah format data yang dapat dibaca oleh manusia maupun mesin dengan menggunakan markup tags yang mirip dengan HTML untuk mendefinisikan suatu struktur data. XML digunakan untuk pertukaran data yang lebih kompleks dan lebih terstruktur, contohnya mengirim data sebagai API.

Contoh :
```xml
<?xml version="1.0" encoding="utf-8"?>
<django-objects version="1.0">
    <object model="main.item" pk="1">
        <field name="name" type="CharField">Aqua Galon</field>
        <field name="amount" type="IntegerField">5</field>
        <field name="description" type="TextField">Galon Aqua untuk didistribusikan kepada masyarakat</field>
        <field name="category" type="TextField">Minuman</field>
        <field name="date_added" type="DateTimeField">2023-09-19T09:04:00.815031+00:00</field>
    </object>
</django-objects>
```

### JSON :

JSON (JavaScript Object Notation) adalah format data ringan  untuk pertukaran data antara aplikasi yang telah didesain untuk mudah dibaca oleh manusia dan mudah diproses oleh mesin.
JSON mendukung penggunaan tipe data dasar seperti objek, array, string, integer, dan lainnya.

Contoh : 
```json
[
    {
        "model": "main.item",
        "pk": 1,
        "fields": {
            "name": "Aqua Galon",
            "amount": 5,
            "description": "Galon Aqua untuk didistribusikan kepada masyarakat",
            "category": "Minuman",
            "date_added": "2023-09-19T09:04:00.815Z"
        }
    }
]
```

### HTML :

HTML (Hypertext Markup Language) adalah bahasa markup yang digunakan untuk membuat dan menyusun struktur, tampilan, konten, serta script dari sebuah website. Fungsi dari HTML bukan untuk pertukaran data secara langsung seperti XML atau JSON, tetapi sebagai penyusun konten yang akan ditampilkan dalam browser web.

Contoh :
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

Jawab :

Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern adalah penulisannya yang simple serta machine and human readable. JSON adalah format data yang ringan dan mudah diproses oleh mesin, sehingga mengurangi beban pada server dan meningkatkan kinerja aplikasi. Selain itu, JSON menggunakan `dictionary` dan `list` sebagai kontainer yang sudah biasa digunakan oleh programmer.


### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab :

### Membuat Input Form Untuk Menambahkan Objek

- Membuat file bernama `forms.py` pada `main` untuk membuat struktur form dengan menambahkan kode berikut:

``` python
from django.forms import ModelForm
from main.models import Item

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "category"]
```

- Membuat file bernama `create_product.html` pada folder `template` di dalam folder `main`
```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

### Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, JSON, XML by ID, dan JSON by ID

- Membuat fungsi `create_product` pada `views.py` dengan parameter `request` untuk melakukan rendering halaman form serta mengubah fungsi `show_main` untuk menghitung jumlah item yang disimpan (Bonus Question).

```python
def show_main(request):
    items = Item.objects.all()
    items_total = 0
    for item in items:
        items_total += item.amount
    
    context = {
        'app' : 'Lontongistic',
        'name': 'Reyhan Zada Virgiwibowo',
        'class': 'PBP C',
        'items' : items,
        'items_total' : int(items_total)
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```

- Membuat fungsi yang menerima parameter request pada `views.py` di `main` dalam bentuk JSON maupun XML dan akan menyimpan hasil query dari seluruh data yang ada pada `Item`, serta menambahkan return function berupa `HttpResponse` yang berisi parameter data hasil qeury yang sudah diserialisasi.

```python
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### Membuat routing URL untuk masing-masing views yang telah ditambahkan  

- Mengimpor fungsi yang telah dibuat sebelumnya dan menambahkan path url kedalam `urlpatterns` pada `urls.py` di `main` untuk mengakses fungsi yang telah diimpor sehingga kode menjadi :

``` python
urlpatterns = [
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'), 
    path('create-product', create_product, name='create_product'),
    path('', show_main, name='show_main'),
]
```
### Screenshot Postman

- JSON

<img src="/images/postman_json.png">

- JSON by ID

<img src="/images/postman_json_id.png">

- XML

<img src="/images/postman_xml.png">

- XML by ID

<img src="/images/postman_xml_id.png">

</details>
<details>
<summary><b>Tugas 4</h1></b></summary>

## Tugas 4

### 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

Jawab :

Django UserCreationForm adalah salah satu bentuk form yang disediakan oleh framework Django yang dirancang untuk membuat proses registrasi dan autentikasi user. Dengan menggunakan UserCreationForm, developer bisa membuat sistem registerasi, login, dan logout dari user dengan mudah dan cepat.

Kelebihan : 
- Simple
- Mudah untuk didevelop
- Aman

Kekurangan :
- Tidak cocok untuk data registrasi yang kompleks
- Tampilan bawaan yang baku
- Terbatas dalam kustomisasi

### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Jawab :

Autentikasi merupakan proses untuk mengidentifikasi pengguna yang akan login kepada suatu aplikasi. Autentikasi biasanya berupa verifikasi password, kartu akses login, atau biometrik seperti sidik jari atau facial identification.

Otorisasi adalah proses menentukan apa yang izinkan dan apa yang tidak diizinkan untuk diakses oleh pengguna yang telah berhasil terautentikasi. Contoh umumnya adalah penggunaan roles seperti admin, dimana admin dapat mengakses seluruh halaman pada aplikasi, sedangkan user biasa hanya dapat mengakses beberapa halaman.

Penggunaan keduanya menjadi penting untuk menjaga keamanan, privasi user, mengontrol akses, serta melacak jika terjadi penyalahgunaan atau pelanggaran.

### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Jawab :

Cookies dalam konteks aplikasi web adalah semacam data kecil yang disimpan di dalam perangkat pengguna oleh server web yang nantinya akan dikirim kembali ke server saat perangkat user tersebut melakukan request ke situs web yang sama. Django mengelola data sesi pengguna dengan menggunakan cookies untuk menyimpan session ID untuk mengidentifikasi sesi yang terakhir dibuka oleh user. Data dari session yang sebenarnya disimpan di dalam database yang nantinya dapat diakses menggunakan session ID. Hal ini akan meningkatkan keamanan data karena data tidak disimpan di dalam cookies yang lebih rentan terhadap serangan dibandingkan database.


### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Jawab :

Penggunaan cookies akan menjadi aman jika diimplementasikan dengan benar. Akan tetapi, terdapat beberapa risiko potensial yang harus diwaspadai, seperti penyalahgunaaan cookies, masalah privasi, pelacakan (tracking), dan lainnya.


### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab : 

#### - Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar

- Mengimpor `redirect`, `UserCreationForm`, dan `messages` di dalam `views.py` pada folder `main`: 
```python
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
- Menambahkan fungsi `register` untuk menghasilkan formulir registrasi secara otomatis dengan menambahkan kode berikut : 

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

- Membuat berkas HTML bernama `register.html` pada folder `main/templates` sebagai kerangka dari halaman registrasi dengan isi berikut :

```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

- Mengimport fungsi `register` yang telah dibuat ke `urls.py` dan menambahkan `path url` ke dalam `urlpatterns`

```python
from main.views import register
```

```python
...
path(`register/`, register, name='register')
...
```

- Membuat fungsi login bernama `login_user` pada `views.py` di dalam folder `main` dengan parameter `request`, serta mengimport `authenticate` dan `login` sehingga kode menjadi :

```python
...
from django.contrib.auth import authenticate, login
...

...
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
...
```

- Membuat file HTML bernama `login.html` pada folder `main/templates` sebagai kerangka dari halaman login dan mengisinya dengan :

```html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

- Membuat fungsi `logout_user` dengan parameter `request` di `views.py` pada folder `main` serta mengimport `logout` sehingga kode menjadi :

```python
from django.contrib.auth import logout
...

...
def logout_user(request):
    logout(request)
    return redirect('main:login')

```

- Menambahkan potongan kode berikut pada `main.html` untuk button `Logout`
```html
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```
- Mengimpor fungsi logout ke `urls.py` pada folder `main` dan menambahkan path  url ke dalam `urlpatterns`

```python
from main.views import logout_user
```
```python
...
path('logout/', logout_user, name='logout'),
...
```

#### - Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal

- Melakukan registrasi akun dan membuat password
- Melakukan login dengan menginput username dan password yang telah dibuat
- Menambahkan 3 item berbeda ke dalam inventory user

User 1

<img src="/images/dummy1.png">

User 2

<img src="/images/dummy2.png">

#### - Menghubungkan model `Item` dengan `User`

- Mengimport model `User` pada `models.py` di dalam folder `main`

```python
...
from django.contrib.auth.models import User
...
```

- Menambahkan potongan kode berikut pada model `Item`

```python
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
...
```

- Mengubah fungsi `create_product` pada `views.py` di dalam folder `main` menjadi : 

```python
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
```

- Mengubah fungsi `main` pada `views.py` di dalam folder main menjadi :
```python
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
```

- Menyimpan semua perubahan dengan melakukan migrasi model dengan menjalankan `python manage.py makemigrations` dan `python manage.py migrate` pada terminal

#### - Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi                     

- Mengimport `HttpResponseRedirect`, `reverse`, dan `datetime` pada `views.py` pada folder `main`

```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

- Menambahkan fungsi untuk menambahkan cookie dengan nama `last_login` serta mengubah blok `if use is not None` pada fungsi `login_user`

```python
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

- Menambahkan context bernama `last_login` pada fungsi `show_main` yang menyimpan informasi cookie `last_login`

```python
...
context = {
    ...
    'last_login': request.COOKIES['last_login'],
    ...
}
```

- Mengubah fungsi `logout_user` dengan menambahkan method untuk menghapus cookie

```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

- Menambahkan tombol logout pada `main.html`

```html
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```
</details>
<details>
<summary><b>Tugas 5</h1></b></summary>

 ## Tugas 5

 ### 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

 Jawab : 
   
Elemen Selector
Type selector akan memengaruhi semua elemen dengan tipe yang sama, contohnya seperti p, h, table, dll.

Contoh : 
```css
p1{
...
}
```

Class Selector
Class selector akan memengaruhi semua elemen yang memiliki kelas yang sama. Sebaiknya digunakan untuk mengatur gaya beberapa elemen yang dikelompokkan ke kelas yang sama secara bersamaan.

Contoh :
```css
.card-header{
...
}
```

ID Selector
ID Selector akan emengaruhi elemen dengan ID yang sesuai. Cocok untuk mengatur elemen tertentu yang hanya ada satu di halaman (ID harus unik).

Contoh:
```html
#header{
...
}
```
  
### 2. Jelaskan HTML5 Tag yang kamu ketahui. 

Jawab : 
 
HTML Memiliki ratusan tag dan memiliki kegunaannya masing-masing. Berikut adalah beberapa contoh tag HTML yang umum digunakan.
- `<html>` Menandai awal dan akhir dokumen HTML.
- `<head>` Berisi informasi tentang halaman web, seperti judul dan tautan ke stylesheet.
- `<title>` Menentukan judul halaman web yang akan ditampilkan di tab browser.
- `<link>` Menghubungkan halaman web dengan stylesheet eksternal atau favicon.
- `<style>` Digunakan untuk menyisipkan CSS langsung ke dalam dokumen HTML.
- `<body>` Memuat semua konten yang akan ditampilkan di halaman web.
- `<h1>, <h2>, ..., <h6>` Membuat heading atau judul dengan level yang berbeda dimana h1 adalah yang tertinggi
- `<p>` Membuat paragraf teks.
- `<a>` Membuat tautan (link) ke halaman web atau sumber daya lainnya.
- `<img>` Menampilkan gambar di halaman web.

### 3. Jelaskan perbedaan antara margin dan padding.

Jawab :

Padding adalah ruang di dalam elemen atau jarak antara konten/isi elemen dengan batas elemen, sedangkan Margin adalah ruang di luar elemen atau jarak antara suatu elemen dengan elemen-elemen lain di sekitarnya

### 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Jawab : 

Perbedaan utama framework Tailwind dan Bootstrap adalah dari pendekatan mereka dalam membantu pengembangan web. Bootstrap memberikan banyak templates yang mudah untuk digunakan kembali serta dimodifikasi. Sedangkan Tailwind menggunakan pendekatan "utility-first" dimana Tailwind menyediakan komponen-komponen untuk dirakit dari simple menjadi kompleks sehingga memungkinkan kita untuk menggunakan kreatifitas kita secara penuh.

Jika memerlukan pembuatan website yang simple, mudah, dan hanya memerlukan waktu singkat, lebih baik menggunakan bootstrap. Namun jika ingin membuat website from scratch dan melakukan kustomisasi yang kompleks dengan jangka waktu yang lama, lebih baik menggunakan tailwind.
  
### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Pertama, saya mengubah tampilan halaman `login` menggunakan bantuan dari bootstrap. Saya menggunakan `Card` untuk menjadi container utama dari form login saya. Untuk bagian formsnya, saya mengubah dari bentuk tabel dari tutorial dan memecahnya satu-satu agar bisa dimodikasi menggunakan bootstrap. Selain itu, saya juga mengubah background dari halaman `login` menjadi sebuah gambar agar terlihat lebih berwarna dan menarik. 
 
login.html
```html
    ...
    <section class="vh-100" style="backdrop-filter: blur(20px);">
            <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col-12 col-md-8 col-lg-6 col-xl-5" >
                <div class="card shadow-2-strong" style="border-radius: 1rem; background-color: whitesmoke;">
                    <div class="card-body p-5 text-center">
                        <form method="POST" action="">
                            <h1 class="mb-5" style="font-weight: bold; padding: 0px">Lontongistic</h1>
                            <h1 class="mb-5" style="font-weight: lighter; padding: 0px; font-size: 20px;">"Your digital inventory maestro"</h1>
                            {% csrf_token %}
                            <h3 class="mb-5" style="text-align: left;">Login</h3>
                            <div class="form-outline mb-4">
                                <input type="text" name="username" placeholder="Username" class="form-control">
                            </div>
                
                            <div class="form-outline mb-4">
                                <input type="password" name="password" placeholder="Password" class="form-control">
                            </div>
                            <div class="mb-4" style="padding-bottom:20px;">
                                Don't have an account yet? <a href="{% url 'main:register' %}" style="padding-left: 5px;"> Register Now </a>
                            </div>
                            {% if messages %}
                            <ul>
                                {% for message in messages %}
                                    <li>{{ message }}</li>
                                {% endfor %}
                            </ul>
                            {% endif %}   
                            <input class="btn btn-primary btn-lg btn-block" type="submit" value="Login" style="width: 200px; background-color: #708951;">
                        </form>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </section>
    ...
```

- Kemudian, saya menggunakan kode bootstrap yang serupa dengan login page saya untuk mengubah tampilan halaman `register` serta tampilan halaman untuk `menambahkan item` dan menyesuaikan kode sesuai dengan apa yang seharusnya di input.

register.html
```html
    <section class="vh-100" style="backdrop-filter: blur(20px);">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                    <div class="card shadow-2-strong" style="border-radius: 1rem;">
                        <div class="card-body p-5 text-center">
                            <form method="POST">
                                {% csrf_token %} 
                                <h1 class="mb-5" style="font-weight: bold;">Register</h1>
                                <div class="form-outline mb-4">
                                    <input type="text"  name={{form.username.name}} placeholder="Username" class="form-control form-control-lg"/>
                                </div>
                                <div class="form-outline mb-4">
                                    <input type="password" name={{form.password1.name}} placeholder="Password" class="form-control form-control-lg"/>
                                </div>
                                <div class="form-outline mb-4">
                                    <input type="password" name={{form.password2.name}} placeholder="Confirm Password" class="form-control form-control-lg"/>
                                </div>
                                <input class="btn btn-primary btn-lg btn-block" type="submit" name="submit" value="Daftar" style="width: 200px; background-color: #708951;"/>
                            </form>
                            {% if messages %}  
                                <ul>   
                                    {% for message in messages %}  
                                        <li>{{ message }}</li>  
                                        {% endfor %}  
                                </ul>   
                            {% endif %}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
```

create_product.html
```html
    <section class="vh-100" style="backdrop-filter: blur(20px);">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100" style="padding: 10px;">
                <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                    <div class="card shadow-2-strong" style="border-radius: 1rem; background-color: whitesmoke;">
                        <div class="card-body p-5 text-center">
                            <form method="POST" action="">
                                {% csrf_token %}
                                <h1 class="mb-5" style="font-weight: bold; padding: 0px">Add New Item</h1>
                                <div class="form-outline mb-4">
                                    <input type="text" name="name" placeholder="Item Name" class="form-control" >
                                </div>
                                <div class="form-outline mb-4">
                                    <input type="number" name="amount" placeholder="Amount" class="form-control">
                                </div>
                                <div class="form-outline mb-4">
                                    <input type="text" name="category" placeholder="Category" class="form-control">
                                </div>
                                <div class="form-outline mb-4">
                                    <input type="text" name="description" placeholder="Description" class="form-control" style="height: 100px;">
                                </div>
                                <input class="btn btn-primary btn-lg btn-block" type="submit" value="Add Item" style="width: 200px; background-color: #708951;"/>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
```

- Selanjutnya, saya mengubah tampilan pada `main` page dimulai dengan menambahkan `navbar` menggunakan bantuan dari bootstrap. `Navbar` saya memiliki 3 tombol yaitu `Home`, `Add New Item`, serta `Logout`.

```html
    ...
    <nav class="navbar navbar-expand-lg" style="background-color: #708951; border-radius: 10px;">
        <div class="container-fluid">
        <a class="navbar-brand" href="#" style="font-size: 40px; font-weight: bold; padding: 10px; vertical-align: auto; color: whitesmoke;">Lontongistic</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0" style="padding: 20px;">
            <li class="nav-item">
                <a class="nav-link" aria-current="page" href="#" style="font-size: 25px; padding-left: 25px; padding-right: 25x; color: whitesmoke;">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{% url 'main:create_product' %}" style="font-size: 25px; padding-left: 25px; padding-right: 25px; color: whitesmoke;">Add Item</a>
            </li>
            </ul>
            <span class="navbar-text">
                <a class="nav-link" href="{% url 'main:logout' %}" style="font-size: 25px; font-weight: bold; padding-left: 20px; padding-right: 20px; color: whitesmoke;">
                    Logout
                </a>
            </span>
        </div>
        </div>
    </nav>
    ...
```

- Lalu, saya juga menambahkan kontainer `Card` dengan bantuan bootstrap untuk merepresentasikan setiap barang yang disimpan.
```html
        ...
        <div class="card-container">
            {% for item in items %}
            <div class="card">
                <div class="card-header" style="font-weight: bold; background-color: #708951; color: white;">
                    {{ item.name }}
                </div>
                <div class="card-body">
                    <p>Amount: {{ item.amount }}</p>
                    <p>Description: {{ item.description }}</p>
                    <p>Category: {{ item.category }}</p>
                    <p>Date Added: {{ item.date_added }}</p>
                </div>
                <div class="card-footer">
                    <form method="post" action="{% url 'main:increase_item_amount' item.id %}">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-primary" style="background-color:  #708951; color: white;">Increase</button>
                    </form>
                    <form method="post" action="{% url 'main:decrease_item_amount' item.id %}">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-danger" style="background-color:  #708951; color: white;">Discard</button>
                    </form>
                    <form method="post" action="{% url 'main:remove_item' item.id %}">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-warning" style="background-color:  #708951; color: white;">Remove</button>
                    </form>
                </div>
            </div>
            {% endfor %}
        </div>
        ...
```

- Dan terakhir, saya mengubah background utama dari halaman serta mengubah warna-warna pada tabel, card, dan juga navbar menggunakan CSS agar memperindah tampilan website, serta menyelesaikan soal bonus.

Referensi Bootstrap :   
Login, Register, dan Create Item : https://mdbootstrap.com/docs/standard/extended/login/#
Navbar : https://getbootstrap.com/docs/5.2/components/navbar/  
Cards : https://getbootstrap.com/docs/5.0/components/card/

</details>
<details>
<summary><b>Tugas 6</h1></b></summary>

## Tugas 6

### 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Jawab : 

- Synchronous Programming

Pada synchronous programming, kode akan dieksekusi secara berurutan, sehingga jika ada blok kode yang melakukan operasi dan memakan waktu lama, maka program akan berhenti dan menunggu operasi tersebut selesai. Hal ini dapat menyebabkan terjadinya "blocking" pada aplikasi jika operasi memakan waktu yang lama.

- Asynchronous Programming 

Pada asynchronous programming, program dapat terus berjalan tanpa harus menunggu operasi yang memakan waktu. Hal tersebut dapat dilakukan dengan menggunakan callback, promise, atau async/await untuk menangani hasil operasi tersebut saat hasilnya telah tersedia. Dengan demikian, "blocking" pada aplikasi dapat dihindari menggunakan asynchronous programming.

Dapat disimpulkan bahwa synchronous programming mungkin kurang responsif terhadap input pengguna pada suatu aplikasi dan cenderung dapat mengalami "blocking". Sedangkan asynchronous programming lebih responsif terhadap input pengguna karena tidak menghentikan program demi menunggu operasi yang memerlukan waktu.

### 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Paradigma Event-Driven Programming adalah pendekatan pemrograman di mana kode merespons peristiwa atau kejadian yang terjadi dalam sistem atau aplikasi seperti mengklik tombol, mengisi forms, serta peristiwa lain seperti pemrosesan data yang diambil dari server melalui AJAX.

Berikut adalah contoh penerapan event-driven programming yang saya gunakan pada program saya untuk tugas ini. 

```html
...
<script>
    ...
    function addProduct() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
    }

    document.getElementById("button_add").onclick = addProduct
    ...
</script>
...

```

Potongan kode tersebut berasal dari file `main.html`, dimana pada bagian `script`, terdapat fungsi yang bernama `addProduct` yang berfungsi untuk menambahkan product ke dalam database menggunakan AJAX. Lalu pada baris kode `document.getElementById("button_add").onclick = addProduct`, baris tersebut berfungsi untuk menjalankan fungsi `addProduct` saat button yang memiliki id `button_add` ditekan.

### 3. Jelaskan penerapan asynchronous programming pada AJAX.

Asynchronous JavaScript and XMLHTTP atau biasa disebut AJAX merupakan salah satu konsep yang menerapkan metode asynchronous dalam menjalankan pekerjaannya. Biasa nya AJAX digunakan untuk melakukan permintaan data (request) dan menangani sebuah tanggapan (handling response), baik response dalam bentuk XML, Javascript ataupun JSON dari sebuah Rest API.

### 4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan. 

Fetch API adalah bagian dari JavaScript modern. Fetch API menggunakan Promise untuk mengelola respons HTTP yang membuat kode lebih bersih dan mudah dikelola. Sedangkan jQuery adalah sebuah build-in library dari JavaScript yang lebih lawas dan dirancang untuk menyederhanakan pengembangan web. jQuery menyediakan berbagai fungsi dan metode yang mempermudah tugas-tugas umum dalam pengembangan web, seperti manipulasi dokumen HTML, pengiriman permintaan HTTP asinkron (AJAX), animasi, dan penanganan peristiwa. 

Menurut saya, Fetch API adalah pilihan yang lebih baik karena lebih modern, kode yang dihasilkan lebih bersih, serta memiliki performa yang lebih baik dan lebih cocok digunakan untuk mengembangkan aplikasi web modern. 

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Membuat fungsi `get_item_json` pada `views.py` untuk mengambil data dalam bentuk JSON yang berisi sebagai berikut :

```python
def get_item_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))
```

- Membuat fungsi untuk menambahkan produk menggunakan AJAX dimulai dengan mengimport `csrf_exempt` dan membuat fungsi baru bernama `add_item_ajax` :

```python
@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, amount=amount, category=category, description=description, user=user)
        new_product.save()


        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()
```

- Mengambil Item pada `main.html` menggunakan `fetch()` API dengan menambahkan tag block `<script>` di akhir kode HTML dan membuat fungsi asynchronous `getProducts` seperti berikut :

```html
<script>
        async function getProducts() {
            return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
        }
...
```

- Menghapus cards yang telah saya buat sebelumnya hingga hanya menjadi `<div class="card-container" id="card-product"></div>` dan membuat fungsi asynchronous `refreshProducts()` pada blok `<script>` untuk memunculkan cards menggunakan AJAX dan merefresh data dari item serta mengupdate informasi jumlah item yang tersimpan secara asynchronous :

```html
<script>
    ...
    async function refreshProducts() {
        const products = await getProducts()
        document.getElementById("card-product").innerHTML = ""
        let htmlStringCards = ``
        let totalItem = 0
        products.forEach((item) => {
            htmlStringCards += `
            <div class="card">
                <div class="card-header" style="font-weight: bold; background-color: #708951; color: white;">${item.fields.name}</div>
                <div class="card-body">
                    <p>Amount: ${item.fields.amount}</p>
                    <p>Description: ${item.fields.description}</p>
                    <p>Category: ${item.fields.category}</p>
                    <p>Date Added: ${item.fields.date_added}</p>
                </div>
                <div class="card-footer">
                    <a href='increase_item_amount/${item.pk}'>
                        <button type="submit" class="btn btn-primary" style="background-color:  #708951; color: white;">Increase</button>
                    </a>
                    <a href='decrease_item_amount/${item.pk}'>
                        <button type="submit" class="btn btn-danger" style="background-color:  #708951; color: white;">Decrease</button>
                    </a>
                    <a href='remove_item/${item.pk}'>
                        <button type="submit" class="btn btn-warning" style="background-color:  #708951; color: white;">Delete</button>
                    </a>
                    <button class="btn btn-warning" style="background-color:  #708951; color: white;" onclick="deleteItem(${item.pk})">Delete by AJAX</button>
                </div>
            </div>
            `
            totalItem++
        })
        document.getElementById("card-product").innerHTML = htmlStringCards
        document.getElementById("item-amount").innerHTML = `There are ${totalItem} unique items in your inventory`
    }
    
</script>
```

- Menambahkan modal baru sebagai form berbentuk popup untuk menambahkan item menggunakan AJAX

```html
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form id="form" onsubmit="return false;">
                        {% csrf_token %}
                        <div class="mb-3">
                            <label for="name" class="col-form-label">Name:</label>
                            <input type="text" class="form-control" id="name" name="name"></input>
                        </div>
                        <div class="mb-3">
                            <label for="amount" class="col-form-label">Amount:</label>
                            <input type="number" class="form-control" id="amount" name="amount"></input>
                        </div>
                        <div class="mb-3">
                            <label for="category" class="col-form-label">Category:</label>
                            <textarea class="form-control" id="category" name="category"></textarea>
                        </div>
                        <div class="mb-3">
                            <label for="description" class="col-form-label">Description:</label>
                            <textarea class="form-control" id="description" name="description"></textarea>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Item</button>
                </div>
            </div>
        </div>
    </div>
```

serta menambahkan button untuk memunculkan form baru tersebut pada navbar dengan menambahkan :

```html
<button class="nav-link" data-bs-toggle="modal" data-bs-target="#exampleModal" style="font-size: 25px; padding-left: 25px; padding-right: 25px; color: whitesmoke;">Add Item by AJAX</button>
```
- Membuat fungsi pada bagian `<script>` untuk menambahkan Item :

```html
<script>
...
function addItem() {
            fetch("{% url 'main:add_item_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(refreshProducts)

            document.getElementById("form").reset()
            return false
        }
```

kemudian menambahkan fungsi tersebut sebagai fungsi `onClick` pada button yang terdapat di dalam modal : 
```html
<script>
    ...
    document.getElementById("button_add").onclick = addItem
```

- Membuat fungsi untuk menghapus item menggunakan AJAX pada `views.py` bernama `delete_item_ajax` yang memiliki parameter berupa id dari item yang akan dihapus :

```python
@csrf_exempt
def delete_item_ajax(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponse(b"DELETED", status=201)
```

- Menambahkan fungsi `deleteProduct(id)` pada bagian `<script>` di `main.html` untuk menghapus item dengan AJAX :

```html
<script>
    ...
    function deleteItem(id) {
        fetch("/delete-item-ajax/" + id + "/", {
            method: "POST"
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
    }

```

dan menambahkan button pada cards untuk menghapus item menggunakan AJAX pada `main.html` dan menambahkan atribut `onclick="deleteItem(${item.pk})"` untuk memanggil fungsi deleteItem saat button di click :

```html
<button class="btn btn-warning" style="background-color:  #708951; color: white;" onclick="deleteItem(${item.pk})">Delete by AJAX</button>
```

- Melakukan perintah collecstatic dengan melakukan mapping untuk output file static ke directory yang sesuai dengan memodifikasi bagian `STATIC_URL` dan `STATIC_ROOT` pada `settings.py`:

```python
STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

lalu menjalankan perintah collectstatic pada terminal : 
```
python manage.py collectstatic
```

</details>
