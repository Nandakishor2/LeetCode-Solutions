class Solution(object):
    

    def strStr( self,haystack, needle):
        #Case : if Haystack or needle is empty
        if(haystack == "" or needle == ""):
            return -1
            
        for i in range(len(haystack)):
            if(haystack[i:i+len(needle)] == needle):
                return i

        return -1       
        