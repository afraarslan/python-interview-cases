first_string = input('a:')
second_string = input('b:')


def map_to_dict(input_text):
    char_map = {}
    for character in input_text:
        if character not in char_map:
            char_map[character] = 1
        else:
            char_map[character] += 1
    return char_map


def comparison(dict1, dict2):
    count = 0
    for key in dict1:
        if key in dict2:
            if dict1[key] > dict2[key]:
                count += (dict1[key] - dict2[key])
        else:
            count += dict1[key]
    return count


first_dict = map_to_dict(first_string)
second_dict = map_to_dict(second_string)

if first_dict == second_dict:
    print('they are anagrams')
else:
    first_count = comparison(first_dict, second_dict)
    second_count = comparison(second_dict, first_dict)
    print('remove {} characters from {} and {} characters from {}'.format(first_count, first_string, second_count,
                                                                          second_string))
