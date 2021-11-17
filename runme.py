import joulescope

def run():
    #Create file localy to see where is it stored on the Jenkins agent
    print("Started the script") 

    device = joulescope.scan_require_one(config='ignore')

    with device:
        print("Joulescope started")
        f= open("report_from_script.txt","w+")

        f.write("The Joulescope is started succcesfully, and the script runs fine!")


    return 0


if __name__ == '__main__':
    run()