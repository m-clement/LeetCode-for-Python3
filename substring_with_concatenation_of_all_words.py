class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # If either s or words is empty, return an empty list
        if not s or not words:
            return []

        word_len = len(words[0])  # Length of each word
        concat_len = word_len * len(words)  # Length of concatenated words
        word_count = collections.Counter(words)  # Count of each word
        result = []

        # Loop for each character in the string s
        for i in range(min(word_len, len(s) - concat_len + 1)):
            j = i
            current_count = collections.Counter()

            # Sliding window
            while j < len(s) - word_len + 1:
                word = s[j:j + word_len]
                j += word_len

                if word in word_count:
                    current_count[word] += 1

                    while current_count[word] > word_count[word]:
                        current_count[s[i:i + word_len]] -= 1
                        i += word_len

                    if j - i == concat_len:
                        result.append(i)
                else:
                    i = j
                    current_count.clear()

        return result
