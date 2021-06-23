# Test functions goes here
import unittest

from huffman import encode, decode

class TestHuffman(unittest.TestCase):
	# write all your tests here
	# function name should be prefixed with 'test'

	def test_1_encode1(self):

		f_in = 'test_encode1.txt'
		f_out = 'test_encode_res1.txt'

		f_encode = open(f_in,'w+')

		# test-1
		inp_content = 'abcde'
		actual_result = '110111000110'

		f_encode.write(inp_content)
		f_encode.close()

		encode(f_in, f_out)
		f_out = open(f_out,'r')
		output = f_out.readlines()

		check = (output[0]==actual_result)

		self.assertTrue(check)

	def test_2_decode1(self):
		
		f_in = 'test_encode_res1.txt'
		f_out = 'test_decode_res1.txt'

		decode(f_in, f_out)

		f_decode = open(f_out,'r')
		output = f_decode.readlines()

		actual_result = 'abcde'
		check = (output[0]==actual_result)

		self.assertTrue(check)
	def test_3_encode2(self):

		f_in = 'test_encode2.txt'
		f_out = 'test_encode_res2.txt'

		f_encode = open(f_in,'w+')

		# test-1
		inp_content = 'LJKJI|}|{|{>?'
		actual_result = '1100100110110011100111110110101101000001'

		f_encode.write(inp_content)
		f_encode.close()

		encode(f_in, f_out)
		f_out = open(f_out,'r')
		output = f_out.readlines()

		check = (output[0]==actual_result)

		self.assertTrue(check)


	def test_4_decode2(self):
		
		f_in = 'test_encode_res2.txt'
		f_out = 'test_decode_res2.txt'

		decode(f_in, f_out)

		f_decode = open(f_out,'r')
		output = f_decode.readlines()

		actual_result = 'LJKJI|}|{|{>?'
		check = (output[0]==actual_result)

		self.assertTrue(check)
		
	def test_5_encode3(self):

		f_in = 'test_encode3.txt'
		f_out = 'test_encode_res3.txt'

		f_encode = open(f_in,'w+')

		# test-1
		inp_content = 'H()&|}|'
		actual_result = '100101110111010001'

		f_encode.write(inp_content)
		f_encode.close()

		encode(f_in, f_out)
		f_out = open(f_out,'r')
		output = f_out.readlines()

		check = (output[0]==actual_result)

		self.assertTrue(check)


	def test_6_decode3(self):
		
		f_in = 'test_encode_res3.txt'
		f_out = 'test_decode_res3.txt'

		decode(f_in, f_out)

		f_decode = open(f_out,'r')
		output = f_decode.readlines()

		actual_result = 'H()&|}|'
		check = (output[0]==actual_result)

		self.assertTrue(check)



if __name__ == '__main__':
	unittest.main()
