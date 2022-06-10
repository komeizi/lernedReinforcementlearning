#  Reinforcementlearning_algorithm
強化学習について学んだアルゴリズムなどを載せます。

# light_UI.py
```
streamlit run light_UI.py
```
を実行後,8501ポートでStreamlitのアプリケーションサーバが立ち上がる.ブラウザで開くと,```0_number_arm,1_number_arm,2_number_arm,e_percent```と書かれた数字を入力する箇所と```checek```と書かれたボタンが表示される.```e_percent```以外の入力箇所はカジノで言うスロットマシンの当たる確率であり,```e_percent```は```ε-greedy```法で使う確率である.それぞれに数字を入力後,```Check```を押すと下記のアルゴリズムを実行し,その結果,どのアームを引くべきか,その番号を表示してくれる.

# Greedy.py
ε-greedy法
