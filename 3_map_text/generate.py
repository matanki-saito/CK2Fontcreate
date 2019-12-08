import os
import subprocess

from PIL import Image, ImageFilter, ImageEnhance


def invert(image):
    return image.point(lambda p: 255 - p)


def nega_posi(name, ext):
    # 画像反転。組み込みのinvertではRGBAを処理できないために一度splitしている。
    im = Image.open('./out/' + name + ext).convert('RGBA')
    r, g, b, a = im.split()
    r, g, b = map(invert, (r, g, b))

    # 透明度を上げる（アルファを下げる）
    enhancer = ImageEnhance.Brightness(a)
    a_enh = enhancer.enhance(0.75)

    # RGBとAを結合
    im_enh = Image.merge(im.mode, (r, g, b, a_enh))

    # ぼかし
    im_g = im_enh.filter(ImageFilter.GaussianBlur(radius=0.1))

    # 上書き
    im_g.save('./out/' + name + ".tga", quality=100)


def generate_bm_font(name, ext, add_source_file):
    # コマンド
    cmd_list = [
        '../1_tool/bmfont64.exe',
        '-c', "./bmfc/" + name + ext,
        '-o', "./out/" + name + ".fnt"
    ]

    # 追加ファイルあり
    if add_source_file is not None:
        cmd_list.append('-t')
        cmd_list.append(add_source_file)

    # BFFont実行
    subprocess.call(" ".join(cmd_list))


def read_seed_text_from_file(name):
    f = open('./source/' + name + '.txt', "r", encoding='utf_8_sig')
    text = f.read()
    f.close()
    return text


def main():
    source_text = ""

    # sourceフォルダ内を走査
    files = os.listdir("./source")
    for file in files:
        # 拡張子とファイル名を分離
        file_name, file_ext = os.path.splitext(file)

        # 拡張子がtxt
        if file_ext == ".txt":
            source_text = source_text + read_seed_text_from_file(file_name)

    # source textを作成
    f = open('source.txt', 'w', encoding='utf_8_sig')
    f.write(source_text)
    f.close()

    # bmfcフォルダ内を走査
    files = os.listdir("./bmfc")
    for file in files:
        # 拡張子とファイル名を分離
        file_name, file_ext = os.path.splitext(file)

        # フォント生成
        generate_bm_font(file_name, file_ext, add_source_file="source.txt")

    # outフォルダ内を走査
    files = os.listdir("./out")
    for file in files:
        # 拡張子とファイル名を分離
        file_name, file_ext = os.path.splitext(file)

        if file_ext == ".png":
            # ネガポジ反転
            nega_posi(file_name, file_ext)

            # 変換
            # convertPngToDds(file_name, file_ext);


if __name__ == "__main__":
    # execute only if run as a script
    main()
