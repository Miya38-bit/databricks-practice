# databricks-pyspark

VSCode + Databricks Connect を使ったPySpark実務開発の練習リポジトリ。

## 環境

| 項目 | バージョン |
|---|---|
| Python | 3.12.9 |
| databricks-connect | 16.1.7 |
| Databricks Runtime | 18.1 (Spark 4.1.0) |

## セットアップ

```bash
# 仮想環境の作成と有効化
python -m venv .venv
.venv\Scripts\activate

# 依存パッケージのインストール
pip install databricks-connect==16.1.7

# Databricks認証（ブラウザが開く）
databricks auth login --host <ワークスペースURL>
```

`~/.databrickscfg` に以下を追記：

```ini
[databricks-dev]
host = <ワークスペースURL>
cluster_id = <クラスターID>
```

## 接続確認

```bash
python test.py
# → Spark バージョンが表示されれば成功
```

## 学習進捗

ROADMAP.md（ローカルのみ）を参照。
