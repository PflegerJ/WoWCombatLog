
data = [5, 0, 3, 0, 2, 0, 0, 2, 0, 0]
data2 = [3, 0, 2, 0, 1, 1, 0, 1, 0, 1]
data3 = [1, 5, 3, 5]
def cosineSim(vector1, vector2):

    length_v1 = 0
    length_v2 = 0
    dot_product = 0
    for i in range(len(vector1)):
        length_v1 += vector1[i] ** 2
        length_v2 += vector2[i] ** 2
        dot_product += vector1[i] * vector2[i]
    
    length_v1 = length_v1 ** 0.5
    length_v2 = length_v2 ** 0.5
 

    return dot_product / ( length_v1 * length_v2 )


print(cosineSim(data, data2))