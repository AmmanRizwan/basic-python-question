/**
 * What parameters should be sent to the range constructor, to produce a 
 * range with values 8, 6, 4, 2, 0, -2, -4, -6, -8?
 */

export function customRangeV2(): number[] {
    let listNum: number[] = [];
    for (let i = 8; i >= -8; i -= 2) {
        listNum.push(i);
    }
    return listNum;
}
