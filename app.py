from flask import Flask,render_template,request,url_for,redirect,jsonify,json,Response
import pymysql
app = Flask (__name__)

conn = pymysql.connect("dingo1981.xyz",'root','0329','renthouse',charset='utf8',port=8306)
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






@app.route ('/getAll')
def getAllTenant():
    # if cookie=="yes":
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
        print(tenantName)
        print(tenantPhone)
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
    # else:
    #     return redirect("/login")

@app.route("/apitest")
def apitest():

    return jsonify({'a':1,'b':2})

@app.route("/apitest2")
def apitest2():


    return json.dumps([{'name':"狗伦",'age':8,'school':'中澳'},
                       {'name': "蔡徐昆", 'age': 28, 'school': '野鸡学校'},
                       {'name': "王大力", 'age': 18, 'school': '哈弗'},
                       {'name': "沙老板", 'age': 8, 'school': '南京大学'},
                       {'name': "钟无艳", 'age': 8, 'school': '北邮'},
                       {'name': "吴法天", 'age': 8, 'school': '海洋大学'},
                       {'name':"杨雅晴","age":10,"school":"中澳"}])


@app.route("/testpage")
def test():
    return render_template("./dom_study/get_json.html")




@app.route("/getTenants")
def getTenants():

    tenantName = request.args.get ("Tname")
    if tenantName is None:
        tenantName=""
    tenantName = "%" + tenantName +"%"

    tenantPhone = request.args.get ("Tphone")
    if tenantPhone is None:
        tenantPhone =""
    tenantPhone = str(tenantPhone)
    print(tenantPhone)
    tenantPhone = "%" + tenantPhone +"%"


    tenantRoom = request.args.get ("Troom")
    if tenantRoom is None:
        tenantRoom=""
    print(tenantRoom)
    tenantRoom = "%" + tenantRoom +"%"

    sql = "select * from tenant"
    # sql = "select * from tenant where 姓名 like '%s' and 手机 like '%s' and 房间号 like '%s' limit %s, %s;" % (tenantName,tenantPhone,
    #                                                                                       tenantRoom,(pagenumber-1)*pagesize,pagesize)

    sql = "select * from tenant where 姓名 like '%s' and 手机 like '%s' and 房间号 like '%s';" % (
        tenantName, tenantPhone,
        tenantRoom)
    print (sql)
    cursor.execute (sql)

    try:
        rv = cursor.fetchall ()
        payload = []
        content = {}
        for result in rv:
            content = {'name': result[1], 'tel': result[2], 'room': result[3],'startdate':result[4],'enddate':result[5]}
            payload.append (content)
            content = {}
        # return jsonify (payload)
        return jsonify(payload)

    except:
        pass



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
        return  redirect("http://127.0.0.1:5000/")
    else:
        return "failure"

@app.route("/queryAjax")
def getAjax():
    print(request.POST)
    return render_template(request,"ajax_demo_02.html")




if __name__ == '__main__':
    app.run (debug=True)
