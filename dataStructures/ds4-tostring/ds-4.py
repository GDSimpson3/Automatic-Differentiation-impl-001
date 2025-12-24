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
    generalCoefficient: Optional[float] = 1
    terms: Optional[List[Term]] = None
    functionType: Optional[FunctionType] = None
    nestedFunction: Optional["functionDS"] = None
    functionExponent: Optional[float] = 1

@dataclass
class functionMain:
    MainFunction: List[functionDS]




functionPY = functionMain(
    MainFunction=[
    
            functionDS(
                functionFlag=FunctionFlag.POLY,
                generalCoefficient=3,
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

        print(functionDSParam.functionFlag.value)
        # 
        if functionDSParam.functionFlag.value == 'P':
            if functionDSParam.terms:
                for term in functionDSParam.terms:
                    CompSTR = CompSTR + f'{term.coefficient}X^{term.exponent} '
        elif functionDSParam.functionFlag.value == 'T':
            CompSTR = CompSTR + f'{functionDSParam.functionType.value}({FunctionDSToString(functionDSParam.nestedFunction)})'

        # print('sdfs')

        return CompSTR

    for Component1 in functionParam.MainFunction: # functionDS

        # CompSTR = f""

        # print(f'FLAG: {Component1.functionFlag.name}')

        # CompSTR = CompSTR + f"{Component1.generalCoefficient or ''}"



        print(FunctionDSToString(Component1))




ToStringFunc(functionPY)