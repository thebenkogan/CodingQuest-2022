package main

import (
	"fmt"
	"strings"

	"github.com/samber/lo"
	lib "github.com/thebenkogan/CodingQuest-2022"
)

var lotteryNumbers = map[int]struct{}{
	12: {},
	48: {},
	30: {},
	95: {},
	15: {},
	55: {},
	97: {},
}
var winnings = map[int]int{
	3: 1,
	4: 10,
	5: 100,
	6: 1000,
}

func main() {
	input := lib.GetInput()
	lines := strings.Split(input, "\n")

	total := 0
	for _, line := range lines {
		nums := lib.ParseNums(line)
		count := lo.CountBy(nums, func(n int) bool {
			_, ok := lotteryNumbers[n]
			return ok
		})
		total += winnings[count]
	}

	fmt.Println(total)
}
