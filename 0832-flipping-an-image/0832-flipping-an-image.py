class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for width in range(len(image)):
            image[width].reverse()
        for width in range(len(image)):
            for height in range(len(image[width])):
                if image[width][height]==1:
                    image[width][height]=0
                else:
                    image[width][height]=1
        return image
