from enum import Enum
from dataclasses import dataclass
from typing import Optional, List

class FunctionFlag(Enum):
    POLY = "P"
    TRIG = "T"


class FunctionType(Enum):
    TAN = "Tan"
    COS = "Cos"
    SIN = "Sin"


@dataclass
class Term:
    coefficient: float
    exponent: float

@dataclass
class functionDS:
    functionFlag: FunctionFlag
    generalCoefficient: Optional[float] = None
    terms: Optional[List[Term]] = None
    functionType: Optional[FunctionType] = None
    nestedFunction: Optional["functionDS"] = None
    functionExponent: Optional[float] = None

@dataclass
class functionMain:
    MainFunction: List[functionDS]




functionPY = functionMain(
    MainFunction=[
    
            functionDS(
                functionFlag=FunctionFlag.POLY,
                terms=[
                    Term(2, 2),
                    Term(3, 1),
                    Term(4, 0)
                ]
            ),
        
    
            functionDS(
                functionFlag=FunctionFlag.TRIG,
                functionType=FunctionType.TAN,
                generalCoefficient=-3,
                nestedFunction=functionDS(
                    functionFlag=FunctionFlag.POLY,
                    terms=[Term(2,2), Term(3,1), Term(4,0)],
                    functionExponent=-1
                )
            ),
        
    ],
)


def ToStringFunc(functionParam: functionMain):

    def FunctionDSToString(functionDSParam: functionDS):
        CompSTR = ''


        if functionDSParam.functionFlag.value == 'P':
            if functionDSParam.terms:
                for term in functionDSParam.terms:
                    CompSTR = CompSTR + f'{term.coefficient}X^{term.exponent} '
        elif functionDSParam.functionFlag.value == 'T':
            CompSTR = CompSTR + f'{functionDSParam.functionType.value}({FunctionDSToString(functionDSParam.nestedFunction)})'

        # print('sdfs')

        return f'({functionDSParam.generalCoefficient or ''}({CompSTR}))^{functionDSParam.functionExponent or '1'}'

    MainouterFunc = ''

    for Component1 in functionParam.MainFunction: # functionDS

        MainouterFunc = MainouterFunc + f' + {FunctionDSToString(Component1)}'
    return MainouterFunc



# print(ToStringFunc(functionPY))


import math

def TrigLIB(func:str, value:int):
   match func.upper():
        case 'SIN':
           return math.sin(value)
        case 'COS':
           return math.cos(value)
        case 'TAN':
           return math.tan(value)
       

def FX(functionParam: functionMain,X):

    def FunctionDSFX(functionDSParam: functionDS,X) -> int:
        CompCUMU = 0


        if functionDSParam.functionFlag.value == 'P':
            if functionDSParam.terms:
                for term in functionDSParam.terms:
                    CompCUMU = CompCUMU + term.coefficient * X ** term.exponent

        elif functionDSParam.functionFlag.value == 'T':
            CompCUMU = CompCUMU + TrigLIB(functionDSParam.functionType.value, FunctionDSFX(functionDSParam.nestedFunction,X))

       
        print(ToStringFunc(functionMain(MainFunction=[functionDSParam])))

        return (functionDSParam.generalCoefficient or 1) * CompCUMU ** (functionDSParam.functionExponent or 1)

    MainouterFunc = 0

    for Component1 in functionParam.MainFunction: # functionDS

        MainouterFunc = MainouterFunc + FunctionDSFX(Component1,X)
    return MainouterFunc




print(ToStringFunc(functionPY))
print(FX(functionPY,1))