# learning-log
# 記録を残すリポジトリ
これがギットハブでみえていたらおｋ


## 第2週：Claude APIを使う準備

### 2-1 Anthropic Consoleの準備（10/10）

**やったこと**
- Anthropic Console（platform.claude.com）にアカウント登録
- 少額のクレジットを購入（前払い、使った分だけ減る）
- APIキーを発行し、安全な場所に保管
- 利用上限を設定

**学んだこと**
- APIは、自分のアプリからClaudeにお願いするための「注文窓口」
- ConsoleはClaude.aiとは別アカウント・別課金
- APIキーは「自分の残高を使える合言葉」。漏れると他人に使われるので、厳重に保管する
- 有効期限と利用上限は、漏れたときやバグのときの被害を抑える保険

### 2-2 APIキーを安全に使う設定（10/10）

**やったこと**
1. `.gitignore`に`.env`と`.venv`を書く
2. `.env`に`ANTHROPIC_API_KEY=キー`の形で書く（`=`の前後にスペースや引用符は付けない）
3. 仮想環境を有効にして`python -m pip install python-dotenv`を実行
4. `git check-ignore .env`で、`.env`がGit管理の対象外になっていることを確認

**学んだこと**
- キーはコードに直接書かず、`.env`に分けてGitHubに上げない
- `.gitignore`自体はGitHubに上がるが、中身は除外するファイル名だけなので問題ない
- `.env`は1つのプロジェクトにつき1つ置き、サービスごとに1行ずつ追加できる
- キーが漏れたかもしれないときは、Consoleでそのキーを無効化して作り直す

**つまずいたこと**
- `pip install`で「Fatal error in launcher」が出た
  - 原因：フォルダの場所が変わったため、`.venv`が古いパスを覚えたままだった
  - 対処：`.venv`を作り直し、`python -m pip install`で入れ直した
- `pip`ではなく`python -m pip`と書くほうが、今のPythonに確実に入る
