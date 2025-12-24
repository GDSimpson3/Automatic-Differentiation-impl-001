enum functionType {
    TRIG="T",
    POLY="P"
}

interface term {
    coefficent: number,
    exponent: number
}

interface functionDS {
    functionFlag: functionType,
    coEfficient: number,
    function?: functionDS | number,
    Terms?: term[]
}



/*

Data type example


[

["T",12, 'tan', ["P", 3, [{coefficent:2, exponent:2}, {coefficent:3, exponent:1}, {coefficent:4, exponent:0}]]],

]

*/
