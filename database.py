from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine=create_engine('postgresql://avnadmin:AVNS_b1AYuNU7LHng_BIqa0U@pizza-delivery-api-musaajmal57-6bf8.g.aivencloud.com:11389/defaultdb',
    echo=True
)

Base=declarative_base()

Session=sessionmaker()