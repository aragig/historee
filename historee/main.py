import csv
import hashlib
import time


class HistoryManager:
    __history_records = {}
    """
    CSVファイルのフォーマット
        hash,text,last_timestamp

    ** hashはtextのMD5ハッシュ値 **
    """

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.__load_history_from_file()

    def __load_history_from_file(self):
        # CSVファイルから履歴データを読み込む
        with open(self.file_path) as file:
            reader = csv.reader(file)
            for row in reader:
                self.__history_records[row[0]] = {
                    'text': row[1],
                    'last_timestamp': float(row[2]),
                }

    def __write_history_to_file(self):
        # 履歴データをCSVファイルに書き込む
        with open(self.file_path, mode='w') as file:
            for key, data in self.__history_records.items():
                line = '{},{},{}\n'.format(key, data['text'], data['last_timestamp'])
                file.write(line)

    def __generate_key(self, text):
        # テキストからMD5ハッシュキーを生成する
        return hashlib.md5(text.encode("utf-8")).hexdigest()

    def history_exists(self, text):
        key = self.__generate_key(text)
        return self.__history_records.get(key, None) is not None

    def add_history(self, text):
        # 新しい履歴データを追加または更新する
        key = self.__generate_key(text)
        current_timestamp = time.time()
        self.__history_records[key] = {'text': text, 'last_timestamp': current_timestamp}
        self.__write_history_to_file()

    def is_newer_than_history(self, text, timestamp):
        """
        与えられたテキストの履歴が存在し、かつ指定されたタイムスタンプよりも古いかどうかを確認する。

        :param text: 履歴を検索するテキスト
        :param timestamp: 比較するタイムスタンプ
        :return: 履歴が存在しない、または履歴のタイムスタンプが引数のタイムスタンプより古い場合はTrue、それ以外はFalse
        """
        key = self.__generate_key(text)
        history = self.__history_records.get(key)
        if history is None:
            return True
        return history['last_timestamp'] < timestamp
