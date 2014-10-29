def generate_zp_powers(num, p):
	generated_list = [(num**i % p) for i in range(0, p-1)]
	return generated_list


def order_of_modulo_set(g, modulo_set_num):
	generated_list = [(g**i % modulo_set_num) for i in range(0, modulo_set_num - 1)]
	unique_list = []
	
	for num in generated_list:
		if num not in unique_list:
			unique_list.append(num)
	
	return len(unique_list)

def number_of_invertable_elements(modulo_num):
	count = 0
	for i in range(1, modulo_num):
		# if gcd(i, modulo_num) == 1:
		# We're looking for gcd(x, N)
		# We know that (a * x) + (b * y) = gcd(x,y),
		# so "b" can be zero and we just need to find an (a * x)
		# that gives us 1 mod N
		#
		# This can be tested with Fermet's theorem: Given x in Zp,
		# if x^p-1 = 1, it is relatively prime within Zp (and thus has an inverse!) 
		if (i**(modulo_num-2)) % modulo_num == 1:
			count +=1
	return count



def exponential_n(g, exp, mod=None):
	"""
	Problem: Given g in G and e, we want g^e mod G

	Solution: Repeated Squaring Algorithm
		
		- Convert e to binary digits
		- Take all 1-points in the binary number and compute their
		  corresponding exponents (2^n)
		    - e.g. g^53 ==> 53 = 110101 ==> acuqire exponents of 32, 16, 4 and 1  (32+16+4+1=52)

	    - Create "y" to compute each square of g, create "z" as an accumulator to multiply in values to y when needed
	    
	    - For i in len(G) 
	    	- Square y at every iteration	
	    	- When we're at one of the a corresponding exponents we found,
	    	  accumulate current value of y into z

	  	- Output z
	"""
	z = 1
	y = g
	bits_of_exp = bin(exp)[2:]
	print bits_of_exp
	
	for i in range(len(bits_of_exp)):
		#print "Bit being computed on: {}".format(bits_of_exp[i])

		if bits_of_exp[i] == "1":
			z = z * y
			#print "Here: {}".format(z)
		y = y**2

	if mod:
		return z % mod
	return z




