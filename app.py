from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('ggOq8DNQP4OehkTN5wPkmkE1m5RNJV9oKn736VHHsybtAuzpGJs5JrBAeMz2k/DZOMZvNHkA2uJWIqQbianf1hFqaSkdq7L4DbzLk4QItJuxUhxuziinl7ExxEBJ6YWZRNRGXDa0mK7IlqrsYxkLcwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('196c7a50dcea8ac7cc7f475c739c5423')

@app.route("/")
def test():
    return "OK"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()