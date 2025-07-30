/**
 * Write a short typescript function that takes a positive integer n and returns
 * the sum of the squares of all the odd positive integers smaller than n
 */

export function sum_of_all_squares_odd(num: number): number | string {
    let listNum: number[] = [];
    if (num <= 0) {
        return "Input must be a positive integer.";
    }
    else {
        for (let i = num; i >= 0; i--) {
            if((i & 1) !== 0) {
                listNum.push(i * i);
            }
        }
        return listNum.reduce((acc, curr) => acc + curr, 0);
    }
}