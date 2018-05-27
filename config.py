class Config(object):
    DEBUG = False
    SECRET_KEY = 'this is secret string'

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # catalog max depth
    CATALOG_DEEP = 3
    ERROR_LOG = "../logs/error.log"
    INFO_LOG = "../logs/info.log"

    DB_PREFIX = "bb_"
    PER_PAGE = 20

    STATIC_IMG_PATH = "img"

    AVATAR_PATH = "resource/image/avatar"
    TMP_PATH = "resource/tmp"
    IMAGE_PATH = "resource/image/image"

    BOOK_COVER_PATH = "resource/image/cover"

    UPLOAD_IMAGE_PATH = "data/image"
    UPLOAD_VIDEO_PATH = "data/video"


# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/f_luntan?charset=utf8'
# 测试环境
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# 设置一个config 字典中,注册了不同的配置环境
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
    }