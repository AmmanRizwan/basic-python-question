/**
 * Demonstrate how to use Python's list comprehension syntax to produce
 *  the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
 */

export function list_of_squares_compress(): number[] {
    return Array.from({ length: 9 }, (_, i) => 2 ** i);
}
