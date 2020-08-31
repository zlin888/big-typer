from typing import List, Type

'''
 @author Zhitao Lin
 * @email zhitao.lin@mail.mcgill.ca
 * @create date 2020-08-31 14:21:07
 * @modify date 2020-08-31 14:21:07
 * @desc a type reference demo 
'''

'''
A function, named bar, receives a and b and returns c where a, b and c are types:
=> bar: a, b -> c

Generic:
=> a[b]

Union (or):
=> a or b

Dependent:
=> a(func)

auto currying:

'''

class Category:
    FUNC = 0

# Try to test driven
class Func:
    def __init__(self, parameters: List[str], returns: List[str], name:str = ''):
        """parsing the raw_func
        """
        self.name = name
        self.parameters = parameters 
        self.returns = returns
    
    def __str__(self):
        return '{}: {} -> {}'.format(self.name, self.parameters, self.returns)
    
    def __repr__(self):
        return self.__str__()
    
    def __call__(self, *parameters):
        assert list(parameters) == self.parameters, 'param not matched, given {}, need {}'.format(parameters, self.parameters)
        return self.returns

    
    @property
    def catogory(self):
        return Category.FUNC

def build(name:str, parameters:str, returns:str):
    parameters = list(map(lambda _:_.strip(), parameters.split(',')))
    returns = list(map(lambda _:_.strip(), returns.split(',')))
    return Func(parameters, returns, name)

def currying(func: Type[Func]) -> Type[Func]:
    """take one parameter out and return the rest of parameter -> returns
    """
    if len(func.parameters) > 1:
        return Func([func.parameters[0]], currying(Func(func.parameters[1:], func.returns)), func.name)
    else:
        return func
    
    
if __name__ == "__main__":
    bar = build('bar','a,b,c','d,g')
    print(bar('a', 'b', 'c'))
    print(currying(build('bar','a,b,c','d')))
    print(build('bar','a,b,c','d,g'))