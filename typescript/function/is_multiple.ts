/*
* 1. Write a short Python function, is_multiple(n, m), that takes two integer
* values and returns. True if n is a multiple of m, that is, n = mi for some
* integer i and False otherwise
* */

export function is_multiple(n: number, m: number): boolean {
    if (n % m === 0) {
        return true;
    }
    else {
        return false;
    }
}
