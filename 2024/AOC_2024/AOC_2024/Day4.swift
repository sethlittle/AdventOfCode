/*
 --- Day 4: Ceres Search ---
 "Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

 As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

 This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


 ..X...
 .SAMX.
 .A..A.
 XMAS.S
 .X....
 The actual word search will be full of letters instead. For example:

 MMMSXXMASM
 MSAMXMSMSA
 AMXSXMAAMM
 MSAMASMSMX
 XMASAMXAMM
 XXAMMXXAMA
 SMSMSASXSS
 SAXAMASAAA
 MAMMMXMMMM
 MXMXAXMASX
 In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

 ....XXMAS.
 .SAMXMS...
 ...S..A...
 ..A.A.MS.X
 XMASAMX.MM
 X.....XA.A
 S.S.S.S.SS
 .A.A.A.A.A
 ..M.M.M.MM
 .X.X.XMASX
 Take a look at the little Elf's word search. How many times does XMAS appear?
 */

import Foundation

class Day4: AOCDay {
    var grid: [[Character]] = []
    
    init(input: FileInput) {
        guard let input = HelperFunctions.getInput(for: input, day: .four)?.split(separator: "\n"), input.count > 0 else { return }
        
        for row in input {
            let charArray = Array(row)
            grid.append(charArray)
        }
    }
    
    func part1() -> Int {
        var totalNumberOfXmasWords = 0
        
        for (rowIndex, row) in grid.enumerated() {
            for (columnIndex, character) in row.enumerated() {
                if character == "X" {
                    totalNumberOfXmasWords += testForXMAS(rowIndex, columnIndex)
                }
            }
        }
        
        grid = []
        return totalNumberOfXmasWords
    }
    
    /// Each `XMAS` word has to have `X` exactly once, so we can check this for each `X`
    /// This needs to check for `XMAS` in every direction, vertical, horizontal, diagonal, backwards
    func testForXMAS(_ rowIndex: Int, _ columnIndex: Int) -> Int {
        var wordParts: [[Character]] = []
        var output: Int = 0
        
        let length = 3
        let match: [Character] = ["M", "A", "S"]

        var items: [Character] = []
        // left
        for i in 1...length {
            if let item = grid[safe: rowIndex]?[safe: columnIndex - i] {
                items.append(item)
            }
        }
        wordParts.append(items)
        items.removeAll()
        
        // up-left diagonal
        for i in 1...length {
            if let item = grid[safe: rowIndex - i]?[safe: columnIndex - i] {
                items.append(item)
            }
        }
        wordParts.append(items)
        items.removeAll()
        
        // up
        for i in 1...length {
            if let item = grid[safe: rowIndex - i]?[safe: columnIndex] {
                items.append(item)
            }
        }
        wordParts.append(items)
        items.removeAll()
        
        // up-right diagonal
        for i in 1...length {
            if let item = grid[safe: rowIndex - i]?[safe: columnIndex + i] {
                items.append(item)
            }
        }
        wordParts.append(items)
        items.removeAll()
        
        // right
        for i in 1...length {
            if let item = grid[safe: rowIndex]?[safe: columnIndex + i] {
                items.append(item)
            }
        }
        wordParts.append(items)
        items.removeAll()
        
        // down-right diagonal
        for i in 1...length {
            if let item = grid[safe: rowIndex + i]?[safe: columnIndex + i] {
                items.append(item)
            }
        }
        wordParts.append(items)
        items.removeAll()
        
        // down
        for i in 1...length {
            if let item = grid[safe: rowIndex + i]?[safe: columnIndex] {
                items.append(item)
            }
        }
        wordParts.append(items)
        items.removeAll()
        
        // down-left diagonal
        for i in 1...length {
            if let item = grid[safe: rowIndex + i]?[safe: columnIndex - i] {
                items.append(item)
            }
        }
        wordParts.append(items)
        items.removeAll()
        
        for word in wordParts {
            if word == match {
                output += 1
            }
        }
        return output
    }
}

/*
 --- Part Two ---
 The Elf looks quizzically at you. Did you misunderstand the assignment?

 Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

 M.S
 .A.
 M.S
 Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

 Here's the same example from before, but this time all of the X-MASes have been kept instead:

 .M.S......
 ..A..MSMS.
 .M.S.MAA..
 ..A.ASMSM.
 .M.S.M....
 ..........
 S.S.S.S.S.
 .A.A.A.A..
 M.M.M.M.M.
 ..........
 In this example, an X-MAS appears 9 times.

 Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
 */

extension Day4 {
    func part2() -> Int {
        var totalNumberOfXmasWords = 0
        
        for (rowIndex, row) in grid.enumerated() {
            for (columnIndex, character) in row.enumerated() {
                if character == "A" {
                    totalNumberOfXmasWords += checkForMAS(rowIndex, columnIndex) ? 1 : 0
                }
            }
        }
        
        grid = []
        return totalNumberOfXmasWords
    }
    
    func checkForMAS(_ rowIndex: Int, _ columnIndex: Int) -> Bool {
        // check four corners, if 2 Ms and 2 Ss, then true
        var corners: [Character] = []
        let upperLeftCorner = grid[safe: rowIndex - 1]?[safe: columnIndex - 1]
        let upperRightCorner = grid[safe: rowIndex - 1]?[safe: columnIndex + 1]
        let lowerRightCorner = grid[safe: rowIndex + 1]?[safe: columnIndex + 1]
        let lowerLeftCorner = grid[safe: rowIndex + 1]?[safe: columnIndex - 1]
        
        // Need all four corners to be present
        if let upperLeftCorner, let upperRightCorner, let lowerLeftCorner, let lowerRightCorner {
            corners += [upperLeftCorner, upperRightCorner, lowerLeftCorner, lowerRightCorner]
            
            // Only edge case we need to consider is when Ms are opposite of each other
            if upperLeftCorner == lowerRightCorner || upperRightCorner == lowerLeftCorner {
                return false
            }
        }
        
        return corners.filter{ $0 == "M"}.count == 2 && corners.filter{ $0 == "S"}.count == 2
    }
}
