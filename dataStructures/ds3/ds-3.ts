enum functionClass {
    TRIG="T",
    POLY="P"
}

enum functionType {
    TAN = "T",
    COS = "C",
    SIN = "S",
    EXP = "E",
    LOG = "L"
}

interface term {
    coefficent: number,
    exponent: number
}

interface functionDS {
    functionFlag: functionClass,
    nestedFunction?: functionDS,
    terms?: term[],
    functionType?: functionType,
    generalCoefficient?: number,
    functionExponent?: number,
}



/*

Data type example




["P", 3, [{coefficent:2, exponent:2}, {coefficent:3, exponent:1}, {coefficent:4, exponent:0}]]

A SIMPLE Polynomial function

[functionFlag: "T",3, tan, ["P", 3, [{coefficent:2, exponent:2}]]]

3 Tan (3 )




*/
