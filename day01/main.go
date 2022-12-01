package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	input, _ := os.Open("input.txt")
	defer input.Close()

	scanner := bufio.NewScanner(input)

	cal_sum := 0
	var cal_slice []int

	for scanner.Scan() {
		if scanner.Text() == "" {
			cal_slice = append(cal_slice, cal_sum)
			cal_sum = 0
		} else {
			item, _ := strconv.ParseInt(scanner.Text(), 10, 32)
			cal_sum += int(item)
		}
	}
	cal_slice = append(cal_slice, cal_sum)
	sort.Slice(cal_slice, func(i, j int) bool {
		return cal_slice[i] > cal_slice[j]
	})

	fmt.Println("part 1:", cal_slice[0])

	part2_result := 0
	for i := 0; i < 3; i++ {
		part2_result += cal_slice[i]
	}

	fmt.Println("part 2:", part2_result)

}
