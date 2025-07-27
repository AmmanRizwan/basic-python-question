/*
    Write a short Python function, `minmax(data)`, that takes a sequence of
    one or more numbers, and returns the smallest and largest numbers, in the
    form of a tuple of length two. Do not use the built-in functions min or
    max in implementing your solution
 */

export function minmax(data: number[]): [number, number] {
    let minNum: number = data[0];
    let maxNum: number = data[0];

    for (let i = 0; i < data.length; i++) {
        if (data[i] > maxNum) {
            maxNum = data[i];
        }
        else if (data[i] < minNum) {
            minNum = data[i];
        }
    }
    return [minNum, maxNum];
}