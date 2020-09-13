from flask import Flask,render_template,request,url_for,redirect,jsonify,json,Response
import datetime
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


@app.route("/apitest")  # 测试学习用
def apitest():
    return json.dumps({'a':1,'b':2})

@app.route("/apitest2") # 测试学习用
def apitest2():
    return jsonify([
                       {'name':"狗伦",'age':8,'school':'中澳'},
                       {'name': "蔡徐昆", 'age': 28, 'school': '野鸡学校'},
                       {'name': "王大力", 'age': 18, 'school': '哈弗'},
                       {'name': "沙老板", 'age': 8, 'school': '南京大学'},
                       {'name': "钟无艳", 'age': 8, 'school': '北邮'},
                       {'name': "吴法天", 'age': 8, 'school': '海洋大学'},
                       {'name':"杨涛","age":38,"school":"澳门理工"},
                       {'name':"张毅","age":30,"school":"深圳大学"},
                       {'name':"孙二朗","age":10,"school":"中山大学"},
                       {'name':"刁三","age":15,"school":"早稻田大学"},
                       {'name':"道明寺","age":28,"school":"台北大学"},
                       {'name':"明道","age":29,"school":"福田三中"},
                       {'name':"樱木花道","age":36,"school":"神奈川三中"},
                       ])

@app.route("/testpage") # 测试学习ajax用
def test():
    return render_template("./dom_study/get_json.html")

@app.route("/getTenants")  # 最终方案，支持ajax
def getTenants():
    # 从前台获取租客姓名
    tenantName = request.args.get ("Tname")
    if tenantName is None:
        tenantName=""
    tenantName = "%" + tenantName +"%"

    # 从前台获取租客电话
    tenantPhone = request.args.get ("Tphone")
    if tenantPhone is None:
        tenantPhone =""
    tenantPhone = str(tenantPhone)
    tenantPhone = "%" + tenantPhone +"%"

    # 从前台获取房间号
    tenantRoom = request.args.get ("Troom")
    if tenantRoom is None:
        tenantRoom=""
    tenantRoom = "%" + tenantRoom +"%"

    # 执行查询
    sql = "select * from tenant where 姓名 like '%s' and 手机 like '%s' and 房间号 like '%s';" % (
        tenantName, tenantPhone, tenantRoom)
    print(sql)
    cursor.execute (sql)

    try:
        rv = cursor.fetchall ()
        payload = []
        content = {}
        for result in rv:
            print(result)

            startdate = datetime.datetime.strftime(result[4],"%Y-%m-%d")
            enddate = datetime.datetime.strftime (result[5], "%Y-%m-%d")

            content = {'name': result[1], 'tel': result[2], 'room': result[3],'startdate':startdate,'enddate':enddate}
            payload.append (content)
            content = {}

        return jsonify(payload)

    except:
        pass

@app.route('/addNew')    # 添加记录
def addNew():
    if cookie == "yes":
        return render_template('add.html', cookie=cookie)
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


if __name__ == '__main__':
    app.run (debug=True)
