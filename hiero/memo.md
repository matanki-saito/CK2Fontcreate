# Map用フォント

## 準備
 - Javaが起動する環境。JREをインストールすればOK。
 - この[リンク](https://drive.google.com/open?id=1mzlgumZn_YnE17VYVIQ_msHD_M6IGENN)からrunnable-hiero-ck2.jarをダウンロードしておく。
 - この[リンク](http://ch.nicovideo.jp/sevrunear/blomaga/ar539518)からNvcompressFrontEndをダウンロードしてzip解凍しておく。
 - この[リンク](https://drive.google.com/open?id=1Qb5pyH4Cx3ouBIMbEw3KhnlTspx5Qfs_)からフォントをダウンロードしてインストールしておく

## フォントfntとテクスチャpng画像の生成
runnable-hiero.jarをダブルクリックして、起動したHieroからaoyagireisyo60.hieroを読み込む。
![img](2018-03-21_16h44_47.png)

メニュー＞File＞Save BMFontで、ファイルを書き出す用に指示。時間はかかるが指定した場所にfntファイルとpngファイルが出来上がるのを待つ。

## テクスチャpng画像をddsに変換する
NvcompressFrontEndを起動して、規定のフォーマットをRGBAにする。

![img2](2018-03-21_16h48_12.png)

pngファイルをD&Dして、変換ボタンを押す。一瞬でddsに変換される。

