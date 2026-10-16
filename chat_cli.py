from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

messages = []  # 会話履歴をここに溜める

print("Claudeと会話します。終了するには 'exit' と入力してください。")

while True:
    user_input = input("あなた:").strip()

    if user_input == "exit":
        break
    if user_input == "":
        continue  # 空のときは送らない

    # 1. 自分の発言を履歴に追加
    messages.append({"role": "user", "content": user_input})

    # 2. 履歴ごと送る
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=500,
        messages=messages,
    )

    reply = response.content[0].text
    print("Claude:", reply)

    # 3. Claudeの返事も履歴に追加
    messages.append({"role": "assistant", "content": reply})

    print(f"（入力 {response.usage.input_tokens} / 出力 {response.usage.output_tokens} トークン）")