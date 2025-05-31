package main

import (
	"fmt"

	"github.com/samber/lo"
	lib "github.com/thebenkogan/CodingQuest-2022"
)

const (
	windowSize = 60
	minAverage = float64(1500)
	maxAverage = float64(1600)
)

func main() {
	input := lib.GetInput()
	nums := lib.ParseNums(input)

	total := 0
	sum := lo.Sum(nums[:windowSize])
	total += checkAvg(sum)
	for i := windowSize; i < len(nums); i++ {
		sum += nums[i]
		sum -= nums[i-windowSize]
		total += checkAvg(sum)
	}

	fmt.Println(total)
}

func checkAvg(sum int) int {
	avg := float64(sum) / float64(windowSize)
	if avg < minAverage || avg > maxAverage {
		return 1
	}
	return 0
}
