def vowel_filter(function):

    def wrapper():
        array = function()
        vowels = ["a", "e", "i", "y", "o", "u"]
        result = [v for v in array if v.lower() in vowels]
        return result
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
