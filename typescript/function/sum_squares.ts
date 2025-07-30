/**
 * Write a short Python function that takes a positive integer n and returns
 * the sum of the squares of all the positive integer smaller than n.
 */

export function sum_squares(num: number): number[] | string {
    let listNum: number[] = [];
    if (num <= 0) {
        return "Input must be a positive integer.";
    }
    else {
        for (let i = num - 1; i > 0; i--) {
            listNum.push(i * i);
        }
        return listNum;
    }
}