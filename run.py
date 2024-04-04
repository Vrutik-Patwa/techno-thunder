from agro_ml import app
import webbrowser
from pyngrok import ngrok
ngrok.set_auth_token("2dSuZ0eOuPERzfCOYAxya3k9Jvg_4QMe3M7CqAaTfi2tA8Soo")
public_url = ngrok.connect(5000).public_url

if __name__ == '__main__':
    print(public_url)
    webbrowser.open_new('http://127.0.0.1.5000/')
    app.run()