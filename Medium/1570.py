# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description
# Given two sparse vectors, compute their dot product.
# Implement class SparseVector:
# SparseVector(nums) Initializes the object with the vector nums.
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec.
# A sparse vector is a vector that has mostly zero values, you should store the sparse
# vector efficiently and compute the dot product between two SparseVector.


class SparseVector:
    def __init__(self, nums):
        self.hmap = {}

        for i, n in enumerate(nums):
            if n != 0:
                self.hmap[i] = n

    def dotProduct(self, vec):
        res = 0

        for key in self.hmap:
            if key in vec.hmap:
                res += self.hmap[key] * vec.hmap[key]

        return res
      
