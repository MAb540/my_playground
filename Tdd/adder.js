const add = (...numbers) => {
    if (numbers.length > 0) {
        return numbers.reduce((acc, number) => acc += number)
    }
    return 0

}

module.exports = {
    add
}