class Solution:
    def twoSum(self, nums, target):
        hashSolution = {}
        for idx, i in enumerate(nums):
            # early return
            if hashSolution.get(i) is not None:
                return [hashSolution.get(i), idx]
            # adicionando complemento do target ao dicionario como chave e valor o index, pedido como resposta :))
            hashSolution[target - i] = idx
        
solution_instance = Solution()

print(solution_instance.twoSum([3,3], 6))
