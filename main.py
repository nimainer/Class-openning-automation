import webbrowser

class_ = input(""" 
    what class you want to open ?

1-math
2-karofanavari
3-ghoran (gh-o-r-an)
4-arabi
5-farsi
6-tafkor va sabk zendegy
7-hadie ha ye asemani
8-motaleaate ejtemai
9-english
10-ooloom tajrobi
11-farhang va honar

""")

new=2

url1="https://openlearn.iut.ac.ir/mod/adobeconnect/view.php?id=4868";
url2="https://openlearn.iut.ac.ir/mod/adobeconnect/view.php?id=5089";
url3="https://openlearn.iut.ac.ir/mod/adobeconnect/view.php?id=4860";
url4="https://openlearn.iut.ac.ir/mod/adobeconnect/view.php?id=4866";
url5="https://openlearn.iut.ac.ir/mod/adobeconnect/view.php?id=4871";
url6="https://openlearn.iut.ac.ir/mod/adobeconnect/view.php?id=4906";
url7="https://openlearn.iut.ac.ir/mod/adobeconnect/view.php?id=4869";
url8="https://openlearn.iut.ac.ir/mod/adobeconnect/view.php?id=4874";
url9="https://openlearn.iut.ac.ir/mod/adobeconnect/view.php?id=4872";
url10="https://openlearn.iut.ac.ir/mod/adobeconnect/view.php?id=4873";
url11="https://openlearn.iut.ac.ir/mod/adobeconnect/view.php?id=4867";

if class_ == "1":
    webbrowser.open(url2,new=new);

#math

if class_ == "2":
    webbrowser.open(url1,new=new);

#karofanavari

if class_ == "3":
    webbrowser.open(url3,new=new);

#ghoran

if class_ == "4":
    webbrowser.open(url4,new=new);

#arabi

if class_ == "5":
    webbrowser.open(url5,new=new);

#farsi

if class_ == "6":
    webbrowser.open(url6,new=new);
    
#tafkor va sabk zendegy

if class_ == "7":
    webbrowser.open(url7,new=new);

#hadie ha ye asemani

if class_ == "8":
    webbrowser.open(url8,new=new);

#motaleaate ejtemai

if class_ == "9":
    webbrowser.open(url9,new=new);

#english

if class_ == "10":
    webbrowser.open(url10,new=new);

#ooloom tajrobi

if class_ == "11":
    webbrowser.open(url11,new=new);

#farhang va honar