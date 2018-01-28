=> Log Analysis Project

by Harsh Massand, in fulfillment of Udacity's [Full-Stack Web Developer Nanodegree Part 1].
=>This project basically deals with how to write queries
  that will go to server and send some output.


=>Steps that will guide you to run the project::
	1)Download the newsdata.sql file from link given below:
	  (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
	2)Open your virtual machine and cmd or git bash.
	3)Clone this file and point your vm to this folder.
	3)Use vagrant up command to set up virtual machine.
	4)Then use vagrant ssh command.	
	5)Execute a psql command to import the uncompressed newsdata.sql file into the news 
	  database (psql -d news -f newsdata.sql).
	6)Run log.py file using python log.py.
	7)Desired output will be displayed on your screen.

=>Details about the tables:
$ This project contains three pre defined tables log,articles,authors
  the descprition of each one is given below

1) log:
	  	 Column |           Type           |                    Modifiers
--------+--------------------------+--------------------------------------------------
 path   | text                     |
 ip     | inet                     |
 method | text                     |
 status | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('log_id_seq'::regclass)


2) articles:

 Column |           Type           |                       Modifiers
--------+--------------------------+-------------------------------------------------------
 author | integer                  | not null
 title  | text                     | not null
 slug   | text                     | not null
 lead   | text                     |
 body   | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('articles_id_seq'::regclass)

3) authors:

 Column |  Type   |                      Modifiers
--------+---------+------------------------------------------------------
 name   | text    | not null
 bio    | text    |
 id     | integer | not null default nextval('authors_id_seq'::regclass)


So the queries are written in accordance to these tables.

