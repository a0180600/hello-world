# Single line comments start with a hash.
# ����ע����һ�����ſ�ͷ��
""" Multiline strings can be written
    using three "'s, and are often used
    as comments
    ����˫���ţ������ţ�֮�����д�����ַ�����
    ͨ������дע�͡�
"""
 
####################################################
## 1. Primitive Datatypes and Operators
## 1. �����������ͺͲ�����
####################################################
 
# You have numbers
# ���־�������
3 #=> 3
 
# Math is what you would expect
# ��������Ҳ����������������
1 + 1 #=> 2
8 - 1 #=> 7
10 * 2 #=> 20
35 / 5 #=> 7
 
# Division is a bit tricky. It is integer division and floors the results
# automatically.
# ������һ�㼬�֡�
# ��������������˵�����������Զ�ȡ����
5 / 2 #=> 2
 
# To fix division we need to learn about floats.
# Ϊ���������������⣬������Ҫ��ѧϰ��������
2.0     # This is a float
2.0     # ����һ��������
11.0 / 4.0 #=> 2.75 ahhh...much better
11.0 / 4.0 #=> 2.75 �����������ͺö���
 
# Enforce precedence with parentheses
# ʹ��С������ǿ�Ƽ��������˳��
(1 + 3) * 2 #=> 8
 
# Boolean values are primitives
# ����ֵҲ�ǻ�����������
True
False
 
# negate with not
# ʹ�� not ��ȡ��
not True #=> False
not False #=> True
 
# Equality is ==
# ��ʽ�ж��� ==
1 == 1 #=> True
2 == 1 #=> False
 
# Inequality is !=
# ����ʽ�ж����� !=
1 != 1 #=> False
2 != 1 #=> True
 
# More comparisons
# ���и���ıȽ�����
1 < 10 #=> True
1 > 10 #=> False
2 <= 2 #=> True
2 >= 2 #=> True
 
# Comparisons can be chained!
# ��Ȼ���԰ѱȽ����㴮��������
1 < 2 < 3 #=> True
2 < 3 < 2 #=> False
 
# Strings are created with " or '
# ʹ�� " �� ' �������ַ���
"This is a string."
'This is also a string.'
 
# Strings can be added too!
# �ַ���Ҳ������ӣ�
"Hello " + "world!" #=> "Hello world!"
 
# A string can be treated like a list of characters
# һ���ַ���������Ϊһ���ַ����б�
# ����ע������ὲ�����б�����
"This is a string"[0] #=> 'T'
 
# % can be used to format strings, like this:
# % ����������ʽ���ַ���������������
"%s can be %s" % ("strings", "interpolated")
 
# A newer way to format strings is the format method.
# This method is the preferred way
# ��������һ�ָ�ʽ���ַ������·�����format ������
# �����Ƽ�ʹ�����������
"{0} can be {1}".format("strings", "formatted")
 
# You can use keywords if you don't want to count.
# ����㲻ϲ�������Ļ�������ʹ�ùؼ��֣���������
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
 
# None is an object
# None ��һ������
None #=> None
 
# Don't use the equality `==` symbol to compare objects to None
# Use `is` instead
# ��Ҫʹ����ȷ��� `==` ���Ѷ���� None ���бȽϣ�
# ��Ҫ�� `is`��
"etc" is None #=> False
None is None  #=> True
 
# The 'is' operator tests for object identity. This isn't
# very useful when dealing with primitive values, but is
# very useful when dealing with objects.
# ��� `is` ���������ڱȽ���������ı�ʶ��
# ����ע������һ�����������ʶ�Ͳ���ı䣬������Ϊ�����Ƕ�����ڴ��ַ����
# �ڴ��������������ʱ�����ò��ϣ�
# �����ڴ������ʱ�����á�
 
# None, 0, and empty strings/lists all evaluate to False.
# All other values are True
# None��0 �Լ����ַ����Ϳ��б����� False��
# �������������ֵ������ True��
0 == False  #=> True
"" == False #=> True
 
 
####################################################
## 2. Variables and Collections
## 2. �����ͼ���
####################################################
 
# Printing is pretty easy
# ��ӡ����ܼ�
print "I'm Python. Nice to meet you!"
 
 
# No need to declare variables before assigning to them.
# �ڸ�ֵ������֮ǰ����Ҫ����
some_var = 5    # Convention is to use lower_case_with_underscores
                # ��������Լ����ʹ���»��߷ָ���Сд����
some_var #=> 5
 
# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
# ����һ��δ��ֵ�ı��������һ���쳣��
# ��һ���˽��쳣�����ɲμ���һ�ڡ�����������
some_other_var  # Raises a name error
                # ���׳�һ�����ƴ���
 
# if can be used as an expression
# if ������Ϊ���ʽ��ʹ��
"yahoo!" if 3 > 2 else 2 #=> "yahoo!"
 
# Lists store sequences
# �б����ڴ洢����
li = []
# You can start with a prefilled list
# �����ȳ���һ��Ԥ�����õ��б�
other_li = [4, 5, 6]
 
# Add stuff to the end of a list with append
# ʹ�� append ������Ԫ����ӵ��б��β��
li.append(1)    #li is now [1]
                #li ������ [1]
li.append(2)    #li is now [1, 2]
                #li ������ [1, 2]
li.append(4)    #li is now [1, 2, 4]
                #li ������ [1, 2, 4]
li.append(3)    #li is now [1, 2, 4, 3]
                #li ������ [1, 2, 4, 3]
# Remove from the end with pop
# ʹ�� pop ���Ƴ����һ��Ԫ��
li.pop()        #=> 3 and li is now [1, 2, 4]
                #=> 3��Ȼ�� li ������ [1, 2, 4]
# Let's put it back
# �����ٰ����Ż�ȥ
li.append(3)    # li is now [1, 2, 4, 3] again.
                # li �������� [1, 2, 4, 3] ��
 
# Access a list like you would any array
# ������������Ե��������������б�
li[0] #=> 1
# Look at the last element
# ��ѯ���һ��Ԫ��
li[-1] #=> 3
 
# Looking out of bounds is an IndexError
# Խ���ѯ�����һ����������
li[4] # Raises an IndexError
      # �׳�һ����������
 
# You can look at ranges with slice syntax.
# (It's a closed/open range for you mathy types.)
# �����ʹ����Ƭ�﷨����ѯ�б��һ����Χ��
# �������Χ�൱����ѧ�е�����ҿ����䡣��
li[1:3] #=> [2, 4]
# Omit the beginning
# ʡ�Կ�ͷ
li[2:] #=> [4, 3]
# Omit the end
# ʡ�Խ�β
li[:3] #=> [1, 2, 4]
 
# Remove arbitrary elements from a list with del
# ʹ�� del ��ɾ���б��е�����Ԫ��
del li[2] # li is now [1, 2, 3]
          # li ������ [1, 2, 3]
 
# You can add lists
# ���԰��б����
li + other_li #=> [1, 2, 3, 4, 5, 6] - Note: li and other_li is left alone
              #=> [1, 2, 3, 4, 5, 6] - ������ li �� other_li �����ᱻ�޸�
 
# Concatenate lists with extend
# ʹ�� extend ���ϲ��б�
li.extend(other_li) # Now li is [1, 2, 3, 4, 5, 6]
                    # ���� li �� [1, 2, 3, 4, 5, 6]
 
# Check for existence in a list with in
# �� in ������Ƿ������ĳ���б���
1 in li #=> True
 
# Examine the length with len
# �� len ������б�ĳ���
len(li) #=> 6
 
 
# Tuples are like lists but are immutable.
# Ԫ������б������ǡ����ɱ䡱�ġ�
tup = (1, 2, 3)
tup[0] #=> 1
tup[0] = 3  # Raises a TypeError
            # �׳�һ�����ʹ���
 
# You can do all those list thingies on tuples too
# �����б�ķ�ʽͨ��Ҳ������Ԫ������
len(tup) #=> 3
tup + (4, 5, 6) #=> (1, 2, 3, 4, 5, 6)
tup[:2] #=> (1, 2)
2 in tup #=> True
 
# You can unpack tuples (or lists) into variables
# ����԰�Ԫ�飨���б��е�Ԫ�ؽ����ֵ���������
a, b, c = (1, 2, 3)     # a is now 1, b is now 2 and c is now 3
                        # ���� a �� 1��b �� 2��c �� 3
# Tuples are created by default if you leave out the parentheses
# �����ʡȥ��С���ţ���ôԪ��ᱻ�Զ�����
d, e, f = 4, 5, 6
# Now look how easy it is to swap two values
# ����������������ֵ�Ƕ�ô�򵥡�
e, d = d, e     # d is now 5 and e is now 4
                # ���� d �� 5 �� e �� 4
 
 
# Dictionaries store mappings
# �ֵ����ڴ洢ӳ���ϵ
empty_dict = {}
# Here is a prefilled dictionary
# ����һ��Ԥ�������ֵ�
filled_dict = {"one": 1, "two": 2, "three": 3}
 
# Look up values with []
# ʹ�� [] ����ѯ��ֵ
filled_dict["one"] #=> 1
 
# Get all keys as a list
# ���ֵ�����м�����ȡΪһ���б�
filled_dict.keys() #=> ["three", "two", "one"]
# Note - Dictionary key ordering is not guaranteed.
# Your results might not match this exactly.
# ��ע�⣺�޷���֤�ֵ������˳��������С�
# ��õ��Ľ�����ܸ������ʾ����һ�¡�
 
# Get all values as a list
# ���ֵ�����м�ֵ��ȡΪһ���б�
filled_dict.values() #=> [3, 2, 1]
# Note - Same as above regarding key ordering.
# ��ע�⣺˳������������һ����
 
# Check for existence of keys in a dictionary with in
# ʹ�� in �����һ���ֵ��Ƿ����ĳ������
"one" in filled_dict #=> True
1 in filled_dict #=> False
 
# Looking up a non-existing key is a KeyError
# ��ѯһ�������ڵļ��������һ����������
filled_dict["four"] # KeyError
                    # ��������
 
# Use get method to avoid the KeyError
# ����Ҫʹ�� get �����������������
filled_dict.get("one") #=> 1
filled_dict.get("four") #=> None
# The get method supports a default argument when the value is missing
# get ����֧�ִ���һ��Ĭ��ֵ����������ȡ����ֵʱ���ء�
filled_dict.get("one", 4) #=> 1
filled_dict.get("four", 4) #=> 4
 
# Setdefault method is a safe way to add new key-value pair into dictionary
# Setdefault �������԰�ȫ�ذ��µ���ֵ����ӵ��ֵ���
filled_dict.setdefault("five", 5) #filled_dict["five"] is set to 5
                                  #filled_dict["five"] ������Ϊ 5
filled_dict.setdefault("five", 6) #filled_dict["five"] is still 5
                                  #filled_dict["five"] ��ȻΪ 5
 
 
# Sets store ... well sets
# set ���ڱ��漯��
empty_set = set()
# Initialize a set with a bunch of values
# ʹ��һ��ֵ����ʼ��һ������
some_set = set([1,2,2,3,4]) # some_set is now set([1, 2, 3, 4])
                            # some_set ������ set([1, 2, 3, 4])
 
# Since Python 2.7, {} can be used to declare a set
# �� Python 2.7 ��ʼ��{} ������������һ������
filled_set = {1, 2, 2, 3, 4} # => {1, 2, 3, 4}
                             # ����ע���������������ظ���Ԫ�ؼ�������ظ��� 2 ���˳��ˡ���
                             # ����ע��{} ���ᴴ��һ���ռ��ϣ�ֻ�ᴴ��һ�����ֵ䡣��
 
# Add more items to a set
# �Ѹ����Ԫ����ӽ�һ������
filled_set.add(5) # filled_set is now {1, 2, 3, 4, 5}
                  # filled_set ������ {1, 2, 3, 4, 5}
 
# Do set intersection with &
# ʹ�� & ����ȡ����
other_set = {3, 4, 5, 6}
filled_set & other_set #=> {3, 4, 5}
 
# Do set union with |
# ʹ�� | ����ȡ����
filled_set | other_set #=> {1, 2, 3, 4, 5, 6}
 
# Do set difference with -
# ʹ�� - ����ȡ����
{1,2,3,4} - {2,3,5} #=> {1, 4}
 
# Check for existence in a set with in
# ʹ�� in ������Ƿ������ĳ��������
2 in filled_set #=> True
10 in filled_set #=> False
 
 
####################################################
## 3. Control Flow
## 3. ������
####################################################
 
# Let's just make a variable
# �����ȴ���һ������
some_var = 5
 
# Here is an if statement. Indentation is significant in python!
# prints "some_var is smaller than 10"
# ������һ��������䡣������ Python �п��Ǻ���Ҫ��Ŷ��
# ������ӡ�� "some_var is smaller than 10"
# ����ע����Ϊ��some_var �� 10 С������
if some_var > 10:
    print "some_var is totally bigger than 10."
    # ����ע����Ϊ��some_var ��ȫ�� 10 �󡱡���
elif some_var < 10:    # This elif clause is optional.
                       # ����� elif �Ӿ��ǿ�ѡ��
    print "some_var is smaller than 10."
    # ����ע����Ϊ��some_var �� 10 С������
else:           # This is optional too.
                # ��һ��Ҳ�ǿ�ѡ��
    print "some_var is indeed 10."
    # ����ע����Ϊ��some_var ���� 10������
 
 
"""
For loops iterate over lists
for ѭ�����Ա����б�
prints:
���Ҫ��ӡ����
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # You can use % to interpolate formatted strings
    # �����������ʹ�� % ����ʽ���ַ���
    print "%s is a mammal" % animal
    # ����ע����Ϊ��%s �ǲ��鶯�����
 
"""
`range(number)` returns a list of numbers 
from zero to the given number
`range(����)` �᷵��һ�������б�
����б��������㵽���������֡�
prints:
���Ҫ��ӡ����
    0
    1
    2
    3
"""
for i in range(4):
    print i
 
"""
While loops go until a condition is no longer met.
while ѭ����һֱ������ֱ�������������㡣
prints:
���Ҫ��ӡ����
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print x
    x += 1  # Shorthand for x = x + 1
            # ���� x = x + 1 �ļ�д��ʽ
 
# Handle exceptions with a try/except block
# ʹ�� try/except ������������쳣
 
# Works on Python 2.6 and up:
# ������ Python 2.6 �����ϰ汾��
try:
    # Use raise to raise an error
    # ʹ�� raise ���׳�һ������
    raise IndexError("This is an index error")
    # �׳�һ���������󣺡�����һ���������󡱡�
except IndexError as e:
    pass    # Pass is just a no-op. Usually you would do recovery here.
            # pass ֻ��һ���ղ�����ͨ����Ӧ����������һЩ�ָ�������
 
 
####################################################
## 4. Functions
## 4. ����
####################################################
 
# Use def to create new functions
# ʹ�� def �������º���
def add(x, y):
    print "x is %s and y is %s" % (x, y)
    # ����ע����Ϊ��x �� %s ���� y �� %s������
    return x + y    # Return values with a return statement
                    # ʹ�� return ���������ֵ
 
# Calling functions with parameters
# ���ú������������
add(5, 6) #=> prints out "x is 5 and y is 6" and returns 11
          # ����ע����Ϊ��x �� 5 ���� y �� 6���������� 11��
 
# Another way to call functions is with keyword arguments
# ���ú�������һ�ַ�ʽ�Ǵ���ؼ��ֲ���
add(y=6, x=5)   # Keyword arguments can arrive in any order.
                # �ؼ��ֲ�������������˳����
 
# You can define functions that take a variable number of
# positional arguments
# ����Զ���һ�����������������ܿɱ������Ķ�λ������
def varargs(*args):
    return args
 
varargs(1, 2, 3) #=> (1,2,3)
 
 
# You can define functions that take a variable number of
# keyword arguments, as well
# ��Ҳ���Զ���һ�����������������ܿɱ������Ĺؼ��ֲ�����
def keyword_args(**kwargs):
    return kwargs
 
# Let's call it to see what happens
# �������ŵ������������ᷢ��ʲô��
keyword_args(big="foot", loch="ness") #=> {"big": "foot", "loch": "ness"}
 
# You can do both at once, if you like
# �㻹����ͬʱʹ�������������ֻҪ��Ը�⣺
def all_the_args(*args, **kwargs):
    print args
    print kwargs
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""
 
# When calling functions, you can do the opposite of varargs/kwargs!
# Use * to expand tuples and use ** to expand kwargs.
# �ڵ��ú���ʱ����λ�����͹ؼ��ֲ��������Է������á�
# ʹ�� * ��չ��Ԫ�飬ʹ�� ** ��չ���ؼ��ֲ�����
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args) # equivalent to foo(1, 2, 3, 4)
                    # �൱�� all_the_args(1, 2, 3, 4)
all_the_args(**kwargs) # equivalent to foo(a=3, b=4)
                       # �൱�� all_the_args(a=3, b=4)
all_the_args(*args, **kwargs) # equivalent to foo(1, 2, 3, 4, a=3, b=4)
                              # �൱�� all_the_args(1, 2, 3, 4, a=3, b=4)
 
# Python has first class functions
# ������ Python ����һ�ȹ���
def create_adder(x):
    def adder(y):
        return x + y
    return adder
 
add_10 = create_adder(10)
add_10(3) #=> 13
 
# There are also anonymous functions
# ������������
(lambda x: x > 2)(3) #=> True
 
# There are built-in higher order functions
# ����һЩ�ڽ��ĸ߽׺���
map(add_10, [1,2,3]) #=> [11, 12, 13]
filter(lambda x: x > 5, [3, 4, 5, 6, 7]) #=> [6, 7]
 
# We can use list comprehensions for nice maps and filters
# ���ǿ���ʹ���б��Ƶ�ʽ��ģ�� map �� filter
[add_10(i) for i in [1, 2, 3]]  #=> [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5] #=> [6, 7]
 
####################################################
## 5. Classes
## 5. ��
####################################################
 
# We subclass from object to get a class.
# ���ǿ��ԴӶ����м̳У����õ�һ���ࡣ
class Human(object):
 
    # A class attribute. It is shared by all instances of this class
    # ������һ�������ԡ�����������������ʵ������
    species = "H. sapiens"
 
    # Basic initializer
    # �����ĳ�ʼ�����������캯����
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        # �Ѳ�����ֵΪʵ���� name ����
        self.name = name
 
    # An instance method. All methods take self as the first argument
    # ������һ��ʵ�����������з������� self ��Ϊ��һ��������
    def say(self, msg):
       return "%s: %s" % (self.name, msg)
 
    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    # �෽���ᱻ����ʵ������
    # �෽���ڵ���ʱ���Ὣ�౾����Ϊ��һ���������롣
    @classmethod
    def get_species(cls):
        return cls.species
 
    # A static method is called without a class or instance reference
    # ��̬�����ڵ���ʱ�����ᴫ�����ʵ�������á�
    @staticmethod
    def grunt():
        return "*grunt*"
 
 
# Instantiate a class
# ʵ����һ����
i = Human(name="Ian")
print i.say("hi")     # prints out "Ian: hi"
                      # ��ӡ�� "Ian: hi"
 
j = Human("Joel")
print j.say("hello")  # prints out "Joel: hello"
                      # ��ӡ�� "Joel: hello"
 
# Call our class method
# �������ǵ��෽��
i.get_species() #=> "H. sapiens"
 
# Change the shared attribute
# �޸Ĺ�������
Human.species = "H. neanderthalensis"
i.get_species() #=> "H. neanderthalensis"
j.get_species() #=> "H. neanderthalensis"
 
# Call the static method
# ���þ�̬����
Human.grunt() #=> "*grunt*"
 
 
####################################################
## 6. Modules
## 6. ģ��
####################################################
 
# You can import modules
# ����Ե���ģ��
import math
print math.sqrt(16) #=> 4
 
# You can get specific functions from a module
# Ҳ���Դ�һ��ģ���л�ȡָ���ĺ���
from math import ceil, floor
print ceil(3.7)  #=> 4.0
print floor(3.7) #=> 3.0
 
# You can import all functions from a module.
# Warning: this is not recommended
# ����Դ�һ��ģ���е������к���
# ���棺������ʹ�����ַ�ʽ
from math import *
 
# You can shorten module names
# ���������ģ�������
import math as m
math.sqrt(16) == m.sqrt(16) #=> True
 
# Python modules are just ordinary python files. You
# can write your own, and import them. The name of the 
# module is the same as the name of the file.
# Python ģ�������ͨ�� Python �ļ���
# ����Ա�д���Լ���ģ�飬Ȼ�������ǡ�
# ģ����������ļ�����ͬ��
 
# You can find out which functions and attributes
# defines a module.
# ����Բ��һ��ģ��������Щ����������
import math
dir(math)