/*
* 2. Write a short Python function, `is_even(k)`, that takes an integer value and
* return True if k is even, and False otherwise. However, your function cannot use
* the multiplication, module, or division operators.
*
*/

export function is_even(k: number): boolean {
    if ((k & 1) === 0) {
        return true;
    }
    else {
        return false;
    }
}