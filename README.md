## Nama    : Reyhan Zada Virgiwibowo
## NPM     : 2206081723
## Kelas   : PBP C
## Link Aplikasi : https://lontongistic.adaptable.app/main/

<details>
<summary><b>Tugas 2</b></summary>

## Tugas 2
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

