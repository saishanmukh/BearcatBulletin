from app import create_app
from app import config

app = create_app(config_class=config.DevelopmentConfig)

if __name__ == '__main__':
    app.run()