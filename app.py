from flask import Flask,render_template,request
import pymysql
app = Flask (__name__)

conn = pymysql.connect("localhost",'root','0329','renthouse',charset='utf8')
cursor = conn.cursor()

@app.route ('/')
def hello_world():
    return render_template('home.html')

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
    tenantName = request.args.get ("Tname")
    print(tenantName)
    tenantName = "%" + tenantName +"%"

    tenantPhone = request.args.get ("Tphone")
    tenantPhone = "%" + tenantPhone +"%"

    tenantRoom = request.args.get ("Troom")
    tenantRoom = "%" + tenantRoom +"%"

    sql = "select * from tenant"
    sql = "select * from tenant where 姓名 like '%s' and 手机 like '%s' and 房间号 like '%s';" % (tenantName,tenantPhone,
                                                                                           tenantRoom)
    print (sql)
    cursor.execute (sql)

    try:
        results = cursor.fetchall ()
        print (results)

    except:
        pass

    return render_template('queryAll.html',results = results)

@app.route('/addNew')
def addNew():

    return render_template('addNew3.html')

@app.route('/save')
def save():

    addname=request.args.get("Addname")
    print(addname)


    addroom=request.args.get("addroom")
    print(addroom)
    # addstart=request.args.get("addstart")
    # addend=request.args.get("addend")

    if addname!=None:
        return "done"
    else:
        return "failure"



if __name__ == '__main__':
    app.run (debug=True)
