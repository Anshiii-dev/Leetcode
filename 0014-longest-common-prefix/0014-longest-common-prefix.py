class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""  # Handle empty input list

        # Start with the first string as the initial common prefix
        common = strs[0]

        # Iterate through each string in the list starting from the second
        for i in range(1, len(strs)):
            x = common
            y = strs[i]
            min_len = min(len(x), len(y))
            common_temp = ""

            # Compare characters up to the minimum length
            for j in range(min_len):
                if x[j] == y[j]:
                    common_temp += x[j]
                else:
                    break  # Stop comparing when characters don't match
            
            # Update the common prefix
            common = common_temp

            # If at any point common becomes empty, no common prefix exists
            if not common:
                break

        return common

# Example usage
sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))    # Output: ""