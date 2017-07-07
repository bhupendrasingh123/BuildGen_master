import paramiko
class connection :
    def linuxConnection(self, buildName, directory):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #error_flag = []
        error_msg = []
        try: #connection to cable mw-dev-2
            print 'STEP 1 : Initiating connection with cable-mw-dev-2'
            ssh.connect('cable-mw-dev-2.in.nds.com', port=22, username='bbartwal', password='C(sc0nds')
            print 'Connection to cable-mw-dev-2.in.nds.com established successfully'
        except:
            print 'Connection failed to cable-mw-dev-2.in.nds.com'
            error_msg.append('Connection failed to cable-mw-dev-2.in.nds.com')
            ssh.close()
        try: # creating Directory for repo , changing directory and running bash
            print 'STEP 2 : make directory where repo will store'
            ssh.exec_command('mkdir ' + directory +' && cd ' + directory +' && bash')
            print ('directory created UPC_Repo')
        except:
            print ('could not create / locate directory UPC_Repo')
            error_msg.append('could not create / locate directory UPC_Repo')
        try: #initialising repo
            print 'STEP 3 : Initialising Repo'
            stdin, stdout, stderr = ssh.exec_command("cd " + directory +" && repo init --manifest-branch upc/" + buildName + " --manifest-url ssh://gpk-apl-grt7.cisco.com:29418/MANIFESTS.git")
            exit_status = stdout.channel.recv_exit_status()
            if exit_status == 0:
                print 'Repo Initialised successfully'
            else:
                print("Error", exit_status)
                error_msg.append('failed to initialise repo')
        except:
            print 'failed to initialise repo'
            error_msg.append('failed to initialise repo')
        try: #git checkout command execution
            print 'STEP 4 : starting GIT checkout'
            stdin, stdout,stderr =ssh.exec_command("cd " + directory +" && repo --no-pager forall -p --verbose --command 'git checkout $REPO_RREV'")
            exit_status = stdout.channel.recv_exit_status()
            if exit_status == 0:
                print 'git checkout command ran successfully'
            else:
                print("Error", exit_status)
                error_msg.append('Git checkout failed')
        except:
            print'Git checkout failed'
            error_msg.append('Git checkout failed')
        try: # repo sync command execution
            print 'STEP 5 : starting Repo sync'
            stdin, stdout, stderr = ssh.exec_command("cd " + directory +" && repo sync")
            exit_status = stdout.channel.recv_exit_status()
            if exit_status == 0:
                print 'repo sync successful'
            else:
                print("Error", exit_status)
                error_msg.append('repo sync failed')
        except:
            print 'repo sync failed'
            error_msg.append('repo sync failed')
        try : #git checkout command execution
            print 'STEP 6 : starting GIT checkout'
            stdin, stdout,stderr =ssh.exec_command("cd " + directory +" && repo --no-pager forall -p --verbose --command 'git checkout $REPO_RREV'")
            exit_status = stdout.channel.recv_exit_status()
            if exit_status == 0:
                print 'git checkout command successfully'
            else:
                print("Error", exit_status)
                error_msg.append('git checkout failed')
        except:
            print 'git checkout failed'
            error_msg.append('git checkout failed')

        try: # running artifacts command
            print 'STEP 7 : Starting to build artifacts'
            stdin, stdout,stderr =ssh.exec_command("cd " + directory +" && ./tools/artifact_retriever/retrieve_artifact.py")
            exit_status = stdout.channel.recv_exit_status()
            if exit_status == 0:
                print 'ran Artifacts command successfully'
            else:
                print("Error", exit_status)
                error_msg.append('building artifcats failed')
        except:
            print'building of artifcats failed'
            error_msg.append('building artifcats failed')
        ssh.close()
        print 'connection closed'
        return error_msg
'''
def main():
    con = connection()
    branch = 'CSCvf13217'
    directory = 'UPC_Repo'
    msg = con.linuxConnection(branch, directory)
    for data in msg :
        print data

if __name__ == '__main__':
    main()
'''
