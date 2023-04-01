import pandas as pd
import datetime
import psycopg2
import unicodedata
import unidecode


def update_price(resource,prix100,prix10,prix1):
    conn = psycopg2.connect(
        host="90.3.12.65",
        database="postgres",
        user="postgres",
        password="postgres")

    prix100 = int(prix100)
    prix10 = int(prix10)
    prix1 = int(prix1)

    resource_bdd = resource.lower()
    print(resource_bdd)
    resource_bdd  = unidecode.unidecode(resource_bdd,'utf-8')
    print(resource_bdd)

    resource_bdd = str(resource_bdd)
    print(resource_bdd)
    resource_bdd = resource_bdd.replace(" ", "_").replace("-", "_").replace("'", "_").replace("`", "_").replace(":", "")
    print(resource_bdd)
    cur = conn.cursor()

    new_line = pd.DataFrame(columns=['date', 'prix100','prix10','prix1'])
    new_line.loc[0] = [datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), prix100,prix10,prix1]
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS ' + resource_bdd + ' (date TIMESTAMP,prix_100 integer NULL,prix_10 integer NULL,prix_1 integer NULL);')
        conn.commit()
        cur.execute('insert into ' + resource_bdd+ ' values(now(),'+str(prix100)+','+str(prix10)+','+str(prix1)+');')
        conn.commit()
        data = pd.read_csv('valeur/'+resource+'.csv')
    except (Exception, Error) as error:
        #cur.execute('CREATE TABLE IF NOT EXISTS' + resource + '(date date,prix_100 integer NULL,prix_10 integer NULL,prix_1 integer NULL);')
        #conn.commit()
        #cur.execute('insert into ' + resource + ' values(now(),prix100,prix10,prix1);')
        #conn.commit()
        data = None

    if data is not None:
        frames = [data, new_line]
        #print(new_line['prix100'].mean()*100)
        #print(data['prix100'].mean())
        if ((new_line['prix100'].mean()*100) /data['prix100'].mean()) < 80 :
            print(resource)
            print(new_line['prix100'].mean())
            print(data['prix100'].mean())
            print((new_line['prix100'].mean()*100) /data['prix100'].mean())

        result = pd.concat(frames)
        #print(result)
        result.to_csv('valeur/'+resource+'.csv', index=False)
    else:
        new_line.to_csv('valeur/'+resource+'.csv', index=False)