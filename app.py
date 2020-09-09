from flask import Flask,render_template,request,url_for,redirect
import pymysql
app = Flask (__name__)

conn = pymysql.connect("localhost",'root','123456','renthouse',charset='utf8')
cursor = conn.cursor()

cookie ="no"

@app.route ('/')
def home():
    global cookie
    if cookie=='yes':
        return render_template('home.html',cookie=cookie)
    else:

        if request.values.get("username")=="dydx" and request.values.get("password")=="123":

            cookie="yes"
            return render_template('home.html',cookie=cookie)
        else:
            return redirect("/login")


@app.route('/login')
def login():
    if cookie=="yes":
        return redirect("http://127.0.0.1:5000/")
    else:
        return render_template('login.html')



@app.route ('/getfirst')  #nouse
def getFirstTenant():

    # list1 =list(result)
    # return "第一位租客: %s, 手机号码： %s"%(result[1],result[2])
    # 先从前台页面获取到租客姓名
    tenantName=request.args.get("Tname")
    print(tenantName)

    # 通过租客姓名查询租客相关资料
    sql = "select * from tenant where 姓名 = '%s';" % tenantName
    print(sql)
    cursor.execute (sql)
    try:
        result = cursor.fetchone ()
        print (result)

        # 将查询结果返回前台页面
        # return "您查询的租客是：<font color='red'> %s</font> \n 他的手机号号是：<font color='blue'> %s <blue>" %(result[1],result[2])
        html_result ='''
        <table align ="center" style="border-collapse:collapse;" border="1">
            <tr>
                 <th>租客姓名</td>
                 <th>租客电话</td>
            </tr>
            
            <tr>
                 <td>%s</td>
                 <td>%s</td>          
            </tr>
        
        </table>''' % (result[1],result[2])

        # return html_result
        return  render_template('queryOne.html',tenantName=result[1],tenantPhone=result[2],roomNum=result[3],
                                startDate =result[4],endDate=result[5])

    except:
        return render_template('queryOne.html')


@app.route ('/getAll')
def getAllTenant():
    if cookie=="yes":
        # pagesize =request.args.get('pagesize')
        # pagesize=int(pagesize)
        # pagenumber=request.args.get('pagenumber')
        # pagenumber=int(pagenumber)
        tenantName = request.args.get ("Tname")
        print(tenantName)
        tenantName = "%" + tenantName +"%"

        tenantPhone = request.args.get ("Tphone")
        tenantPhone = "%" + tenantPhone +"%"

        tenantRoom = request.args.get ("Troom")
        tenantRoom = "%" + tenantRoom +"%"

        sql = "select * from tenant"
        #sql = "select * from tenant where 姓名 like '%s' and 手机 like '%s' and 房间号 like '%s' limit %s, %s;" % (tenantName,tenantPhone,
        #                                                                                       tenantRoom,(pagenumber-1)*pagesize,pagesize)

        sql = "select * from tenant where 姓名 like '%s' and 手机 like '%s' and 房间号 like '%s';" % (
        tenantName, tenantPhone,
        tenantRoom)
        print (sql)
        cursor.execute (sql)

        try:
            results = cursor.fetchall ()
            print (results)

        except:
            pass

        return render_template('queryAll.html',i=0,results = results,cookie=cookie)
    else:
        return redirect("/login")

@app.route('/addNew')
def addNew():
    if cookie == "yes":
        return render_template('addNew.html',cookie=cookie)
    else:
        return redirect("/login")

@app.route('/save')
def save():

    addname=request.args.get("addname")
    print(addname)
    addphone=request.args.get("addphone")
    addroom=request.args.get("addroom")
    addstart=request.args.get("addstart")
    addend=request.args.get("addend")

    insertSQL='''
    
    insert into tenant (姓名,手机,房间号,承租日期,到期日期) values("%s","%s","%s","%s","%s")
    ''' % (addname,addphone,addroom,addstart,addend);
    cursor.execute(insertSQL)
    conn.commit()
    # conn.close()

    if addname!=None:
        return  redirect("http://127.0.0.1:5000/getAll?Tname=&Tphone=&Troom=")
    else:
        return "failure"



if __name__ == '__main__':
    app.run (debug=True)
