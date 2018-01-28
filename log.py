#!/usr/bin/env python
import psycopg2
import sys
dbname = "news"


try:
    conn = psycopg2.connect(database=dbname)
except:
    print "Unable to establish connection"
    sys.exit(0)

cursor = conn.cursor()

# Queries->

query_1 = '''select articles.title, count(log.path) as num
             from articles left join log
             on log.path like(concat('%',articles.slug))
             group by articles.title
             order by num desc
             limit 3
          '''

query_2 = '''select authors.name,sum(num) as total
             from authors,(select articles.slug, count(log.path) as num
             from articles left join log
             on log.path like(concat('%', articles.slug))
             group by articles.slug) as tasks_1,articles
             where articles.author=authors.id and articles.slug=tasks_1.slug
             group by authors.name order by total desc;
          '''

query_3 = '''select TO_CHAR(kos.l1,'dd-Mon-YYYY'), ((error/(num+.0)*100.0)) as percent
             from (select date(time) as l1,count(*) as num from log
             group by date(time)) as kos
             join (select date(time) as l2,count(*) as error from log
             where status like('%404%') group by l2) as mos
             on kos.l1=mos.l2 where ((error/(num+.0)*100.0))>=1
          '''
print("==> Most popular three articles of all time:")
print''
cursor.execute(query_1)  # First query to be executed
result = cursor.fetchall()

for i in result:
    print str(i[0])+'-----'+str(i[1])+' views'

print''
print("==> Most popular authors of all time:")
print''
cursor.execute(query_2)  # Second query to be executed
result = cursor.fetchall()
for i in result:
    print str(i[0])+"-----"+str(i[1])+" views"
print ''
print("==> Days that did more than 1% of requests lead to errors:")
print''
cursor.execute(query_3)   # Third query to be executed
result = cursor.fetchall()
for i in result:
    print str(i[0])+"-----"+str(round(i[1], 2))+"%"
conn.close()
