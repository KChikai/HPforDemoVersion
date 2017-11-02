鬼塚研究室ホームページβ版 (2017.11.3)
=============

ホームページ？

***DEMO:***


<p align="center">
<img src="https://github.com/OnizukaLab/HomePageDemo/blob/master/demo.gif?raw=true" alt="demo">
</p>

<br>


Requirements
-------

- Django (python3系) バージョンは1.10.1，

  pipとかでインストール可能 `pip install django==1.10.1`

- static files は別途 vishnu に入れているのでローカルに入れる必要あり．下記参照．

<br>


Features
-----------

変更点

* static file を極力減らす　 

* 各種headerとfooterの追加

* views, urls, models の統合

<br>


How to see this Demo
-----------

置き場所が変わってるので注意

1. `git clone https://github.com/OnizukaLab/HomePageDemo.git`

2. vishnuの`E:\Shares\users\home\chikai\data\hp_demo\images`（静的ファイル用ディレクトリ）
を`demo/static`下にimageディレクトリごと置く．(もしディレクトリがなければ`E:\Shares\users\home\_graduates\2018\chikai`内にあるはず)

3. 同様にvishnu`E:\Shares\users\home\chikai\data\hp_demo\setting_local.py`を`HPDemo`ディレクトリ下に置く (`settings.py`と同じ場所)．

4. `python manage.py runserver` でローカル8000番ポートに web server が起動される．

5. `http://localhost:8000/demo/embedding/`にブラウザでアクセスすることで見れる．

6. 楽しい．✌('ω'✌ )三✌('ω')✌三( ✌'ω')✌

<br>




Reference
---------

使用している主なライブラリ．

- [Material Cards][mc]: jQuery を用いた Card Design
- [salvattore][sal]: CSSドリブンなdivボックスのレスポンシブな配置ライブラリ
- [AOS][aos]: スクロール要素に動きを付けるアニメーションを簡単に実装できるライブラリ
- [Slidebars][side]: スマホやタブレットのサイドバーを簡易的に実装することができるライブラリ

[mc]: https://github.com/marlenesco/material-cards "mc"
[sal]: https://github.com/rnmp/salvattore "sal"
[aos]: https://github.com/michalsnik/aos "aos"
[side]: https://github.com/adchsm/Slidebars "side"