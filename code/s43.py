class Solution:
    '''
    @description:计算字符串和单独一个数字相乘 
    @param {*} num_str
    @param {*} dig
    @return {*} res_str
    '''
    def BignumMultiplyDigit(self, num_str, dig):
        num_str = num_str[::-1]
        res_str = ''
        ci = 0
        for ch in num_str:
            tmp_multi = int(ch) * int(dig) + ci
            ci = tmp_multi // 10
            res_str += str(tmp_multi % 10)
        if ci != 0:
            res_str += str(ci)
        return res_str[::-1]

    '''
    @description:计算大数相加和 
    @param {*} num1
    @param {*} num2
    @return {*} res_str
    '''
    def BignumAdd(self, num1,num2):
        num1, num2 = num1[::-1], num2[::-1]
        strlen1, strlen2 = len(num1), len(num2)
        if strlen1 < strlen2:
            num1, num2 = num2, num1
            strlen1, strlen2 = strlen2, strlen1

        res_str = ''
        ci = 0
        idx = 0
        while idx < strlen2:
            tmp_sum = int(num1[idx]) + int(num2[idx]) + ci
            ci = tmp_sum // 10
            res_str += str(tmp_sum % 10)
            idx += 1
        while idx < strlen1:
            if ci > 0:
                tmp_sum = int(num1[idx]) + ci
                ci = tmp_sum // 10
                res_str += str(tmp_sum % 10)
            else:
                res_str += num1[idx]
            idx += 1
        if ci>0:
            res_str += str(ci)

        return res_str[::-1]

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return '0'
        # num1 * dig [for dig in num2]
        res_str = '0'
        for idx, dig in enumerate(num2[::-1]):
            multy_dig_res = self.BignumMultiplyDigit(num1, dig)
            multy_dig_res += '0' * idx
            res_str = self.BignumAdd(res_str, multy_dig_res)
        return res_str
        