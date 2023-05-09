try:
	from numpy import sin,cos,tan,arcsin,arccos,arctan,pi,sqrt
	import numpy as np
	is_numpy = True
except ImportError:
	from math import sin,cos,tan,pi,sqrt
	from math import asin as arcsin
	from math import acos as arccos
	from math import atan as arctan
	is_numpy = False
import warnings
from functools import reduce
DEGREES = pi/180
RADIANS = 180/pi

def get_vector(i_vect,j_vect,k_vect):
	'''takes 3 inputs converts them to i,j,k vects'''
	vect = str(i_vect)+"i+"+str(j_vect)+"j+"+str(k_vect)+"k"
	vect = vect.replace("+-","-")
	return vect

def split_string(string):
	'''
	accepts string input
	splits string based on arthematic operators '+' and '-'
	returns list containing splitted string
	ex :
		given input '2+3-4'
		returns ['2','3','-4']
	'''
	string = string.replace("-","+-")
	string = string.split("+")
	string = list(filter(None,string)) #to remove empty elements
	return string

def is_int(a):
	'''
	takes single string
	check given string can be converted into int or not
	returns true or false
	'''
	try:
		int(a)
		return True
	except:
		return False

def is_float(a):
	'''
	takes single string
	check given string can be converted into float or not
	returns true or false
	'''
	try:
		float(a)
		return True
	except:
		return False

def is_negative(string):
	'''check for negative sign infront of string'''
	if string[0]=="-":
		return True
	else:
		return False

def is_pre_value(string):
	'''checks string contains pre value'''
	if is_negative(string):
		string = string[1:]
	if string[0]==str(get_pre_value(string))[0]:
		return True
	else:
		return False

def is_post_value(string):
	'''checks string contains contains post value'''
	if is_negative(string):
		string = string[1:]
	pre_val = str(get_pre_value(string))
	if is_pre_value(string):  #To remove pre val since it's useless
		string = string[len(pre_val):]
	if str(get_post_value(string)) in str(get_digits(string)):
		return True
	else:
		return False

def solve(string):
	'''
	performs arthimatic operations addition and subtraction
	solves any type of string except trigs
	input = 3a+3+4
	returns = 3a+7
	'''
	string = split_string(string)
	numericals = []
	unknowns = []
	total = 0
	for i in string:
		if not get_variable(i):
			numericals.append(i)
		else:
			unknowns.append(i)
	for i in numericals:
		total+=float(i)
	added_unknowns = []
	while unknowns:
		val = 0
		sorted_var = get_elements_by_variable(unknowns,get_variable(unknowns[0]))
		unknowns = [var for var in unknowns if var not in sorted_var]
		for d in sorted_var:
			if is_pre_value(d):
				val+=get_pre_value(d)
			elif is_post_value(d):
				val+=get_post_value(d)
		if val:
			added_unknowns.append(str(val)+get_variable(sorted_var[0]))
	if total:
		added_unknowns.append(str(total))
	#print(added_unknowns,"d")
	return get_eqaution(added_unknowns)

def get_eqaution(target):
	'''takes list and add them as string ['2a',1,-3] = '2a+1-3'''
	string = ""
	for i in target:
		string+=str(i)+"+"
	string = string[:-1]
	string = string.replace("+-","-")
	if string:
		return string
	else:
		return "0"

def get_elements_by_variable(elements,variable):
	'''returns same elements having given variable'''
	same_var = []
	for i in elements:
		if variable == get_variable(i):
			same_var.append(i)
	return same_var

def get_alpha(string):
	'''
	returns every alphabet in string
	'''
	string = ''.join(list(filter(lambda x:x.isalpha(),string)))
	return string

def get_variable(string):
	'''
	returns variable of string
	ex :
		input 23s
		returns s
	'''
	var = ""
	string = get_alpha(string)
	return string

def get_variables(string):
	'''	returns list of varibles of string'''
	string = split_string(string)
	var = []
	for i in string:
		var.append(get_variable(i))
	var = list(filter(None,var))
	return var

def get_pre_variable(string):
	'''returns first variable only'''
	var = ""
	pre_val = str(get_pre_value(string))
	if is_pre_value(string):
		string = string[len(pre_val):]
	for i in string:
		if is_float(i) or i==".":
			break
		var+=i
	return var

def get_digits(string):
	'''returns every digit'''
	string = ''.join(list(filter(lambda x:x.isdigit(),string)))
	return string
def get_pre_value(string):
	'''
	returns first value of string
	input = 4s
	returns s
	'''
	pre_val = '0'
	multiplier = 1
	if is_negative(string): #remove negative sign
		string = string[1:]
		multiplier = -1
	for i in string:
		if not is_float(i) and i!='.':
			break
		pre_val+=i
	if pre_val=='0':
		pre_val = 1
	pre_val = float(pre_val)
	if int(pre_val)==pre_val:
		pre_val = int(pre_val)
	return pre_val*multiplier
def get_variable_coefficient(string):
	'''another name for prevalue'''
	return get_pre_value(string)
def get_post_value(string):
	'''
	returns last value of string
	input = cos28
	returns 28
	'''
	pre_val = str(get_pre_value(string))
	if is_pre_value(string):
		string = string[string.index(pre_val)+len(pre_val):]
	pre_var = get_pre_variable(string)
	if pre_var!="":
		string = string[string.index(pre_var)+len(pre_var):]
	if string!="":
		string = get_pre_value(string)
	else:
		string = 0
	return string
def check_for_unit_component(string):
	'''
	if given string contains no digits adds 1 and returns string
	input = 'i'
	returns '1i'
	'''
	negative = False
	if is_negative(string):
		string = string[1:]
		negative = True
	if not is_pre_value(string):
		string = "1"+string
	if negative:
		string = "-"+string
	return string
def remove_empty_spaces(string):
	'''removes empty spaces'''
	string = ''.join(string.split())
	return string
def get_components(vector):
	'''
	takes vector in form of string ex : '2i+3j+4k'
	splits string based on i,j,k components
	returns i,j,k components ex : '2i','3j','4k'
	'''	
	count=0
	vector = split_string(vector)
	i_vect = 0
	j_vect = 0
	k_vect = 0
	for vect in vector:
		vect = remove_empty_spaces(vect)
		vect = check_for_unit_component(vect)
		if "i" in vect[-1]:
			i_vect += float(vect[:-1])
		elif "j" in vect[-1]:
			j_vect += float(vect[:-1])
		elif "k" in vect[-1]:
			k_vect += float(vect[:-1])
		else:
			warnings.warn('Got value without component')
	return str(i_vect)+"i",str(j_vect)+"j",str(k_vect)+"k"
def get_components_with_unknown(vector):
	'''
	Copy of get_components
	splits vector with unknown variable and returns components
	'''
	vector = split_string(vector)
	i_vect = "0"
	j_vect = "0"
	k_vect = "0"
	for vect in vector:
		vect = remove_empty_spaces(vect)
		vect = check_for_unit_component(vect)
		if "i" in vect[-1]:
			i_vect += "+"+vect[:-1]
		elif "j" in vect[-1]:
			j_vect += "+"+vect[:-1]
		elif "k" in vect[-1]:
			k_vect += "+"+vect[:-1]
		else:
			warnings.warn('Got value without component')
	return i_vect+"i",j_vect+"j",k_vect+"k"
def get_x(vector):
	'''returns x component'''
	vector = get_components(vector)
	return vector[0][:-1]
def get_y(vector):
	'''returns y component'''
	vector = get_components(vector)
	return vector[1][:-1]
def get_z(vector):
	'''returns z component'''
	vector = get_components(vector)
	return vector[2][:-1]
def get_components_val(vector):
	'''returns values of components'''	
	return float(get_x(vector)),float(get_y(vector)),float(get_z(vector))
def get_vector_mag(vector):
	'''returns vector magnitude'''
	i_vect,j_vect,k_vect = get_components_val(vector)
	return sqrt(i_vect**2+j_vect**2+k_vect**2)
def get_unit_vector(vector):
	'''returns unit_vector of given vector'''
	i_vect,j_vect,k_vect = get_components_val(vector)
	vect_mag = get_vector_mag(vector)
	i_vect /= vect_mag
	j_vect /= vect_mag
	k_vect /= vect_mag
	return get_vector(i_vect,j_vect,k_vect)
def get_trig_vect(vector):
	'''
	takes vector as string
	vector can be of mixed trig form
	splits the vector into x,y,z components
	input = 'cos30i+30sin30cos40j-30sin45k'
	returns '0.8660254037844387i+11.49066664678467j-21.213203435596423k'
	'''
	i_vect,j_vect,k_vect = get_components_with_unknown(vector)
	i_vect = trig_addition(i_vect[:-1])
	j_vect = trig_addition(j_vect[:-1])
	k_vect = trig_addition(k_vect[:-1])
	return get_vector(i_vect,j_vect,k_vect)
def trig_addition(vect):
	'''takes trigs as string solves them and return the result'''
	result = 0
	vect = split_string(vect)
	for i in vect:
		splitted = split_trigs(i)
		result+=trig_multiplication(splitted)
	return result
def split_trigs(string):
	'''
	splits the string based on trigs returns list
	input = 60cos30sin30
	returns ['60','cos30','sin30']
	'''

	splitted = []
	pre_val = str(get_pre_value(string))
	if is_pre_value(string):
		splitted.append(pre_val)
		string = string[string.index(pre_val)+len(pre_val):]
	while string!="":
		post_val = str(get_post_value(string))
		pre_var = get_pre_variable(string)
		extra = 0
		if len(pre_var)>3:  #To avoid typo mistakes like cossin45
			warnings.warn('Missing degree in the string')
			pre_var = pre_var[3:]
			extra = 3
		if not is_post_value(string) and len(pre_var)>0:   #To avoid typo mistakes like cos
			warnings.warn('Missing degree in the string')
			pre_var = 'sin'
		splitted.append(pre_var+post_val)
		string = string[len(pre_var)+len(post_val)+extra:]
	return splitted
def trig_multiplication(vect):
	'''
	Takes multiple trigs in form of list
	returns sumation of all trigs
	'''
	result = 1
	for i in vect:
		result*=solve_trig(i)
	return result
def solve_trig(trig):
	'''
	take trig as input makes a math and returns the solution
	need to solve negative degrees acceptance
	'''
	post_val = get_post_value(trig)
	pre_val = get_pre_value(trig)
	post_val %= 360 #to get degrees less than 360
	post_val *= DEGREES
	res = 1
	if "sin" in trig:
		res = sin(post_val)
	elif "cos" in trig:
		res = cos(post_val)
	elif "tan" in trig:
		res = tan(post_val)
	elif "sec" in trig:
		res = arccos(post_val)
	elif "csc" in trig:
		res = arcsin(post_val)
	elif "cot" in trig:
		res = arctan(post_val)
	return res*pre_val
def multiply_vect_by_constant(unit_vector,force_mag):
	'''multiplies given vector by constant value'''
	i_vect,j_vect,k_vect = get_components_val(unit_vector)
	i_vect *= force_mag
	j_vect *= force_mag
	k_vect *= force_mag
	return get_vector(i_vect,j_vect,k_vect)
def get_component(force_mag,angle):
	'''returns magnitude of component which makes given angle from the vector'''
	force_mag = float(force_mag)
	return force_mag*cos(angle*DEGREES)
def get_force(component,angle):
	'''returns magnitude of vector which makes given angle from the component'''
	force_mag = float(component)
	return force_mag/cos(angle*DEGREES)
def get_angle(component,mag):
	'''returns angle b/w two vectors'''
	theta = arccos(component/mag)
	return theta*RADIANS
def get_angles(vector):
	'''returns angle made by vector with x,y,z axis respectively'''
	i_vect,j_vect,k_vect = get_components_val(vector)
	vect_mag = get_vector_mag(vector)
	return get_angle(i_vect,vect_mag),get_angle(j_vect,vect_mag),get_angle(k_vect,vect_mag)
def get_all(vector):
	'''returns all angles and all components of vector'''
	return get_angles(vector),get_components(vector)
def get_unknown_angle(theta_x,theta_y,direction = "positive"):
	'''returns third angle if two angles are given'''
	theta_x = theta_x*DEGREES
	theta_y = theta_y*DEGREES
	theta_z = sqrt(1-(cos(theta_x))**2-(cos(theta_y))**2)
	if direction=="negative":
		theta_z = -theta_z
	return arccos(theta_z)*RADIANS
def add_vectors(*vectors):
	'''returns addition of multiple of vectors'''
	i_vect,j_vect,k_vect = [0]*3
	for vect in vectors:
		i,j,k = get_components_val(vect)
		i_vect+=i
		j_vect+=j
		k_vect+=k
	return get_vector(i_vect,j_vect,k_vect)
def add_unknown_vectors(*vectors):
	'''
	takes multiple vectors having unknowns
	returns addition of all vectors
	'''
	x_vects = ''
	y_vects = ''
	z_vects = ''
	remove_last_value = lambda x:x[:-1]
	for vect in vectors:
		x_vect,y_vect,z_vect = list(map(remove_last_value,get_components_with_unknown(vect)))
		x_vects += x_vect+"+"
		y_vects += y_vect+"+"
		z_vects += z_vect+"+"
	x_vects,y_vects,z_vects = list(map(remove_last_value,[x_vects,y_vects,z_vects]))
	x_vects = x_vects.replace("+-","-")
	y_vects = y_vects.replace("+-","-")
	z_vects = z_vects.replace("+-","-")
	x_vects,y_vects,z_vects = solve(x_vects),solve(y_vects),solve(z_vects)
	print(x_vects)
	print(y_vects)
	print(z_vects)
	return x_vects,y_vects,z_vects
def multiply_vect_by_unknown(unit_vector,unknown):
	'''multiply each component of vector by given unknown'''
	i_vect,j_vect,k_vect = list(map(str,get_components_val(unit_vector)))
	i_vect += unknown
	j_vect += unknown
	k_vect += unknown
	return get_vector(i_vect,j_vect,k_vect)
def solve_for_one_unknown(vector):
	'''check unknown variable and returns value of that variable'''
	vector = solve(vector)
	vector = split_string(vector)
	if len(vector)>2:
		raise Exception("Got more than one variable, This can solve for only one variable")
	value = -float(vector[1])/get_pre_value(vector[0]) #first val contains var. 'solve' returns var vals first
	print(value)
	return str(value)
def substitute_one_variable(vector,var):
	'''returns solution for the given variable'''
	vector = solve(vector)
	val = split_string(vector)
	string = ""
	for i in range(len(val)):
		if get_variable(val[i])==var:
			for j in range(len(val)-1,0,-1):
				a = -get_pre_value(val[i-j])/get_pre_value(val[i])
				string+=str(a)+get_variable(val[i-j])+"+"
			break
	string = string[:-1]
	string = string.replace("+-","-")
	return string
def cross(vect1,vect2):
	'''backup to make cross product if numpy doesn't exist'''
	i_vect_f,j_vect_f,k_vect_f = vect1
	i_vect_r,j_vect_r,k_vect_r = vect2
	i_vect = j_vect_r*k_vect_f-j_vect_f*k_vect_r
	j_vect = k_vect_r*i_vect_f-k_vect_f*i_vect_r
	k_vect = i_vect_r*j_vect_f-i_vect_f*j_vect_r
	return i_vect,j_vect,k_vect
def cross_product(*vectors):
	'''returns cross product of the given vectors'''
	vects = list(map(lambda x:get_components_val(x),vectors))
	if is_numpy:
		i_vect,j_vect,k_vect = list(reduce(lambda x,y:np.cross(x,y),vects))
	else:
		i_vect,j_vect,k_vect = list(reduce(lambda x,y:cross(x,y),vects))
	return get_vector(i_vect,j_vect,k_vect)
def dot_product(vect1,vect2):
	'''returns dot product of two vectors'''
	i_vect_1,j_vect_1,k_vect_1 = get_components_val(vect1)
	i_vect_2,j_vect_2,k_vect_2 = get_components_val(vect2)
	i_vect = i_vect_1*i_vect_2
	j_vect = j_vect_1*j_vect_2
	k_vect = k_vect_1*k_vect_2
	tot = i_vect+j_vect+k_vect
	return tot
def get_unknown_variable(vect):
	#string = split_string(string)
	for i in vect:
		if not is_float(i):
			return i
def get_unknown_side_by_hypot(l):
	'''returns one unknown side value if we know one side and hypotheses'''
	val = sqrt(float(l[-1])**2-float(l[-2])**2-float(l[-3])**2)
	return val
def get_var_val_of_unknown_coord(vect,mag):
	'''returns unknown value of the unknown variable if we know 2 or 1 components and mag of vect'''
	vect = list(map(lambda x:x[:-1],get_components_with_unknown(vect)))
	vect = list(map(lambda x:solve(x),vect))
	vect2 = vect.copy()
	vect.append(-float(mag))
	unknown_val = get_unknown_variable(vect)
	vect.remove(unknown_val)
	val = get_unknown_side_by_hypot(vect)
	val = val/get_pre_value(unknown_val)
	return val
def solve_unknown_coord(vect,mag):
	'''solves vector containing unknown component if we know 2 or 1 components and mag of vect'''
	vect = list(map(lambda x:x[:-1],get_components_with_unknown(vect)))
	vect = list(map(lambda x:solve(x),vect))
	vect2 = vect.copy()
	vect.append(-float(mag))
	unknown_val = get_unknown_variable(vect)
	vect.remove(unknown_val)
	val = get_unknown_side_by_hypot(vect)
	vect2[vect2.index(unknown_val)] = val
	i_vect,j_vect,k_vect = vect2
	return get_vector(i_vect,j_vect,k_vect)
def get_2Dvect_angle(string):
	'''returns angle of vect if we know two components'''
	i_vect,j_vect,k_vect = get_components_val(string)
	return arctan(j_vect/i_vect)*RADIANS
def substitute_variables(vector,**knowns):
	'''
	substitute given values for unknown values
	input should be string and unknown values
	syntax substitute_variables('2a+3b+4c',a = 2,b = 3a,c = 2b)
	returns 70
	'''
	vector = solve(vector)
	vector = split_string(vector)
	for i,val1 in knowns.items():
		for j,val2 in knowns.items():
			if i in val2:
				if j in val1:
					if get_pre_value(val2)*get_pre_value(val1)==1:
						knowns[i] = i
						knowns[j] = j
					else:
						raise Exception("Math Error Equation Mismatched")
				else:
					knowns[j] = str(get_pre_value(val1)*get_pre_value(val2))
	for i,value in knowns.items():
		val = 0
		for j in vector:
			if get_variable(j)==i:
				vector.remove(j)
				val += get_pre_value(j)*get_pre_value(value)
		vector.append(str(val)+get_variable(value))
	print(solve(get_eqaution(vector)))
	return solve(get_eqaution(vector))
def substitute_multivariable(vector,**knowns):
	'''
	subtitute variable in place of given variable
	substitute given values for unknown values
	input should be string and unknown values
	syntax substitute_multivariable('2a+3b+4c',a = 2,b = 3a,c = 2b)
	returns '9a+8b+4'
	'''
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
					res.append(substitute_variables(vect,**kwargs))
	vector+=res
	vector = solve(get_eqaution(vector))
	print(vector)
	return vector
def solve_vectors(p_vect,q_vect):
	'''
	Takes two strings containing same components
	solves two strings contains two unknowns
	string1 = '2a+3b-7'
	string2 = '3a+10b-5'
	returns 5,-1 which means a = 5 b = -1
	'''
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