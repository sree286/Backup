try:
	from numpy import sin,cos,tan,arcsin,arccos,arctan,pi,sqrt
except ImportError:
	from math import sin,cos,tan,pi,sqrt
	from math import asin as arcsin
	from math import acos as arccos
	from math import atan as arctan
DEGREES = pi/180
RADIANS = 180/pi
def split_string(string):
	string = string.replace("-","+-")
	if string[0]=="+":
		string = string[1:]
	return string.split("+")

def get_components(vector):
	vector = split_string(vector)
	i_vect = ""
	j_vect = ""
	k_vect = ""
	for vect in vector:
		vect = check_for_unit_variable(vect)
		if "i" in vect[-1]:
			i_vect = vect
		elif "j" in vect[-1]:
			j_vect = vect
		elif "k" in vect[-1]:
			k_vect = vect
	return i_vect,j_vect,k_vect
def is_int(a):
	try:
		int(a)
		return True
	except:
		return False
def check_for_unit_variable(string):
	val = False
	for i in string:
		if is_int(i):
			val = True
	if not val:
		var = get_variable(string)
		rep = "1"+var
		string = string.replace(var,rep)
	return string
def get_vector(i_vect,j_vect,k_vect):
	vect = str(i_vect)+"i+"+str(j_vect)+"j+"+str(k_vect)+"k"
	vect = vect.replace("+-","-")
	return vect

def get_vector_mag(vector):
	i_vect,j_vect,k_vect = get_components_val(vector)
	return sqrt(i_vect**2+j_vect**2+k_vect**2)

def get_unit_vector(vector):
	i_vect,j_vect,k_vect = get_components_val(vector)
	vect_mag = get_vector_mag(vector)
	i_vect /= vect_mag
	j_vect /= vect_mag
	k_vect /= vect_mag
	return get_vector(i_vect,j_vect,k_vect)
def get_trig_vect(vector):
	i_vect,j_vect,k_vect = get_components(vector)
	i_vect = split_trigs(i_vect[:-1])
	j_vect = split_trigs(j_vect[:-1])
	k_vect = split_trigs(k_vect[:-1])
	return get_vector(trigs(i_vect),trigs(j_vect),trigs(k_vect))
def trigs(vect):
	result = 1
	if vect==[]:
		vect = "0"
	for i in vect:
		if i!="" and i!="-":
			result*=solve_trig(i)
	if vect[-1]=="-":
		result = -result
	return str(result)
def get_post_value(string):
	
	a = ""
	count = 0
	for i in string:
		if is_float(i):
			count = 1
			a+=i
		else:
			count = 0
		if a!="" and count == 0:
			break
	if a:
		if float(a)==int(a):
			return int(a)
		else:
			return float(a)
	else:
		return 1
def split_trigs(string):
	res = []
	operator = ""
	while string!="":
		if "sin" in string:
			index = string.index("sin")
			a = "sin"+str(get_post_value(string[index:]))
			res.append(a)
			string = string.replace(a,"")
		elif "cos" in string:
			index = string.index("cos")
			a = "cos"+str(get_post_value(string[index:]))
			res.append(a)
			string = string.replace(a,"")
		elif "tan" in string:
			index = string.index("tan")
			a = "tan"+str(get_post_value(string[index:]))
			res.append(a)
			string = string.replace(a,"")
		elif "cot" in string:
			index = string.index("cot")
			a = "cot"+str(get_post_value(string[index:]))
			res.append(a)
			string = string.replace(a,"")
		elif "sec" in string:
			index = string.index("sec")
			a = "sec"+str(get_post_value(string[index:]))
			res.append(a)
			string = string.replace(a,"")
		elif "csc" in string:
			index = string.index("csc")
			a = "csc"+str(get_post_value(string[index:]))
			res.append(a)
			string = string.replace(a,"")
		else:
			res.append(string)
			string = ""
	return res
def get_numerical(force_mag):
	force_mag = str(force_mag)
	if force_mag[-1] == 'N':
		force_mag = force_mag[:-1]
	force_mag = float(force_mag)
	return force_mag
def multiply_by_unit_vector(unit_vector,force_mag):
	force_mag = get_numerical(force_mag)
	i_vect,j_vect,k_vect = get_components_val(unit_vector)
	i_vect *= force_mag
	j_vect *= force_mag
	k_vect *= force_mag
	return get_vector(i_vect,j_vect,k_vect)
def get_component(force_mag,angle):
	force_mag = get_numerical(force_mag)
	return force_mag*cos(angle*DEGREES)
def get_force(component,angle):
	force_mag = get_numerical(component)
	return force_mag/cos(angle*DEGREES)
def get_angles(vector):
	i_vect,j_vect,k_vect = get_components_val(vector)
	vect_mag = get_vector_mag(vector)
	return get_angle(i_vect,vect_mag),get_angle(j_vect,vect_mag),get_angle(k_vect,vect_mag)
def get_all(vector):
	return get_angles(vector),get_components(vector)
def get_angle(component,mag):
	theta = arccos(component/mag)
	return theta*RADIANS

def get_unit_angle(theta_x,theta_y,direction = "positive"):
	theta_x = theta_x*DEGREES
	theta_y = theta_y*DEGREES
	theta_z = sqrt(1-(cos(theta_x))**2-(cos(theta_y))**2)
	if direction=="negative":
		theta_z = -theta_z
	return arccos(theta_z)*RADIANS

def add_vectors(p_vect,q_vect):
	i_vect,j_vect,k_vect = get_components_val(p_vect)
	x_vect,y_vect,z_vect = get_components_val(q_vect)
	return get_vector(i_vect+x_vect,j_vect+y_vect,k_vect+z_vect)

def get_x(vector):
	vector = get_components(vector)
	return vector[0][:-1]
def get_y(vector):
	vector = get_components(vector)
	return vector[1][:-1]
def get_z(vector):
	vector = get_components(vector)
	return vector[2][:-1]

def get_components_val(vector):
	i_val = get_x(vector)
	if i_val!="":
		i_val = float(i_val)
	else:
		i_val = 0
	j_val = get_y(vector)
	if j_val!="":
		j_val = float(j_val)
	else:
		j_val = 0
	k_val = get_z(vector)
	if k_val!="":
		k_val = float(k_val)
	else:
		k_val = 0
	return i_val,j_val,k_val

def add_unknown_vectors(*vectors):
	x_vects = ''
	y_vects = ''
	z_vects = ''
	for vect in vectors:
		x_vect = get_x(vect)
		y_vect = get_y(vect)
		z_vect = get_z(vect)
		if x_vect!="":
			x_vects += x_vect+"+"
		if y_vect!="":
			y_vects += y_vect+"+"
		if z_vect!="":
			z_vects += z_vect+"+"
	x_vects = x_vects[:-1]
	y_vects = y_vects[:-1]
	z_vects = z_vects[:-1]
	x_vects = x_vects.replace("+-","-")
	y_vects = y_vects.replace("+-","-")
	z_vects = z_vects.replace("+-","-")
	x_vects,y_vects,z_vects = solve(x_vects),solve(y_vects),solve(z_vects)
	print(x_vects)
	print(y_vects)
	print(z_vects)
	return x_vects,y_vects,z_vects
def multiply_by_unknown_unit_vector(unit_vector,unknown):
	i_vect,j_vect,k_vect = list(map(str,get_components_val(unit_vector)))
	i_vect += unknown
	j_vect += unknown
	k_vect += unknown
	return get_vector(i_vect,j_vect,k_vect)
def get_numbers(string):
	var = get_variable(string)
	string = string.replace(var,"")
	if string == "" or string == "-":
		string += "1"
	string+='0'
	return float(string)
def get_pre_value(string):
	string = string.replace(str(get_post_value(string)),"")
	return get_numbers(string)
def get_variable(string):
	var = ""
	for s in string:
		if s.isalpha():
			var+=s
	return var
def get_variable_coefficient(string):
	return get_pre_value(string)
def solve_one_var(vector):
	val = []
	vector = solve(vector)
	vector = split_string(vector)
	for i in vector:   #It finds zeros and remove them
		if not get_variable_coefficient(i)==0:
			val.append(i)
	if len(val)>2:
		raise Exception("Got more than one variable, This can solve for only one variable")
	for i in range(2):
		if get_variable(val[i])!="":
			value = -float(val[i-1])/get_variable_coefficient(val[i])
	print(value)
	return str(value)
def filter_operators(string):
	string = string[:-1]
	string = string.replace("+-","-")
	return string
def get_one_var(vector,var):
	val = []
	vector = solve(vector)
	vector = split_string(vector)
	string = ""
	print(vector)
	for i in vector:   #It finds zeros and remove them
		if not get_variable_coefficient(i)==0:
			val.append(i)
	print(val)
	val  = vector
	for i in range(len(vector)):
		if get_variable(val[i])==var:
			for j in range(len(val)-1,0,-1):
				a = -get_variable_coefficient(val[i-j])/get_variable_coefficient(val[i])
				string+=str(a)+get_variable(val[i-j])+"+"
			break

	string = string[:-1]
	string = string.replace("+-","-")
	return string
	#return string
def solve(vector):
	vector = split_string(vector)
	numericals = []
	unknowns = []
	total = 0
	for i in vector:
		if get_variable(i)=="":
			numericals.append(i)
		else:
			unknowns.append(i)
	for i in numericals:
		total+=get_variable_coefficient(i)
	var_list = get_variables(unknowns)
	add_unknowns = []
	for i in var_list:
		val = 0
		for j in unknowns:
			if i==get_variable(j):
				val+=get_variable_coefficient(j)
		add_unknowns.append(str(val)+i)
	add_unknowns.append(str(total))
	return get_eqaution(add_unknowns)
def get_variables(unknowns):
	var_list = []
	for k in unknowns:
		var = get_variable(k)
		if var not in var_list:
			var_list.append(var)
	return var_list
def get_eqaution(target):
	string = ""
	for i in target:
		string+=str(i)+"+"
	string = string[:-1]
	string = string.replace("+-","-")
	return string

def solve_vectors(p_vect,q_vect):
	p_vect = split_string(p_vect)
	q_vect = split_string(q_vect)
	if len(p_vect)!=len(q_vect):
		while len(p_vect)<len(q_vect):
			p_vect.append("0")
		while len(q_vect)<len(p_vect):
			q_vect.append("0")
	p_vect_val = [get_variable_coefficient(i) for i in p_vect]
	q_vect_val = [get_variable_coefficient(i) for i in q_vect]
	p_vect_var = [get_variable(i) for i in p_vect]
	q_vect_var = [get_variable(i) for i in q_vect]
	eqa_1 = [float(i)*float(q_vect_val[0]) for i in p_vect_val]
	eqa_2 = [float(i)*float(p_vect_val[0]) for i in q_vect_val]
	eqa_3 = []
	for i in range(len(eqa_1)):
		k = 0
		if p_vect_var[i]==q_vect_var[i]:
			k = eqa_1[i]-eqa_2[i]
			eqa_3.append(k)
	try:
		var_2 = -eqa_3[2]/eqa_3[1]
	except ZeroDivisionError:
		print("Some Error")
		var_2 = 1
	eqa_2[1] = eqa_2[1]*var_2
	var_1 = (-eqa_2[2]-eqa_2[1])/eqa_2[0]
	print((var_1,var_2))
	return str(var_1),str(var_2)
def is_float(val):
	try:
		float(val)
		return True
	except:
		return False

'''def substitude_unknowns(vector,*knowns):
	vect = split_string(vector)
	if len(vect)!=len(knowns):
		raise Exception('Length Mismatched, Use "None" in place of unknown variable or no variables')
	count = 0
	for i,j in zip(vect,knowns):
		if j!=None:
			vect[count] = get_variable_coefficient(i)*j
		count+=1
	return solve(get_eqaution(vect))'''
def substitude_variables(vector,**knowns):
	vector = solve(vector)
	#knowns = solve(knowns)
	vector = split_string(vector)
	for i,val1 in knowns.items():
		for j,val2 in knowns.items():
			if i in val2:
				if j in val1:
					if get_variable_coefficient(val2)*get_variable_coefficient(val1)==1:
						knowns[i] = i
						knowns[j] = j
						pass
					else:
						raise Exception("Math Error Equation Mismatched")
				else:
					knowns[j] = str(get_variable_coefficient(val1)*get_variable_coefficient(val2))
	for i,value in knowns.items():
		val = 0
		#print(value)
		for j in vector:
			if get_variable(j)==i:
				vector.remove(j)
				val += get_variable_coefficient(j)*get_variable_coefficient(value)
		vector.append(str(val)+get_variable(value))
	#vector+=vect
	print(solve(get_eqaution(vector)))
	return solve(get_eqaution(vector))
def substitude_multivariable(vector,**knowns):
	res = []
	vector = split_string(vector)
	for i,val in knowns.items():
		for s in vector:
			if i in s:
				vector.remove(s)
				vect = s
				values = split_string(val)
				for k in values:
					kwargs = {i:k}
					res.append(substitude_variables(vect,**kwargs))
	vector+=res
	vector = solve(get_eqaution(vector))
	print(vector)
	return vector
def make_vect(string):
	vector = list(get_components(string))
	vect = []
	for v in vector:
		vect.append(v[:-1])
	if vect[0]=="":
		vect[0] = "0"
	if vect[1]=="":
		vect[1] = "0"
	if vect[2]=="":
		vect[2] = "0"
	return get_vector(vect[0],vect[1],vect[2])
def get_quadrant(integer):
	integer %= 360
	#print(integer)
	if integer<=90:
		return 1
	elif 90<integer<=180:
		return 2
	elif 180<integer<=270:
		return 3
	elif 270<integer:
		return 4
def solve_trig(trig):
	val = get_post_value(trig)
	pre_val = get_pre_value(trig)
	quadrant = get_quadrant(val)
	#print(quadrant,val)
	val %= 180
	val *= DEGREES
	negative = False
	res = 0
	if quadrant > 1:
		negative = True
	if "sin" in trig:
		if quadrant==2:
			negative = False
		res = sin(val)
	elif "cos" in trig:
		if quadrant==4:
			negative = False
		res = cos(val)
	elif "tan" in trig:
		if quadrant==3:
			negative = False
		res = tan(val)
	elif "sec" in trig:
		if quadrant==4:
			negative = False
		res = arccos(val)
	elif "csc" in trig:
		if quadrant==2:
			negative = False
		res = arcsin(val)
	elif "cot" in trig:
		if quadrant==3:
			negative = False
		res = arctan(val)
	if negative:
		res = -res
	return res*pre_val

def get_unknown_coord(vect,mag):
	vects = get_x(vect),get_y(vect),get_z(vect)
	unknown = ""
	for i in range(3):
		if not is_float(vects[i]):
			unknown_coeff = get_variable_coefficient(vects[i])
			val = sqrt(float(mag)**2-float(vects[i-1])**2-float(vects[i-2])**2)
			val/=unknown_coeff
			return vects[i],val


def solve_unknown_coord(vect,mag):
	unknown,unknown_val = get_unknown_coord(vect,mag)
	i_vect,j_vect,k_vect = get_x(vect),get_y(vect),get_z(vect)
	vects = []
	for i in i_vect,j_vect,k_vect:
		vects.append(i)
	for i in range(3):
		if vects[i]==unknown:
			vects[i]=unknown_val
	i_vect,j_vect,k_vect = vects
	return get_vector(i_vect,j_vect,k_vect)
 
def get_vect_angle(string):
	i_vect,j_vect,k_vect = get_components_val(string)
	return arctan(j_vect/i_vect)*RADIANS
def cross_product(position,force):
	i_vect_f,j_vect_f,k_vect_f = get_components_val(force)
	i_vect_r,j_vect_r,k_vect_r = get_components_val(position)
	i_vect = j_vect_r*k_vect_f-j_vect_f*k_vect_r
	j_vect = k_vect_r*i_vect_f-k_vect_f*i_vect_r
	k_vect = i_vect_r*j_vect_f-i_vect_f*j_vect_r
	return get_vector(i_vect,j_vect,k_vect)
def dot_product(vect1,vect2):
	i_vect_1,j_vect_1,k_vect_1 = get_components_val(vect1)
	i_vect_2,j_vect_2,k_vect_2 = get_components_val(vect2)
	i_vect = i_vect_1*i_vect_2
	j_vect = j_vect_1*j_vect_2
	k_vect = k_vect_1*k_vect_2
	tot = i_vect+j_vect+k_vect
	return tot
 