"""

Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord


Test.describe("Basic tests")
Test.assert_equals(camel_case("test case"), "TestCase")
Test.assert_equals(camel_case("camel case method"), "CamelCaseMethod")
Test.assert_equals(camel_case("say hello "), "SayHello")
Test.assert_equals(camel_case(" camel case word"), "CamelCaseWord")
Test.assert_equals(camel_case(""), "")


"""
def upChar(word):
    return word.title()

def camel_case(string):
    #your code here
    return "".join(map(upChar,string.split()))

print(camel_case("camel case method"))

# other best answer
def camel_case(string):
    return string.title().replace(" ", "")
