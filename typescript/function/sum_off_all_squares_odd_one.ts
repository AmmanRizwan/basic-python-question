/**
 * Give a single command that computes the sum from Question No. 6 relying on typescript syntax and the built-in reduce method.
 */

export function sum_of_all_squares_odd_one(num: number): number | string {
    if (num <= 0) {
        return "Input must be a positive integer.";
    }
    return Array.from({ length: num }, (_, i) => i + 1)
        .filter(i => i % 2 !== 0)
        .reduce((acc, curr) => acc + curr * curr, 0);
}