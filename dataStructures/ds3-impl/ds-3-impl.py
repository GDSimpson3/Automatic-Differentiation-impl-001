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

# interface functionDS {
    # functionFlag: functionClass,
    # nestedFunction?: functionDS,
    # terms?: term[],
    # functionType?: functionType,
    # generalCoefficient?: number,
    # functionExponent?: number,
# }


functionPY = functionMain(
    MainFunction=[
        (
            functionDS(
                functionFlag=FunctionFlag.POLY,
                generalCoefficient=3,
                terms=[
                    Term(2, 2),
                    Term(3, 1),
                    Term(4, 0)
                ]
            ),
        ),
        (
            functionDS(
                functionFlag=FunctionFlag.TRIG,
                functionType=FunctionType.TAN,
                generalCoefficient=3,
                nestedFunction=functionDS(
                    functionFlag=FunctionFlag.POLY,
                    terms=[Term(2,2), Term(3,1), Term(4,0)]
                )
            ),
        ),
    ],
)




FunctionEquasionSTATIC = {
    "Main Function": [
        [
            {
                "functionFlag": "P",
                "genericCoefficent": 3,
                "Terms": [
                    {
                        "coefficent": 2,
                        "exponent": 2
                    },
                    {
                        "coefficent": 3,
                        "exponent": 1
                    },
                    {
                        "coefficent": 4,
                        "exponent": 0
                    }
                ]
            },
            "3 * (2X^2 + 3X + 4)"
        ],
        [
            {
                "functionFlag": "T",
                "functionType": "Tan",
                "genericCoefficent": 3,
                "NestedFunction": {
                    "functionFlag": "P",
                    "Terms": [
                        {
                            "coefficent": 2,
                            "exponent": 2
                        },
                        {
                            "coefficent": 3,
                            "exponent": 1
                        },
                        {
                            "coefficent": 4,
                            "exponent": 0
                        }
                    ]
                }
            },
            "3 * tan (2X^2 + 3X + 4)"
        ],
        [
            {
                "functionFlag": "T",
                "functionType": "Tan",
                "genericCoefficent": 3,
                "NestedFunction": {
                    "functionFlag": "P",
                    "Terms": [
                        {
                            "coefficent": 2,
                            "exponent": 2
                        },
                        {
                            "coefficent": 3,
                            "exponent": 1
                        },
                        {
                            "coefficent": 4,
                            "exponent": 0
                        }
                    ],
                    "functionExponent": -1
                }
            },
            "3 * tan (1 / (2X^2 + 3X + 4))"
        ]
    ],

    "Equals": "3 * (2X^2 + 3X + 4) + 3 * tan (2X^2 + 3X + 4) + 3 * tan (1 / (2X^2 + 3X + 4))"
}



