import pymysql



def run(user,password,database):  
    db = pymysql.connect("localhost",user,password,database )
    cursor = db.cursor()
    cursor.execute("""create table if not exists `newspaper`(
                    `newspaper_id` INT UNSIGNED AUTO_INCREMENT,
                    `newspaper_name` VARCHAR(40) NOT NULL,
                    `publisher` VARCHAR(40) NOT NULL,
                    `newspaper_price` FLOAT NOT NULL,
                    `newspaper_type` VARCHAR(40) NOT NULL,
                    PRIMARY KEY ( `newspaper_id` )
                    )ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
    cursor.execute("""insert into newspaper(newspaper_name,publisher,newspaper_price,newspaper_type)                    
                    values
                    ("人民政协报","人民政协报社",1.3,"周六报");
                    """)
    cursor.execute("""insert into newspaper(newspaper_name,publisher,newspaper_price,newspaper_type)                    
                    values
                    ("人民日报","人民日报社",1.8,"日报");
                    """)
    cursor.execute("""insert into newspaper(newspaper_name,publisher,newspaper_price,newspaper_type)                    
                    values
                    ("光明日报","光明日报社",1.0,"日报");
                    """)
    cursor.execute("""insert into newspaper(newspaper_name,publisher,newspaper_price,newspaper_type)                    
                    values
                    ("环球时报","人民日报社",1.36,"周六报");
                    """)
    cursor.execute("""insert into newspaper(newspaper_name,publisher,newspaper_price,newspaper_type)                    
                    values
                    ("经济日报","经济日报社",1.0,"日报");
                    """)
    cursor.execute("""insert into newspaper(newspaper_name,publisher,newspaper_price,newspaper_type)                    
                    values
                    ("南方日报","南方日报出版社",1.0,"日报");
                    """)
    cursor.execute("""insert into newspaper(newspaper_name,publisher,newspaper_price,newspaper_type)                    
                    values
                    ("南方都市报","南方报业传媒集团",2.0,"日报");
                    """)
    cursor.execute("""insert into newspaper(newspaper_name,publisher,newspaper_price,newspaper_type)                    
                    values
                    ("工人时报","工人时报社",1.0,"周四报");
                    """)
    cursor.execute("""insert into newspaper(newspaper_name,publisher,newspaper_price,newspaper_type)                    
                    values
                    ("扬子晚报","新华日报社",1.2,"日报");
                    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS `user`(
                    `id` INT UNSIGNED,
                    `pwd` VARCHAR(20) NOT NULL,
                    `name` VARCHAR(20) NOT NULL,
                    `tel` VARCHAR(20) NOT NULL,
                    `address` VARCHAR(100) NOT NULL,
                    `zip` VARCHAR(10) NOT NULL,
                    PRIMARY KEY ( `id` )
                    )ENGINE=InnoDB DEFAULT CHARSET=utf8;""")   

    cursor.execute("""create table if not exists `book_state`(
                    `newspaper_id` INT(10) UNSIGNED NOT NULL,
                    `user_id` INT(10) UNSIGNED NOT NULL,
                    `number` INT(10) UNSIGNED NOT NULL,
                    FOREIGN KEY(newspaper_id) REFERENCES newspaper(newspaper_id),
                    FOREIGN KEY(user_id) REFERENCES user(id)
                    )ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
    db.commit()

def reset(user,password,database):  
    db = pymysql.connect("localhost",user,password,database )
    cursor = db.cursor()
    cursor.execute("drop table newspaper")


run("root","1234","testdb")