/**
 *  Typescript has no randRange function, so we implement our own.
 *  and create a random choice function. same as Python's random.choice.
 */

export function randrange(start: number, stop?: number, step: number = 1): number {
    if (stop === undefined) {
        stop = start;
        start = 0;
    }
    if (step === 0) throw new Error("step must not be zero");
    const width = stop - start;
    const n = Math.floor(width / step);
    if (n <= 0) throw new Error("empty range for randrange()");
    const randomIndex = Math.floor(Math.random() * n);
    return start + randomIndex * step;
}

export function my_choice(data: number[]): number {
    if (data.length === 0) {
        throw new Error("Cannot choose from an empty sequence");
    }
    const index = randrange(0, data.length);
    return data[index];
}