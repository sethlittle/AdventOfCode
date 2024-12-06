//
//  HelperFunctions.swift
//  AOC_2024
//
//  Created by Seth Little on 12/2/24.
//

import Foundation

protocol AOCDay {
    func part1() -> Int
    func part2() -> Int
}

enum Day: String {
    case one = "1"
    case two = "2"
    case three = "3"
    case four = "4"
    case five = "5"
    case six = "6"
    
    func day(input: FileInput) -> AOCDay {
        switch self {
            case .one:
                return Day1(input: input)
            case .two:
                return Day2(input: input)
            case .three:
                return Day3(input: input)
            case .four:
                return Day4(input: input)
            case .five:
                return Day5(input: input)
            case .six:
                return Day6(input: input)
        }
    }
    
    func executeDay(justTest: Bool = false) {
        print("------ DAY \(self.rawValue) ------")
        print("PART 1 - TEST:", day(input: .test).part1())
        if !justTest {
            print("PART 1:", day(input: .input).part1())
        }
        print("PART 2 - TEST:", day(input: .test).part2())
        if !justTest {
            print("PART 2:", day(input: .input).part2())
        }
    }
}

enum FileInput {
    case input
    case test
    
    func filePath(for day: Day) -> String {
        switch self {
            case .input:
                "/Users/seth/AdventOfCode/2024/day\(day.rawValue)/input.txt"
            case .test:
                "/Users/seth/AdventOfCode/2024/day\(day.rawValue)/test_input.txt"
        }
    }
}

enum HelperFunctions {
    static func getInput(for input: FileInput, day: Day) -> String? {
        let path = URL(fileURLWithPath: input.filePath(for: day))
        return try? String(contentsOf: path)
    }
}

struct Point: Hashable, CustomStringConvertible {
    let x: Int
    let y: Int
    
    var description: String {
        "(\(x), \(y))"
    }
}

enum Direction {
    case north
    case south
    case west
    case east
    
    func turnClockwise() -> Direction {
        switch self {
            case .north:
                .east
            case .south:
                .west
            case .west:
                .north
            case .east:
                .south
        }
    }
}

// Extensions
extension Collection where Indices.Iterator.Element == Index {
    subscript (safe index: Index) -> Iterator.Element? {
        return indices.contains(index) ? self[index] : nil
    }
}
