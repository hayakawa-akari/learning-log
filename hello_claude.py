from dotenv import load_dotenv
import anthropic

load_dotenv()  # .envのキーを読み込む
client = anthropic.Anthropic()  # 読み込んだキーを自動で使う

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=300, # トークンの制限
    messages=[
        {"role": "user", "content": "こんにちは！自己紹介を1文でしてください。"}
    ],
)

print("入力:", response.usage.input_tokens)
print("出力:", response.usage.output_tokens)