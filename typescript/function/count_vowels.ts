/**
 * Write a short typescript function that counts the number of vowels in a given 
 * character string.
 */

export function countVowels(input: string): number {
    const vowels = 'aeiou';
    let count = 0;

    for (const char of input.toLowerCase()) {
        if (vowels.includes(char)) {
            count++;
        }
    }

    return count;
}