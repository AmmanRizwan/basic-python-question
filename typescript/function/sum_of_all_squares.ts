/**
 * Give a single command that computes the sum from Question No. 4,
 * relying on typescript and the built-in reduce method.
 */

import { sum_squares } from './sum_squares';

export function sum_of_all_squares(n: number): number | string {
    let listNum: number[] | string = sum_squares(n);
    if (listNum instanceof Array) {
        return listNum.reduce((acc, curr) => acc + curr, 0);
    } else {
        return listNum;
    }
}
