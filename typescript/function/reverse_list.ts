/**
 * Write a pseudo-code description of a function that reverses a list of n
 * integers, so that the numbers are listed in the opposite order than they
 * were before, and compare this method to an equivalent typescript function for doing the same thing.
 */

export function reverse_list(data: number[]): number[] {
    // Create a new list by reversing the input list
    let listNum: number[] = [];
    // Iterate through the input list in reverse order
    for (let i = data.length - 1; i >= 0; i--) {
        listNum.push(data[i]);
    }
    // Return the new list containing the reversed elements
    return listNum;
}