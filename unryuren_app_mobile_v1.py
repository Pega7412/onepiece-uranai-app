
import streamlit as st
import datetime
import os

st.set_page_config(page_title="雲龍蓮 四柱推命キャラ診断", layout="centered")

# タイトル部分（漢字化＋中央寄せ）
st.markdown("""
<div style="text-align: center;">
    <h1 style="font-size:1.6em;">🌀 雲龍蓮オリジナル 四柱推命</h1>
    <h2 style="font-size:1.3em;">× ワンピース風キャラ診断</h2>
</div>
""", unsafe_allow_html=True)

# キャッチコピー
st.markdown("""
<div style="text-align: center; padding-top:10px; padding-bottom:20px;">
    <p style="font-size:1.1em;">🌙 自分でも知らない「もう一人の自分」と出会える</p>
    <p style="font-size:1.1em;">生年月日から導く、魂のキャラクター診断！</p>
</div>
""", unsafe_allow_html=True)

# 生年月日入力
st.markdown("### 🔹 生年月日を選択してください")
birthdate = st.date_input(" ", value=None, min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())

st.markdown("<br>", unsafe_allow_html=True)

# 診断ボタン
if st.button("🔮 診断スタート！"):

    if birthdate is not None:
        day = birthdate.day
        character_list = [
            "luffy", "zoro", "nami", "sanji", "chopper", "robin",
            "usopp", "franky", "brook", "jinbe", "vivi", "ace"
        ]
        char_index = day % len(character_list)
        char_type = character_list[char_index]

        filename = f"{char_type}.txt"

        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                diagnosis = file.read()
            st.subheader(f"🧭 あなたのキャラタイプは「{char_type.capitalize()}」タイプ！")
            st.text(diagnosis)
        else:
            st.error(f"診断結果ファイルが見つかりません: {filename}")
    else:
        st.warning("生年月日を入力してください。")

# 下部案内
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <h3>🌱 迷いや不安を抱えているあなたへ</h3>
    <p>雲龍蓮が「今のあなた」に必要なメッセージを、本格鑑定でお届けします。</p>
    <p>少しでも心が軽くなるきっかけを届けられたら嬉しいです。</p>
    <a href="https://akio7412.jimdofree.com/form" target="_blank">
        <button style="padding:10px 20px; font-size:16px; border-radius:10px;">🔍 無料体験鑑定に申し込む</button>
    </a>
    <br><br>
    <a href="https://lin.ee/tbVHFmG" target="_blank">
        <button style="padding:10px 20px; font-size:16px; background-color:#06C755; color:white; border:none; border-radius:10px;">💬 LINEで相談する</button>
    </a>
    <br><br>
    <a href="https://x.com/unryuren" target="_blank">🐦 X（旧Twitter）</a>｜
    <a href="https://www.instagram.com/unryuren" target="_blank">📷 Instagram</a>
</div>
""", unsafe_allow_html=True)
