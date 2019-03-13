# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cameron:swsquad!@smartaps-customers.c6x5al6bomw6.us-east-2.rds.amazonaws.com:3306/smartaps'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = '0uiSm1zcR5l2ZsozPsz6azfpo7VM9sY2CK1mJzFj'
