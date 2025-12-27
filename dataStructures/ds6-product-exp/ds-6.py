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
    FunctionAsExponent: Optional[List["functionDS"]] = None


@dataclass
class functionMain:
    MainFunction: List[functionDS]
    FunctionAsExponentMAIN: Optional[List["functionDS"]] = None

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
            FunctionAsExponent=functionDS(
                functionFlag=FunctionFlag.POLY,
                terms=[
                    Term(2, 2),
                    Term(3, 1),
                    Term(4, 0)],
            )

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
    FunctionAsExponentMAIN=functionDS(
        functionFlag=FunctionFlag.POLY,
        terms=[
            Term(2, 2),
            Term(3, 1),
            Term(4, 0)],
    ),
    productFunction=[
        functionDS(
            functionFlag=FunctionFlag.POLY,
            terms=[
                Term(2, 2),
                Term(3, 1),
                Term(4, 0)],
            FunctionAsExponent=functionDS(
                functionFlag=FunctionFlag.POLY,
                terms=[
                    Term(2, 2),
                    Term(3, 1),
                    Term(4, 0)],
            )
        )
    ]
)


def ToStringFunc(functionParam: functionMain):

    def FunctionDSToString(functionDSParam: functionDS):
        CompSTR = ''
        # POLY FUNC
        if functionDSParam.functionFlag.value == 'P':
            if functionDSParam.terms:
                for term in functionDSParam.terms:
                    CompSTR = CompSTR + f'{term.coefficient}X^{term.exponent} '
        #    TRIG FUNC
        elif functionDSParam.functionFlag.value == 'T':
            CompSTR = CompSTR + \
                f'{functionDSParam.functionType.value}({FunctionDSToString(functionDSParam.nestedFunction)})'

        # print('sdfs')
        # PRODUCT FUNCTIONS
        if functionDSParam.productFunctionTERM:
            for TermsProductFunction in functionDSParam.productFunctionTERM:
                CompSTR = CompSTR + \
                    f'({FunctionDSToString(TermsProductFunction)})'

        # EXPONENTIATION
        Exponent = ''

        if functionDSParam.FunctionAsExponent:
            Exponent = Exponent + \
                f' ({FunctionDSToString(functionDSParam.FunctionAsExponent)})'

        if functionDSParam.functionExponent:
            Exponent = Exponent + f' {functionDSParam.functionExponent}'

        FinalReturn = f'({functionDSParam.generalCoefficient or ''}({CompSTR}))'

        if not Exponent == '':
            FinalReturn = FinalReturn + f'^{Exponent}'

        return FinalReturn

    MainouterFunc = ''

    # SUMS OF FUNCTIONS
    for Component1 in functionParam.MainFunction:  # functionDS

        MainouterFunc = MainouterFunc + f' + {FunctionDSToString(Component1)}'

    #  GREATER PRODUCT
    if functionParam.productFunction:
        for ProductFunction in functionParam.productFunction:
            MainouterFunc = MainouterFunc + \
                f' ({FunctionDSToString(ProductFunction)})'

    # GREATER EXPONENTS
    Exponent = ''

    if functionParam.FunctionAsExponentMAIN:
        Exponent = Exponent + \
            f' ({FunctionDSToString(functionParam.FunctionAsExponentMAIN)})'

    # if functionParam.functionExponent:
    #     Exponent = Exponent + f' {functionParam.functionExponent}'
    if not Exponent == '':
        MainouterFunc = f'({MainouterFunc})' + \
            f'^{Exponent}'

    return MainouterFunc


# print(ToStringFunc(functionPY))


def TrigLIB(func: str, value: int):
    match func.upper():
        case 'SIN':
            return math.sin(value)
        case 'COS':
            return math.cos(value)
        case 'TAN':
            return math.tan(value)


def FX(functionParam: functionMain, X):

    def FunctionDSFX(functionDSParam: functionDS, X) -> int:
        CompCUMU = 0

        # POLY FUNC
        if functionDSParam.functionFlag.value == 'P':
            if functionDSParam.terms:
                for term in functionDSParam.terms:
                    CompCUMU = CompCUMU + term.coefficient * X ** term.exponent
        # TRIG FUNC
        elif functionDSParam.functionFlag.value == 'T':
            CompCUMU = CompCUMU + \
                TrigLIB(functionDSParam.functionType.value,
                        FunctionDSFX(functionDSParam.nestedFunction, X))

        #  EMBEDDED PRODUCT FUNCTIONS
        if functionDSParam.productFunctionTERM:
            for TermsProductFunction in functionDSParam.productFunctionTERM:
                CompCUMU = CompCUMU + FunctionDSFX(TermsProductFunction, X)
                
                
        Exponent = 1

        if functionDSParam.FunctionAsExponent:
            Exponent = Exponent * FunctionDSFX(functionDSParam.FunctionAsExponent,X)

        if functionDSParam.functionExponent:
            Exponent = Exponent * functionDSParam.functionExponent

        # FinalReturn = f'({functionDSParam.generalCoefficient or ''}({CompSTR}))'



        print(ToStringFunc(functionMain(MainFunction=[functionDSParam])))

        return (functionDSParam.generalCoefficient or 1) * CompCUMU ** Exponent

    MainouterFunc = 0

    for Component1 in functionParam.MainFunction:  # functionDS

        MainouterFunc = MainouterFunc + FunctionDSFX(Component1, X)

    if functionParam.productFunction:
        for ProductFunction in functionParam.productFunction:
            MainouterFunc = MainouterFunc + FunctionDSFX(ProductFunction, X)
            
            
    # GREATER EXPONENTS
    Exponent = 1

    if functionParam.FunctionAsExponentMAIN:
        Exponent = Exponent * FunctionDSFX(functionParam.FunctionAsExponentMAIN, X)

    # if functionParam.functionExponent:
    #     Exponent = Exponent + f' {functionParam.functionExponent}'
        
    
    MainouterFunc = MainouterFunc ** Exponent

    return MainouterFunc


print(ToStringFunc(functionPY))
print('----',FX(functionPY, 1))
