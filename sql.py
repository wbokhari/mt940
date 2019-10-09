#!/usr/bin/python
import config

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT id,TRN_NUMBER FROM transactions" )

    for id,TRN_NUMBER in cur.fetchall() :
        print id,TRN_NUMBER


def insertQuery( conn ) :
	cur = conn.cursor()
	insert =''' INSERT INTO transactions
	(TRN_DATE,TRN_NUMBER,TEXT_TYPE,SEQUENCE_NO, DST_ORDINAL, TRN_TIMESTAMP,MESSAGE_TEXT,
	 RECORD_EXPIRED, RECORD_UPDATED, PODIUM_DELIVERY_DATE ) 
	 VALUES ('9-7-19', '39', 'A', '11', 'dfd','5:30:02','test data','a', 'b','c' ) ''';
	cur.execute(insert)
	conn.commit();
	print("Record inserted successfully")


print "Using psycopg2 to read data"
import psycopg2
myConnection = psycopg2.connect( host=config.hostname, user=config.username, password=config.password, dbname=config.database )
doQuery( myConnection )
insertQuery(myConnection)
myConnection.close()