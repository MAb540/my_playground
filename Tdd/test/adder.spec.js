const { add } = require("../adder");


test('should return 0 for no input',()=>{
    const result = add();
    expect(result).toBe(0);
})

test('should return addition for two numbers',()=>{
    const result = add(2,3);
    expect(result).toBe(5);
})

test('should return addition for three numbers',()=>{
    const result = add(3,3,4);
    expect(result).toBe(10);
})
