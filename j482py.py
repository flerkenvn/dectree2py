#!/usr/bin/python3
import re, os, sys

varlist = list()
returntype = "string"
header = "#!/usr/bin/python3\n"

def getResult(line):
    global returntype
    res=""
    if (line.count(":")>0):
        remainder = (line[(line.find(":")):len(line)])
        res = ((re.search(r'[\d\w.-]+',remainder)).group())
        ret = re.search(r'[a-zA-Z]',res)
        if ret or returntype=="string":
            returntype="string"
            return "return \"" + res +"\""
        else:
            signloc = res.rfind("-")
            if (signloc>0):
                returntype="string"
            else:
                if (returntype!="string"):
                    returntype="numeric"
            return "return "  + res

if __name__ == "__main__":
	input_path = sys.argv[1]
	output_path = input_path + '.py'
	
	output = ""
	logfile = open(input_path).readlines()
	

	for line in logfile:
		depth = line.count("|") + 1 
		indent = '\t' * depth 	#make tab
		pattern = '\(.*\)' 		
		line = re.sub(pattern, "", line) #remove ()
		varname=((re.search(r'[-_\w]+',line)).group()) #find varname
		if varname not in varlist:
			varlist.append(varname)
		operator = re.search(r'[<=>]+',line).group()
		postop = (line[(line.find(operator)):len(line)])
		value = re.search(r'[\d.\w-]+',postop).group()
		result = getResult(line)
		if operator == '=':
			operator = '=='
		if not value.isdigit():
			value = "\"" + value + "\""
		full = indent + "if " + varname + " " + operator + " " + value + ":"
		output += full + '\n'
		# print(full)
		if result:
			result = indent + '\t' + result
			output += result + '\n'
			# print(result)
	output =header + "def classify(" + ', '.join(varlist) + '):\n' + output
	# print(output)
	f = open(output_path, 'w')
	f.write(output)
	f.close()
