class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        text = text.split(" ")

        words = [(word, index) for index, word in enumerate(text)]

        words.sort(key = lambda x: (len(x[0]), x[1]))
        
        ret = words[0][0][0].upper() + words[0][0][1:]

        for (word, _) in words[1:]:
            ret +=' ' + word[0].lower() + word[1:]
        return ret