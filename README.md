# インストール項目

## Pythonで OpenCV を使用できるようにする
```
libgl1-mesa-dev
```

## ffmpeg を使用できるようにする
```
wget https://www.johnvansickle.com/ffmpeg/old-releases/ffmpeg-4.2.2-arm64-static.tar.xz
tar xvf ffmpeg-4.2.2-arm64-static.tar.xz
cp -ip ./ffmpeg-4.2.2-arm64-static/ffmpeg /usr/local/bin/
cp -ip ./ffmpeg-4.2.2-arm64-static/ffprobe /usr/local/bin/
```

## font を使用できるようにする
```
apt-get install -y fonts-ipafont-gothic
```

## Text-to-Speech を使用できるようにする
### API を設定する
1. サービス アカウントを作成します。
    1. Cloud Console で [サービス アカウントの作成] ページに移動します。
    2. プロジェクトを選択します。
    3. [サービス アカウント名] フィールドに名前を入力します。Cloud Console は、この名前に基づいて [サービス アカウント ID] フィールドに入力します。
    4. [作成] をクリックします。
    5. [ロールを選択] フィールドをクリックします。
    6. [続行] をクリックします。
    7. [完了] をクリックして、サービス アカウントの作成を完了します。
2. サービス アカウント キーを作成します。
    1. Cloud Console で、作成したサービス アカウントのメールアドレスをクリックします。
    2. [キー] をクリックします。
    3. [鍵を追加]、[新しい鍵を作成] の順にクリックします。
    4. [作成] をクリックします。JSON キーファイルがパソコンにダウンロードされます。
    5. [閉じる] をクリックします。


### JSON キーを設定する
1. サーバーにダウンロードしたJSONキーを設置する。
2. 下記のコマンドを実行しJSONキーを読み込む。
```
export GOOGLE_APPLICATION_CREDENTIALS="./service-account-xxxxxx-xxxxxxxxxxxx.json"
```