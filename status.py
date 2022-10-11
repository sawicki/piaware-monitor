import subprocess, mypushover as mpo
cmd = 'piaware-status'
check_list =  ["is running", 
            "is running", 
            "is not running", 
            "is running", 
            "is running", 
            "is listening", 
            "is connected",
            "is connected", 
            "is producing"]
# run cmd "piaware-status" and save output
sp = subprocess.Popen(cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
# Store the return code in rc variable
rc=sp.wait()
# Separate the output and error by communicating with sp variable.
out,err=sp.communicate()
out_list = str(out).split('\\n')
# remove blank lines
out_list= [x for x in out_list if x != '']
# generate list with true or false for each line of output
test_results = [test in out_list[i] for i, test in enumerate(check_list)]
if False in test_results:
     mpo.pushover('Flightaware East has a probmlem',
            'Flightaware East has a problme','climb')
else:
    pass

pass