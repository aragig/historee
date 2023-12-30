# アクション履歴を管理するPythonパッケージ

画像変換などの思い処理を管理するのに役立ちます。

Historee - 「履歴(History)」と「記録する(Record)」を組み合わせた造語。

## Install


```shell
pip3 install git+https://github.com/aragig/historee.git
```

## Update

```shell
pip3 install --upgrade git+https://github.com/aragig/historee.git
```


## Usage: 画像ファイル変換などの履歴管理に使うケース

```python
# HistoryManager インスタンスの作成
history_manager = HistoryManager('path/to/history.csv')


def convert_image(src_path):
    # 履歴が存在するか確認
    if history_manager.history_exists(src_path):
        # ファイルのの最終更新日時を取得
        last_modified = os.stat(src_path).st_mtime
        # ファイルのの最終更新日時が履歴のタイムスタンプより新しいか確認
        if history_manager.is_newer_than_history(src_path, last_modified):
            # 画像を変換する処理
            pass
        else:
            # 何もしない
            pass
    else:
        # 画像を変換する処理
        # 履歴へ追加
        history_manager.add_history(src_path)

```
