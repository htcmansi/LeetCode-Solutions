class Solution:
    def compress(self, chars: List[str]) -> int:
        ans=""
        if len(chars) == 1:
            return len(chars)
        count=1
        for i in range(len(chars)):
            if i==len(chars)-1 or chars[i] != chars[i +1]:
                ans +=chars[i]
                if count > 1:
                    ans += str(count)
                    count=1
            else:
                count +=1
        for i in range(len(ans)):
            chars[i] =ans[i]
        return len(ans)
        