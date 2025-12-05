package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func part1(ranges [][]int, vals []int) {
	ans := 0
	for _, val := range vals {
		for _, r := range ranges {
			if r[0] <= val && val <= r[1] {
				ans++
				break
			}
		}
	}
	fmt.Println(ans)
}

func part2(ranges [][]int) {
	sort.Slice(ranges, func(i, j int) bool {
		return ranges[i][0] < ranges[j][0]
	})
	var ans [][]int
	for _, r := range ranges {
		if len(ans) == 0 || r[0] > ans[len(ans)-1][1] {
			ans = append(ans, r)
		}
		ans[len(ans)-1][1] = max(ans[len(ans)-1][1], r[1])
	}
	tot := 0
	for _, r := range ans {
		tot += r[1] - r[0] + 1
	}
	fmt.Println(tot)
}

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var ranges [][]int
	var vals []int
	space_found := false
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			space_found = true
			continue
		}
		if space_found {
			n, _ := strconv.Atoi(line)
			vals = append(vals, n)
		} else {
			a, b, _ := strings.Cut(line, "-")
			x, _ := strconv.Atoi(a)
			y, _ := strconv.Atoi(b)
			ranges = append(ranges, []int{x, y})
		}
	}
	part1(ranges, vals)
	part2(ranges)
}
