class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    # 1:59
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        rootValue = preorder.pop(0)
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)

        root.left = self.buildTree(preorder, inorder[:inorderIndex])
        root.right = self.buildTree(preorder, inorder[inorderIndex+1:])

        return root