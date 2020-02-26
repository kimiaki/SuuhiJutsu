# -*- coding: utf-8 -*-
import os
import psycopg2

class Postgres:
    
    # DBと接続
    def get_connection(self):
        return psycopg2.connect(os.environ["DATABASE_URL"])
    
    """
    def get_connect(self):
        return psycopg2.connect(os.environ["DB_DANCE"])
    """
        
    # 新規登録            
    def register_user(self, user_id = None):
        query = "INSERT INTO user_info (user_id) VALUES('%s');"
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query % user_id)
    
    def get_users(self, channel_id):
        query = "SELECT (user_id FROM user_info ;"
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
            
    def is_user_exists(self, user_id):
        query = "SELECT user_id FROM user_info WHERE user_id = '%s';"
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query % user_id)
                if cur.fetchall() != []:
                    return True
                else:
                    return False
                
    """           
    def create_table(self):
        query = "CREATE TABLE cotanct (id serial, user_id varchar(50), name varchar(50), kana varchar(50), mail varchar(100), title varchar(50), text varchar(500), date date, time time);"
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
    """