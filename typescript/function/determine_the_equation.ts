/**
 * Write a short program that takes as input three integers, a, b, and c, from
 * the console and determines if they can be used in a correct arithmetic
 * formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”
 */

export function determineTheEquation(a: number, b: number, c: number): boolean {
    let correctEquation: boolean = false;
    if (a + b === c) {
        correctEquation = true;
    }
    else if (b - c === a) {
        correctEquation = true;
    }
    else if (a * b === c) {
        correctEquation = true;
    } else {
        correctEquation = false;
    }
    return correctEquation;
}