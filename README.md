# WIRED crawler
WIRED `wired.jp` から記事を収集します。  
Collect articles from the WIRED `wired.jp`.

## execution 
```
% python crawling_WIRED.py
```

カレントディレクトリに３種類のファイル、`xxxxxxxx_xxxxxx_wired.jsonl`と、`xxxxxxxx_xxxxxx_wired_cwlLog.jsonl`、`xxxxxxxx_xxxxxx_wired_html_list.jsonl`が出力されます。  
また、`xxxxxxxx_xxxxxx_html`という名前のフォルダに、収集したhtmlファイルが保存されます。  
（`xxxxxxxx_xxxxxx`には、実行した日付と時刻からユニークな文字列が入ります）  
Three files `xxxxxxxxxxxxxx_wired.jsonl`, `xxxxxxxxxxxxxx_wired_cwlLog.jsonl` and `xxxxxxxxxxxxxx_wired_html _list.jsonl` will be output in the current directory.  
In addition, the collected html files will be saved in a folder named `xxxxxxxxxxxx_xxxxxx_html`.  
(where `xxxxxxxxxxxx_xxxxxxxx` is a unique string from the date and time of execution)

* `xxxxxxxxxxxxxx_wired.jsonl`  
記事のURLと記事のテキストデータが保存されます。  
The text data of the article is saved.
* `xxxxxxxxxxxxxx_wired_cwlLog.jsonl`  
クロールしたURLと、htmlから抽出した記事のデータ（htmlタグ付きと、テキストデータ）が保存されます。  
The crawled URL and the article data (html tagged and text data) extracted from the html are saved.
* `xxxxxxxxxxxxxx_wired_html _list.jsonl`  
`xxxxxxxxxxxx_xxxxxx_html`に保存されているhtmlのファイル名と、収集元のURLが保存されます。  
The file name of the html file stored in `xxxxxxxxxxxxxxxxx_xxxxxxxxx_html` and the URL of the collection source will be saved.
* `xxxxxxxxxxxx_xxxxxx_html`  
収集したhtmlはこのフォルダに保存されます。  
The collected html is stored in this folder.

## Saved data format

### xxxxxxxxxxxxxx_wired.jsonl

１記事につき、１行のJSONフォーマットで保存されます。（JSONLフォーマット）内容は下記の通り。  
One line per article will be saved in JSON format.(JSONL Format) The contents are as follows

```
{"url": "https://www....", "text":"Article Data"}
{"url": "https://www....", "text":"Article Data"}
{"url": "https://www....", "text":"Article Data"}
.....
```

Example.
```
{"url": "https://wired.jp/about/wired-japanese-edition/", "text": "Wired Japanese Edition\n『WIRED』は、テクノロジーによって、生活や社会、カルチャーまでを包括したわたしたち自身の「未来がどうなるのか」についてのメディアです。\n『WIRED』は1993年、米国でプリントマガジンとして登場しました。以来、テクノロジーという窓から社会や文化を切り取り、その「ありうべき未来像」を世に問うてきました。そのスタンスはいまなお変わることなく、英国、イタリア、ドイツ、そして日本で出版されている各国語版のWIREDは、もれなくその視座を受け継いでいます。\n創刊から1年後に、WIREDの兄弟分として「HotWired」というウェブサイトが立ち上がりました。これは世界で初めてのウェブマガジンとされています。その後も時代の移り変わり、技術の進歩とともにWIREDは、読者とのコミュニケーションの形態を拡張してきました。\nそしていま、わたしたちは多種多様な「窓」を手にしています。レイヤーは多層化し、情報の流れる速度や届く射程がそれぞれの階層において異なる、複雑な社会がかたちづくられています。そして、その社会の姿は、1つのチャンネルを通したコミュニケーションだけでは、よりよく映し出すことが困難です。\n雑誌からスタートしたWIREDは、社会の多層性に合わせ、ウェブやソーシャルメディア、電子書籍にリアルイヴェントと、メディアとしての可能性を拡張して続けてきました。さらに2016年4月からはより新しいチャレンジに挑んでいます。ニュービジネスとカテゴライズする領域において、「発信」から「実装」へとメディアの役割を拡張しています。"}
{"url": "https://wired.jp/article/best-bike-helmets/", "text": "自転車ヘルメットはどう選ぶ？ 人気ブランドから目的別まで、多様なスタイルに対応するおすすめ11選：WIRED SHOPPING GUIDE\n2023年4月から道路交通法が一部改正され、自転車のヘルメット着用が努力義務化された。努力義務に法的な強制力はないが、ヘルメットの着用を習慣化するいいきっかけになるだろう。そこで、最適なヘルメットの選び方や車種別・目的別のおすすめを紹介する。\n自転車通勤から通学、ポタリングまで。あると便利なおすすめのサイクリングギア7選\nコロナ禍の都市部の通勤手段やアクティビティとしても定着した自転車。2023年4月1日から道路交通法が改正され、自転車に乗る際のヘルメットの着用が努力義務化された。これまでは「児童または幼児を自転車に乗せる際ヘルメットの着用に努めなければならない」と対象が限定されていたが、今後は「自転車に乗る全国民」が対象になったのである。\nこの努力義務化に法的な強制力はない。だが、ヘルメット非着用時の自転車事故による致死率は着用時の2倍以上にもなるので、今回の法改正を機に自分のサイクルスタイルに合ったヘルメットを取り入れてみてはいかがだろうか。\n以下にヘルメットの選び方をはじめ、おすすめのメーカーのほか、ロード、シティ、キッズ用などジャンル別のおすすめの製品を紹介する。\nINDEX\n1.自転車ヘルメットの選び方\n2.自転車ヘルメットおすすめメーカー\n3.ロードバイク向けおすすめヘルメット\n4.クロスバイク向けおすすめヘルメット\n5.ミニベロ・折りたたみ自転車向けおすすめヘルメット\n6.Eバイク向けおすすめヘルメット\n7.コストパフォーマンスでおすすめのヘルメット\n8.軽量タイプのおすすめヘルメット\n9.折りたたみタイプのおすすめヘルメット\n10.帽子型デザインのおすすめヘルメット\n11.キッズ向けおすすめヘルメット\n12.スマートテクノロジー搭載のおすすめヘルメット\n13.ヘルメット代わりになる頭部プロテクションデバイス\n14.WIRED SHOPPING GUIDEをチェック\n自転車ヘルメットを選ぶ際に最も重要になるのがサイズとフィット感だ。どれだけ高性能なヘルメットでも、サイズが合っていなければ性能を十分に発揮できない。必ず自分の頭に合ったサイズを選ぶよう気をつけてほしい。\nまた、ロードバイクなどスポーツバイク向けのヘルメットの場合は、海外メーカーなら「アジアンフィット」のタイプ、あるいは日本市場向けに開発された国内メーカーのヘルメットがフィットしやすいだろう。もしサイズやフィット感に不安がある場合は、店舗で試着してから購入したい。\nサイズだけでなく通気性や携帯性などの特性別では、以下に紹介するおすすめリストのなかから、愛車の種類やライディングスタイルに合わせて選ぶといい。\n1985年にカリフォルニア州サンタクルーズで創業したGIRO（ジロ）は、サイクリングアクセサリーとウィンタースポーツアクセサリーを展開するブランド。独自の構造と高い安全性、先進性で自転車ヘルメットのあり方に多大な影響を与えたとされ、世界中のトップライダーたちに支持され続けている。\n「アスリートやアスリートを目指す人々の命を守り、事故の影響を軽減する」というミッションを掲げ05年にスウェーデンで誕生したPOC（ポック）。ストックホルム郊外にあるラボで素材の研究者、インダストリアルデザイナー、グラフィックデザイナー、脳神経外科医など各分野の専門家によるアドバイスに基づき、プロテクション性能の向上に努めている。機能性とデザイン性を高次元で両立したヘルメットが揃う。\nGIROのロードバイク向けの定番モデル「AETHER」のアジアンフィットモデルが、「AETHER SPHERICAL AF」。自転車ヘルメットの安全機構として広まっている多方向衝撃保護システム（MIPS：Multi-directional Impact Protecti on System）をさらに進化させた「スフェリカルテクノロジー」を搭載。衝撃吸収性だけでなく、優れた通気性と快適なフィットを併せもつフラッグシップモデルだ。\n米国の消費者製品安全法（CPSA：Consumer Product Safety Act）に適合し、欧州の安全基準認証であるCE（Conformité Européenne）マークや「TUV（Technischer Überwachungs-Verein）」認証を得るなど、最も厳しいとされる安全基準をクリアしたヘルメットをラインナップするNUTCASE HELMET（ナットケースヘルメット）。サイクリングだけでなくスケート、カヌー、スノースポーツなどに対応するヘルメットが揃う。\n「VIO KIT」は、フロントに明るさが200ルーメンの白色ライト、サイドとリアに65ルーメンの赤とオレンジのLEDライトを搭載している（LEDライトはUSB充電が可能）。本体には耐衝撃性が高いABS樹脂製のアウターシェルを採用し、3つのベンチレーションで頭の蒸れを防ぐという。\nマグネットで片手で簡単に着脱できるバックル「FIDLOCK」を装備するほか、フィット感を簡単に調整できるアジャスタブル・スピンダイヤルを搭載。最適なフィット感を得られるインナーパッドも付属する。\n「1,000人の命を救う」というテーマから命名されたロサンゼルス生まれの「Thousand（サウザンド）」。シティサイクリストのためのミニマルなデザインが人気のブランドだ。\nフラッグシップモデルの「CHAPTER（チャプター）」は、自転車ヘルメットの安全機構として広まっている多方向衝撃保護システム（MIPS）を採用。ライナーとパッドの間に低摩擦のレイヤーを入れることで、転倒時に脳内で起きる回転運動の衝撃を軽減させる。\nまた、ヘルメット後部にあるダイヤルフィットシステムは、頭にフィットしやすいように調整できる。マグネット式のテールライトは明るさが最大30ルーメンの点滅が約4時間にわたって持続し、マルチユースアダプターを使えば自転車のシートポストやハンドルバーにも装着可能だ。自転車本体とヘルメットを連結して鍵をかけられるシークレットポップロック機構は、置き場に困るヘルメットの固定にひと役買ってくれる。\nレーシングスペックのモデルを多く発表してきたPOCのアーバンヘルメット「MYELIN（ミエリン）」。乗馬ヘルメットのような布製のアウターシェルに、軽量の発泡スチロールのヘルメットライナーなどの素材を接着剤を一切使わずに固定したことで、簡単に分解して個々の部品をリサイクルできる。サステナブルなマイクロモビリティとして注目されている電動アシスト自転車（Eバイク）で使うにはもってこいのコンセプトだ。\n後頭部にダイヤルアジャスターはなく、ストレッチ性のあるサイドストラップが伸縮してフィットする構造。布製のアウターシェルと通気孔のついたインナーシェルの組み合わせで熱がこもらず、気温が上がる季節もストレスなく着用できる。\nツール・ド・フランスのチャンピオンが着用していたことでも知られる『MET（メット）』は、イタリアで1987年に創業したスポーツサイクル用のヘルメットメーカー。「STRALE」は、上位モデルのデザインや技術を踏襲したリーズナブルなエントリーモデルだ。\n独自のエアフロー構造により効率的な空気の抜け道をつくり、蒸れることなく長時間のライドも快適という。頭部を一周するベルトが特徴的なアジャスターシステム「Safe-T Duo」が締めつけ感のない快適なフィットを実現する。\nアジアンフィットタイプではないのでフィットには注意が必要だが、実売価格が10,000円程度なので、ロードバイク用ヘルメットの入門アイテムとしておすすめだ。\nサイクルヘルメットで最軽量クラスの200g以下で、装着していることを忘れるほどの軽い製品が「VENTRAL LITE WF（ベントラル ライト WF）」。POCのヘルメットの全ラインナップでオールラウンドモデルに位置づけられる「VENTRAL」ラインでは軽量モデルとなり、アジア人の頭の形に合うワイドフィットが特徴だ。\n安全性を保ちながらもアウターシェルの使用面積を減らし、アジャストシステムにもより軽量な素材を採用するなど徹底して軽量化を図っている。レース用に開発されたモデルではあるが、街乗りでもヘルメット本体の重さによる着用時のストレスを最小限にしてサイクリングを楽しみ人におすすめだ。\n2013年にスペインで誕生した「CLOSKA（クロスカ）」は、デザイン性に優れたイノベーティブなプロダクトを発表している注目のブランド。ブランド初のプロダクトとして知られるヘルメットと同様の構造をもつ「LOOP」は、建築からインスピレーションを得たというフォルムが特徴的な折り畳みタイプだ。同心円状になったプラスチックとフォームラバーは入れ子式に折り畳むと6cmほどの厚さになり、かさばらずにバッグに収納できる。\n欧州の自転車ヘルメットやスケートボード用ヘルメットの安全基準であるCE規格（EN1078）と、米国消費者製品安全委員会（CPSC）の自転車ヘルメットの安全基準の2つをクリアしているので、安全性の高さも申し分ない。\n商品開発から安全実験、製造販売まで一貫して日本国内で手掛けている「OGK KABUTO（オージーケーカブト）。モーターバイクやロードレース用のヘルメットだけでなく、通勤通学やタウンユース向けモデルも多数展開している。\n日本人の頭の形にフィットするヘルメットは、一見するとヘルメットには見えない帽子型のデザインも人気だ。カジュアルなスタイルになじむ帽子型は、「DAYS」のほかに3種類のデザインがラインナップする。\n2004年に米国のボストンで誕生したヘルメットブランド「BERN（バーン）」。自転車だけでなくスキーやスノーボード、スケートのヘルメットを展開し、日本人の頭の形に合うジャパンフィットもラインナップする。\n2歳から6歳までの子どもにおすすめのキッズ用ヘルメットは、ボーイズ用にNINO（ニーノ）、ガールズ用にNINA（ニーナ）というモデルが用意されており、耐衝撃性の高さと軽さで子どもにとって快適な使用感を実現したという。バイザー付きのインナーは取り外して洗濯が可能。ベルクロでインナーのサイズを簡単に調整できる「EZ-FIT」システムは、日々大きくなる子供の頭のサイズに合わせてフィッティングしやすい。色やデザインの豊富なバリエーションが用意されているので、子どもの好みのモデルが見つかるはずだ。\n総合サイクルブランドとして有名なSPECIALIZED（スペシャライズド）の「S-WORKS PREVAIL II VENT MIPS」は、自動で転倒を検出して緊急連絡先に通報してくれる別売りのANGiセンサーを搭載可能。スマートフォンのアプリと連動させると、転倒の衝撃をセンサーが検知して登録した緊急連絡先にテキストメッセージとを位置情報を送信する。スマートフォンアプリ「Ride」はGPSを用いたアクティビティトラッキングが可能だ。\nヘルメット中央と側面のブリッジ7本を取り除いて通気口と通風路を改善し、空気の流れるスピードを速くすることで頭をより涼しい状態に保つという。部位ごとに発泡素材のタイプを最適化した「Energy Optimized Multi-Density EPS素材」による独自構造で衝撃を吸収。幅を10mmに狭めたストラップを採用した長さ調節が可能な機構「Tri-Fixウェブスプリッター」により、ストラップの調節のしやすさと快適な装着感も両立している。\nアナ・ハウトとテリーズ・アルスティンによって2013年に発表された『Hövding』は、エアバッグタイプの画期的な頭部プロテクションデバイス。改良を重ねて現在は第3世代モデルが欧州で販売されている。現時点では日本での正式販売はないものの、従来のハードシェル型ヘルメットの代替製品として今後の展開が期待されるプロダクトだ。\n『WIRED』では最新のガジェットからキッチングッズ、アウトドア用品まで、自信をもっておすすめできるアイテムを幅広く紹介している。おすすめサイクリングギアや、おすすめサイクリングウェアなど自転車関連のアイテムも豊富に取り揃えているので、効率よくショッピングしたいと考えているならWIRED SHOPPING GUIDEをチェックしてほしい。\n※『WIRED』による自転車の関連記事はこちら。\n次の10年を見通す洞察力を手に入れる！\n『WIRED』日本版のメンバーシップ会員 募集中！\n次の10年を見通すためのインサイト（洞察）が詰まった選りすぐりのロングリード（長編記事）を、週替わりのテーマに合わせてお届けする会員サービス「WIRED SZ メンバーシップ」。無料で参加できるイベントも用意される刺激に満ちたサービスは、無料トライアルを実施中！詳細はこちら。"}
```


### xxxxxxxxxxxxxx_wired_cwlLog.jsonl

１記事につき、１行のJSONフォーマットで保存されます。（JSONLフォーマット）内容は下記の通り。  
One line per article will be saved in JSON format.(JSONL Format) The contents are as follows
```
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
.....
```

Example.
```
{"url": "https://wired.jp/about/wired-japanese-edition/", "contents": ["['<h1 class=\"BaseWrap-sc-gjQpdd BaseText-ewhhUZ ContentHeaderHed-NCyCC iUEiRd iGbNre kctZMs\" data-testid=\"ContentHeaderHed\">Wired Japanese Edition</h1>', '<p>『WIRED』は、テクノロジーによって、生活や社会、カルチャーまでを包括したわたしたち自身の「未来がどうなるのか」についてのメディアです。</p>', '<p>『WIRED』は1993年、米国でプリントマガジンとして登場しました。以来、テクノロジーという窓から社会や文化を切り取り、その「ありうべき未来像」を世に問うてきました。そのスタンスはいまなお変わることなく、英国、イタリア、ドイツ、そして日本で出版されている各国語版のWIREDは、もれなくその視座を受け継いでいます。</p>', '<p>創刊から1年後に、WIREDの兄弟分として「HotWired」というウェブサイトが立ち上がりました。これは世界で初めてのウェブマガジンとされています。その後も時代の移り変わり、技術の進歩とともにWIREDは、読者とのコミュニケーションの形態を拡張してきました。</p>', '<p>そしていま、わたしたちは多種多様な「窓」を手にしています。レイヤーは多層化し、情報の流れる速度や届く射程がそれぞれの階層において異なる、複雑な社会がかたちづくられています。そして、その社会の姿は、1つのチャンネルを通したコミュニケーションだけでは、よりよく映し出すことが困難です。</p>', '<p>雑誌からスタートしたWIREDは、社会の多層性に合わせ、ウェブやソーシャルメディア、電子書籍にリアルイヴェントと、メディアとしての可能性を拡張して続けてきました。さらに2016年4月からはより新しいチャレンジに挑んでいます。ニュービジネスとカテゴライズする領域において、「発信」から「実装」へとメディアの役割を拡張しています。</p>']", ["Wired Japanese Edition", "『WIRED』は、テクノロジーによって、生活や社会、カルチャーまでを包括したわたしたち自身の「未来がどうなるのか」についてのメディアです。", "『WIRED』は1993年、米国でプリントマガジンとして登場しました。以来、テクノロジーという窓から社会や文化を切り取り、その「ありうべき未来像」を世に問うてきました。そのスタンスはいまなお変わることなく、英国、イタリア、ドイツ、そして日本で出版されている各国語版のWIREDは、もれなくその視座を受け継いでいます。", "創刊から1年後に、WIREDの兄弟分として「HotWired」というウェブサイトが立ち上がりました。これは世界で初めてのウェブマガジンとされています。その後も時代の移り変わり、技術の進歩とともにWIREDは、読者とのコミュニケーションの形態を拡張してきました。", "そしていま、わたしたちは多種多様な「窓」を手にしています。レイヤーは多層化し、情報の流れる速度や届く射程がそれぞれの階層において異なる、複雑な社会がかたちづくられています。そして、その社会の姿は、1つのチャンネルを通したコミュニケーションだけでは、よりよく映し出すことが困難です。", "雑誌からスタートしたWIREDは、社会の多層性に合わせ、ウェブやソーシャルメディア、電子書籍にリアルイヴェントと、メディアとしての可能性を拡張して続けてきました。さらに2016年4月からはより新しいチャレンジに挑んでいます。ニュービジネスとカテゴライズする領域において、「発信」から「実装」へとメディアの役割を拡張しています。"]]}
{"url": "https://wired.jp/article/best-bike-helmets/", "contents": ["['<h1 class=\"BaseWrap-sc-gjQpdd BaseText-ewhhUZ ContentHeaderHed-NCyCC iUEiRd iGbNre kctZMs\" data-testid=\"ContentHeaderHed\">自転車ヘルメットはどう選ぶ？ 人気ブランドから目的別まで、多様なスタイルに対応するおすすめ11選：WIRED SHOPPING GUIDE</h1>', '<div class=\"ContentHeaderDek-bIqFFZ eudPTt\">2023年4月から道路交通法が一部改正され、自転車のヘルメット着用が努力義務化された。努力義務に法的な強制力はないが、ヘルメットの着用を習慣化するいいきっかけになるだろう。そこで、最適なヘルメットの選び方や車種別・目的別のおすすめを紹介する。</div>', '<div class=\"BaseWrap-sc-gjQpdd BaseText-ewhhUZ ContentCardEmbedHed-kJVPGC iUEiRd bhMvlf cewqFA content-card-embed__hed\" data-testid=\"ContentCardEmbedHed\"><a class=\"BaseWrap-sc-gjQpdd BaseText-ewhhUZ BaseLink-eNWuiM ContentCardEmbedHedLink-eXLwe iUEiRd bhMvlf ipKfhK eFUKSb content-card-embed__hed-link\" data-testid=\"ContentCardEmbedHedLink\" href=\"/article/best-bicycle-gear/\">自転車通勤から通学、ポタリングまで。あると便利なおすすめのサイクリングギア7選</a></div>', '<p>コロナ禍の都市部の通勤手段やアクティビティとしても定着した自転車。2023年4月1日から道路交通法が改正され、自転車に乗る際のヘルメットの着用が努力義務化された。これまでは「児童または幼児を自転車に乗せる際ヘルメットの着用に努めなければならない」と対象が限定されていたが、今後は「自転車に乗る全国民」が対象になったのである。</p>', '<p>この努力義務化に法的な強制力はない。だが、ヘルメット非着用時の自転車事故による致死率は着用時の<a class=\"external-link\" data-event-click=\\'{\"element\":\"ExternalLink\",\"outgoingURL\":\"https://www.npa.go.jp/bureau/traffic/anzen/toubuhogo.html\"}\\' data-offer-url=\"https://www.npa.go.jp/bureau/traffic/anzen/toubuhogo.html\" href=\"https://www.npa.go.jp/bureau/traffic/anzen/toubuhogo.html\" rel=\"nofollow noopener\" target=\"_blank\">2倍以上にもなる</a>ので、今回の法改正を機に自分のサイクルスタイルに合ったヘルメットを取り入れてみてはいかがだろうか。</p>', '<p>以下にヘルメットの選び方をはじめ、おすすめのメーカーのほか、ロード、シティ、キッズ用などジャンル別のおすすめの製品を紹介する。</p>', '<h2>INDEX</h2>', '<p>1.<a href=\"#a\">自転車ヘルメットの選び方</a>\\n2.<a href=\"#b\">自転車ヘルメットおすすめメーカー</a>\\n3.<a href=\"#c\">ロードバイク向けおすすめヘルメット</a>\\n4.<a href=\"#d\">クロスバイク向けおすすめヘルメット</a>\\n5.<a href=\"#e\">ミニベロ・折りたたみ自転車向けおすすめヘルメット</a>\\n6.<a href=\"#f\">Eバイク向けおすすめヘルメット</a>\\n7.<a href=\"#g\">コストパフォーマンスでおすすめのヘルメット</a>\\n8.<a href=\"#h\">軽量タイプのおすすめヘルメット</a>\\n9.<a href=\"#i\">折りたたみタイプのおすすめヘルメット</a>\\n10.<a href=\"#j\">帽子型デザインのおすすめヘルメット</a>\\n11.<a href=\"#k\">キッズ向けおすすめヘルメット</a>\\n12.<a href=\"#l\">スマートテクノロジー搭載のおすすめヘルメット</a>\\n13.<a href=\"#m\">ヘルメット代わりになる頭部プロテクションデバイス</a>\\n14.<a href=\"#n\">WIRED SHOPPING GUIDEをチェック</a></p>', '<p>自転車ヘルメットを選ぶ際に最も重要になるのがサイズとフィット感だ。どれだけ高性能なヘルメットでも、サイズが合っていなければ性能を十分に発揮できない。必ず自分の頭に合ったサイズを選ぶよう気をつけてほしい。</p>', '<p>また、ロードバイクなどスポーツバイク向けのヘルメットの場合は、海外メーカーなら「アジアンフィット」のタイプ、あるいは日本市場向けに開発された国内メーカーのヘルメットがフィットしやすいだろう。もしサイズやフィット感に不安がある場合は、店舗で試着してから購入したい。</p>', '<p>サイズだけでなく通気性や携帯性などの特性別では、以下に紹介するおすすめリストのなかから、愛車の種類やライディングスタイルに合わせて選ぶといい。</p>', '<p>1985年にカリフォルニア州サンタクルーズで創業したGIRO（ジロ）は、サイクリングアクセサリーとウィンタースポーツアクセサリーを展開するブランド。独自の構造と高い安全性、先進性で自転車ヘルメットのあり方に多大な影響を与えたとされ、世界中のトップライダーたちに支持され続けている。</p>', '<p>「アスリートやアスリートを目指す人々の命を守り、事故の影響を軽減する」というミッションを掲げ05年にスウェーデンで誕生したPOC（ポック）。ストックホルム郊外にあるラボで素材の研究者、インダストリアルデザイナー、グラフィックデザイナー、脳神経外科医など各分野の専門家によるアドバイスに基づき、プロテクション性能の向上に努めている。機能性とデザイン性を高次元で両立したヘルメットが揃う。</p>', '<p>GIROのロードバイク向けの定番モデル「AETHER」のアジアンフィットモデルが、<a class=\"external-link\" data-event-click=\\'{\"element\":\"ExternalLink\",\"outgoingURL\":\"https://amzn.to/3Hm1obF\"}\\' data-offer-url=\"https://amzn.to/3Hm1obF\" href=\"https://amzn.to/3Hm1obF\" rel=\"nofollow noopener\" target=\"_blank\">「AETHER SPHERICAL AF」</a>。自転車ヘルメットの安全機構として広まっている多方向衝撃保護システム（MIPS：Multi-directional Impact Protecti on System）をさらに進化させた「スフェリカルテクノロジー」を搭載。衝撃吸収性だけでなく、優れた通気性と快適なフィットを併せもつフラッグシップモデルだ。</p>', '<p>米国の消費者製品安全法（CPSA：Consumer Product Safety Act）に適合し、欧州の安全基準認証であるCE（Conformité Européenne）マークや「TUV（Technischer Überwachungs-Verein）」認証を得るなど、最も厳しいとされる安全基準をクリアしたヘルメットをラインナップするNUTCASE HELMET（ナットケースヘルメット）。サイクリングだけでなくスケート、カヌー、スノースポーツなどに対応するヘルメットが揃う。</p>', '<p><a class=\"external-link\" data-event-click=\\'{\"element\":\"ExternalLink\",\"outgoingURL\":\"https://store.nutcasehelmet.jp/items/35039014\"}\\' data-offer-url=\"https://store.nutcasehelmet.jp/items/35039014\" href=\"https://store.nutcasehelmet.jp/items/35039014\" rel=\"nofollow noopener\" target=\"_blank\">「VIO KIT」</a>は、フロントに明るさが200ルーメンの白色ライト、サイドとリアに65ルーメンの赤とオレンジのLEDライトを搭載している（LEDライトはUSB充電が可能）。本体には耐衝撃性が高いABS樹脂製のアウターシェルを採用し、3つのベンチレーションで頭の蒸れを防ぐという。</p>', '<p>マグネットで片手で簡単に着脱できるバックル「FIDLOCK」を装備するほか、フィット感を簡単に調整できるアジャスタブル・スピンダイヤルを搭載。最適なフィット感を得られるインナーパッドも付属する。</p>', '<p>「1,000人の命を救う」というテーマから命名されたロサンゼルス生まれの「Thousand（サウザンド）」。シティサイクリストのためのミニマルなデザインが人気のブランドだ。</p>', '<p>フラッグシップモデルの<a class=\"external-link\" data-event-click=\\'{\"element\":\"ExternalLink\",\"outgoingURL\":\"https://highmount-store.jp/shopdetail/000000001900/thousand/page1/order/\"}\\' data-offer-url=\"https://highmount-store.jp/shopdetail/000000001900/thousand/page1/order/\" href=\"https://highmount-store.jp/shopdetail/000000001900/thousand/page1/order/\" rel=\"nofollow noopener\" target=\"_blank\">「CHAPTER（チャプター）」</a>は、自転車ヘルメットの安全機構として広まっている多方向衝撃保護システム（MIPS）を採用。ライナーとパッドの間に低摩擦のレイヤーを入れることで、転倒時に脳内で起きる回転運動の衝撃を軽減させる。</p>', '<p>また、ヘルメット後部にあるダイヤルフィットシステムは、頭にフィットしやすいように調整できる。マグネット式のテールライトは明るさが最大30ルーメンの点滅が約4時間にわたって持続し、マルチユースアダプターを使えば自転車のシートポストやハンドルバーにも装着可能だ。自転車本体とヘルメットを連結して鍵をかけられるシークレットポップロック機構は、置き場に困るヘルメットの固定にひと役買ってくれる。</p>', '<p>レーシングスペックのモデルを多く発表してきたPOCのアーバンヘルメット<a class=\"external-link\" data-event-click=\\'{\"element\":\"ExternalLink\",\"outgoingURL\":\"https://www.pocsports.com/ja/products/myelin?variant=41700442275992\"}\\' data-offer-url=\"https://www.pocsports.com/ja/products/myelin?variant=41700442275992\" href=\"https://www.pocsports.com/ja/products/myelin?variant=41700442275992\" rel=\"nofollow noopener\" target=\"_blank\">「MYELIN（ミエリン）」</a>。乗馬ヘルメットのような布製のアウターシェルに、軽量の発泡スチロールのヘルメットライナーなどの素材を接着剤を一切使わずに固定したことで、簡単に分解して個々の部品をリサイクルできる。サステナブルなマイクロモビリティとして注目されている電動アシスト自転車（Eバイク）で使うにはもってこいのコンセプトだ。</p>', '<p>後頭部にダイヤルアジャスターはなく、ストレッチ性のあるサイドストラップが伸縮してフィットする構造。布製のアウターシェルと通気孔のついたインナーシェルの組み合わせで熱がこもらず、気温が上がる季節もストレスなく着用できる。</p>', '<p>ツール・ド・フランスのチャンピオンが着用していたことでも知られる『MET（メット）』は、イタリアで1987年に創業したスポーツサイクル用のヘルメットメーカー。<a class=\"external-link\" data-event-click=\\'{\"element\":\"ExternalLink\",\"outgoingURL\":\"https://item.rakuten.co.jp/cozybicycle/met-strale-blackyellowpanel-m/\"}\\' data-offer-url=\"https://item.rakuten.co.jp/cozybicycle/met-strale-blackyellowpanel-m/\" href=\"https://item.rakuten.co.jp/cozybicycle/met-strale-blackyellowpanel-m/\" rel=\"nofollow noopener\" target=\"_blank\">「STRALE」</a>は、上位モデルのデザインや技術を踏襲したリーズナブルなエントリーモデルだ。</p>', '<p>独自のエアフロー構造により効率的な空気の抜け道をつくり、蒸れることなく長時間のライドも快適という。頭部を一周するベルトが特徴的なアジャスターシステム「Safe-T Duo」が締めつけ感のない快適なフィットを実現する。</p>', '<p>アジアンフィットタイプではないのでフィットには注意が必要だが、実売価格が10,000円程度なので、ロードバイク用ヘルメットの入門アイテムとしておすすめだ。</p>', '<p>サイクルヘルメットで最軽量クラスの200g以下で、装着していることを忘れるほどの軽い製品が<a class=\"external-link\" data-event-click=\\'{\"element\":\"ExternalLink\",\"outgoingURL\":\"https://www.pocsports.com/products/ventral-lite-wf?variant=41623206527128\"}\\' data-offer-url=\"https://www.pocsports.com/products/ventral-lite-wf?variant=41623206527128\" href=\"https://www.pocsports.com/products/ventral-lite-wf?variant=41623206527128\" rel=\"nofollow noopener\" target=\"_blank\">「VENTRAL LITE WF（ベントラル ライト WF）」</a>。POCのヘルメットの全ラインナップでオールラウンドモデルに位置づけられる「VENTRAL」ラインでは軽量モデルとなり、アジア人の頭の形に合うワイドフィットが特徴だ。</p>', '<p>安全性を保ちながらもアウターシェルの使用面積を減らし、アジャストシステムにもより軽量な素材を採用するなど徹底して軽量化を図っている。レース用に開発されたモデルではあるが、街乗りでもヘルメット本体の重さによる着用時のストレスを最小限にしてサイクリングを楽しみ人におすすめだ。</p>', '<p>2013年にスペインで誕生した「CLOSKA（クロスカ）」は、デザイン性に優れたイノベーティブなプロダクトを発表している注目のブランド。<a href=\"https://wired.jp/2019/02/04/closca-collapsible-helmet/\">ブランド初のプロダクトとして知られるヘルメット</a>と同様の構造をもつ<a class=\"external-link\" data-event-click=\\'{\"element\":\"ExternalLink\",\"outgoingURL\":\"https://amzn.to/3Nl4q3L\"}\\' data-offer-url=\"https://amzn.to/3Nl4q3L\" href=\"https://amzn.to/3Nl4q3L\" rel=\"nofollow noopener\" target=\"_blank\">「LOOP」</a>は、建築からインスピレーションを得たというフォルムが特徴的な折り畳みタイプだ。同心円状になったプラスチックとフォームラバーは入れ子式に折り畳むと6cmほどの厚さになり、かさばらずにバッグに収納できる。</p>', '<p>欧州の自転車ヘルメットやスケートボード用ヘルメットの安全基準であるCE規格（EN1078）と、米国消費者製品安全委員会（CPSC）の自転車ヘルメットの安全基準の2つをクリアしているので、安全性の高さも申し分ない。</p>', '<p>商品開発から安全実験、製造販売まで一貫して日本国内で手掛けている「OGK KABUTO（オージーケーカブト）。モーターバイクやロードレース用のヘルメットだけでなく、通勤通学やタウンユース向けモデルも多数展開している。</p>', '<p>日本人の頭の形にフィットするヘルメットは、一見するとヘルメットには見えない帽子型のデザインも人気だ。カジュアルなスタイルになじむ帽子型は、<a class=\"external-link\" data-event-click=\\'{\"element\":\"ExternalLink\",\"outgoingURL\":\"https://amzn.to/40PPHkq\"}\\' data-offer-url=\"https://amzn.to/40PPHkq\" href=\"https://amzn.to/40PPHkq\" rel=\"nofollow noopener\" target=\"_blank\">「DAYS」</a>のほかに3種類のデザインがラインナップする。</p>', '<p>2004年に米国のボストンで誕生したヘルメットブランド「BERN（バーン）」。自転車だけでなくスキーやスノーボード、スケートのヘルメットを展開し、日本人の頭の形に合うジャパンフィットもラインナップする。</p>', '<p>2歳から6歳までの子どもにおすすめのキッズ用ヘルメットは、ボーイズ用に<a class=\"external-link\" data-event-click=\\'{\"element\":\"ExternalLink\",\"outgoingURL\":\"https://bernjapan.com/view/item/000000000094?category_page_id=kidshelmets\"}\\' data-offer-url=\"https://bernjapan.com/view/item/000000000094?category_page_id=kidshelmets\" href=\"https://bernjapan.com/view/item/000000000094?category_page_id=kidshelmets\" rel=\"nofollow noopener\" target=\"_blank\">NINO（ニーノ）</a>、ガールズ用に<a class=\"external-link\" data-event-click=\\'{\"element\":\"ExternalLink\",\"outgoingURL\":\"https://bernjapan.com/view/item/000000000096?category_page_id=kidshelmets\"}\\' data-offer-url=\"https://bernjapan.com/view/item/000000000096?category_page_id=kidshelmets\" href=\"https://bernjapan.com/view/item/000000000096?category_page_id=kidshelmets\" rel=\"nofollow noopener\" target=\"_blank\">NINA（ニーナ）</a>というモデルが用意されており、耐衝撃性の高さと軽さで子どもにとって快適な使用感を実現したという。バイザー付きのインナーは取り外して洗濯が可能。ベルクロでインナーのサイズを簡単に調整できる「EZ-FIT」システムは、日々大きくなる子供の頭のサイズに合わせてフィッティングしやすい。色やデザインの豊富なバリエーションが用意されているので、子どもの好みのモデルが見つかるはずだ。</p>', '<p>総合サイクルブランドとして有名なSPECIALIZED（スペシャライズド）の<a class=\"external-link\" data-event-click=\\'{\"element\":\"ExternalLink\",\"outgoingURL\":\"https://www.specialized-onlinestore.jp/shop/g/g60921-7103/\"}\\' data-offer-url=\"https://www.specialized-onlinestore.jp/shop/g/g60921-7103/\" href=\"https://www.specialized-onlinestore.jp/shop/g/g60921-7103/\" rel=\"nofollow noopener\" target=\"_blank\">「S-WORKS PREVAIL II VENT MIPS」</a>は、自動で転倒を検出して緊急連絡先に通報してくれる別売りの<a class=\"external-link\" data-event-click=\\'{\"element\":\"ExternalLink\",\"outgoingURL\":\"https://www.specialized-onlinestore.jp/shop/g/g60519-8000/\"}\\' data-offer-url=\"https://www.specialized-onlinestore.jp/shop/g/g60519-8000/\" href=\"https://www.specialized-onlinestore.jp/shop/g/g60519-8000/\" rel=\"nofollow noopener\" target=\"_blank\">ANGiセンサー</a>を搭載可能。スマートフォンのアプリと連動させると、転倒の衝撃をセンサーが検知して登録した緊急連絡先にテキストメッセージとを位置情報を送信する。スマートフォンアプリ「Ride」はGPSを用いたアクティビティトラッキングが可能だ。</p>', '<p>ヘルメット中央と側面のブリッジ7本を取り除いて通気口と通風路を改善し、空気の流れるスピードを速くすることで頭をより涼しい状態に保つという。部位ごとに発泡素材のタイプを最適化した「Energy Optimized Multi-Density EPS素材」による独自構造で衝撃を吸収。幅を10mmに狭めたストラップを採用した長さ調節が可能な機構「Tri-Fixウェブスプリッター」により、ストラップの調節のしやすさと快適な装着感も両立している。</p>', '<p>アナ・ハウトとテリーズ・アルスティンによって<a href=\"https://wired.jp/2013/08/06/invisible-bicycle-helmet/\">2013年に発表された『Hövding』</a>は、エアバッグタイプの画期的な頭部プロテクションデバイス。改良を重ねて現在は第3世代モデルが欧州で販売されている。現時点では日本での正式販売はないものの、従来のハードシェル型ヘルメットの代替製品として今後の展開が期待されるプロダクトだ。</p>', '<p>『WIRED』では最新のガジェットからキッチングッズ、アウトドア用品まで、自信をもっておすすめできるアイテムを幅広く紹介している。<a href=\"https://wired.jp/article/best-bicycle-gear/\">おすすめサイクリングギア</a>や、<a href=\"https://wired.jp/article/best-cycling-wear/\">おすすめサイクリングウェア</a>など自転車関連のアイテムも豊富に取り揃えているので、効率よくショッピングしたいと考えているなら<a href=\"https://wired.jp/tag/wired-recommends/\">WIRED SHOPPING GUIDE</a>をチェックしてほしい。</p>', '<p>※『WIRED』による<a href=\"https://wired.jp/tag/bicycle/\">自転車の関連記事はこちら</a>。</p>', '<p><strong>次の10年を見通す洞察力を手に入れる！</strong>\\n<strong>『WIRED』日本版のメンバーシップ会員 募集中！</strong></p>', '<p>次の10年を見通すためのインサイト（洞察）が詰まった選りすぐりのロングリード（長編記事）を、週替わりのテーマに合わせてお届けする会員サービス「WIRED SZ メンバーシップ」。無料で参加できるイベントも用意される刺激に満ちたサービスは、無料トライアルを実施中！<a href=\"https://wired.jp/membership/about\">詳細はこちら</a>。</p>']", ["自転車ヘルメットはどう選ぶ？ 人気ブランドから目的別まで、多様なスタイルに対応するおすすめ11選：WIRED SHOPPING GUIDE", "2023年4月から道路交通法が一部改正され、自転車のヘルメット着用が努力義務化された。努力義務に法的な強制力はないが、ヘルメットの着用を習慣化するいいきっかけになるだろう。そこで、最適なヘルメットの選び方や車種別・目的別のおすすめを紹介する。", "自転車通勤から通学、ポタリングまで。あると便利なおすすめのサイクリングギア7選", "コロナ禍の都市部の通勤手段やアクティビティとしても定着した自転車。2023年4月1日から道路交通法が改正され、自転車に乗る際のヘルメットの着用が努力義務化された。これまでは「児童または幼児を自転車に乗せる際ヘルメットの着用に努めなければならない」と対象が限定されていたが、今後は「自転車に乗る全国民」が対象になったのである。", "この努力義務化に法的な強制力はない。だが、ヘルメット非着用時の自転車事故による致死率は着用時の2倍以上にもなるので、今回の法改正を機に自分のサイクルスタイルに合ったヘルメットを取り入れてみてはいかがだろうか。", "以下にヘルメットの選び方をはじめ、おすすめのメーカーのほか、ロード、シティ、キッズ用などジャンル別のおすすめの製品を紹介する。", "INDEX", "1.自転車ヘルメットの選び方\n2.自転車ヘルメットおすすめメーカー\n3.ロードバイク向けおすすめヘルメット\n4.クロスバイク向けおすすめヘルメット\n5.ミニベロ・折りたたみ自転車向けおすすめヘルメット\n6.Eバイク向けおすすめヘルメット\n7.コストパフォーマンスでおすすめのヘルメット\n8.軽量タイプのおすすめヘルメット\n9.折りたたみタイプのおすすめヘルメット\n10.帽子型デザインのおすすめヘルメット\n11.キッズ向けおすすめヘルメット\n12.スマートテクノロジー搭載のおすすめヘルメット\n13.ヘルメット代わりになる頭部プロテクションデバイス\n14.WIRED SHOPPING GUIDEをチェック", "自転車ヘルメットを選ぶ際に最も重要になるのがサイズとフィット感だ。どれだけ高性能なヘルメットでも、サイズが合っていなければ性能を十分に発揮できない。必ず自分の頭に合ったサイズを選ぶよう気をつけてほしい。", "また、ロードバイクなどスポーツバイク向けのヘルメットの場合は、海外メーカーなら「アジアンフィット」のタイプ、あるいは日本市場向けに開発された国内メーカーのヘルメットがフィットしやすいだろう。もしサイズやフィット感に不安がある場合は、店舗で試着してから購入したい。", "サイズだけでなく通気性や携帯性などの特性別では、以下に紹介するおすすめリストのなかから、愛車の種類やライディングスタイルに合わせて選ぶといい。", "1985年にカリフォルニア州サンタクルーズで創業したGIRO（ジロ）は、サイクリングアクセサリーとウィンタースポーツアクセサリーを展開するブランド。独自の構造と高い安全性、先進性で自転車ヘルメットのあり方に多大な影響を与えたとされ、世界中のトップライダーたちに支持され続けている。", "「アスリートやアスリートを目指す人々の命を守り、事故の影響を軽減する」というミッションを掲げ05年にスウェーデンで誕生したPOC（ポック）。ストックホルム郊外にあるラボで素材の研究者、インダストリアルデザイナー、グラフィックデザイナー、脳神経外科医など各分野の専門家によるアドバイスに基づき、プロテクション性能の向上に努めている。機能性とデザイン性を高次元で両立したヘルメットが揃う。", "GIROのロードバイク向けの定番モデル「AETHER」のアジアンフィットモデルが、「AETHER SPHERICAL AF」。自転車ヘルメットの安全機構として広まっている多方向衝撃保護システム（MIPS：Multi-directional Impact Protecti on System）をさらに進化させた「スフェリカルテクノロジー」を搭載。衝撃吸収性だけでなく、優れた通気性と快適なフィットを併せもつフラッグシップモデルだ。", "米国の消費者製品安全法（CPSA：Consumer Product Safety Act）に適合し、欧州の安全基準認証であるCE（Conformité Européenne）マークや「TUV（Technischer Überwachungs-Verein）」認証を得るなど、最も厳しいとされる安全基準をクリアしたヘルメットをラインナップするNUTCASE HELMET（ナットケースヘルメット）。サイクリングだけでなくスケート、カヌー、スノースポーツなどに対応するヘルメットが揃う。", "「VIO KIT」は、フロントに明るさが200ルーメンの白色ライト、サイドとリアに65ルーメンの赤とオレンジのLEDライトを搭載している（LEDライトはUSB充電が可能）。本体には耐衝撃性が高いABS樹脂製のアウターシェルを採用し、3つのベンチレーションで頭の蒸れを防ぐという。", "マグネットで片手で簡単に着脱できるバックル「FIDLOCK」を装備するほか、フィット感を簡単に調整できるアジャスタブル・スピンダイヤルを搭載。最適なフィット感を得られるインナーパッドも付属する。", "「1,000人の命を救う」というテーマから命名されたロサンゼルス生まれの「Thousand（サウザンド）」。シティサイクリストのためのミニマルなデザインが人気のブランドだ。", "フラッグシップモデルの「CHAPTER（チャプター）」は、自転車ヘルメットの安全機構として広まっている多方向衝撃保護システム（MIPS）を採用。ライナーとパッドの間に低摩擦のレイヤーを入れることで、転倒時に脳内で起きる回転運動の衝撃を軽減させる。", "また、ヘルメット後部にあるダイヤルフィットシステムは、頭にフィットしやすいように調整できる。マグネット式のテールライトは明るさが最大30ルーメンの点滅が約4時間にわたって持続し、マルチユースアダプターを使えば自転車のシートポストやハンドルバーにも装着可能だ。自転車本体とヘルメットを連結して鍵をかけられるシークレットポップロック機構は、置き場に困るヘルメットの固定にひと役買ってくれる。", "レーシングスペックのモデルを多く発表してきたPOCのアーバンヘルメット「MYELIN（ミエリン）」。乗馬ヘルメットのような布製のアウターシェルに、軽量の発泡スチロールのヘルメットライナーなどの素材を接着剤を一切使わずに固定したことで、簡単に分解して個々の部品をリサイクルできる。サステナブルなマイクロモビリティとして注目されている電動アシスト自転車（Eバイク）で使うにはもってこいのコンセプトだ。", "後頭部にダイヤルアジャスターはなく、ストレッチ性のあるサイドストラップが伸縮してフィットする構造。布製のアウターシェルと通気孔のついたインナーシェルの組み合わせで熱がこもらず、気温が上がる季節もストレスなく着用できる。", "ツール・ド・フランスのチャンピオンが着用していたことでも知られる『MET（メット）』は、イタリアで1987年に創業したスポーツサイクル用のヘルメットメーカー。「STRALE」は、上位モデルのデザインや技術を踏襲したリーズナブルなエントリーモデルだ。", "独自のエアフロー構造により効率的な空気の抜け道をつくり、蒸れることなく長時間のライドも快適という。頭部を一周するベルトが特徴的なアジャスターシステム「Safe-T Duo」が締めつけ感のない快適なフィットを実現する。", "アジアンフィットタイプではないのでフィットには注意が必要だが、実売価格が10,000円程度なので、ロードバイク用ヘルメットの入門アイテムとしておすすめだ。", "サイクルヘルメットで最軽量クラスの200g以下で、装着していることを忘れるほどの軽い製品が「VENTRAL LITE WF（ベントラル ライト WF）」。POCのヘルメットの全ラインナップでオールラウンドモデルに位置づけられる「VENTRAL」ラインでは軽量モデルとなり、アジア人の頭の形に合うワイドフィットが特徴だ。", "安全性を保ちながらもアウターシェルの使用面積を減らし、アジャストシステムにもより軽量な素材を採用するなど徹底して軽量化を図っている。レース用に開発されたモデルではあるが、街乗りでもヘルメット本体の重さによる着用時のストレスを最小限にしてサイクリングを楽しみ人におすすめだ。", "2013年にスペインで誕生した「CLOSKA（クロスカ）」は、デザイン性に優れたイノベーティブなプロダクトを発表している注目のブランド。ブランド初のプロダクトとして知られるヘルメットと同様の構造をもつ「LOOP」は、建築からインスピレーションを得たというフォルムが特徴的な折り畳みタイプだ。同心円状になったプラスチックとフォームラバーは入れ子式に折り畳むと6cmほどの厚さになり、かさばらずにバッグに収納できる。", "欧州の自転車ヘルメットやスケートボード用ヘルメットの安全基準であるCE規格（EN1078）と、米国消費者製品安全委員会（CPSC）の自転車ヘルメットの安全基準の2つをクリアしているので、安全性の高さも申し分ない。", "商品開発から安全実験、製造販売まで一貫して日本国内で手掛けている「OGK KABUTO（オージーケーカブト）。モーターバイクやロードレース用のヘルメットだけでなく、通勤通学やタウンユース向けモデルも多数展開している。", "日本人の頭の形にフィットするヘルメットは、一見するとヘルメットには見えない帽子型のデザインも人気だ。カジュアルなスタイルになじむ帽子型は、「DAYS」のほかに3種類のデザインがラインナップする。", "2004年に米国のボストンで誕生したヘルメットブランド「BERN（バーン）」。自転車だけでなくスキーやスノーボード、スケートのヘルメットを展開し、日本人の頭の形に合うジャパンフィットもラインナップする。", "2歳から6歳までの子どもにおすすめのキッズ用ヘルメットは、ボーイズ用にNINO（ニーノ）、ガールズ用にNINA（ニーナ）というモデルが用意されており、耐衝撃性の高さと軽さで子どもにとって快適な使用感を実現したという。バイザー付きのインナーは取り外して洗濯が可能。ベルクロでインナーのサイズを簡単に調整できる「EZ-FIT」システムは、日々大きくなる子供の頭のサイズに合わせてフィッティングしやすい。色やデザインの豊富なバリエーションが用意されているので、子どもの好みのモデルが見つかるはずだ。", "総合サイクルブランドとして有名なSPECIALIZED（スペシャライズド）の「S-WORKS PREVAIL II VENT MIPS」は、自動で転倒を検出して緊急連絡先に通報してくれる別売りのANGiセンサーを搭載可能。スマートフォンのアプリと連動させると、転倒の衝撃をセンサーが検知して登録した緊急連絡先にテキストメッセージとを位置情報を送信する。スマートフォンアプリ「Ride」はGPSを用いたアクティビティトラッキングが可能だ。", "ヘルメット中央と側面のブリッジ7本を取り除いて通気口と通風路を改善し、空気の流れるスピードを速くすることで頭をより涼しい状態に保つという。部位ごとに発泡素材のタイプを最適化した「Energy Optimized Multi-Density EPS素材」による独自構造で衝撃を吸収。幅を10mmに狭めたストラップを採用した長さ調節が可能な機構「Tri-Fixウェブスプリッター」により、ストラップの調節のしやすさと快適な装着感も両立している。", "アナ・ハウトとテリーズ・アルスティンによって2013年に発表された『Hövding』は、エアバッグタイプの画期的な頭部プロテクションデバイス。改良を重ねて現在は第3世代モデルが欧州で販売されている。現時点では日本での正式販売はないものの、従来のハードシェル型ヘルメットの代替製品として今後の展開が期待されるプロダクトだ。", "『WIRED』では最新のガジェットからキッチングッズ、アウトドア用品まで、自信をもっておすすめできるアイテムを幅広く紹介している。おすすめサイクリングギアや、おすすめサイクリングウェアなど自転車関連のアイテムも豊富に取り揃えているので、効率よくショッピングしたいと考えているならWIRED SHOPPING GUIDEをチェックしてほしい。", "※『WIRED』による自転車の関連記事はこちら。", "次の10年を見通す洞察力を手に入れる！\n『WIRED』日本版のメンバーシップ会員 募集中！", "次の10年を見通すためのインサイト（洞察）が詰まった選りすぐりのロングリード（長編記事）を、週替わりのテーマに合わせてお届けする会員サービス「WIRED SZ メンバーシップ」。無料で参加できるイベントも用意される刺激に満ちたサービスは、無料トライアルを実施中！詳細はこちら。"]]}
```

### xxxxxxxxxxxxxx_wired_html_list.jsonl

`xxxxxxxxxxxx_xxxxxx_html`に保存されているhtmlのファイル名と、収集元のURLがJSONL形式で保存されます。  
The html file name stored in `xxxxxxxxxxxxxxxxx_xxxxxxxxx_html` and the URL of the collection source will be saved in JSONL format.

```
{"filename": "xxxxx_wired_article.html", "url": "https://www......."}
{"filename": "xxxxx_wired_article.html", "url": "https://www......."}
{"filename": "xxxxx_wired_article.html", "url": "https://www......."}
.....
```

Example.
```
{"filename": "00001_wired_article.html", "url": "https://ameblo.jp/kumikotakeda/entry-12805291014.html"}
{"filename": "00002_wired_article.html", "url": "https://ameblo.jp/kawata--hiromi/entry-12805341645.html"}
{"filename": "00003_wired_article.html", "url": "https://ameblo.jp/hiranonora/entry-12805304197.html"}
```

### xxxxxxxxxxxx_xxxxxx_html

収集したhtmlはこのフォルダに保存されます。  
The collected html is stored in this folder.

個々のファイルの名前は５桁の数字の後に`_wired_article.html`を付けたものになります。  
The name of each individual file will be a five-digit number followed by `_wired_article.html`.