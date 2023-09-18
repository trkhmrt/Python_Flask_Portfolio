from datetime import *
import requests
from flask import *
import sqlite3
app = Flask(__name__)


#SAYFA İÇERİĞİ
@app.route('/',methods=["GET","POST"])
def Anasayfa():
    if request.method=="POST":
        abone_ol_tarihi = date.today()
        print(abone_ol_tarihi)
        mail=request.form['mail']
        con=sqlite3.connect("CvDB.db")
        cur=con.cursor()
        cur.execute(f"insert into Aboneler (AboneMail,AbonelikTarihi) values('{mail}','{abone_ol_tarihi}')")
        con.commit()
        return redirect(url_for('Anasayfa'))
    return render_template('Home.html')


@app.route('/About')
def Hakkinda():
    con = sqlite3.connect("CvDB.db")
    cur = con.cursor()
    cur.execute(f"select * from Hakkımda")
    veri = cur.fetchone()
    return render_template('About.html', hakkımda_verisi=veri)


@app.route('/Services')
def Hizmetler():
    return render_template('Services.html')

@app.route('/Portfolio')
def Portfolyo():
    return render_template('Portfolio.html')

@app.route('/Pricing')
def Ucretlendirme():
    return render_template('Pricing.html')

@app.route('/Contact')
def Iletisim():
    return render_template('Contact.html')




#ADMİN SAYFALARI

@app.route('/Admin')
def AdminSayfasi():
    return render_template('AdminPanelLayout.html')

@app.route('/AdminAbout',methods=["GET","POST"])
def AdminAboutSayfasi():
    if request.method=="POST":
        con = sqlite3.connect("CvDB.db")
        cur = con.cursor()
        baslik1=request.form['baslik1']
        altbaslik=request.form['altbaslik']
        aciklama=request.form['aciklama']
        baslik2=request.form['baslik2']
        misyon=request.form['misyon']
        vizyon=request.form['vizyon']
        cur.execute(f"update Hakkımda set Baslik='{baslik1}',AltBaslik='{altbaslik}',Aciklama='{aciklama}',Baslik2='{baslik2}',Misyon='{misyon}',Vizyon='{vizyon}'")
        con.commit()


    con = sqlite3.connect("CvDB.db")
    cur = con.cursor()
    cur.execute(f"select * from Hakkımda")
    veri=cur.fetchone()
    return render_template('AdminAbout.html',hakkımda_verisi=veri)

@app.route('/Adminsubcribers',methods=["GET","POST"])
def AdminSubscribers():
    if request.method=="POST":
        con = sqlite3.connect("CvDB.db")
        cur = con.cursor()
        abone_id = request.form['abone_id']
        cur.execute(f"delete from Aboneler where AboneID='{abone_id}'")
        con.commit()
        return redirect(url_for('AdminSubscribers'))
    con = sqlite3.connect("CvDB.db")
    cur = con.cursor()
    cur.execute("select * from Aboneler")
    aboneler=cur.fetchall()
    return render_template('AdminSubscribers.html',aboneler=aboneler)

@app.route('/Adminservices',methods=["GET","POST"])
def AdminServices():
    con = sqlite3.connect("CvDB.db")
    cur = con.cursor()
    cur.execute(f"select * from Hizmetler")
    veri = cur.fetchone()
    return render_template('AdminServices.html',veri=veri)

@app.route('/Adminpricing')
def AdminPricing():
    return render_template('AdminPricing.html')

@app.route('/Admincontact')
def Admincontact():
    return render_template('AdminContact.html')

@app.route('/Adminportfolio')
def Adminportfolio():
    return render_template('AdminPortfolio.html')


if __name__ == '__main__':
    app.run()
