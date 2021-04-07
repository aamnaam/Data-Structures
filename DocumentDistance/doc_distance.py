# Document distance is the amount of dissimilarity between any two pieces of text.
# If each word is treated as a dimension in a space, and a vector is created for each text such that
# it has magnitudes corresponding to frequencies of each word, then the angle between any two such
# vectors can be a relevant measurement of the dissimilarity between the two.

# This program calculates the angle between two 'text vectors' in a similar fashion, and
# returns a 'Distance Score' on a scale of 0 (no difference) to 100 (completely different)


import math


# returns the frequencies of each word of the text as a dictionary
def count_frequency(text):
    word_list = text.split()
    count_dict = {}
    for word in word_list:
        if word in count_dict:
            count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1

    return count_dict


# Dot product needed for the calculation of the angle
def get_dot_product(count_dict1, count_dict2):
    sum_of_products = 0

    # Each 'dimension' of the first vector
    for key in count_dict1:

        # if the other text-vector has that word (dimension)
        if key in count_dict2:
            sum_of_products += count_dict1[key] * count_dict2[key]

    return sum_of_products


# angle between two vectors using the dot product
def angular_separation(dict1, dict2):
    numerator = get_dot_product(dict1, dict2)
    denominator = math.sqrt(get_dot_product(dict1, dict1) * get_dot_product(dict2, dict2))
    angle = math.acos(numerator / denominator)
    return angle


# Creating a dictionary of frequencies for text from given file
def text_to_dict(filename):
    with open(filename, 'r') as f:
        text = f.read().strip()

    return count_frequency(text)


# Scaling document distance to a score of 0 to 100
def angle_to_scale(angle):
    return angle * 100 / (math.pi / 2)


def main():
    document1 = "doc1.txt"
    document2 = "doc2.txt"

    dict1 = text_to_dict(document1)
    dict2 = text_to_dict(document2)

    angle = angular_separation(dict1, dict2)
    distance_score = angle_to_scale(angle)

    print("Distance Score:", distance_score)


if __name__ == '__main__':
    main()
