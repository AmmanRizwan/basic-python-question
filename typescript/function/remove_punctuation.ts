/**
 * Write a Typescript function that removes all punctuation characters from a given string.
 */

export function removePunctuation(input: string): string {
    return input.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, '');
}
