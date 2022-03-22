"""
first approach
"""
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # create an array equal to n, I wan n letters
        arr_response = [1]*n
		# remainder
        k =k-n
		#idx
        i = n-1
		# avoid calculation each time
        ascci_a = ord('a')-1
		# start iterating from the lasted to the first
        while k and i>-1:
			# if k lower than 26,  we will convertd 
            if k<26:
                arr_response[i] = chr(arr_response[i]+k+ascci_a)
                break
            else:
				#substract a y and convert to z the current position
                k+=-25
                arr_response[i] = chr(arr_response[i]+25+ascci_a) # 'z'
            i+=-1
		#convert the first integers, to chars
        for j in range(0, i):
            arr_response[j] = chr(arr_response[j]+ascci_a)
        return "".join(arr_response)
