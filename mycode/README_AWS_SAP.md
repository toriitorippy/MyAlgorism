# AWS Solutions Architect Professional (SAP) Exam Question Generator

このモジュールは、AWS Solutions Architect Professional (SAP) 試験の練習問題を提供します。

## 機能

- 複数のAWSドメインにわたる問題集
- ランダムクイズ機能
- ドメイン別の問題フィルタリング
- 問題と解説のJSON形式でのエクスポート
- インタラクティブなコマンドラインインターフェース

## 使用方法

### モジュールの実行

```bash
python aws_sap_questions_main.py
```

### メインメニュー

1. **ランダムクイズを受ける**: ランダムに選ばれた問題でクイズを受けます
2. **ドメイン別クイズを受ける**: 特定のAWSドメイン（ネットワーキング、セキュリティなど）に関する問題でクイズを受けます
3. **利用可能なドメインを表示**: サポートされているAWSドメインとそれぞれの問題数を表示します
4. **問題をJSONにエクスポート**: 問題集をJSON形式でファイルにエクスポートします
5. **終了**: プログラムを終了します

### 対応しているAWSドメイン

- compute: コンピューティングとコンテナ
- storage: ストレージソリューション
- database: データベースサービス
- networking: ネットワーク設計と接続性
- security: セキュリティとアイデンティティ
- migration: 移行と転送
- cost: コスト最適化
- ha: 高可用性と災害復旧
- serverless: サーバーレスアーキテクチャ
- hybrid: ハイブリッドアーキテクチャ

## プログラムの拡張

### 新しい問題の追加

`aws_sap_questions.py` ファイルの `_create_question_bank` メソッドに新しい問題を追加できます：

```python
questions.append(AWSQuestion(
    question_text="質問文をここに記入",
    options={
        "A": "選択肢A",
        "B": "選択肢B",
        "C": "選択肢C",
        "D": "選択肢D"
    },
    correct_answer="正解の選択肢（A、B、C、またはD）",
    explanation="解説文をここに記入",
    domain="該当するドメイン"
))
```

## テスト

テストを実行するには：

```bash
python -m unittest test_code.test_aws_sap_questions
```

## 注意事項

- このモジュールは学習目的で作成されており、実際のAWS SAP試験の問題とは異なる場合があります
- 実際の試験準備には、AWS公式のトレーニングリソースも併せて利用することをお勧めします