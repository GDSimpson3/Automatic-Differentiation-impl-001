import math
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
    # f(x)g(x) as a term only
    productFunctionTERM: Optional[List["functionMain"]] = None


@dataclass
class functionMain:
    MainFunction: List[functionDS]
    productFunction: Optional[List["functionMain"]] = None


functionPY = functionMain(
    MainFunction=[

        functionDS(
            functionFlag=FunctionFlag.POLY,
            terms=[
                Term(2, 2),
                Term(3, 1),
                Term(4, 0)
            ],


        ),


        functionDS(
            functionFlag=FunctionFlag.TRIG,
            functionType=FunctionType.TAN,
            generalCoefficient=-3,
            nestedFunction=functionDS(
                functionFlag=FunctionFlag.POLY,
                terms=[Term(2, 2), Term(3, 1), Term(4, 0)],
                functionExponent=-1
            )
        ),

    ],
    productFunction=[
        functionDS(
            functionFlag=FunctionFlag.POLY,
            terms=[
                Term(2, 2),
                Term(3, 1),
                Term(4, 0)],
        )
    ]
)




# print(ToStringFunc(functionPY))
# print(FX(functionPY,1))


# def Differentiate(functionParam: functionMain,X):

#     Derivative = functionMain(MainFunction=[])

#     def FunctionDifferentiate(functionDSParam: functionDS,X) -> functionDS:
#         Component = functionDS ()


#         if functionDSParam.functionFlag.value == 'P':
           

#         elif functionDSParam.functionFlag.value == 'T':
           
       

#         return 


#     for Component1 in functionParam.MainFunction: # functionDS

#         Derivative.MainFunction.append(FunctionDifferentiate(Component1))


#     return Derivative

