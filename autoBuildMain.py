from bottle import get, post, request, run, route, template
from connect_to_linux import*
from userBuildData import*
from presql_check import*
def main():
    print("test")
    bd = BuildData()
    con = connection()
    dbF = dbFuntion()
    @route('/build-gen')
    def buildUi():
        return '''
            <form action="/build-gen" method="post">
            <h1> Auto build Generation </h1>
            </br></br>
            User Name <input name="userName" type="text" /></br>
            </br>
            Please enter Branch/US name to get repository for <input name="branchName" type="text" /></br>
            </br>
            Select the Binary Type <select name="binaryType">
            <option value=" CISCO_REL_DOCSIS_AUTH_UT "> CISCO_REL_DOCSIS_AUTH_UT </option>
            <option value=" CISCO_REL_DOCSIS_AUTH_UT_MANUAL "> CISCO_REL_DOCSIS_AUTH_UT_MANUAL </option>
            <option value=" CISCO_REL_NO-PS "> CISCO_REL_NO-PS </option>
            <option value=" CISCO_REL_NO-PS_MANUAL "> CISCO_REL_NO-PS_MANUAL </option>
            <option value=" CISCO_RLDBG_ALL_LEVELS_DOCSIS_AUTH_RPROF "> CISCO_RLDBG_ALL_LEVELS_DOCSIS_AUTH_RPROF </option>
            <option value=" CISCO_RLDBG_ALL_LEVELS_DOCSIS_AUTH_RPROF_MANUAL "> CISCO_RLDBG_ALL_LEVELS_DOCSIS_AUTH_RPROF_MANUAL </option>
            <option value=" SAMSUNG_PROD_ALL_LEVELS_DOCSIS_AUTH_PRODCAK_REMOTEDIAGBIN_UP "> SAMSUNG_PROD_ALL_LEVELS_DOCSIS_AUTH_PRODCAK_REMOTEDIAGBIN_UP </option>
            <option value=" SAMSUNG_PROD_ALL_LEVELS_DOCSIS_AUTH_REMOTEDIAGBIN_UT "> SAMSUNG_PROD_ALL_LEVELS_DOCSIS_AUTH_REMOTEDIAGBIN_UT </option>
            <option value=" SAMSUNG_ PROD_DOCSIS_AUTH_MAXRUNIPC_HARDCODED_PRODCAK_UP "> SAMSUNG_ PROD_DOCSIS_AUTH_MAXRUNIPC_HARDCODED_PRODCAK_UP </option>
            <option value=" SAMSUNG_ PROD_DOCSIS_AUTH_MAXRUNIPC_HARDCODED_TESTCAK_UP "> SAMSUNG_ PROD_DOCSIS_AUTH_MAXRUNIPC_HARDCODED_TESTCAK_UP </option>
            <option value=" SAMSUNG_ PROD_DOCSIS_AUTH_PRODCAK_UP "> SAMSUNG_ PROD_DOCSIS_AUTH_PRODCAK_UP </option>
            <option value=" SAMSUNG_ PROD_DOCSIS_AUTH_UT "> SAMSUNG_ PROD_DOCSIS_AUTH_UT </option>
            <option value=" SAMSUNG_ REL_DOCSIS_AUTH_PRODCAK_UP "> SAMSUNG_ REL_DOCSIS_AUTH_PRODCAK_UP </option>
            <option value=" SAMSUNG_ REL_DOCSIS_AUTH_UT "> SAMSUNG_ REL_DOCSIS_AUTH_UT </option>
            <option value=" SAMSUNG_ REL_NO-PS "> SAMSUNG_ REL_NO-PS </option>
            <option value=" SAMSUNG_ REL_NO-PS_DOCSIS "> SAMSUNG_ REL_NO-PS_DOCSIS </option>
            <option value=" SAMSUNG_ RLDBG_ALL_LEVELS_DOCSIS_AUTH_DIAG_UT "> SAMSUNG_ RLDBG_ALL_LEVELS_DOCSIS_AUTH_DIAG_UT </option>
            <option value=" SAMSUNG_ RLDBG_ALL_LEVELS_DOCSIS_AUTH_PRODCAK_DIAG_UP "> SAMSUNG_ RLDBG_ALL_LEVELS_DOCSIS_AUTH_PRODCAK_DIAG_UP </option>
            <option value=" SAMSUNG_ RLDBG_ALL_LEVELS_DOCSIS_AUTH_RPROF "> SAMSUNG_ RLDBG_ALL_LEVELS_DOCSIS_AUTH_RPROF </option>
            <option value=" SAMSUNG_ RLDBG_DOCSIS_AUTH_PRODCAK_UP "> SAMSUNG_ RLDBG_DOCSIS_AUTH_PRODCAK_UP </option>
            <option value=" SAMSUNG_ RLDBG_DOCSIS_AUTH_UT "> SAMSUNG_ RLDBG_DOCSIS_AUTH_UT </option>
            </select> </br>
            </br>
            <input value="Start" type="submit" />
            </form>
            '''

    @post('/build-gen') # or @route('/build-gen', method='POST')
    def generateBuild():
        bd.set_userName(request.forms.get('userName'))
        bd.set_buildName(request.forms.get('branchName'))
        bd.set_buildType(request.forms.get('binaryType'))
        #con.servercon()
        branch = bd.get_buildName()
        print 'branch name  : ' + branch
        directory = 'UPC_Repo'
        if(len(bd.get_userName()) == 0):
            return '<h2> go back to the previous page and enter proper User Name </h2> </br> <a href = "http://localhost:8080/build-gen"> previous page </a>'
        if(len(bd.get_buildName()) == 0):
            return '<h2> go back to the previous page and enter proper Branch Name </h2> </br> <a href = "http://localhost:8080/build-gen"> previous page </a>'
        if(len(bd.get_buildType()) == 0):
            return '<h2> go back to the previous page and Select Binary Type </h2> </br> <a href = "http://localhost:8080/build-gen"> previous page </a>'
        dbF.addValues(bd.get_userName(), bd.get_buildName(), bd.get_buildType(), dbF.currentDateTime(), 'NotStarted')
        msg = ''
        if len(msg) == 0 :
            print "generating binary"
            return '<h1> Thanks ' + bd.get_userName() + ' for the inputs </h1></br><h3> Branch Name : ' + bd.get_buildName() + '</h3><h3> Binray Type : ' + bd.get_buildType() + '</h3> </br> <a href = "http://localhost:8080/build-gen"> home </a> </br> Build in Progress ..... </br>'
        else :
            return '<h1>' + msg + '</h1>'

    run(host='localhost', port=8080, debug=True)

if __name__ == '__main__':
    main()
