/**
 * What parameters should be sent to the range constructor, to produce a 
 * range with values 50, 60, 70, 80
 */

export function customRangeV1(): number[] {
    let listNum: number[] = [];
    for (let i = 50; i < 81; i += 10) {
        listNum.push(i);
    }
    return listNum;
}