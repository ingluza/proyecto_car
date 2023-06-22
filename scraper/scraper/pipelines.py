import re
import psycopg2

class ScraperPipeline:

    def __init__(self):
        ## Connection Details
        hostname = 'localhost'
        username = 'postgres'
        password = 'postgres' # your password
        database = 'proyecto_arquitectura'

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()


    def process_item(self, course, spider):
        ## Check to see if text is already in database 
        if course['name']:
            course['name'] = re.sub("'","",course['name'])
            self.cur.execute("select * from courses_course where name = '%s'" % (course['name']))
            result = self.cur.fetchone()

            if result:
                spider.logger.warn("Curso ya exite en la base de datos: %s" % course['name'])

            else:

                try:
                    self.cur.execute(""" insert into courses_course (name, description, rating) values (%s,%s,%s)""", (
                        course["name"],
                        course["description"],
                        course["rating"]
                    ))
                ## Execute insert of data into database
                    self.connection.commit()
                
                except:
                    self.connection.rollback()
                
            return course

    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.connection.close()
