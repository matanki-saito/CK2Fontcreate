# CK2fontcreate
## これはなに？
　Steam配信されているWindows版Crusader Kings IIの日本語化パッチの副産物です。パッチはこのプログラムを使って作成されたフォントのみを受け付けます。

## 環境
 - Windows10 以上
 - python 3以上をインストールしておく

## 使い方
 同梱のbmfont64.exeを使用して、作成したいフォントのconfigurationファイル（.bmfc）をbmfcフォルダに保存してください。この時文字は空にしてください。含めたい文字はsourceフォルダに任意の名前のBOM付きのUTF-8のtxtファイルに入れておきます。こちらで予めCP1252の追加文字と大体のSHIFTJISの範囲の文字を入れたテキストを用意していますので、これ以外で必要な文字をtxtとして追加してください。

 マップフォントの用に容量の関係で、特定の文字だけを入れたフォントを作る必要がある場合、bmfont64.exeの時点で必要な文字を入れておき、上記のフォルダにconfigurationファイルを保存後、拡張子（.bmfc）にアンダースコアを入れて._bmfcにしてください。generate.pyはその拡張子のフォント生成のときのみ、sourceフォルダのテキストを追加してフォントを生成しません。

 準備が整ったら、generate.pyを実行します。outフォルダに生成されたフォントが入ります。

## 注意点
花文字（GenkaiMincho100）の文字セットの最新版は下記にあります。
https://drive.google.com/drive/folders/1GUxQuOP6-Pm1ZSn-0o7F4yaOFmnqDvWQ?usp=sharing

## ライセンス
　generate.pyはMITライセンス。bmfont64.exeはbmfontのソースライセンスに準拠。