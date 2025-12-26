<h1 align='center'>Automatic Differentiation</h1>


<h2>Function Representation</h2>

F(x):
<img width="964" height="98" alt="image" src="https://github.com/user-attachments/assets/cf1cf5f7-871a-4020-a988-ed7c76a9dd16" />
```
 + ((2X^2 3X^1 4X^0 ))^ (((2X^2 3X^1 4X^0 ))) + (-3(Tan(((2X^2 3X^1 4X^0 ))^ -1))) (((2X^2 3X^1 4X^0 ))^ (((2X^2 3X^1 4X^0 ))))^ (((2X^2 3X^1 4X^0 )))
```
Datastructure:
```py
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
```

Datatype definitions
```py
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
```
