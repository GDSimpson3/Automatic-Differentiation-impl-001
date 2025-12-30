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
    variable: str


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

    Parameters: Optional[List[str]] = None # We need them to help with the function - even in product and nested


functionPY = functionMain(
    
    Parameters= ['X','Y','Z'],
    MainFunction=[

        functionDS(
            functionFlag=FunctionFlag.POLY,
            terms=[
                Term(2, 2, variable='x'),
                Term(3, 1, variable='y'),
                Term(4, 0,variable='x')
            ],
            FunctionAsExponent=functionDS(
                functionFlag=FunctionFlag.POLY,
                terms=[
                    Term(2, 2,variable='x'),
                    Term(3, 1,variable='z'),
                    Term(4, 0,variable='x')],
            )

        ),


        functionDS(
            functionFlag=FunctionFlag.TRIG,
            functionType=FunctionType.TAN,
            generalCoefficient=-3,
            nestedFunction=functionDS(
                functionFlag=FunctionFlag.POLY,
                terms=[Term(2, 2,variable='x'), Term(3, 1,variable='x'), Term(4, 0,variable='x')],
                functionExponent=-1
            )
        ),

    ],
    FunctionAsExponentMAIN=functionDS(
        functionFlag=FunctionFlag.POLY,
        terms=[
            Term(2, 2,variable='x'),
            Term(3, 1,variable='x'),
            Term(4, 0,variable='x')],
    ),
    productFunction=[
        functionDS(
            functionFlag=FunctionFlag.POLY,
            terms=[
                Term(2, 2,variable='x'),
                Term(3, 1,variable='z'),
                Term(4, 0,variable='x')],
            FunctionAsExponent=functionDS(
                functionFlag=FunctionFlag.POLY,
                terms=[
                    Term(2, 2,variable='x'),
                    Term(3, 1,variable='x'),
                    Term(4, 0,variable='x')],
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
                    CompSTR = CompSTR + f'{term.coefficient}{term.variable}^{term.exponent} '
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


print(ToStringFunc(functionPY))


def TrigLIB(func: str, value: int):
    match func.upper():
        case 'SIN':
            return math.sin(value)
        case 'COS':
            return math.cos(value)
        case 'TAN':
            return math.tan(value)


def FX(functionParam: functionMain, ParametersMULTIVARIATE: List[int]):
    
    
    # FROM {term.variable} ==> we need to get Parameters, use indexes, find what index {term.variable} is in, then can simply return it
    def MapParameters(TermVariable:str):
        for index, paramExact in enumerate(functionParam.Parameters):
            if paramExact.upper() == TermVariable.upper():
                
                return ParametersMULTIVARIATE[index]
    
    

    def FunctionDSFX(functionDSParam: functionDS) -> int:
        CompCUMU = 0

        # POLY FUNC
        if functionDSParam.functionFlag.value == 'P':
            if functionDSParam.terms:
                for term in functionDSParam.terms:
                    print(f'{term} ===== {term.variable} ----- { MapParameters(term.variable)}')
                    CompCUMU = CompCUMU + term.coefficient * (MapParameters(term.variable) ** term.exponent)
        # TRIG FUNC
        elif functionDSParam.functionFlag.value == 'T':
            CompCUMU = CompCUMU + \
                TrigLIB(functionDSParam.functionType.value,
                        FunctionDSFX(functionDSParam.nestedFunction))

        #  EMBEDDED PRODUCT FUNCTIONS
        if functionDSParam.productFunctionTERM:
            for TermsProductFunction in functionDSParam.productFunctionTERM:
                CompCUMU = CompCUMU + FunctionDSFX(TermsProductFunction)
                
                
        Exponent = 1

        if functionDSParam.FunctionAsExponent:
            Exponent = Exponent * FunctionDSFX(functionDSParam.FunctionAsExponent)

        if functionDSParam.functionExponent:
            Exponent = Exponent * functionDSParam.functionExponent

        # FinalReturn = f'({functionDSParam.generalCoefficient or ''}({CompSTR}))'



        # print(ToStringFunc(functionMain(MainFunction=[functionDSParam])))

        return (functionDSParam.generalCoefficient or 1) * (CompCUMU ** Exponent)

    MainouterFunc = 0

    for Component1 in functionParam.MainFunction:  # functionDS

        MainouterFunc = MainouterFunc + FunctionDSFX(Component1)

    if functionParam.productFunction:
        for ProductFunction in functionParam.productFunction:
            MainouterFunc = MainouterFunc + FunctionDSFX(ProductFunction)
            
            
    # GREATER EXPONENTS
    Exponent = 1

    if functionParam.FunctionAsExponentMAIN:
        Exponent = Exponent * FunctionDSFX(functionParam.FunctionAsExponentMAIN)

    # if functionParam.functionExponent:
    #     Exponent = Exponent + f' {functionParam.functionExponent}'
        
    
    MainouterFunc = MainouterFunc ** Exponent

    return MainouterFunc


# print(ToStringFunc(functionPY))
print('----',FX(functionPY, [1,1,2]))
