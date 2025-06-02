# Django Todo アプリケーション

このプロジェクトは、Djangoフレームワークを使用して構築されたシンプルなTodoリストアプリケーションです。

## 機能

- タスクの一覧表示、詳細表示
- タスクの作成、更新、削除 (CRUD)
- ユーザー登録、ログイン、ログアウト
- ログインユーザーのみがタスクを操作可能

## 環境構築 (Docker)

このプロジェクトはDockerを使用して簡単に環境を構築できます。

### 前提条件

- Docker と Docker Compose がインストールされていること
- Git がインストールされていること

### セットアップ手順

1. リポジトリをクローンします。

   ```bash
   git clone <リポジトリのURL>
   cd todo-app-django
   ```

2. Dockerイメージをビルドします。

   ```bash
   docker compose up -d --build
   ```

   これで、アプリケーションがバックグラウンドで起動します。

3. アプリケーションを起動します。

   ```bash
   docker exec -it CONTAINER ID bash
   ```

   コンテナ内に入ります。

### アクセス

1. サーバーの起動

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

ブラウザで [http://localhost:8000](http://localhost:8000) にアクセスすると、Todoアプリケーションが表示されます。

2. データベースのマイグレーションを作成します。

   ```bash
   python manage.py makemigrations
   ```

3. データベースのマイグレーションを適用します。

  ```bash
   python manage.py migrate
   ```

4. 管理ユーザーを作成します (任意)。

   ```bash
   python manage.py createsuperuser
   ```

   画面の指示に従ってユーザー名とパスワードを設定してください。

## プロジェクト構成 (主要ファイル)

- `src/todoproject/todoapp/models.py`: タスクモデルの定義
- `src/todoproject/todoapp/views.py`: ビューロジック (CRUD, 認証)
- `src/todoproject/todoapp/urls.py`: URLルーティング
- `src/todoproject/todoapp/templates/`: テンプレートファイル
  - `todoapp/task_list.html`: タスク一覧
  - `todoapp/task_detail.html`: タスク詳細
  - `todoapp/task_form.html`: タスク作成・更新フォーム
  - `todoapp/task_confirm_delete.html`: タスク削除確認
  - `todoapp/login.html`: ログインフォーム
  - `todoapp/register.html`: ユーザー登録フォーム
- `Dockerfile`: アプリケーションのDockerイメージ定義
- `docker-compose.yml`: アプリケーションとデータベースサービス定義
