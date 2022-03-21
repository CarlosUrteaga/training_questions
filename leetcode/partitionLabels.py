class Solution:
    def partitionLabels(self, s: str) -> List[int]:
		# base case if we only have 1 letter 
        if len(s)<2:
            return [1] #change to [len(s)]
        response = [] # final response
        memory = []  #track
        memory.append(s[0])# we already known that we have at least 2 letters
        count = 1 # counter 
        i = 1
        while i<len(s):
            if s[i] in memory:
                count+=1 #if the current value char is in our memory add the count
            else: # is a new character
                bl = False # boolean flag, true to add the new character into the current count or in a new
                for each in memory: #we want to keep track of each letter into the remaining string
                    if each  in s[i+1:]: #if at least one of the letters in our memory appers later, we can change the flag and stop the for 
                        bl = True
                        break
                if bl: # add the new letter into the memory
                    memory.append(s[i])
                    count+=1
                else:
                    memory = [] # empty the memory
                    memory.append(s[i]) # add the current new character 
                    response.append(count) # add the current count into the response
                    count = 1 #counter
            i+=1
        response.append(count) #add the remaining letters 
        return response
