from datetime import timedelta

Config = {
    'SQLALCHEMY_DATABASE_URI':'mysql+pymysql://root:123456@!#@192.168.52.130:3306/test',
    'JWT_SECRET_KEY':'kOSNs01zR5BGmM9rgFTP5UzqRodnuCFo',
    'JWT_ACCESS_TOKEN_EXPIRES':timedelta(minutes=60)
}